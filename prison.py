import noise

size('A3')
stroke(None)

n_w = 19   
n_h = round(n_w * sqrt(2))

m = 0

w = (width() - 2*m)/n_w
h = (height() - 2*m)/n_h

transparent_bg = False

mode = 3

for _x in range(n_w):
    for _y in range(n_h):
        
        x0 = _x * w + m
        y0 = _y * h + m
        
        # part perlin, half noise 
        perlin = 0.93
        
        r1 = perlin * abs(noise.pnoise1((n_w-_x)/n_w, repeat=n_w//8)) + (1-perlin) * random()
        r2 = perlin * abs(noise.pnoise1((n_h-_y)/n_h, repeat=n_h//8)) + (1-perlin) * random()
        # print(f'{r1} {r2}')
        
        frac = min([0.9, 0.2 + 0.4 * r1 + 0.4 * r2]) # % of bigger rect
        small_s = w * frac
        
        sx0 = x0 + r1 * (1 - frac) * w
        sy0 = y0 + r2 * (1 - frac) * h
        
        x1 = x0 + w
        y1 = y0 + h
        
        sx1 = sx0 + small_s
        sy1 = sy0 + small_s
        
        
        if mode == 1 or mode == 2:
            cmykFill(.18, 1, .25, 0)
            rect(x0, y0, w, h)
            
            cmykFill(.48, 1, .48, .48)
            rect(sx0, sy0, small_s, small_s)
            
        if mode == 2:                        
            fill(None)
            stroke(1)
            
            # Left
            polygon((x0, y0), (x0, y1), (sx0, sy1), (sx0, sy0), close = True)
        
            # Right
            polygon((x1, y1), (x1, y0), (sx1, sy0), (sx1, sy1), close = True)
        
            # Top
            polygon((x0, y1), (x1, y1), (sx1, sy1), (sx0, sy1), close = True)
        
            # Bottom
            polygon((x0, y0), (x1, y0), (sx1, sy0), (sx0, sy0), close = True)
        
        if mode == 3:
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
    