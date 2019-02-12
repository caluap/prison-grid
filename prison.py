import noise

transparent_bg = True

# 1 : boxes only
# 2 : lines only
# 3 : 3d boxes
mode = 3
s_mode = 4
mode_adjustment = 1

# Poster
if s_mode == 1:
    size('A3')
    n_w = 19
elif s_mode == 2:
    # Facebook
    size(1702, 630)
    n_w = 60
    mode_adjustment = 1.2
elif s_mode == 3:
    # Twitter    
    size(1500, 500)
    n_w = 53
    mode_adjustment = 1.3
elif s_mode == 4:
    # Site background texture    
    size(1280, 640)
    n_w = 44
    
n_h = round(n_w * height()/width())

if n_h == 0:
    n_h = 1
    aux_n_w = n_w
    n_w = round(width()/height())
    print(f'Too few squares to fill this page! \nYou’d need {n_w} squares, so we went ahead and overrode your initial setting of {aux_n_w}!')

w = (width())/n_w
h = (height())/n_h

if not transparent_bg:
    cmykFill(0,0,0,1)
    rect(0,0,width(),height())
    

for _x in range(n_w):
    for _y in range(n_h):
        
        x0 = _x * w
        y0 = _y * h
        
        # part perlin, half noise 
        perlin = 0.93
        
        rx = perlin * abs(noise.pnoise1(_x/n_w, repeat=n_w)) + (1-perlin) * random()
        ry = perlin * abs(noise.pnoise1(_y/n_h, repeat=n_h)) + (1-perlin) * random()
        
        frac = min([0.9, 0.2 + 0.4 * rx + 0.4 * ry])
        
        frac = min([0.9, frac*mode_adjustment])
        
        small_s = w * frac
        
        sx0 = x0 + rx * (1 - frac) * w
        sy0 = y0 + ry * (1 - frac) * h
        
        x1 = x0 + w
        y1 = y0 + h
        
        sx1 = sx0 + small_s
        sy1 = sy0 + small_s
        
        
        if mode == 1:
            stroke(1)
            cmykFill(.18, 1, .25, 0)
            rect(x0, y0, w, h)

            stroke(None)            
            cmykFill(.48, 1, .48, .48)
            rect(sx0, sy0, small_s, small_s)
            
        if mode == 2:                        
            fill(None)
            cmykStroke(.18, 1, .25, 0)
            
            # Left
            polygon((x0, y0), (x0, y1), (sx0, sy1), (sx0, sy0), close = True)
        
            # Right
            polygon((x1, y1), (x1, y0), (sx1, sy0), (sx1, sy1), close = True)
        
            # Top
            polygon((x0, y1), (x1, y1), (sx1, sy1), (sx0, sy1), close = True)
        
            # Bottom
            polygon((x0, y0), (x1, y0), (sx1, sy0), (sx0, sy0), close = True)
        
        if mode == 3:
            
            stroke(None)
            
            # Left
            cmykFill(.29, 1, .29, .19)
            polygon((x0, y0), (x0, y1), (sx0, sy1), (sx0, sy0), close = True)
        
            # Right
            cmykFill(.18, 1, .25, 0)
            polygon((x1, y1), (x1, y0), (sx1, sy0), (sx1, sy1), close = True)
        
            # Top       
            cmykFill(.48, 1, .48, .48)
            polygon((x0, y1), (x1, y1), (sx1, sy1), (sx0, sy1), close = True)
        
            # Bottom
            cmykFill(0, .73, 0, .13)        
            polygon((x0, y0), (x1, y0), (sx1, sy0), (sx0, sy0), close = True)
    