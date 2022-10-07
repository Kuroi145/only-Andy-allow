from cProfile import label
from cgitb import text
from email.mime import image
import tkinter
import googletrans
from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator

# tạo giao diện
root = Tk()
root.title('Google Galaxy') #tên ứng dụng
root.geometry('600x770') # chỉnh kích thước giao diện
root.iconbitmap('D:\Project\gg transfake\logo.ico') # tạo logo

load = Image.open('D:\Project\gg transfake\sky.png')
render = ImageTk.PhotoImage(load)
img =Label(root, image=render)
img.place(x=0, y= 0)

name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg='#00142C')#fg để chỉnh màu kiếm code màu trên mạng là có vd:#FFFFFF là màu trắng
name.config(font=("D:\Project\gg transfake\Transformers Movie.ttf",30))  #chèn và chỉnh kích thước phông chữ
name.pack(pady=10)

box= Text(root, width=28,height=8, font=("Times New Roman",16)) #tạo 2 hộp để nhập và xuất dữ liệu
box.pack(pady=20)
box1= Text(root, width=28,height=8, font=("Times New Roman",16))
box1.pack(pady=80)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate(): #phương thức dịch 
    INPUT=box.get(1.0,END)
    print(INPUT)
    t =Translator()
    a = t.translate(INPUT, src="vi", dest="en")
    b = a.text
    box1.insert(END,b)

clear_button=Button(button_frame,text="Clear Text" ,font=(("Arial"),10,'bold'), bg='#303030', fg="#FFFFFF", command=clear) #nút reset
clear_button.place(x=150,y=380)
trans_button=Button(button_frame,text="Translate" ,font=(("Arial"),10,'bold'), bg='#303030', fg="#FFFFFF", command=translate) #nút bắt đầu dịch
trans_button.place(x=350,y=380)

root.mainloop()