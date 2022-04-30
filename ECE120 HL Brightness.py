from PIL import Image

while True:
    imag = Image.open("Cam")                       #load camera input
    imag = imag.convert ('RGB')                    #convert camera input in terms of RGB value
    error_bound = #some number                     #set a number that will tell us when the difference between rightside and leftside 
    minimum_brightness = #some number              #set a number that will tell us if there is no light sources to follow
    left_list = []
    right_list = []
    total_list = []
    for X in range(33):
        for Y in range(25):
            pixelRGB = imag.getpixel((X,Y))
            R, G, B = pixelRGB
            brightness = sum(R, G, B)/3            #iterate throughout the whole image from the camera, calculate brightness and store it in appropriate side
            if X<13:
                left_list.append(brightness)

            else:
                right_list.append(brightness)

    left_sum = sum(left_list)                       #The sum of RGB values in pixels from leftside
    right_sum = sum(right_list)                     #The sum of RGB values in pixels from right side

    if left_sum - right_sum > error_bound:          #sum in left side is larger than rightside, and difference exceeds error bound
        #drive toward left
    elif right_sum - left_sum > error_bound:        #sum in right side is larger than leftside, and difference exceeds error bound
        #drive towards right
    elif abs(left_sum - right_sum) < error_bound:   #difference between leftside and rightside is not significant.
        total_list = left_list + right_list         
        total_sum = sum(total_list)                 #add all pixel's RGB values in the image
        if total_sum < minimum_brightness:          #if the input from camera is generally dark (i.e. no light source)
            #stop
        else:
            #drive forward
    
