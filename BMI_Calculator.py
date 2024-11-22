from tkinter import *

window = Tk()
window.title("BMI Calculater")
window.minsize(width=350,height=250)
window.config(padx=30,pady=30)
FONT = ("Arial",12,"normal")

#weight label - entry
weight_label = Label(text="Enter Your Weight(kg)",font=FONT)
weight_label.pack()
weight_entry = Entry(width=20)
weight_entry.focus()
weight_entry.pack()


#height label - entry
height_label = Label(text="Enter Your Height(cm)",font=FONT)
height_label.pack()
height_entry = Entry(width=20)
height_entry.pack()

#weight validation
def weight_validation(weight,height):
    if weight.isdigit() and height.isdigit():
        return True
    return False

#button
def button_calculater():
    weight = weight_entry.get()
    height = height_entry.get()
    if not weight_validation(weight,height):
        messagebox = Label(text="Please enter only digit!")
        messagebox.pack()
    else:
        global result_bmi
        calculater =(int(weight_entry.get())) / (((int(height_entry.get()))/100)**2)
        if calculater <= 18.5:
            result_bmi = f"Your BMI score {calculater} = Underweight"
        elif 18.5 < calculater <= 25:
            result_bmi = f"Your BMI score {calculater} = Normal Weight"
        elif 25 < calculater <= 29.9:
            result_bmi = f"Your BMI score {calculater} = Overweight"
        elif calculater >= 30:
            result_bmi = f"Your BMI score {calculater} = Obese"
        result_label = Label(text=result_bmi)
        result_label.pack()

the_button = Button(text="Calculate",command=button_calculater)
the_button.pack()

window.mainloop()
