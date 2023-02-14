from tkinter import * 
from tkinter import filedialog as fd
from encript import * 




filed = ''

base = Tk() 
base.geometry('500x400')  



def open_file():
    filed = fd.askopenfilename()
    entery.config(text=filed)
    
    

btn = Button(base, text ='select image', command = open_file)
btn.place(x=50,y=50)


entery = Label(base , width=50 , bg='white', fg='black',text=filed)
entery.place(x=130,y=55)


Label(base, text="Enter the name of the image file:").place(x=130,y=75)

Label(base, text="R               G                  B").place(x=100,y=120)






r1,r2,r3,g1,g2,g3,b1,b2,b3 = [IntVar() for i in range(9)]

Checkbutton(base,variable=r1).place(x=100,y=150)
Checkbutton(base,variable=r2).place(x=100,y=180)
Checkbutton(base,variable=r3).place(x=100,y=210)

Checkbutton(base,variable=g1).place(x=150,y=150)
Checkbutton(base,variable=g2).place(x=150,y=180)
Checkbutton(base,variable=g3).place(x=150,y=210)


Checkbutton(base,variable=b1, text="Henon Map").place(x=210,y=150)
Checkbutton(base,variable=b2, text="Skew Tent Map").place(x=210,y=180)
Checkbutton(base,variable=b3, text="Bernulli Map").place(x=210,y=210)



def Encrypted():
    r = [r1.get(),r2.get(),r3.get()]
    g = [g1.get(),g2.get(),g3.get()]
    b = [b1.get(),b2.get(),b3.get()]

    
    print(r,g,b)
    img = Encrypt(entery.cget('text'), r, g, b)

    img.show()
    

Button(base, text ='Encrypt', command = Encrypted).place(x=100,y=250)



# Start the GUI event loop
base.mainloop()




   