def a(my_dream, colors):
    house = False
    roof_color = colors[0]
    house_color = colors[1]
    door_color = colors[2]
    roof = my_dream[0]
    walls = my_dream[1]

    while not house:
        roof_status = build_roof(roof, roof_color)
        walls_status = build_walls(walls, house_color)
        door_status = build_door(door_color)

def build_roof(r, rc):
    pass
def build_walls(r, ws):
    pass
def build_door(r):
    pass
idea = ('roof', 'walls')
colors = ('red', 'white', 'blue')
a(idea, colors)