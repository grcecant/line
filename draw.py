from display import *

#bresenham's line algorithm
def draw_line( x0, y0, x1, y1, screen, color ):

    #check if x0 is smaller than x1. If not, switch
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #variables
    x0, y0 = int(x0), int(y0)
    x1, y1 = int(x1), int(y1)

    #other variables
    A = y1 - y0
    B = -(x1 - x0)
    if B!=0:
        m = A / B

    #undefined slope (vertical line)
    if B == 0:
        while (y0 <= y1):
            plot(screen, color, x0, y0)
            y0+=1

    #zero slope (horizontal line)
    elif A == 0:
        while (x0 <= x1):
            plot(screen, color, x0, y0)
            x0+=1

    #octant 1 and 5
    elif m <= 1 and m > 0:
        d = 2*A + B
        while (x0 <= x1):
            plot(screen, color, x0, y0)
            if d > 0:
                d+=(2*B)
                y0+=1
            x0+=1
            d+=(2*A)

    #octant 2 and 6
    elif m > 1:
        d = 2*B + A
        while (y0 <= y1):
            plot(screen, color, x0, y0)
            if d < 0:
                d+=(2*A)
                x0+=1
            y0+=1
            d+=(2*B)

    #octant 3 and 7
    elif m < -1:
        d = A - 2*B
        while (y0 <= y1):
            plot(screen, color, x0, y0)
            if d > 0:
                d+=(2*B)
                y0+=1
            x0-=1
            d-=(2*B)

    #octant 4 and 8
    elif m >= -1 and m < 0:
        d = 2*A - B
        while (x0 <= x1):
            plot(screen, color, x0, y0)
            if d < 0:
                d+=(2*B)
                y0+=1
            x0+=1
            d+=(2*A)
