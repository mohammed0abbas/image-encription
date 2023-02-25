from tkinter import *
from PIL import ImageTk, Image
import histogram as hist




def open_form_output(img_org,img,snr,psnr,msc,sim):
    
    
    root = Tk()
    root.geometry('500x550')
    root.title('Output')
    width, height = img.size
    temp = width/300
    img = ImageTk.PhotoImage(img.resize(size=(int(width/temp), int(height/temp))))
    panel = Label(root, image = img)
    panel.place(x=50,y=200)

    img_org = ImageTk.PhotoImage(img_org.resize(size=(int(width/temp), int(height/temp))))
    panel = Label(root, image = img_org)
    panel.place(x=50,y=10)


    Label(root, text=f"SNR = {snr} db").place(x=50,y=450)
    Label(root, text=f"PSNR = {psnr}").place(x=250,y=450)
    Label(root, text=f"MSE = {msc}").place(x=50,y=480)
    Label(root, text=f"SSIM = {sim}").place(x=250,y=480)
   

    app.mainloop()



