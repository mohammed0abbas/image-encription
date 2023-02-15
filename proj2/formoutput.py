from tkinter import *
from PIL import ImageTk, Image




def open_form_output(img,snr,psnr,msc,sim):
    
    
    root = Tk()
    root.geometry('500x400')
    root.title('Output')
    width, height = img.size
    temp = width/300
    img = ImageTk.PhotoImage(img.resize(size=(int(width/temp), int(height/temp))))
    panel = Label(root, image = img)
    panel.place(x=50,y=10)

    Label(root, text=f"SNR = {snr} db").place(x=50,y=330)
    Label(root, text=f"PSNR = {psnr}").place(x=250,y=330)
    Label(root, text=f"MSE = {msc}").place(x=50,y=350)
    Label(root, text=f"SSIM = {sim}").place(x=250,y=350)
   

    app.mainloop()



