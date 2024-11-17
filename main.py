from tkinter import *

window = Tk()
window.title("Mile to Kilometer Calculator")
window.minsize(500,300)
window.config(padx=20,pady=20)

#label

mile_entry = Entry()
mile_entry.grid(column=1, row=0)
label1 = Label(text="Miles",font=("Aerial", 24, "bold"))
label1.grid(column=2,row=0 )
label2 = Label(text="is equal to",font=("Aerial", 24, "bold"))
label2.grid(column=0, row=1)
def button_clicked():
    val = int(mile_entry.get())
    km_label["text"]=f"{round(1.609*val,2)}"

km_label = Label(text=0,font=("Aerial", 24, "bold"))
km_label.grid(column=1, row=1)
label3 = Label(text="Km",font=("Aerial", 24, "bold"))
label3.grid(column=2, row=1)

button = Button(text="calculate", command=button_clicked)
button.grid(column=1, row=2)

    # label1["text"]=val





window.mainloop()