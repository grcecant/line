from display import *
from draw import *
import random

s = new_screen()
c = [0, 255, 0]

'''
#sun
for i in range(100):
     c[RED]=random.randint(220,250)
     c[GREEN]=random.randint(150,250)
     c[BLUE]=random.randint(0,30)
     draw_line(490, 420, 390+random.randint(-170, 200), 390+random.randint(-150, 200), s, c)

#river: dark
c = [30, 141, 250]
for i in range(32):
    draw_line(0, 160-(i*5), XRES, 160-(i*5), s, c)

#river: light
c = [100, 149, 237]
for i in range(8):
    draw_line(125, 157-(i*20), 375, 157-(i*20), s, c)
for i in range(16):
    draw_line(100, 158-(i*10), 400, 158-(i*10), s, c)
for i in range(8):
    draw_line(50, 158-(i*20), 450, 158-(i*20), s, c)

#river: white
c = [173, 215, 230]
for i in range(4):
    draw_line(200, 157-(i*40), 300, 157-(i*40), s, c)
for i in range(4):
    draw_line(150, 158-(i*40), 350, 158-(i*40), s, c)
for i in range(8):
    draw_line(225, 158-(i*20), 275, 158-(i*20), s, c)

'''
c = [ 0, 255, 0 ]

#octants 1 and 5, works!
draw_line(0, 0, XRES-1, YRES-1, s, c)
draw_line(0, 0, XRES-1, YRES / 2, s, c)
draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

#octants 8 and 4, works!
c[BLUE] = 255;
draw_line(0, YRES-1, XRES-1, 0, s, c);
draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
draw_line(XRES-1, 0, 0, YRES/2, s, c);

#octants 2 and 6, works!
c[RED] = 255;
c[GREEN] = 0;
c[BLUE] = 0;
draw_line(0, 0, XRES/2, YRES-1, s, c);
draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);

#octants 7 and 3, works!
c[BLUE] = 255;
draw_line(0, YRES-1, XRES/2, 0, s, c);
draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);


#horizontal and vertical, works!
c[BLUE] = 0;
c[GREEN] = 255;
draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
