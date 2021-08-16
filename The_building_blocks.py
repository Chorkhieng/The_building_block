from tkinter import *
from tkinter import colorchooser

# import time, might need to import time later
 
    

def add_block(): # to add block
    print("Add Block!") # TODO
    #label = Label(window, bg="red", width=10, height=5)
    label.place(x=0, y=0)
    label.forget()

    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)  

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    print("Selected!")

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)
    print("Dragged!")

def change_size(): # to change the size of the selected block
    print("Change Size!") # TODO

def change_color(): # to change color of each block
    print("Change Color!")
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex) # print to hexadecimal value
    label.config(bg=colorHex) # change the label color
 
def move_block(): # to move any selected block
    print("Move Block!") # TODO
       
def delete_block(): # to delete block
    print("Deleted!") # TODO
    label.destroy()    

def background_color():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex) # print to hexadecimal value
    canvas.config(bg=colorHex) # change background color

window = Tk()

#window.geometry("420x420")
window.title("The Building Block")
#size of the board
WIDTH = 600
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="cyan")
#canvas.create_line(0, 0, 500, 500, fill="blue", width=10) # line (starting point, ending point)
#canvas.create_line(0, 500, 500, 0, fill="red", width=10)
#canvas.create_rectangle(50, 50, 250, 250, fill="purple")
#canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="green", outline="black", width=10)
#canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=180, fill="blue", extent=180)
#canvas.create_oval(190, 190, 310, 310, fill="white", width=10)
canvas.pack()
label = Label(window, width=10, height=5)
label.pack()


# add button
button_add = Button(window, text="Add Block",
                command=add_block,
                font=("Comic Sans", 10),
                fg="purple",
                bg="green",
                activeforeground="purple",
                activebackground="green",
                state=ACTIVE,
                )
# to change background color
button_background_color = Button(window, text="Change Background Color",  # the text that will show on the button
                                command=background_color,
                                font=("Comic Sans", 10),
                                fg="purple",
                                bg="green",
                                activebackground="purple",                              
                                )

button_background_color.pack(side=LEFT)

button_add.pack(side=LEFT)

# to change size button
button_size = Button(window, text="Change Size",
                command=change_size,
                font=("Comic Sans", 10),
                fg="purple",
                bg="green",
                activeforeground="purple",
                activebackground="green",
                state=ACTIVE,   # to be able to click multiple times
                )

button_size.pack(side=LEFT)

# to change color button
button_color = Button(window, text="Change Color",
                command=change_color,
                font=("Comic Sans", 10),
                fg="purple",
                bg="green",
                activeforeground="purple",
                activebackground="green",
                state=ACTIVE,
                )

button_color.pack(side=LEFT)

# to move the block button
button_move = Button(window, text="Move Block",
                command=move_block,
                font=("Comic Sans", 10),
                fg="purple",
                bg="green",
                activeforeground="purple",
                activebackground="green",
                state=ACTIVE,
                )

button_move.pack(side=LEFT)

# to delete button
button_delete = Button(window, text="Delete",
                command=delete_block,
                font=("Comic Sans", 10),
                fg="purple",
                bg="green",
                activeforeground="purple",
                activebackground="green",
                state=ACTIVE,
                )

button_delete.pack(side=LEFT)

# the quit button
button_quit = Button(window, text="Exit",
                command=quit,
                font=("Comic Sans", 10),
                fg="purple",
                bg="green",
                activeforeground="purple",
                activebackground="green",
                state=ACTIVE,
                )

button_quit.pack(side=LEFT)

window.mainloop()