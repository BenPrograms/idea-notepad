from tkinter import *

class navBar():
    
    def __init__(self, master):
        
        #Top bar and lower bar
        frame = Frame(master)
        frame.pack()

        menu = Menu(master)
        root.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu = subMenu)
        subMenu.add_command(label="Exit", command = exit)

        status = Label(master, text="Version 1.0", bd = 1, relief = SUNKEN, anchor = W)
        status.pack(side=BOTTOM, fill = X)

        #app stuff
        user_entry = "user entry"

        frame3 = Frame(root)
        frame3.pack(side=TOP)
                
        label = Label(frame3, text="WELCOME TO NOTEPAD")
        label.config(font=("Courier", 24))
        label.pack(side=TOP)
        self.entry_1 = Entry(frame3, width=50)
        self.entry_1.config(font=("Courier", 12))
        self.entry_1.pack(side=LEFT, pady = 15, padx = 5)
                
        postB = Button(frame3, text="Post", command = self.user, width = 10)
        postB.pack(side=LEFT, padx = 5, pady = 30)

    def user(self):
        clear = False
        
        user_entry = self.entry_1.get()
        
        print(user_entry)

        frame2 = Frame(root)
        frame2.pack(side= TOP)
        
        post = Label(frame2, text=user_entry)
        post.config(font=("Courier", 12))
        post.pack(side=LEFT)
    
    def export(self):
        print("file exported")

root = Tk()
nav = navBar(root)

root.title('NOTEPAD')
root.iconbitmap('favicon.bmp')
root.mainloop()
