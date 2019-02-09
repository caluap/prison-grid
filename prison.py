def hex2rgb(c_hex):
    c = tuple(int(c_hex[i:i+2], 16)/255 for i in (0, 2, 4))
    return {'r':c[0], 'g':c[1], 'b':c[2]}
    
def pl(l, p):
    return round(len(l)*p)


import noise

size('A3')

n_w = 21    
n_h = round(n_w * sqrt(2))

m = width()/n_w * 0.1

w = (width() - 2*m)/n_w
h = (height() - 2*m)/n_h

tints = [
    '000000',
    '14010b',	
    '290117',	
    '3d0222',	
    '51032e',	
    '660439',	
    '7a0444',	
    '8e0550',	
    'a2065b',	
    'b70667',	
    'cb0772',	
    'd02080',	
    'd5398e',	
    'db519c',	
    'e06aaa',	
    'e583b9',	
    'ea9cc7',	
    'efb5d5',	
    'f5cde3',	
    'fae6f1',	
    'ffffff'
    ]

for _x in range(n_w):
    for _y in range(n_h):
        
        colors = {
            'top': hex2rgb(tints[pl(tints, 0.2)]),
            'left': hex2rgb(tints[pl(tints, 0.5)]),
            'right': hex2rgb(tints[pl(tints, 0.6)]),
            'bottom': hex2rgb(tints[pl(tints, 0.8)]),
            'fill': hex2rgb(tints[pl(tints, 0.1)])
            }
        
        x0 = _x * w + m
        y0 = _y * h + m
        
        # big rect
        if True:
            strokeWidth(2)
            stroke(**colors['left'])
            fill(0)
            rect(x0, y0, w, h)
        
        # small rect
        stroke(1)
        fill(1)
        
        frac = 0.6 # % of bigger rect
        small_s = w * frac
        
        # part perlin, half noise 
        perlin = 0.7
        
        r1 = perlin * abs(noise.pnoise1(_x/n_w)) + (1-perlin) * random()
        r2 = perlin * abs(noise.pnoise1(_y/n_h)) + (1-perlin) * random()
        # print(f'{r1} {r2}')
        
        sx0 = x0 + r1 * (1 - frac) * w
        sy0 = y0 + r2 * (1 - frac) * h
        
        x1 = x0 + w
        y1 = y0 + h
        
        sx1 = sx0 + small_s
        sy1 = sy0 + small_s
        
        strokeWidth(0)
        
        fill(**colors['left'])
        polygon((x0, y0), (x0, y1), (sx0, sy1), (sx0, sy0), close = True)
        
        fill(**colors['right'])
        polygon((x1, y1), (x1, y0), (sx1, sy0), (sx1, sy1), close = True)
        
        fill(**colors['top'])        
        polygon((x0, y1), (x1, y1), (sx1, sy1), (sx0, sy1), close = True)
        
        fill(**colors['bottom'])
        polygon((x0, y0), (x1, y0), (sx1, sy0), (sx0, sy0), close = True)
        
        fill(**colors['fill'])
        rect(sx0, sy0, small_s, small_s)
    