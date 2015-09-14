# Creates a PPM image of size 320 x 240. The background
# is light grey and contains a horizontal red line and
# a vertical green line that have been translated 50 in
# the x direction and -50 in the y direction.

import one_color
import write_ppm
import add_to_image
import copy

# list holding red and green lines.
# line_list[0] = red, line_list[1] = green
line_list = [
    [[60,120,],[160,120]],
    [[160,120],[160,220]]
    ]

#Function to gather all points -> pixels needed, returns structure
def line(x1, y1, x2, y2):

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #Find absolute value of x length, y length
    x_length = abs(x1 - x2)
    y_length = abs(y1 - y2)

    #compare x length, y length, if x length is longer...
    if x_length >= y_length:
        m = float(y2-y1)/float(x2-x1)               # slope
        b = (-(float(y2-y1)/float(x2-x1)))*x1 + y1  # y-intercept

        #Find integer values from x1 to x2
        big_x = 0
        small_x = 0
        
        if x1 > x2+1:
            big_x = x1
            small_x = x2
        else:
            big_x = x2
            small_x = x1
        
        for x in range(small_x, big_x+1):
            temp.x = x

            #solve for corresponding y values using Eq. 2.1
            y_value = m * x + b

            #Round y values to nearest integer value
            y_value = round(y_value)
            temp.y = int(y_value)

            #add x and y values to data structure
            points.append(copy.deepcopy(temp))

    #compare x length, y length, if y length is longer...        
    elif y_length > x_length:
        m_inverse = float(x2-x1)/float(y2-y1)       # slope inverse

        #Find integer values from y1 to y2
        big_y = 0
        small_y = 0
        
        if y1 > y2+1:
            big_y = y1
            small_y = y2
        else:
            big_y = y2
            small_y = y1
        
        for y in range(small_y, big_y+1):
            temp.y = y

            #solve for corresponding x values using Eq. 2.4
            x_value = m_inverse*y - m_inverse*y1 + x1

            #Round x values to nearest integer value
            x_value = round(x_value)
            temp.x = int(x_value)

            #add x and y values to data structure
            points.append(copy.deepcopy(temp))

    del points[0]   # remove unused location
    return points

# draw light gray background
image = one_color.main(320,240,245,245,245)

# add xt, yt to the x values, y values
for i in range(0, len(line_list)):
    for k in range(0, len(line_list[i])):
        line_list[i][k][0] = line_list[i][k][0] + 50
        line_list[i][k][1] = line_list[i][k][1] - 50

# find new points using line algorithm
##for i in range(0, len(line_list)):
##    image = add_to_image.main(image,line(line_list[i][0][0],line_list[i][0][1],line_list[i][1][0],line_list[i][1][1]),0,0,0)

image = add_to_image.main(image,line(line_list[0][0][0],line_list[0][0][1],line_list[0][1][0],line_list[0][1][1]),255,0,0)
image = add_to_image.main(image,line(line_list[1][0][0],line_list[1][0][1],line_list[1][1][0],line_list[1][1][1]),0,255,0)

write_ppm.main(image,'Chap3_Exercise1')

print 'printing done'
