# creates human stick figure, Chap 3 problem 10

import one_color
import write_ppm
import add_to_image
import copy
import math

head_circle = [
    [160,200],
    20
    ]
neck = [[160,180],[160,170]]
body_vertexes = [
    [130,170],
    [190,170],
    [190,110],
    [130,110]
    ]
right_arm = [[130,170],[100,100]]
left_arm = [[190,170],[220,100]]
right_hand_circle = [
    [100,100],
    10
    ]
left_hand_circle = [
    [220,100],
    10
    ]
right_leg = [[140,110],[120,50]]
left_leg = [[180,110],[200,50]]
right_foot_ellipse = [
    [120,50],
    20,
    5
    ]
left_foot_ellipse = [
    [200,50],
    20,
    5
    ]

flag_pole = [[100,125],[100,50]]
flag_vertexes = [
    [100,125],
    [100,95],
    [60,110]
    ]

x_translation = 0
y_translation = 35

rotation_angle = 45
rotation_point = [100,100]

x_scale = 1.25
y_scale = 1.25

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

#Function to gather all points -> pixels needed, returns structure
def circle(radius, center_x, center_y):

    biglist = []        #data structure to hold points

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #initialize starting point to (r,0)
    temp.x = radius
    temp.y = 0

    #add points to temporary data structure
    biglist.append([temp.x, temp.y])
    biglist.append([temp.y, temp.x])
    biglist.append([-(temp.x), temp.y])
    biglist.append([temp.y, -(temp.x)])

    while True:

        #compute next y location for the first octant
        temp.y = temp.y + 1

        #compute the corresponding x value for y + 1 using Eq. 2.6
        temp.x = math.sqrt((pow(radius, 2.0)) - (pow(temp.y, 2.0)))

        #Round to the nearest integer value
        temp.x = int(round(temp.x))

        #Check to see if points are still in first octant
        if temp.x == temp.y:

            #compute other points on the circle  by symmetry
            #Don't compute duplicate coordinates
            biglist.append([temp.x, temp.y])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([temp.x, -(temp.y)])
        else:

            #compute other points on the circle  by symmetry
            biglist.append([temp.x, temp.y])
            biglist.append([temp.y, temp.x])
            biglist.append([-(temp.y), temp.x])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([-(temp.y), -(temp.x)])
            biglist.append([temp.y, -(temp.x)])
            biglist.append([temp.x, -(temp.y)])

        if temp.x <= temp.y:
            break

    #add center point to all points
    for i in range(0, len(biglist)):
        temp.x = biglist[i][0] + center_x
        temp.y = biglist[i][1] + center_y

        #add updated/finalized points to data structure
        points.append(copy.deepcopy(temp))

        
    del points[0]   # remove unused location
    return points

#Function to gather all points -> pixels needed, returns structure
def ellipse(a,b, center_x, center_y):
    # a == major axis
    # b == minor axis
    
    biglist = []        #data structure to hold points

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #initialize starting point to (a,0)
    temp.x = a
    temp.y = 0
    
    biglist.append([temp.x, temp.y])
    biglist.append([-(temp.x), temp.y])

    while True:

        #check to see if in region 2
        if ((pow(a, 2.0))*(temp.y +1)) < ((pow(b, 2.0))*(temp.x - 0.5)):

            #compute next y location for region 2
            temp.y = temp.y +1

            #compute the corresponding x value for y + 1 using Eq. 2.8
            temp.x = math.sqrt( (pow(a, 2.0)) * ( 1 - ((pow(temp.y, 2.0))/(pow(b, 2.0)))  ) )

            #Round to the nearest integer value
            temp.x = int(round(temp.x))

            #compute other points on the circle  by symmetry
            biglist.append([temp.x, temp.y])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([temp.x, -(temp.y)])

            #check if still in region 2, if not move on
            if ((pow(a, 2.0))*(temp.y+1)) >= ((pow(b, 2.0))*(temp.x-.5)):
                break
        #if not in region 2, move on to region 1
        else:
            break

    while True:

        #compute next x location for region 1
        temp.x = temp.x - 1

        #compute the y value for x - 1 using Eq. 2.9
        temp.y = math.sqrt( (pow(b, 2.0)) * ( 1 - ((pow(temp.x, 2.0))/(pow(a, 2.0)))  ) )

        #Round to the nearest integer
        temp.y = int(round(temp.y))

        #if x > 0, keep looping through looking to compute y values
        if temp.x == 0:
            biglist.append([temp.x, temp.y])
            biglist.append([temp.x, -(temp.y)])
        else:
            biglist.append([temp.x, temp.y])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([temp.x, -(temp.y)])

        if temp.x <= 0:
            break

    #add center point to all points
    for i in range(0, len(biglist)):
        temp.x = biglist[i][0] + center_x
        temp.y = biglist[i][1] + center_y

        biglist[i][0] = biglist[i][0] + center_x
        biglist[i][1] = biglist[i][1] + center_y

        #add updated/finalized points to data structure
        points.append(copy.deepcopy(temp))

    del points[0]   # remove unused location
    return points

