# This file translates an
# x-y location to a pixel number

# xd : x-dimension
# yd : y-dimension

def main(x,y,xd,yd):
    i = x + xd*(yd-y-1)+1
    return i
