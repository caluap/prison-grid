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
        strokeWidth(1)
        stroke(1)
        fill(0)
        rect(x0, y0, w, h)
        
        # small rect
        stroke(1)
        fill(1)
        
        frac = 0.4 # % of bigger rect
        small_s = w * frac        
        sx0 = x0 + random() * (1 - frac) * w
        sy0 = y0 + random() * (1 - frac) * h
        
        x1 = x0 + w
        y1 = y0 + h
        
        sx1 = sx0 + small_s
        sy1 = sy0 + small_s
        
        
        line((x0, y0), (sx0, sy0))
        line((x1, y0), (sx1, sy0))
        line((x0, y1), (sx0, sy1))
        line((x1, y1), (sx1, sy1))
        
        # strokeWidth(0)
        rect(sx0, sy0, small_s, small_s)
    