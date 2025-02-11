from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from tkinter import ttk


from criminal_app import Criminal

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1420x900+0+0')
        self.root.title("CRIMINAL RECORD LOGIN PAGE")

        
        self.bg_image = Image.open("images/bgp.jpg")  # Replace with your image path
        self.bg_image = self.bg_image.resize((1420, 900), Image.LANCZOS)  # Resize the image to fit the window
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Variables
        self.username = StringVar()
        self.password = StringVar()
        
        # Login Form
        lbl_title = Label(self.root, text="CRIMINAL RECORD LOGIN PAGE", font=(' Colonna MT', 30, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0, relwidth=1, height=50)
        
        frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        frame.place(x=815, y=245, width=550, height=350)
        
        lbl_user = Label(frame, text="Username:", font=('Times New Roman', 15, 'bold'), bg='white')
        lbl_user.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        txt_user = Entry(frame, textvariable=self.username, font=('Times New Roman', 15))
        txt_user.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        
        lbl_pass = Label(frame, text="Password:", font=('Times New Roman', 15, 'bold'), bg='white')
        lbl_pass.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        txt_pass = Entry(frame, textvariable=self.password, font=('Times New Roman', 15), show="*")
        txt_pass.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        
        btn_login = Button(frame, text="Login", command=self.login, font=('Times New Roman', 15, 'bold'),width=30, bg='blue', fg='white')
        btn_login.grid(row=3, columnspan=2, pady=10,padx=60)
        
        btn_register = Button(frame, text="Register", command=self.open_register_page,width=35, font=('Times New Roman', 12, 'bold'), bg='green', fg='white')
        btn_register.grid(row=4, columnspan=2, pady=10,padx=60)
    
    def login(self):
        user = self.username.get()
        pwd = self.password.get()
        
        if user == "" or pwd == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="piyush@2318p",  # Replace with your MySQL password
                database="management"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                messagebox.showinfo("Success", "Login Successful!")
                self.root.destroy()
                self.open_main_app()
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
        except Exception as ex:
            messagebox.showerror("Error", f"Error connecting to database: {str(ex)}")
    
    def open_main_app(self):
        root = Tk()
        app = Criminal(root)
        root.mainloop()

    def open_register_page(self):
        self.root.destroy()
        root = Tk()
        app = RegisterPage(root)
        root.mainloop()


class RegisterPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1420x900+0+0')
        self.root.title("Registration Page")

        self.bg_image = Image.open("images/reg.png")  # Replace with your image path
        self.bg_image = self.bg_image.resize((1420, 900), Image.LANCZOS)  # Resize the image to fit the window
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        # Variables
        self.username = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()
        
        # Registration Form
        lbl_title = Label(self.root, text="Register", font=('Colonna MT', 30, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0, relwidth=1, height=50)
        
        frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        frame.place(x=100, y=245, width=450, height=350)
        
        lbl_user = Label(frame, text="Username:", font=('Times New Roman', 15, 'bold'), bg='white')
        lbl_user.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        txt_user =( Entry(frame, textvariable=self.username, font=('arial', 15)))
        txt_user.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        
        lbl_pass = Label(frame, text="Password:", font=('Times New Roman', 15, 'bold'), bg='white')
        lbl_pass.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        txt_pass = Entry(frame, textvariable=self.password, font=('arial', 15), show="*")
        txt_pass.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        
        lbl_confirm_pass = Label(frame, text="Confirm Password:", font=('Times New Roman', 15, 'bold'), bg='white')
        lbl_confirm_pass.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        txt_confirm_pass = Entry(frame, textvariable=self.confirm_password, font=('arial', 15), show="*")
        txt_confirm_pass.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        
        btn_register = Button(frame, text="Register", command=self.register_user,width=20, font=('Times New Roman', 15, 'bold'), bg='green', fg='white')
        btn_register.grid(row=3, columnspan=2, pady=10)
    
    def register_user(self):
        user = self.username.get()
        pwd = self.password.get()
        confirm_pwd = self.confirm_password.get()
        
        if user == "" or pwd == "" or confirm_pwd == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        if pwd != confirm_pwd:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="piyush@2318p",  # Replace with your MySQL password
                database="management"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user, pwd))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful!")
            self.root.destroy()
            root = Tk()
            LoginPage(root)
            root.mainloop()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
        except Exception as ex:
            messagebox.showerror("Error", f"Error connecting to database: {str(ex)}")


# Run the Login Page
if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()
