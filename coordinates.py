def get_line(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    m = (y2-y1) / (x2-x1)
    b = y1-m*x1
    return m,b

def get_y(m,b):
    x1,y1 = p1
    x2,y2 = p2
    m = (y2-y1) / (x2-x1)
    b = y1 - m*x1
    y = m*x+b
    return y

if __name__ == "__main__":
    p1 = (7,1)
    p2 = (-3,-4)
    m, b = get_line(p1,p2)
    y = get_y(m, b)
    print(y)
