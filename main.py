from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from map import load_map
# from menu import *

game = Ursina()

ground = Entity(model='plane', scale=(50, 1, 50), color=color.white.tint(-0.2), texture='rrock12.png', collider='box')

passage_width = 10
passage_height = 5

player = FirstPersonController(model='cube',speed=5, position=(-2, 2, -23), color=color.orange, origin_y=-.5, collider='box')
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
editor_camera = EditorCamera(enabled=False, ignore_paused=True)

player_hp = 100
max_player_hp = 100

class ElevatingBlock(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            texture='wall2.png',
            scale=(1, passage_height, passage_width),
            position=(-15, 2, -22.5),
            collider='box',
        )

    def update(self):
        if self.intersects(player).hit:
            self.y -=6


elevating_block = ElevatingBlock()

gray_1 = Entity(parent=camera.ui, model='quad', scale=(2, 0.2), origin=(0, 0), position=(0, -0.45), color=color.gray)
hp_bar = Entity(parent=camera.ui, model='quad', scale=(0.5, 0.04), origin=(-0.5, 0), position=(-0.6, -0.4), color=color.green)
ammo = Entity(parent=camera.ui, model='quad', scale=(0.3, 0.06), origin=(-0.5, 0), position=(0.2, -0.4), color=color.red)





muzzle_flash_texture = '5.png'
gun_texture = '0.png'
gun = Entity(model='cube',texture=gun_texture, parent=camera, position=(.0,-.10,.2), scale=(.3,.2,1), origin_z=-.6, on_cooldown=False)
gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5, model='quad', texture=muzzle_flash_texture, enabled=False)

shootables_parent = Entity()
mouse.traverse_target = shootables_parent

def update():
    if held_keys['left mouse']:
        shoot()

def shoot():
    if not gun.on_cooldown:
        # print('shoot')
        gun.on_cooldown = True
        gun.muzzle_flash.enabled=True
        from ursina.prefabs.ursfx import ursfx
        ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise', pitch=random.uniform(-13,-12), pitch_change=-12, speed=3.0)
        invoke(gun.muzzle_flash.disable, delay=.05)
        invoke(setattr, gun, 'on_cooldown', False, delay=.15)
        if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
            mouse.hovered_entity.hp -= 10
            mouse.hovered_entity.blink(color.red)

npc_texture = '12.png'
class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=shootables_parent, model='cube', scale_y=2.5, origin_y=-.5, texture=npc_texture, collider='box', **kwargs)
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self):
        dist = distance_xz(player.position, self.position)
        if dist > 40:
            return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)


        self.look_at_2d(player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == player:
            if dist > 2:
                self.position += self.forward * time.dt * 5

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        self.health_bar.alpha = 1

# Enemy()
enemies = [Enemy(x=x*4) for x in range(4)]


sky_texture = 'sky2.png'
sky = Entity(
    model='sphere', texture=sky_texture,
    scale=1000, double_sided=True
)


def pause_input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        gun.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position

        application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)



load_map()
shoot()


game.run()
