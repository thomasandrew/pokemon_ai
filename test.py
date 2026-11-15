from tkinter import *
root = Tk()
root.geometry("400x400")
bg = PhotoImage(file = "pokeimg.png")
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)
root.mainloop()