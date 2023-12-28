from tkinter import*
from PIL import Image,ImageTk # pip install pillow
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Regiseration Window")
        self.root.geometry("1350x700+0+0")
        #==Bg Image===
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")     #Variable
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #===LEFT Image===
        self.left=ImageTk.PhotoImage(file="images/side.jpg")
        left = Label(self.root,image=self.left).place(x=80,y=100,width=40,height=500)

root=Tk()
obj=Register(root)
root.mainloop()