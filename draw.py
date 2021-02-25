from display import *

#bresenham's line algorithm
def draw_line( x0, y0, x1, y1, screen, color ):

    #check if x0 is smaller than x1. if not, switch
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #set initial variables
    x = x0
    y = y0

    x, y = int(x), int(y)
    x1, y1 = int(x1), int(y1)

    dx = x1-x
    dy = y1-y
    if dx != 0:
        m = dy/dx

    A = dy
    B = -dx

    #undefined slope (vertical line)
    if B == 0:
        while (y <= y1):
            plot(screen, color, x, y)
            y+=1

    #zero slope (horizontal line)
    elif A == 0:
        while (x <= x1):
            plot(screen, color, x, y)
            x+=1

    #octant 1 and 5
    elif m <= 1 and m > 0:
        d = 2*A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if d > 0:
                y+=1
                d+=(2*B)
            x+=1
            d+=(2*A)

    #octant 2 and 6
    elif m > 1:
        d = 2*B + A
        while (y <= y1):
            plot(screen, color, x, y)
            if d < 0:
                d+=(2*A)
                x+=1
            y+=1
            d+=(2*B)

    #octant 3 and 7
    elif m < -1:
        d = A - 2*B
        while (y >= y1):
            plot(screen, color, x, y)
            if d > 0:
                d+=(2*A)
                x+=1
            y-=1
            d-=(2*B)

    #octant 4 and 8
    elif m >= -1 and m < 0:
        d = 2*A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if d < 0:
                d-=(2*B)
                y-=1
            x+=1
            d+=(2*A)
