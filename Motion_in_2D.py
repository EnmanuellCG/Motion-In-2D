import math
import matplotlib
from matplotlib import pyplot as plt
import formula

vi = float(input("What is the initial velocity of the object in m/s?\n > "))
h = float(input("What is the initial height of the object in meters?\n > "))
angle = float(input("What is the angle that the object was ejected at in degrees?\n > "))
dt = float(input("What is the difference in time(dt) that you want?\n > "))



time = 0

#Getting the Angle degree from the function on the file
cos, sin = formula.get_angle(angle)

# Velocity In x and y directions
vy, vx = formula.get_motion(vi, cos, sin)

#This will be the time
x = []
#This will be the height
y = []

while True:
    time = time + dt

    #|Constant's|
    g = 9.8

    #|Calculations|
    dy = h + vy * time + 0.5 * time**2 * -g

    if dy < 0:
        print(f"At {round(time, 3)} seconds the object hit the ground")

        plt.plot(x, y)


        plt.plot(x, y)

        plt.title("Projectile Motion")
        plt.xlabel('time')
        plt.ylabel('Distance')

        plt.grid(True)

        plt.show()


        break


    x.append(time)
    y.append(dy)

    # |Beutifull Rounded numbers|
    if dt > 0.01:
        time = round(time, 2)
        dy = round(dy, 2)
    else:
        time = round(time, 5)
        dy = round(dy, 5)

    print(f"At {time} seconds the distance over the ground is [{dy}m]")


