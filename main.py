#importing libraries
from tkinter import *
from tkinter import messagebox
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Creating the Gui for email sender
window = Tk()
window.title("Simple Email Sender Using Python")
window.geometry("800x600")
window.minsize(600,350)
window.resizable(width=False,height=True)
#Connecting to Gmail Server Using SSL
def email_sender():
    # Creating Massage Context ( Note that you need to generate a app password in order to send gmail
    message = MIMEMultipart()
    message["From"] = user_email_entry.get()
    message["To"] = target_email_entry.get()
    message["Subject"] = subject_entry.get()
    message.attach(MIMEText(compose_entry.get(1.0, END), "plain"))
    #Starting the connection and sending the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(user_email_entry.get(), user_password_entry.get())
        server.sendmail(user_email_entry.get(), target_email_entry.get(), message.as_string())
    messagebox.showinfo("Message", "The Email was sent successfully")
    #End of connecting and sending email


#Starting to create the Gui Using TK
user_email = Label(window, text="Your Email :")
user_email_entry = Entry(window)
user_email.grid(row=0 ,column = 0 , pady=2 , padx=(5,0), sticky ="e")
user_email_entry.grid(row=0 ,column = 1 , pady=2 , padx=(0,0), sticky = "w")


user_password = Label(window, text="Your App Password :")
user_password_entry = Entry(window)
user_password.grid(row=1 ,column = 0 , pady=2 , padx=(5,0), sticky ="e")
user_password_entry.grid(row=1 ,column = 1 , pady=2 , padx=(0,0), sticky = "w")

target_email = Label(window, text="To :")
target_email_entry = Entry(window)
target_email.grid(row=2 ,column = 0 , pady=2 , padx=(5,0) , sticky="e")
target_email_entry.grid(row=2 ,column = 1 , pady=2 , padx=(0,0) , sticky = "w")

subject_label = Label(window , text="Subject :")
subject_entry = Entry(window)
subject_label.grid(row=3 ,column = 0 , pady=2 , padx=(5,0) , sticky="e")
subject_entry.grid(row=3 ,column = 1 , pady=2 , padx=(0,0) , sticky = "w")

compose_label = Label(window , text="Compose email :")
compose_entry = Text(window , height=10 , width=50)
compose_label.grid(row=4 ,column = 0 , pady=2 , padx=(5,0) , sticky="n")
compose_entry.grid(row=4 ,column = 1 , pady=2 , padx=(0,0) , sticky = "w")

send_button = Button(window , text="Send", command=email_sender)
send_button.grid(row=5 , column = 1 , pady = 4 , sticky = "w")


window.mainloop()
#End of making a Gui















