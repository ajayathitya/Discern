from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import cv2

width = 1000
height = 300
center = height//2
white = (255, 255, 255)
green = (0,128,0)

def save():
    filename = "image.png"
    image1.save(filename)
    root.destroy()

def paint(event):
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=15)
    draw.line([x1, y1, x2, y2],fill="black",width=15)

root = Tk()
root.title("Discern")

cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

button=Button(text="Save",command=save)
button2 = Button(text="Clear",command =save)
button.pack()
root.mainloop()
