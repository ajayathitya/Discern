import numpy as np
import cv2
from PIL import Image
import PIL.ImageOps    


im = cv2.imread('image.png')
im[im == 255] = 1
im[im == 0] = 255
im[im == 1] = 0

im2 = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(im2,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
h_list=[]
for cnt in contours:
    [x,y,w,h] = cv2.boundingRect(cnt)
    if w*h>10000:
        h_list.append([x,y,w,h])
#print h_list          
ziped_list=list(zip(*h_list))
x_list=list(ziped_list[0])
dic=dict(zip(x_list,h_list))
x_list.sort()
i=0
for x in x_list:
      [x,y,w,h]=dic[x]
      #cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),1)
      im3=im[y:y+h,x:x+w]
      re = cv2.resize(im3, (28, 28))
      cv2.imwrite('pix%i.png'%i,re)
      i+=1
      
      cv2.imshow('norm',im)
key = cv2.waitKey(0)
image = Image.open('pix0.png')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('new_name.png')
