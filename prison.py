import noise

transparent_bg = True

# 1 : boxes only
# 2 : lines only
# 3 : 3d boxes
mode = 3
s_mode = 4
mode_adjustment = 1

use_cmyk = True

if s_mode == 1: # Poster
    size('A3')
    n_w = 19

elif s_mode == 2: # Facebook
    size(1702, 630)
    n_w = 60
    mode_adjustment = 1.2
    use_cmyk = False

elif s_mode == 3: # Twitter        
    size(1500, 500)
    n_w = 53
    mode_adjustment = 1.3
    use_cmyk = False

elif s_mode == 4: # Site background texture    
    size(1280, 640)
    n_w = 22
    use_cmyk = False

elif s_mode == 5: # Instagram Post    
    size(1080, 1080)
    n_w = 33
    mode_adjustment = 1.8
    use_cmyk = False

elif s_mode == 6: # Youtube cover
    size(2560, 1440)
    n_w = 80
    use_cmyk = False
    
if not transparent_bg:
    if use_cmyk:
        cmykFill(0,0,0,1)
    else:
        fill(0)
    rect(0,0,width(),height())
    
    
# how many rows for a given (n_w) number of columns?
n_h = round(n_w * height()/width())


# if the width is too wide, change the number of columns to its minimum
# value considering square unites
if n_h == 0:
    n_h = 1
    aux_n_w = n_w
    n_w = round(width()/height())
    print(f'Too few squares to fill this page! \nYou’d need {n_w} squares, so we went ahead and overrode your initial setting of {aux_n_w}!')


# this calculates the width and height of each “square”
# (which will be as square as possible, but rarely so)
w = (width())/n_w
h = (height())/n_h
    


# dras the grid
for _x in range(n_w):
    for _y in range(n_h):
        
        # first coordinates of the bigger square
        x0 = _x * w
        y0 = _y * h
        
        # part perlin, half noise 
        perlin = 0.95
        
        rx = perlin * abs(noise.pnoise1(_x/n_w, repeat=n_w)) + (1-perlin) * random()
        ry = perlin * abs(noise.pnoise1(_y/n_h, repeat=n_h)) + (1-perlin) * random()
        
        frac = min([0.9, 0.2 + 0.4 * rx + 0.4 * ry])
        
        # sometimes i'll need smaller or bigger gaps         
        frac = min([0.9, frac*mode_adjustment])
        
        # the size of the gap
        small_s = w * frac
        
        # first coordinates of the smaller square
        sx0 = x0 + rx * (1 - frac) * w
        sy0 = y0 + ry * (1 - frac) * h
        
        # second coordinates of the bigger square
        x1 = x0 + w
        y1 = y0 + h
        
        # second coordinates of the smaller square
        sx1 = sx0 + small_s
        sy1 = sy0 + small_s
        
        
        # only squares
        if mode == 1:
            stroke(1)
            if use_cmyk:
                cmykFill(.18, 1, .25, 0)
            else:
                fill(210/255, 9/255, 119/255)
            rect(x0, y0, w, h)

            stroke(None)
            if use_cmyk:
                cmykFill(.48, 1, .48, .48)
            else:
                fill(93/255, 5/255, 58/255)
            rect(sx0, sy0, small_s, small_s)
        
        # only lines
        if mode == 2:                        
            fill(None)
            if use_cmyk:
                cmykStroke(.18, 1, .25, 0)
            else:
                stroke(210/255, 9/255, 119/255)
                        
            # Left
            polygon((x0, y0), (x0, y1), (sx0, sy1), (sx0, sy0), close = True)
        
            # Right
            polygon((x1, y1), (x1, y0), (sx1, sy0), (sx1, sy1), close = True)
        
            # Top
            polygon((x0, y1), (x1, y1), (sx1, sy1), (sx0, sy1), close = True)
        
            # Bottom
            polygon((x0, y0), (x1, y0), (sx1, sy0), (sx0, sy0), close = True)
        
        # faux 3d
        if mode == 3:
            
            stroke(None)
            
            # Left            
            if use_cmyk:
                cmykFill(.29, 1, .29, .19)
            else:
                fill(160/255, 11/255, 100/255)

            polygon((x0, y0), (x0, y1), (sx0, sy1), (sx0, sy0), close = True)
        
            # Right            
            if use_cmyk:
                cmykFill(.18, 1, .25, 0)
            else:
                fill(210/255, 9/255, 119/255)
            polygon((x1, y1), (x1, y0), (sx1, sy0), (sx1, sy1), close = True)
        
            # Top            
            if use_cmyk:
                cmykFill(.48, 1, .48, .48)
            else:
                fill(93/255, 5/255, 58/255)
            polygon((x0, y1), (x1, y1), (sx1, sy1), (sx0, sy1), close = True)
        
            # Bottom
            if use_cmyk:
                cmykFill(0, .73, 0, .13)
            else:
                fill(214/255, 82/255, 149/255)
                    
            polygon((x0, y0), (x1, y0), (sx1, sy0), (sx0, sy0), close = True)
    