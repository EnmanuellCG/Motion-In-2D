import math

def get_angle(x):
    # convert angle to radians
    angle = math.radians(x)

    # Breaked down the y, x-axis.
    cos = math.cos(angle)
    sin = math.sin(angle)
    return cos, sin

def get_motion(vi, cos, sin):
    # Velocity In x and y directions
    vy = vi * sin
    vx = vi * cos
    return vy, vx