def fill_polygon(vertex_array):

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #find min y-value (ymin) and max y-value (y-max)
    smallest = vertex_array[0][1]
    smallest_index = 0
    largest = vertex_array[0][1]
    largest_index = 0
    
    for i in range(0, len(vertex_array)):
        if vertex_array[i][1] < smallest:
            smallest = vertex_array[i][1]
            smallest_index = i
        if vertex_array[i][1] > largest:
            largest = vertex_array[i][1]
            largest_index = i

    #DEBUG print 'smallest', smallest, '||| largest', largest
    
    smallest_holder = smallest

    #For all the scan lines from ymin to ymax:
    for k in range(smallest, largest+1):

        intersections = []

        #For each edge:
        for j in range(0, len(vertex_array)):

            x_one = vertex_array[j][0]
            y_one = vertex_array[j][1]

            if j == len(vertex_array)-1:
                x_two = vertex_array[0][0]
                y_two = vertex_array[0][1]
            else:
                x_two = vertex_array[j+1][0]
                y_two = vertex_array[j+1][1]

            if y_two - y_one != 0:
                if (y_two <= smallest_holder <= y_one) or (y_one <= smallest_holder <= y_two):
                    y_max = y_one

                    # Find the y-value of the maximal vertex point

                    if y_one >= y_two :
                        y_max = y_one
                    elif y_one < y_two :
                        y_max = y_two

                    if (smallest_holder != y_max) and ((y_two <= smallest_holder <= y_one) or (y_one <= smallest_holder <= y_two)):
                        m_inverse = float(x_two-x_one)/float(y_two-y_one)       # slope inverse

                        x_value = m_inverse*smallest_holder - m_inverse*y_one + x_one
                        x_value = int(round(x_value))

                        temp.x = x_value
                        temp.y = smallest_holder

                        intersections.append([temp.x, temp.y])

        sorted(intersections, key=lambda x: x[0])
        
        for i in range(0, len(intersections), 2):
            
            counter = 0

            big_x = 0
            small_x = 0
            
            if intersections[i][0] > intersections[i+1][0]:
                big_x = intersections[i][0]
                small_x = intersections[i+1][0]
            else:
                big_x = intersections[i+1][0]
                small_x = intersections[i][0]
            
            for x in range(small_x, big_x+1):
                temp.x = small_x + counter
                temp.y = intersections[i][1]

                #add updated/finalized points to data structure
                points.append(copy.deepcopy(temp))

                counter = counter + 1

        smallest_holder = smallest_holder + 1

    del points[0]   # remove unused location
    return points

