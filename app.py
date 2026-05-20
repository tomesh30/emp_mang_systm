import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
win = Tk()
win.title('EMPLOYEE MANAGEMENT SYSTEM')
win.config(bg='gray')
win.geometry('800x600')

# button functions
def add():
    emp_id=id1.get()
    emp_name=n1.get()
    mob_no=m1.get()
    dept=d1.get()
    emp_salary=s1.get()

    if emp_id=='' or emp_name== '' or mob_no== '' or dept=='' or emp_salary=='':
        messagebox.showinfo('info','All fields are compulsary!')
    else:
        conn=pymysql.connect(user='root',host='localhost',password='881909',database='emp_project')
        qur=f'INSERT INTO emp VALUES("{emp_id}","{emp_name}","{mob_no}","{dept}","{emp_salary}")'
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data inserted successfully!!')
        id1.set('')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')

def show():
    treev.delete(*treev.get_children())
    conn=pymysql.connect(user='root',host='localhost',password='881909',database='emp_project')
    qur='SELECT * FROM emp'
    mycur=conn.cursor()
    mycur.execute(qur)
    tup1=mycur.fetchall()
    for i in tup1:
        treev.insert('',END,values=(i[0],i[1],i[2],i[3],i[4]))
    mycur.close()
    conn.close()

def show_sal():
    s=e9.get()
    if s=='':
        messagebox.showinfo('info','All fields are compulsary!')
    else:
        conn=pymysql.connect(user='root',host='localhost',password='881909',database='emp_project')
        qur=f'SELECT emp_name,emp_salary FROM emp WHERE emp_id="{s}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        tup4=mycur.fetchone()
        mystr=f'Salary of {tup4[0]} is {tup4[1]} Rs'
        l10.config(text=mystr)
        mycur.close()
        conn.close()

