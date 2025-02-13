from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox




class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1450x800+0+0')
        self.root.title('CRIMINAL RECORD HOLDER')

        #Variable
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_Criminal_Name=StringVar()
        self.var_Arrest_Date=StringVar()
        self.var_Address=StringVar()
        self.var_Ocupation=StringVar()
        self.var_Date_of_crime=StringVar()
        self.var_Age=StringVar()
        self.var_Birth_Mark=StringVar()
        self.var_Crime_type=StringVar()
        self.var_Father_Name=StringVar()
        self.var_Date_of_Birth=StringVar()
        self.var_Gender=StringVar()
        self.var_Most_Wanted=StringVar()



        lbl_titel=Label(self.root,text='CRIMINAL RECORD HOLDER SOFTWARE',font=('Colonna MT',45,),bg='black',fg='gold') 
        lbl_titel.place(x=0,y=0,width=1500,height=50)

        #cid logo
        img_logo=Image.open('images/ip.png')
        img_logo=img_logo.resize((90,50),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo,bg='black')
        self.logo.place(x=100,y=0,width=90,height=50)

        # Img_Frame

        img_frame=Frame(self.root, bd = 2 , relief=RIDGE, bg='white')
        img_frame.place( x = 0 , y = 70 ,width=1500,height=150)

        img1=Image.open('images/Mh.jpg')
        img1=img1.resize((540,160), Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame, image=self.photo1)
        self.img_1.place(x=1,y=0,width=500,height=150)

        ## 2st

        img_2=Image.open('images/police.jpeg')
        img_2=img_2.resize((540,160), Image.Resampling.LANCZOS )
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame, image=self.photo2)
        self.img_2.place(x=500,y=0,width=450,height=150)

        ## 3st
        img_3=Image.open('images/car.jpg')
        img_3=img_3.resize((540,160), Image.Resampling.LANCZOS )
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame, image=self.photo3) 
        self.img_3.place(x=950,y=0,width=500,height=150)

        #main fream
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=225,width=1425,height=560)
        #upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1405,height=270)

        #Label Entry
        
        #case id
        caseid=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=Entry(upper_frame,width=22,textvariable=self.var_case_id,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2, pady=7,sticky=W)

        #name
        Cfriminalname=Label(upper_frame,text='Criminal Name:',font=('arial',11,'bold'),bg='white')
        Cfriminalname.grid(row=1,column=0,padx=3,pady=7,sticky=W)

        nameentry=Entry(upper_frame,width=22,textvariable=self.var_Criminal_Name,font=('arial',11,'bold'))
        nameentry.grid(row=1,column=1,padx=2,sticky=W)
        
        #date
        arrestdt=Label(upper_frame,text='Arrest Date:',font=('arial',11,'bold'),bg='white')
        arrestdt.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        dtentry=Entry(upper_frame,width=22,textvariable=self.var_Arrest_Date,font=('arial',11,'bold'))
        dtentry.grid(row=2,column=1,padx=2,sticky=W)
        
        #ADD
        Address=Label(upper_frame,text='Address:',font=('arial',11,'bold'),bg='white')
        Address.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        Addressentry=Entry(upper_frame,width=22,textvariable=self.var_Address,font=('arial',11,'bold'))
        Addressentry.grid(row=3,column=1,padx=2,pady=7,sticky=W)
        
        #Ocupation
        Ocupation=Label(upper_frame,text='Ocupation:',font=('arial',11,'bold'),bg='white')
        Ocupation.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        caseentry=Entry(upper_frame,width=22,textvariable=self.var_Ocupation,font=('arial',11,'bold'))
        caseentry.grid(row=4,column=1,padx=2,sticky=W)
        
        #C no
        Number=Label(upper_frame,text='Criminal No:',font=('arial',11,'bold'),bg='white')
        Number.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        Noentry=Entry(upper_frame,width=22,textvariable=self.var_criminal_no,font=('arial',11,'bold'))
        Noentry.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        
        
        #Date of crime
        DTC=Label(upper_frame,text='Date of crime:',font=('arial',11,'bold'),bg='white')
        DTC.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        DTCentry=Entry(upper_frame,width=22,textvariable=self.var_Date_of_crime,font=('arial',11,'bold'))
        DTCentry.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        #Age
        Age=Label(upper_frame,text='Age:',font=('arial',11,'bold'),bg='white')
        Age.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        Ageentry=Entry(upper_frame,width=22,textvariable=self.var_Age,font=('arial',11,'bold'))
        Ageentry.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        #B mark
        Birthmark=Label(upper_frame,text='Birth Mark:',font=('arial',11,'bold'),bg='white')
        Birthmark.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        BMentry=Entry(upper_frame,width=22,textvariable=self.var_Birth_Mark,font=('arial',11,'bold'))
        BMentry.grid(row=3,column=4,padx=2,pady=7,sticky=W)

        #C type
        Ctyoe=Label(upper_frame,text='Crime Type:',font=('arial',11,'bold'),bg='white')
        Ctyoe.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        CTentry=Entry(upper_frame,width=22,textvariable=self.var_Crime_type,font=('arial',11,'bold'))
        CTentry.grid(row=4,column=4,padx=2,pady=7,sticky=W)

        #F name
        Fname=Label(upper_frame,text='Father Name:',font=('arial',11,'bold'),bg='white')
        Fname.grid(row=1,column=5,padx=2,pady=7,sticky=W)

        Fnameentry=Entry(upper_frame,width=22,textvariable=self.var_Father_Name,font=('arial',11,'bold'))
        Fnameentry.grid(row=1,column=6,padx=2,pady=7,sticky=W)

        #DOB
        DOB=Label(upper_frame,text='Date Of Birth:',font=('arial',11,'bold'),bg='white')
        DOB.grid(row=2,column=5,padx=2,pady=7,sticky=W)

        DOBentry=Entry(upper_frame,width=22,textvariable=self.var_Date_of_Birth,font=('arial',11,'bold'))
        DOBentry.grid(row=2,column=6,padx=2,pady=7,sticky=W)

        #gender
        gender=Label(upper_frame,text='Gender:',font=('arial',11,'bold'),bg='white')
        gender.grid(row=3,column=5,padx=2,pady=7,sticky=W)

        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=700,y=115,width=225,height=30)

        male=Radiobutton(radio_frame_gender,text='Male',value='Male',variable=self.var_Gender,font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,padx=5,pady=2,sticky=W)

        Fmale=Radiobutton(radio_frame_gender,text='Female',value='Female',variable=self.var_Gender,font=('arial',9,'bold'),bg='white')
        Fmale.grid(row=0,column=1,padx=5,pady=2,sticky=W)

        Trance=Radiobutton(radio_frame_gender,text='Transed',value='Transed',variable=self.var_Gender,font=('arial',9,'bold'),bg='white')
        Trance.grid(row=0,column=2,padx=5,pady=2,sticky=W)


        #wanted
        Most_wanted=Label(upper_frame,text='Most Wanted:',font=('arial',11,'bold'),bg='white')
        Most_wanted.grid(row=4,column=5,padx=2,pady=7,sticky=W)

        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=700,y=150,width=190,height=30)

        Yes=Radiobutton(radio_frame_wanted,text='Yes ',value='Yes',variable=self.var_Most_Wanted,font=('arial',9,'bold'),bg='white')
        Yes.grid(row=0,column=0,padx=5,pady=2,sticky=W)

        No=Radiobutton(radio_frame_wanted,text='No ',value='No',variable=self.var_Most_Wanted,font=('arial',9,'bold'),bg='white')
        No.grid(row=0,column=1,padx=5,pady=2,sticky=W)

        #Button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=630,height=45)

        #add button
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #Update button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #delet Button
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #clear button
        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #backgroud right side image
        img_4=Image.open('images/crr.jpg')
        img_4=img_4.resize((470,245), Image.Resampling.LANCZOS )
        self.photo4=ImageTk.PhotoImage(img_4)

        self.img_4=Label(upper_frame, image=self.photo4) 
        self.img_4.place(x=935,y=0,width=460,height=245)


        #down frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=280,width=1420,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1405,height=60)

        search_by=Label(search_frame,text='Search by:',font=('arial',12,'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,padx=2,pady=3,sticky=W)

        self.var_com_search=StringVar()
        #combo box
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',12,'bold'),width=18,state='read')
        combo_search_box['value']=('Select option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,padx=5,pady=3,sticky=W)
        
        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,width=22,textvariable=self.var_search,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,padx=5,pady=3,sticky=W)

        #search button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5,pady=3,sticky=W)

        #all button
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=5,pady=3,sticky=W)

        criminalagency=Label(search_frame,font=("Algerian",30,"bold"),text="NATIONAL CRIME AGENCY",bg="white",fg="crimson")
        criminalagency.grid(row=0,column=5,sticky=W,padx=50)

        
        #logout bouuto
        btn_logout = Button(self.root, text='Logout', command=self.logout,font=('arial', 13, 'bold'), bg='red', fg='white', cursor='hand2')
        btn_logout.place(x=1340, y=8, width=90, height=35)


        #table frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1405,height=170)

       

        
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Criminal_table=ttk.Treeview(table_frame,column=("0","1","2","3","4","5","6","7","8","9","10","11","12","13"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Criminal_table.xview)
        scroll_y.config(command=self.Criminal_table.yview)

        self.Criminal_table.heading("0",text='CaseID')
        self.Criminal_table.heading("1",text='criminal No')
        self.Criminal_table.heading("2",text='Criminam name')
        self.Criminal_table.heading("3",text='Arrest Date')
        self.Criminal_table.heading("4",text='Address')
        self.Criminal_table.heading("5",text='Ocupation')
        self.Criminal_table.heading("6",text='Datr of crime')
        self.Criminal_table.heading("7",text='Age')
        self.Criminal_table.heading("8",text='Birth Mark')
        self.Criminal_table.heading("9",text='Crime type')
        self.Criminal_table.heading("10",text='Father Name')
        self.Criminal_table.heading("11",text='Date of Birth')
        self.Criminal_table.heading("12",text='Gender')
        self.Criminal_table.heading("13",text='Most Wanted')

        self.Criminal_table['show']='headings'

        self.Criminal_table.column("0",width=100)
        self.Criminal_table.column("1",width=100)
        self.Criminal_table.column("2",width=100)
        self.Criminal_table.column("3",width=100)
        self.Criminal_table.column("4",width=100)
        self.Criminal_table.column("5",width=100)
        self.Criminal_table.column("6",width=100)
        self.Criminal_table.column("7",width=100)
        self.Criminal_table.column("8",width=100)
        self.Criminal_table.column("9",width=100)
        self.Criminal_table.column("10",width=100)
        self.Criminal_table.column("11",width=100)
        self.Criminal_table.column("12",width=100)
        self.Criminal_table.column("13",width=100)

        self.Criminal_table.pack(fill=BOTH,expand=1)

        self.Criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #Add function
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Field are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='xyz',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('INSERT INTO criminal1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.var_case_id.get(),
                                                                                                                self.var_criminal_no.get(),
                                                                                                                self.var_Criminal_Name.get(),
                                                                                                                self.var_Arrest_Date.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Ocupation.get(),
                                                                                                                self.var_Date_of_crime.get(),
                                                                                                                self.var_Age.get(),
                                                                                                                self.var_Birth_Mark.get(),
                                                                                                                self.var_Crime_type.get(),
                                                                                                                self.var_Father_Name.get(),
                                                                                                                self.var_Date_of_Birth.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_Most_Wanted.get()
                                                                                                

                                                                                                                     ))
                
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has ben added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    
    #fase data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='xyz',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('SELECT * FROM criminal1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.Criminal_table.delete(*self.Criminal_table.get_children())
            for i in data:
                self.Criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    #get curser
    def get_cursor(self,event=""):
        cursor_row=self.Criminal_table.focus()
        contain=self.Criminal_table.item(cursor_row)
        data=contain['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_Criminal_Name.set(data[2])
        self.var_Arrest_Date.set(data[3])
        self.var_Address.set(data[4])
        self.var_Ocupation.set(data[5])
        self.var_Date_of_crime.set(data[6])
        self.var_Age.set(data[7])
        self.var_Birth_Mark.set(data[8])
        self.var_Crime_type.set(data[9])
        self.var_Father_Name.set(data[10])
        self.var_Date_of_Birth.set(data[11])
        self.var_Gender.set(data[12])
        self.var_Most_Wanted.set(data[13])

    #update
    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Field are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this Criminal Record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='xyz',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('UPDATE criminal1 set Criminal_no=%s,Criminal_Name=%s,Arrest_Date=%s,Address=%s,Ocupation=%s,Date_of_crime=%s,Age=%s,Birth_Mark=%s,Crime_type=%s,Father_Name=%s,Date_of_Birth=%s,Gender=%s,Most_Wanted=%s where Case_id=%s',(
                                                                                                                                                                                                                                                                        self.var_criminal_no.get(),
                                                                                                                                                                                                                                                                        self.var_Criminal_Name.get(),
                                                                                                                                                                                                                                                                        self.var_Arrest_Date.get(),
                                                                                                                                                                                                                                                                        self.var_Address.get(),
                                                                                                                                                                                                                                                                        self.var_Ocupation.get(),
                                                                                                                                                                                                                                                                        self.var_Date_of_crime.get(),
                                                                                                                                                                                                                                                                        self.var_Age.get(),
                                                                                                                                                                                                                                                                        self.var_Birth_Mark.get(),
                                                                                                                                                                                                                                                                        self.var_Crime_type.get(),
                                                                                                                                                                                                                                                                        self.var_Father_Name.get(),
                                                                                                                                                                                                                                                                        self.var_Date_of_Birth.get(),
                                                                                                                                                                                                                                                                        self.var_Gender.get(),
                                                                                                                                                                                                                                                                        self.var_Most_Wanted.get(),
                                                                                                                                                                                                                                                                        self.var_case_id.get()


                    
                                                                                                                                                                                                                                                                         ))
                    

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Update','Criminal Record has ben succesfull Updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')


    #delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Field are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure to Delete this Criminal Record')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='xyz',database='management')
                    my_cursor=conn.cursor()
                    sql='DELETE FROM criminal1 where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Criminal Record has ben succesfull Deleated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
    
    #clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_Criminal_Name.set("")
        self.var_Arrest_Date.set("")
        self.var_Address.set("")
        self.var_Ocupation.set("")
        self.var_Date_of_crime.set("")
        self.var_Age.set("")
        self.var_Birth_Mark.set("")
        self.var_Crime_type.set("")
        self.var_Father_Name.set("")
        self.var_Date_of_Birth.set("")
        self.var_Gender.set("")
        self.var_Most_Wanted.set("")


    #search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Field are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='xyz',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('Select * from criminal1 where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                   self.Criminal_table.delete(*self.Criminal_table.get_children())
                   for i in rows:
                        self.Criminal_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')


    def logout(self):
        # Function to logout or close the app
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            self.root.destroy()



if __name__=="__main__":
   root = Tk()
   obj=Criminal(root)
   root.mainloop()


   
