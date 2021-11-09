import imageio as iio
import cv2
import numpy as np

def gif_to_genga(src_gif=None, out_dir=None):
    im = iio.get_reader(src_gif)
    counter = 0
    for frame in im:
        img = cv2.bitwise_not(frame)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
        cv2.merge((gray, gray, gray), img)
        kernel = np.ones((4,4),np.uint8)
        dilation = cv2.dilate(img,kernel,iterations = 1)
        diff = cv2.subtract(dilation, img)
        negaposi = 255 - diff
        genga = cv2.cvtColor(negaposi, cv2.COLOR_BGR2GRAY) 
        outfile = str(out_dir) + '/' + str(counter) + '.jpg'
        cv2.imwrite(outfile, genga)
        counter += 1