#Function to gather all points -> pixels needed, returns structure
def fill_circle(radius, center_x, center_y):

    biglist = []        #data structure to hold points

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #initialize starting point to (r,0)
    temp.x = radius
    temp.y = 0

    #add points to temporary data structure
    biglist.append([temp.x, temp.y])
    biglist.append([temp.y, temp.x])
    biglist.append([-(temp.x), temp.y])
    biglist.append([temp.y, -(temp.x)])

    while True:

        #compute next y location for the first octant
        temp.y = temp.y + 1

        #compute the corresponding x value for y + 1 using Eq. 2.6
        temp.x = math.sqrt((pow(radius, 2.0)) - (pow(temp.y, 2.0)))

        #Round to the nearest integer value
        temp.x = int(round(temp.x))

        #Check to see if points are still in first octant
        if temp.x == temp.y:

            #compute other points on the circle  by symmetry
            #Don't compute duplicate coordinates
            biglist.append([temp.x, temp.y])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([temp.x, -(temp.y)])
        else:

            #compute other points on the circle  by symmetry
            biglist.append([temp.x, temp.y])
            biglist.append([temp.y, temp.x])
            biglist.append([-(temp.y), temp.x])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([-(temp.y), -(temp.x)])
            biglist.append([temp.y, -(temp.x)])
            biglist.append([temp.x, -(temp.y)])

        if temp.x <= temp.y:
            break

    #add center point to all points
    for i in range(0, len(biglist)):
        temp.x = biglist[i][0] + center_x
        temp.y = biglist[i][1] + center_y
        biglist[i][0] = biglist[i][0] + center_x
        biglist[i][1] = biglist[i][1] + center_y
        
        #add updated/finalized points to data structure
        #points.append(copy.deepcopy(temp))

    smallest = biglist[0][1]
    smallest_index = 0
    largest = biglist[0][1]
    largest_index = 0

    #Find minimum and maximum y values of the circle and their indexes
    for i in range(1, len(biglist)):
        if biglist[i][1]< smallest:
            smallest = biglist[i][1]
            smallest_index = i
        if biglist[i][1] > largest:
            largest = biglist[i][1]
            largest_index = i
            
    left_boundary_index = smallest_index
    right_boundary_index = smallest_index

    smallest_holder = smallest
    
    for k in range(smallest, largest+1):
        
        # list for holding values as we iterate through each row
        rowlist = []


        #find all points in circle with this common y value
        for i in range(0, len(biglist)):
            if biglist[i][1] == (smallest_holder):
                rowlist.append(biglist[i])

        smallest_x = rowlist[0][0]
        smallest_x_index = 0
        largest_x = rowlist[0][0]
        largest_x_index = 0

        #Find points in rowlist that have largest and smallest x values
        for i in range(1, len(rowlist)):
            if rowlist[i][0]< smallest_x:
                smallest_x = rowlist[i][0]
                smallest_x_index = i
            if rowlist[i][0] > largest_x:
                largest_x = rowlist[i][0]
                largest_x_index = i

        # cycle through row and add all copy points
        counter = 0
        for i in range(rowlist[smallest_x_index][0],rowlist[largest_x_index][0]):
            temp.x = rowlist[smallest_x_index][0] + counter
            temp.y = rowlist[smallest_x_index][1]

            #add updated/finalized points to data structure
            points.append(copy.deepcopy(temp))

            counter = counter + 1

        rowlist = []
        smallest_holder = smallest_holder + 1

    del points[0]   # remove unused location
    return points

#Function to gather all points -> pixels needed, returns structure
def fill_ellipse(a,b, center_x, center_y):
    # a == major axis
    # b == minor axis
    
    biglist = []        #data structure to hold points

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #initialize starting point to (a,0)
    temp.x = a
    temp.y = 0
    
    biglist.append([temp.x, temp.y])
    biglist.append([-(temp.x), temp.y])

    while True:

        #check to see if in region 2
        if ((pow(a, 2.0))*(temp.y +1)) < ((pow(b, 2.0))*(temp.x - 0.5)):

            #compute next y location for region 2
            temp.y = temp.y +1

            #compute the corresponding x value for y + 1 using Eq. 2.8
            temp.x = math.sqrt( (pow(a, 2.0)) * ( 1 - ((pow(temp.y, 2.0))/(pow(b, 2.0)))  ) )

            #Round to the nearest integer value
            temp.x = int(round(temp.x))

            #compute other points on the circle  by symmetry
            biglist.append([temp.x, temp.y])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([temp.x, -(temp.y)])

            #check if still in region 2, if not move on
            if ((pow(a, 2.0))*(temp.y+1)) >= ((pow(b, 2.0))*(temp.x-.5)):
                break
        #if not in region 2, move on to region 1
        else:
            break

    while True:

        #compute next x location for region 1
        temp.x = temp.x - 1

        #compute the y value for x - 1 using Eq. 2.9
        temp.y = math.sqrt( (pow(b, 2.0)) * ( 1 - ((pow(temp.x, 2.0))/(pow(a, 2.0)))  ) )

        #Round to the nearest integer
        temp.y = int(round(temp.y))

        #if x > 0, keep looping through looking to compute y values
        if temp.x == 0:
            biglist.append([temp.x, temp.y])
            biglist.append([temp.x, -(temp.y)])
        else:
            biglist.append([temp.x, temp.y])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([temp.x, -(temp.y)])

        if temp.x <= 0:
            break

    #add center point to all points
    for i in range(0, len(biglist)):
        temp.x = biglist[i][0] + center_x
        temp.y = biglist[i][1] + center_y

        biglist[i][0] = biglist[i][0] + center_x
        biglist[i][1] = biglist[i][1] + center_y

        #add updated/finalized points to data structure
        #points.append(copy.deepcopy(temp))

    smallest = biglist[0][1]
    smallest_index = 0
    largest = biglist[0][1]
    largest_index = 0

    #Find minimum and maximum y values of the circle and their indexes
    for i in range(1, len(biglist)):
        if biglist[i][1]< smallest:
            smallest = biglist[i][1]
            smallest_index = i
        if biglist[i][1] > largest:
            largest = biglist[i][1]
            largest_index = i
            
    left_boundary_index = smallest_index
    right_boundary_index = smallest_index

    smallest_holder = smallest
    
    for k in range(smallest, largest+1):
        
        # list for holding values as we iterate through each row
        rowlist = []


        #find all points in circle with this common y value
        for i in range(0, len(biglist)):
            if biglist[i][1] == (smallest_holder):
                rowlist.append(biglist[i])

        smallest_x = rowlist[0][0]
        smallest_x_index = 0
        largest_x = rowlist[0][0]
        largest_x_index = 0

        #Find points in row that have largest and smallest x values
        for i in range(1, len(rowlist)):
            if rowlist[i][0]< smallest_x:
                smallest_x = rowlist[i][0]
                smallest_x_index = i
            if rowlist[i][0] > largest_x:
                largest_x = rowlist[i][0]
                largest_x_index = i

        # cycle through row and add all copy points
        counter = 0
        for i in range(rowlist[smallest_x_index][0],rowlist[largest_x_index][0]):
            temp.x = rowlist[smallest_x_index][0] + counter
            temp.y = rowlist[smallest_x_index][1]

            #add updated/finalized points to data structure
            points.append(copy.deepcopy(temp))

            counter = counter + 1

        rowlist = []
        smallest_holder = smallest_holder + 1

    del points[0]   # remove unused location
    return points


