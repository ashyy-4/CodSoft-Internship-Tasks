from tkinter import *
root = Tk()
root.geometry("500x300")


Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
gender= Label(root, text="Gender")
phone= Label(root, text="Phone")
emergency= Label(root, text="Emergency")
email = Label(root, text="Email")
age = Label(root, text="Age")

name.grid(row=1, column=2)
gender.grid(row=2, column=2)
phone.grid(row=3, column=2)
email.grid(row=4, column=2)
age.grid(row=5, column=2)
emergency.grid(row=6, column=2)

namevalue = StringVar
gendervalue = StringVar
phonevalue = StringVar
emailvalue = StringVar
agevalue = StringVar
emergencyvalue = StringVar

nameentry = Entry(root, textvariable = namevalue)
genderentry = Entry(root, textvariable = gendervalue)
phoneentry = Entry(root, textvariable = phonevalue)
emailentry = Entry(root, textvariable = emailvalue)
ageentry = Entry(root, textvariable = agevalue)
emergencyentry = Entry(root, textvariable = emergencyvalue)

nameentry.grid(row=1, column=3)
genderentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
ageentry.grid(row=5, column=3)
emergencyentry.grid(row=6, column=3)

Button(text="SUBMIT", bg= 'green').grid(row=11, column=3)




root.mainloop
