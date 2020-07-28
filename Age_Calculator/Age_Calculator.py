# imports the nessicary modules 
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import calendar

# sets up the basic window 
root = Tk()
root.title('Age Calculator')
photo = PhotoImage(file='Age Icon.png')
root.iconphoto(False, photo)

# defines labels so the screen can clear when the button is pressed
global answer_label
global bottom_frame

bottom_frame = Label(root)
answer_label = Label(bottom_frame)


# the command for the calculate button
def calculate_age():
    global bottom_frame
    global answer_label

    birth = datetime(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    current = datetime.now()
    current_year = current.year
    current_month = current.month
    # math to get your current age 
    
    year_answer = current_year - birth.year - ((current_month, current.day) < (birth.month, birth.day))
    month_answer = int(current_month) - birth.month
    day_answer = current.day - birth.day - ((current_month, current.day) < (birth.month, birth.day))
    month_end = calendar.monthrange(int(year_entry.get()), int(month_entry.get()))
    answer_label.grid_forget()
    
    # conditions that slighly alter the math or answer 
    if 0 < int(month_entry.get()) < 12:
        answer_label.grid_forget()
        answer_label = Label(bottom_frame,
                        text='Your month should be between 1 and 12 and your day number should fit within the month')
        answer_label.config(font=('Courier', 10))

    if day_answer < 0:
        answer_label.grid_forget()
        day_answer = day_answer + month_end[1] + 1
        answer_label.grid(row=9, column=1)
        month_answer -= 1

    if month_answer < 0:
        answer_label.grid_forget()
        month_answer += 12
        answer_label.grid(row=9, column=1)

    if month_answer == 12:
        answer_label.grid_forget()
        month_answer -= 1
        answer_label = Label(bottom_frame,
                             text=f"{name_entry.get()} is {year_answer} year(s) {month_answer} month(s) and {day_answer} day(s) old")
        answer_label.config(font=('Courier', 20))
        answer_label.grid(row=9, column=1)

        answer_label.config(font=('Courier', 20))
        answer_label.grid(row=9, column=1)

    else:
        answer_label.grid_forget()
        answer_label = Label(bottom_frame,
                             text=f"{name_entry.get()} is {year_answer} year(s) {month_answer} month(s) and {day_answer} day(s) old")
        answer_label.config(font=('Courier', 20))
        answer_label.grid(row=9, column=1)


# labels widgets
main_img = ImageTk.PhotoImage(Image.open('Family_silhouette.png'))
main_label = Label(root, image=main_img)
title_label = Label(root, text='Age Calculator')
title_label.config(font=('Courier', 20))
bottom_frame = LabelFrame(root, )
name_label = Label(bottom_frame, text='Name:           ')
name_entry = Entry(bottom_frame, )
year_label = Label(bottom_frame, text='Year:           ')
year_entry = Entry(bottom_frame, )
month_label = Label(bottom_frame, text='Month(Numeric):           ')
month_entry = Entry(bottom_frame)
day_label = Label(bottom_frame, text='Day:           ')
day_entry = Entry(bottom_frame)
calc_button = Button(bottom_frame, text='Calculate Age', bg='red', padx=15, pady=10, command=calculate_age)
filler = Label(bottom_frame, text='')

# puts widgets on screen
main_label.grid(row=0, column=0, columnspan=1)
title_label.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)
name_label.grid(row=3, column=0)
name_entry.grid(row=3, column=2)
year_label.grid(row=4, column=0)
year_entry.grid(row=4, column=2)
month_label.grid(row=5, column=0)
month_entry.grid(row=5, column=2)
day_label.grid(row=6, column=0)
day_entry.grid(row=6, column=2)
calc_button.grid(row=8, column=1)
filler.grid(row=7, column=1)

root.mainloop()