# Create image with a white background
image = one_color.main(320,240,255,255,255)

# Draw the head
image = add_to_image.main(image,fill_circle(head_circle[1],head_circle[0][0],head_circle[0][1]),255,255,0)
image = add_to_image.main(image,circle(head_circle[1],head_circle[0][0],head_circle[0][1]),0,0,0)

# Draw the neck
image = add_to_image.main(image,line(neck[0][0],neck[0][1],neck[1][0],neck[1][1]),0,0,0)

# Draw the body (polygon)
image = add_to_image.main(image,fill_polygon(body_vertexes),0,0,255)
for i in range(0, len(body_vertexes)):
    if i == len(body_vertexes)-1:
        image = add_to_image.main(image,line(body_vertexes[i][0],body_vertexes[i][1],body_vertexes[0][0],body_vertexes[0][1]),255,0,0)
    else:
        image = add_to_image.main(image,line(body_vertexes[i][0],body_vertexes[i][1],body_vertexes[i+1][0],body_vertexes[i+1][1]),255,0,0)

# Draw the right hand, fill it with color
image = add_to_image.main(image,fill_circle(right_hand_circle[1],right_hand_circle[0][0],right_hand_circle[0][1]),255,0,0)
image = add_to_image.main(image,circle(right_hand_circle[1],right_hand_circle[0][0],right_hand_circle[0][1]),0,255,0)

# Draw the left hand, fill it with color
image = add_to_image.main(image,fill_circle(left_hand_circle[1],left_hand_circle[0][0],left_hand_circle[0][1]),255,0,0)
image = add_to_image.main(image,circle(left_hand_circle[1],left_hand_circle[0][0],left_hand_circle[0][1]),0,255,0)

# Draw the right arm
image = add_to_image.main(image,line(right_arm[0][0],right_arm[0][1],right_arm[1][0],right_arm[1][1]),0,0,0)

# Draw the left arm
image = add_to_image.main(image,line(left_arm[0][0],left_arm[0][1],left_arm[1][0],left_arm[1][1]),0,0,0)

# Draw the right foot
image = add_to_image.main(image,fill_ellipse(right_foot_ellipse[1],right_foot_ellipse[2],right_foot_ellipse[0][0],right_foot_ellipse[0][1]),0,255,0)
image = add_to_image.main(image,ellipse(right_foot_ellipse[1],right_foot_ellipse[2],right_foot_ellipse[0][0],right_foot_ellipse[0][1]),0,0,255)

# Draw the left foot
image = add_to_image.main(image,fill_ellipse(left_foot_ellipse[1],left_foot_ellipse[2],left_foot_ellipse[0][0],left_foot_ellipse[0][1]),0,255,0)
image = add_to_image.main(image,ellipse(left_foot_ellipse[1],left_foot_ellipse[2],left_foot_ellipse[0][0],left_foot_ellipse[0][1]),0,0,255)

# Draw the right leg
image = add_to_image.main(image,line(right_leg[0][0],right_leg[0][1],right_leg[1][0],right_leg[1][1]),0,0,0)

# Draw the left leg
image = add_to_image.main(image,line(left_leg[0][0],left_leg[0][1],left_leg[1][0],left_leg[1][1]),0,0,0)

