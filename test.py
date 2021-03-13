
from tkinter import *

screen = Tk()
screen.geometry("500x500")
screen.title("Python form validation")

def delete():
    screen1.destroy()

def delete1():
    screen2.destroy()

def error():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("150x90")
    screen1.title("Warning!")
    Label(screen1, text = "All fields required", fg = "red").pack()
    Button(screen1, text = "OK", command = delete).pack()

def success():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("150x90")
    screen2.title("Warning!")
    Label(screen2, text = "Registration Sucess!", fg = "green").pack()
    Button(screen2, text = "OK", command = delete1).pack()
    
def register():
  
  username_text = username.get()
  password_text = password.get()

  if username_text == "":
              error()

  elif password_text == "":
              error()

  else:
    success()
    
  
  

heading = Label(text = "Python Form Validation", fg = "black", bg = "grey", width = "500", height = "3").pack()

Label(text = "Username * ").place(x = 15, y = 70)
Label(text = "Password * ").place(x = 15, y = 140)

username = StringVar()
password = StringVar()

Entry(screen, textvariable = username).place(x = 15, y = 100)
Entry(screen, textvariable = password).place(x = 15, y = 170)

Button(screen, text = "Register", width = "7", bg = "grey", command = register).place(x = 15, y = 210)

mainloop()