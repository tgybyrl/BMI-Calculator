from tkinter import *

#window and FONT
window = Tk()
window.title("BMI Calculater")
window.minsize(width=330,height=240)
window.config(padx=30,pady=40)
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

#result label for function
result_label = Label()
messagebox = Label()

#weight validation
def weight_validation(weight,height):
    if weight.isdigit() and height.isdigit():
        return True
    return False

#button
def button_calculater():
    global messagebox
    messagebox.destroy()
    weight = weight_entry.get()
    height = height_entry.get()
    if not weight_validation(weight,height):
        messagebox = Label(text="Please enter a valid number!")
        messagebox.pack()
    else:
        global result_label
        global result_bmi
        messagebox.destroy()
        result_label.destroy()
        calculater =(int(weight_entry.get())) / (((int(height_entry.get()))/100)**2)
        if calculater <= 18.5:
            result_bmi = f"Your BMI score {calculater} = Underweight"
        elif 18.5 < calculater <= 25:
            result_bmi = f"Your BMI score {calculater} = Normal Weight"
        elif 25 < calculater <= 29.9:
            result_bmi = f"Your BMI score {calculater} = Overweight"
        elif 30 <= calculater < 35:
            result_bmi = f"Your BMI score {calculater} = Class 1 Obesity"
        elif 35 <= calculater < 40:
            result_bmi = f"Your BMI score {calculater} = Class 2 Obesity"
        elif calculater >= 40:
            result_bmi = f"Your BMI score {calculater} = Class 3 Obesity"
        result_label = Label(text=result_bmi)
        result_label.pack()
the_button = Button(text="Calculate",command=button_calculater)
the_button.pack()

window.mainloop()