# Draw the flag
#   1. Translate the flag points - add xt, yt to the x values, y values
for i in range(0, len(flag_vertexes)):
    flag_vertexes[i][0] = flag_vertexes[i][0] + x_translation
    flag_vertexes[i][1] = flag_vertexes[i][1] + y_translation
for i in range(0, len(flag_pole)):
    flag_pole[i][0] = flag_pole[i][0] + x_translation
    flag_pole[i][1] = flag_pole[i][1] + y_translation

#   2. Rotate the results
# translate end and start pts to origin using translation algorithm
for i in range(0, len(flag_vertexes)):
    flag_vertexes[i][0] = flag_vertexes[i][0] - rotation_point[0]
    flag_vertexes[i][1] = flag_vertexes[i][1] - rotation_point[1]
for i in range(0, len(flag_pole)):
    flag_pole[i][0] = flag_pole[i][0] - rotation_point[0]
    flag_pole[i][1] = flag_pole[i][1] - rotation_point[1]

# Rotate x values, y values, round them
for i in range(0, len(flag_vertexes)):
    x = flag_vertexes[i][0]
    y = flag_vertexes[i][1]
    flag_vertexes[i][0] = int(round((x)*(math.cos(math.radians(rotation_angle))) - (y)*(math.sin(math.radians(rotation_angle)))))
    flag_vertexes[i][1] = int(round((y)*(math.cos(math.radians(rotation_angle))) + (x)*(math.sin(math.radians(rotation_angle)))))
for i in range(0, len(flag_pole)):
    x = flag_pole[i][0]
    y = flag_pole[i][1]
    flag_pole[i][0] = int(round((x)*(math.cos(math.radians(rotation_angle))) - (y)*(math.sin(math.radians(rotation_angle)))))
    flag_pole[i][1] = int(round((y)*(math.cos(math.radians(rotation_angle))) + (x)*(math.sin(math.radians(rotation_angle)))))

# translate end and start pts back
for i in range(0, len(flag_vertexes)):
    flag_vertexes[i][0] = flag_vertexes[i][0] + rotation_point[0]
    flag_vertexes[i][1] = flag_vertexes[i][1] + rotation_point[1]
for i in range(0, len(flag_pole)):
    flag_pole[i][0] = flag_pole[i][0] + rotation_point[0]
    flag_pole[i][1] = flag_pole[i][1] + rotation_point[1]

#   3. Scale the results
# translate end and start pts to origin using translation algorithm
for i in range(0, len(flag_vertexes)):
    flag_vertexes[i][0] = flag_vertexes[i][0] - rotation_point[0]
    flag_vertexes[i][1] = flag_vertexes[i][1] - rotation_point[1]
for i in range(0, len(flag_pole)):
    flag_pole[i][0] = flag_pole[i][0] - rotation_point[0]
    flag_pole[i][1] = flag_pole[i][1] - rotation_point[1]

# Scale x values, y values, round them
for i in range(0, len(flag_vertexes)):
    flag_vertexes[i][0] = int(round((flag_vertexes[i][0])*(x_scale)))
    flag_vertexes[i][1] = int(round((flag_vertexes[i][1])*(y_scale)))
for i in range(0, len(flag_pole)):
    flag_pole[i][0] = int(round((flag_pole[i][0])*(x_scale)))
    flag_pole[i][1] = int(round((flag_pole[i][1])*(y_scale)))

# translate end and start pts back
for i in range(0, len(flag_vertexes)):
    flag_vertexes[i][0] = flag_vertexes[i][0] + rotation_point[0]
    flag_vertexes[i][1] = flag_vertexes[i][1] + rotation_point[1]
for i in range(0, len(flag_pole)):
    flag_pole[i][0] = flag_pole[i][0] + rotation_point[0]
    flag_pole[i][1] = flag_pole[i][1] + rotation_point[1]

# Fill in flag color
image = add_to_image.main(image,fill_polygon(flag_vertexes),255,0,255)

# add to image and draw
image = add_to_image.main(image,line(flag_pole[0][0],flag_pole[0][1],flag_pole[1][0],flag_pole[1][1]),0,0,0)
for i in range(0, len(flag_vertexes)):
    if i == len(flag_vertexes)-1:
        image = add_to_image.main(image,line(flag_vertexes[i][0],flag_vertexes[i][1],flag_vertexes[0][0],flag_vertexes[0][1]),0,0,0)
    else:
        image = add_to_image.main(image,line(flag_vertexes[i][0],flag_vertexes[i][1],flag_vertexes[i+1][0],flag_vertexes[i+1][1]),0,0,0)

#Write to ppm file
write_ppm.main(image,'Chap3_Exercise10')

print 'printing done'
