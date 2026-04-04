# import tkinter library and pillow

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()


## this function handle login condition when user enter correct email and password it give the login successfully
## otherwise, failed login
def handle_login():
    email = email_input.get()
    password = password_input.get()


    if email == "mamtu@gmail.com" and password == "7878": 
        messagebox.showinfo("yep","Login successfully")
    else:
        messagebox.showinfo("Error","Login failed")     


## first name of the form
root.title("Login Form")
root.iconbitmap("favicorn.ico")
# decide the actual size of gui
root.geometry('450x600')
## to determine the background colour
root.configure(background='#0096DC')

# use the telegram icon image on gui so determine the path from the photoimage
img = ImageTk.PhotoImage(Image.open("tg.png"))
img_label = Label(root,image = img)         ## 
img_label.pack(pady = (10,10))      ## after plot the icon pack this to gui because after packing we can see it 

# name of the icon with background colour and pack it with the suitable size
text_label = Label(root,text = "telegram",fg = "white",bg ="#0096DC")
text_label.pack()
text_label.config(font=("verdana",24))


## now create the label of email and pack it
email_label = Label( root,text = "Enter email",fg = "white",bg ="#0096DC")
email_label.pack(pady = (20,5))
email_label.config(font = ("verdana",12))
 

 ## create  the suitable box to enter email and packed it
email_input = Entry(root,width = 40)
email_input.pack(ipady = 6,pady = (1,15))

## same task with password means give the password label ,packed it and create a open box to enter password
password_label = Label( root,text = "Enter password",fg = "white",bg = "#0096DC")
password_label.pack(pady = (20,5))
password_label.config(font = ("verdana",12))

password_input = Entry(root,width = 40)
password_input.pack(ipady = 6,pady = (1,15))

## add login button below the password 
login_btn = Button(root,text = "Login here",bg = "white",fg= "black",command = handle_login)
login_btn.pack(pady = (10,20))



root.mainloop()