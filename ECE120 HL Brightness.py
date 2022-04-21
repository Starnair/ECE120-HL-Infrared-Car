from PIL import Image
import numpy as np
import time

while True:
    imag = Image.open("Cam")
    imag = imag.convert ('RGB')

    left_list = []
    right_list = []
    total_list = []
    for X in range(25):
        for Y in range(33):
            pixelRGB = imag.getpixel((X,Y))
            R, G, B = pixelRGB
            brightness = sum(R, G, B)/3
            if X<13:
                left_list.append(brightness)

            else:
                right_list.append(brightness)

    left_sum = sum(left_list)
    right_sum = sum(right_list)

    if left_sum > right_sum:
        #turn left and go forward
    elif left_sum < right_sum:
        #turn right and go forward
    elif left_sum = right_sum:
        # Since it is very rare to get this, we might need to set error bounds.
        # If the result falls in error bound (e.g. there is not significant difference in
        # left_sum and right_sum), we assume right and left has similar magnitude of heat source
        total_list = left_list + right_list
        total_sum = sum(total_list)
        if total_sum > #certain number(brightness):
            #drive forward
        else:
            #stop
    time.sleep(1)  #code runs every 1 second