def salary():
    root=Tk()
    root.title('SALARY MANAGEMENT')
    root.config(bg='gray')
    root.geometry('800x600')
   
   
    l8=Label(root,text='SALARY MANAGEMENT',width=35,bg='white',
         fg='black',bd=5,relief='ridge',font=('times new roman',18,'bold'))
   
    l8.place(x=220,y=40)
   
    l9=Label(root,text='ENTER ID>>',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
    l9.place(x=100,y=150)
   
    global e9
    global var3
    global l10
    var3=StringVar()
    e9=Entry(root,textvariable=var3,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
    e9.place(x=310,y=150)


    b9=Button(root,text='SHOW SALARY',width=12,command=show_sal,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
    b9.place(x=310,y=190)
   
   
    l10=Label(root,text='SEE SALARY HERE !!!!',bg='white',fg='black',
        height=5,width=30,bd=5,
        relief='ridge',font=('times new roman',16,'bold'))
    l10.place(x=100,y=240)
   
    root.mainloop()



def delete():
    del_data=var1.get()
    if del_data=='':
        messagebox.showinfo('info','All fields are compulsary!')
    else:
        conn=pymysql.connect(user='root',host='localhost',password='881909',database='emp_project')
        qur=f'DELETE FROM emp where emp_id="{del_data}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data deleted successfully!!')

def select():
    up_data=var2.get()
    if up_data=='':
        messagebox.showinfo('info','All fields are compulsary!')
    else:
        conn=pymysql.connect(user='root',host='localhost',password='881909',database='emp_project')
        qur=f'SELECT * FROM emp WHERE emp_id="{up_data}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        tup2=mycur.fetchone()
        e1.insert(0,tup2[0])
        e2.insert(0,tup2[1])
        e3.insert(0,tup2[2])
        e4.delete(0,END)
        e4.insert(0,tup2[3])
        e5.insert(0,tup2[4])
        mycur.close()
        conn.close()

def update():
    emp_id=id1.get()
    emp_name=n1.get()
    mob_no=m1.get()
    dept=d1.get()
    emp_salary=s1.get()

    if emp_id=='' or emp_name== '' or mob_no== '' or dept=='' or emp_salary=='':
        messagebox.showinfo('info','All fields are compulsary!')
    else:
        conn=pymysql.connect(user='root',host='localhost',password='881909',database='emp_project')
        qur=f'''UPDATE emp SET emp_id="{emp_id}",emp_name="{emp_name}",
        mob_no="{mob_no}",dept="{dept}",emp_salary="{emp_salary}"
        WHERE emp_id="{emp_id}"
        '''
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data updated successfully!!')

def clear():
    treev.delete(*treev.get_children())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)


# Delete interface

# label  entry   button

l6=Label(win,text='ENTER ID>>',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l6.place(x=100,y=400)

var1=StringVar()
e6=Entry(win,textvariable=var1,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e6.place(x=310,y=400)

b5=Button(win,text='DELETE',width=12,command=delete,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b5.place(x=310,y=440)

# update interface
# 1 label ,entry ,2 buttons

l7=Label(win,text='ENTER ID>>',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l7.place(x=100,y=490)

var2=StringVar()
e7=Entry(win,textvariable=var2,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e7.place(x=310,y=490)

b6=Button(win,text='SELECT',width=12,command=select,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b6.place(x=200,y=540)

b7=Button(win,text='UPDATE',width=12,command=update,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b7.place(x=350,y=540)

# tree view

treev=ttk.Treeview(win,height=23)
treev.place(x=700,y=80,width=565)

treev["columns"] = ("1", "2", "3","4","5")
treev['show'] = 'headings'

treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')
treev.column("4", width = 90, anchor ='se')
treev.column("5", width = 90, anchor ='se')

treev.heading("1", text ="Emp_ID")
treev.heading("2", text ="Emp_Name")
treev.heading("3", text ="Mob NO")
treev.heading("4", text ="Dept")
treev.heading("5", text ="Salary")

# clear button
b8=Button(win,text='CLEAR',width=12,command=clear,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b8.place(x=910,y=570)


# main label

l0=Label(win,text='EMPLOYEE MANAGEMENT SYSTEM',width=40,bg='white',
         fg='black',bd=5,relief='ridge',font=('times new roman',18,'bold'))

l0.place(x=268,y=20)

# Employee registration Form

# employee id and entry

l1=Label(win,text='EMPLOYEE ID',width=20,bg='white',
         fg='black',bd=5,relief='ridge',font=('times new roman',12,'bold'))

l1.place(x=100,y=80)


id1=StringVar()
e1=Entry(win,width=40,bg='white',textvariable=id1,
         fg='black',bd=5,relief='ridge',font=('times new roman',12,'bold'))

e1.place(x=310,y=80)


#  emp_name >> label ,entry


l2=Label(win,text='EMPLOYEE NAME',width=20,bg='white',
         fg='black',bd=5,relief='ridge',font=('times new roman',12,'bold'))

l2.place(x=100,y=120)


n1=StringVar()
e2=Entry(win,width=40,bg='white',textvariable=n1,
         fg='black',bd=5,relief='ridge',font=('times new roman',12,'bold'))

e2.place(x=310,y=120)

# mob_num >> label entry

l3=Label(win,text='MOBILE NUMBER',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l3.place(x=100,y=160)

m1=StringVar()
e3=Entry(win,textvariable=m1,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e3.place(x=310,y=160)

# dept >> label entry

l4=Label(win,text='DEPARTMENT',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l4.place(x=100,y=200)

d1=StringVar()
e4=ttk.Combobox(win,textvariable=d1,width=38,font=('times new roman',12,'bold'))
e4.place(x=310,y=200,height=30)
e4['values']=('R&D','Marketing','Production','HR')
e4.current(0)

# salary >> label ,entry

l5=Label(win,text='SALARY',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l5.place(x=100,y=240)

s1=StringVar()
e5=Entry(win,textvariable=s1,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e5.place(x=310,y=240)



# 4 buttons 


b1=Button(win,text='SHOW',width=12,command=show,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b1.place(x=180,y=300)

b2=Button(win,text='ADD',width=12,command=add,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b2.place(x=410,y=300)

b3=Button(win,text='EXIT',width=12,command=win.destroy,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b3.place(x=180,y=340)

b4=Button(win,text='SALARY',width=12,command=salary,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b4.place(x=410,y=340)




win.mainloop()