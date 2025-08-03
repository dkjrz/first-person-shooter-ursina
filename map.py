from ursina import *

def load_map():
    wall_texture = 'wall1.png'
    wall2_texture = 'wall2.png'
    cube_texture = 'wall3.png'
    cube1_texture = 'wall7.png'
    wall_scale = (1, 5, 50)

    passage_width = 10
    passage_height = 5

    passage_left1 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, 25), collider='box')
    passage_left2 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, 15), collider='box')
    passage_left3 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, 5), collider='box')
    passage_left4 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, 0), collider='box')
    passage_left5 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, -25), collider='box')
    passage_left6 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, -15), collider='box')
    passage_left7 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, -5), collider='box')

    passage_right1 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, 25), collider='box')
    passage_right2 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, 15), collider='box')
    passage_right3 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, 5), collider='box')
    passage_right4 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, 0), collider='box')
    passage_right5 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, -25), collider='box')
    passage_right6 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, -15), collider='box')
    passage_right7 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, -5), collider='box')

    passage_front1 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, 25),rotation_y=90, collider='box')
    passage_front2 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(15, 2, 25),rotation_y=90, collider='box')
    passage_front3 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(5, 2, 25),rotation_y=90, collider='box')
    passage_front4 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(0, 2, 25),rotation_y=90, collider='box')
    passage_front5 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, 25),rotation_y=90, collider='box')
    passage_front6 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-15, 2, 25),rotation_y=90, collider='box')
    passage_front7 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-5, 2, 25),rotation_y=90, collider='box')

    passage_back1 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, -25),rotation_y=90, collider='box')
    passage_back2 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-15, 2, -25),rotation_y=90, collider='box')
    passage_back3 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-5, 2, -25),rotation_y=90, collider='box')
    passage_back4 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-0, 2, -25),rotation_y=90, collider='box')
    passage_back5 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(25, 2, -25),rotation_y=90, collider='box')
    passage_back6 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(15, 2, -25),rotation_y=90, collider='box')
    passage_back6 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(5,2, -25),rotation_y=90, collider='box')

    passage_l1 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(1, 2, -20),rotation_y=90, collider='box')
    passage_l2 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-9, 2, -20),rotation_y=90, collider='box')
    passage_l3 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(11, 2, -20),rotation_y=90, collider='box')
    passage_l4 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(21, 2, -20),rotation_y=90, collider='box')
    passage_l5 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(5, 2, -25), collider='box')
    passage_l6 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-15, 2, -20),rotation_y=90, collider='box')
    passage_l7 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-20, 2, -15), collider='box')
    passage_l9 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-15, 2, -10),rotation_y=90, collider='box')
    passage_l10 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-15, 2, -3),rotation_y=90, collider='box')
    passage_l11 = Entity(model='cube', texture=wall_texture, scale=(1, passage_height, passage_width), position=(-25, 2, -3),rotation_y=90, collider='box')

   #стіни які будуть рухатись



  #куби на карті
    cube = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-9, 2, -12), color=color.orange, collider='box')
    cube2 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-5, 2, -16), color=color.orange, collider='box')
    cube3 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-5, 2, -18), color=color.orange, collider='box')
    cube4 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-23, 2, -1), color=color.orange, collider='box')
    cube5 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-23, 2, 3), color=color.orange, collider='box')
    cube6 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-19, 2, -1), color=color.orange, collider='box')
    cube7 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-23, 2, 23), color=color.orange, collider='box')
    cube8 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-23, 2, 19), color=color.orange, collider='box')
    cube9 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(-19, 2, 23), color=color.orange, collider='box')
    cube10 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(23, 2, 23), color=color.orange, collider='box')
    cube11 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(23, 2, 19), color=color.orange, collider='box')
    cube12 = Entity(model='cube',texture=cube_texture ,scale=(4, 5, 4),position=(19, 2, 23), color=color.orange, collider='box')
    cube13 = Entity(model='cube',texture=cube1_texture ,scale=(5, 5, 5),position=(0, 2, 10), color=color.white, collider='box')
    cube14 = Entity(model='cube',texture=cube1_texture ,scale=(5, 5, 5),position=(0, 2, -10), color=color.white, collider='box')
    cube15 = Entity(model='cube',texture=cube1_texture ,scale=(5, 5, 5),position=(14, 2, 10), color=color.white, collider='box')
    cube16 = Entity(model='cube',texture=cube1_texture ,scale=(5, 5, 5),position=(14, 2, -10), color=color.white, collider='box')
    cube17 = Entity(model='cube',texture=cube1_texture ,scale=(5, 5, 5),position=(7, 2, 0), color=color.white, collider='box')



