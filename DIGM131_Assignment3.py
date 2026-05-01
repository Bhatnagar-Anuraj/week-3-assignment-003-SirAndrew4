# Function Creation Area
# Can tell if a nubmer is odd or even
def evenOdd(x):
    
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
        
# Can tell if a number is higher than 10
def higherThanTen(x):
    
    if (x >= 10):
        return "Yes"
    else:
        return "No"
  
#    Creating Trees
def create_tree(x, z, trunk_height=2.0, canopy_radius=1.2):
    """Create a simple tree at the given X, Z position."""
    trunk_radius = 0.3
    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(x, trunk_height / 2.0, z, trunk)
    canopy = cmds.polySphere(radius=canopy_radius)[0]
    canopy_y = trunk_height + canopy_radius * 0.6
    cmds.move(x, canopy_y, z, canopy)
    return trunk, canopy
    
#  Creating Builds  
def create_build(x, z):
    """Create a simple tree at the given X, Z position."""
    build_width = 0.3
    build_height = 3
    build_depth = 1
    build = cmds.polyCube(width=build_width, height=build_height, 
                          depth=build_depth)[0]
    cmds.move(x, build_height / 2.0, z, build)
    return build
    
#  Creating Balls
def create_ball(x, z, ball_radius=1.2):
    """Create a simple tree at the given X, Z position."""
    ball = cmds.polySphere(radius=ball_radius)[0]
    ball_y = ball_radius * 0.6
    cmds.move(x, ball_y, z, ball)
    return ball
    
# Creating Lamps
def create_lamp(x, z, lamp_height=2.0):
    """Create a simple tree at the given X, Z position."""
    lamp_radius = 0.3
    lamp = cmds.polyCylinder(radius=lamp_radius, height=lamp_height)[0]
    cmds.move(x, lamp_height / 2.0, z, lamp)
    return lamp


# Print Area
print(evenOdd(16))
print(evenOdd(7))
print(higherThanTen(7))
print(higherThanTen(17))
create_tree(-4, 0)
create_build(4,-4)
create_ball(0, 10)
create_lamp(0, 0)