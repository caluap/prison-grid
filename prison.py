size('A3')

n_w = 9
n_h = round(n_w * sqrt(2))

m = width()/n_w * 0.1

w = (width() - 2*m)/n_w
h = (height() - 2*m)/n_h

for _x in range(n_w):
    for _y in range(n_h):
        
        x0 = _x * w + m
        y0 = _y * h + m
        
        # big rect
        if False:
            strokeWidth(1)
            stroke(1)
            fill(0)
            rect(x0, y0, w, h)
        
        # small rect
        stroke(1)
        fill(1)
        
        colors = {
            'top': {'r':0.9, 'g':0, 'b':0},
            'left': {'r':0.4, 'g':0, 'b':0},
            'right': {'r':0.4, 'g':0, 'b':0},
            'bottom': {'r':0.2, 'g':0, 'b':0},
            'fill': {'r':1, 'g':0, 'b':0},
            }
        
        frac = 0.6 # % of bigger rect
        small_s = w * frac        
        sx0 = x0 + random() * (1 - frac) * w
        sy0 = y0 + random() * (1 - frac) * h
        
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
    