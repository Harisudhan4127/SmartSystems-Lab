from tkinter import *
from tkinter import messagebox
root= Tk()
root.geometry('900x506')
root.title('Check Box Testing ')
# root.iconbitmap('Avengers.ico')
bg = PhotoImage("marvel_doctor_strange.jpg", width= 900 ,   height= 506 ) 
root.config(background= '#FE0000')

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()

def add():
    print('Saving')
    # print(bg)
    if c1.get == 1 :
        val =chk1.cget('text')
        print(val)
        messagebox.showerror("message", val)
    if c2.get() == 1 :
        val = chk2.cget('text')
        print(val)
        messagebox.showwarning("message", val)
    if c3.get() == 1 :
        val = chk3.cget('text')
        print(val)
        messagebox.showinfo("message", val)
        
    
def remove():
    print('remove')
    chk1.deselect()
    chk2.deselect()
    chk3.deselect()
    messagebox.showinfo("remove","checkbox all are cleared")
    
    
    
l1 = Label(root, text = "Check Box", font = ("Arial Black", 32), bg = '#FE0000', fg='#DDDDDD',width= 10 ,height= 2)
l1.pack(fill= 'x')

chk1 = Checkbutton(root, text = "Java",font = ("Arial", 22), variable= c1,onvalue= 1, offvalue= 0, bg = "LightGray", fg= "black", width= 10 ,height= 1, bd= 2)
chk2 = Checkbutton(root, text = "Python",font = ("Arial", 22), variable= c2,onvalue= 1, offvalue= 0, bg = "LightGray", fg= "black", width= 10 ,height= 1, bd= 2)
chk3 = Checkbutton(root, text = "C & C++",font = ("Arial ", 22), variable= c3,onvalue= 1, offvalue= 0, bg = "LightGray", fg= "black", width= 10 ,height= 1, bd= 2)

btn_save  = Button(root, text = "Save",font = ("Arial", 22, "bold"), bg= "LightGray", fg= "#000000", width= 5, height= 1, command = add())
btn_remove = Button(root, text = "Clear",font = ("Arial", 22, "bold"), bg= "LightGray", fg= "#000000" ,width= 5, height= 1, command = remove())

chk1.pack()
chk2.pack()
chk3.pack()
btn_save.pack()
btn_remove.pack()

root.mainloop()

