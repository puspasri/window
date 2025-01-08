from tkinter import *
window=Tk()


window.geometry("700x800")



label=Label(window,text="name",fg="white",bg="black",width=100,height=1)
label.pack()

entry=Entry(bg="green",fg="blue",width=50)
entry.pack()


def display():
    name=entry.get()
    msg="welcome to tkinter coding with SS"
    greeting="hello" +name+"\n"
    text.insert(END,greeting)
    text.insert(END,msg)
text=Text()
text.pack()
button=Button(text="click on me please ",fg="black",bg="orange",width=20,height=1,command=display)
button.pack()
window.mainloop()