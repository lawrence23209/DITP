from tkinter import * # import everything from Tk

root = Tk() # top level window

# Create label
label = Label(root, text="Hello Python")
label.pack()

# Create button(without command does not do anything)
button = Button(root, text='Click Me!')
button.pack()

root.geometry("350x300")
root.mainloop() # this always at the end of the code