from tkinter import *
import custom_button
# create window 
root = Tk()
root.title("Calculaator")
root.iconbitmap("image\calculator.ico")
root.configure(bg ='white')

def on_click(number):
    s.insert(END, number)
    
def calculate():
    ans = eval(s.get())
    s.delete(0, END)
    s.insert(END, ans)

s = Entry(root,width=50,borderwidth=10,bg="white",justify=RIGHT)
s.grid(row=0,column=0,columnspan=3,padx=15,pady=15)

button_7 = Button(root, text ="7",padx=40,pady=35,bg='navy blue',fg='white', command=lambda:on_click('7'))
button_7.grid(row=2, column=0)

button_8 = Button(root, text ="8",padx=40,pady=35,bg='navy blue',fg='white', command=lambda:on_click('8'))
button_8.grid(row=1, column=1)

button_9 = Button(root, text ="9",padx=40,pady=35, bg='navy blue',fg='white',command=lambda:on_click('9'))
button_9.grid(row=1, column=0)

button_4 = Button(root, text ="4",padx=40,pady=35,bg='navy blue',fg='white', command=lambda:on_click('4'))
button_4.grid(row=3, column=1)

button_5 = Button(root, text ="5", padx=40,pady=35 ,bg='navy blue',fg='white', command=lambda:on_click('5'))
button_5.grid(row=3, column=0)

button_6 = Button(root, text ="6", padx=40,pady=35 ,bg='navy blue',fg='white', command=lambda:on_click('6'))
button_6.grid(row=2, column=1)

button_1 = Button(root, text ="1",padx=40,pady=35 , bg='navy blue',fg='white',command=lambda:on_click('1'))
button_1.grid(row=5, column=0)

button_2 = Button(root, text ="2", padx=40,pady=35 , bg='navy blue',fg='white',command=lambda:on_click('2'))
button_2.grid(row=4, column=1)

button_3 = Button(root, text ="3", padx=40,pady=35,bg='navy blue',fg='white', command=lambda:on_click('3'))
button_3.grid(row=4, column=0)

button_0 = Button(root, text ="0", padx=40,pady=35 ,bg='navy blue',fg='white', command=lambda:on_click('0'))
button_0.grid(row=5, column=1)

#+-*/
add_btn = Button(root, text ="+", padx=40,pady=35 ,bg='navy blue',fg='white', command=lambda:on_click('+'))
add_btn.grid(row=1, column=2)

minus_btn = Button(root, text ="-", padx=40,pady=35 ,bg='navy blue',fg='white', command=lambda:on_click('-'))
minus_btn.grid(row=2, column=2)

multlipy_btn = Button(root, text ="x",padx=40,pady=35, bg='navy blue',fg='white',command=lambda:on_click('*'))
multlipy_btn.grid(row=3, column=2)

divide_btn = Button(root, text ="÷", padx=40,pady=35 , bg='navy blue',fg='white',command=lambda:on_click('/'))
divide_btn.grid(row=4, column=2)

calculate_btn = Button(root, text ="=", padx=40,pady=35 , bg='navy blue',fg='white',command=calculate)
calculate_btn.grid(row=5, column=2)

clear_btn = Button(root, text ="AC",padx=40,pady=35 , bg='navy blue',fg='white',command=lambda:s.delete(0, END))
clear_btn.grid(row=6, column=0,columnspan=3)




root.mainloop()


