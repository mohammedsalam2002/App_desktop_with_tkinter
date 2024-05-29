from tkinter import *
# اظهار الرسائل المنبثقه
from tkinter import messagebox
# للتعامل مع المتصفح
import webbrowser
# للتعامل مع مكاتب النظام
import os
import sys



pro = Tk()
pro.geometry('800x450+30+10')  # حجم النافذه وتثبيت مكان ظهوره
pro.resizable(False,False)   # عدم السماح بلتلاعب بحجم الشاشه
pro.title('Super_Market')
#pro.iconbitmap('D:/super_market_tikenter/imegs/digital-super.jpg')   # icon in my App
title = Label(pro, text='Super Market System', fg='gold', bg='black', font=('tajawal', 16, 'bold'))
title.pack(fill=X)  # # لجعل لون خلفيه النص يمتدد على طول البرنامج

u1 = 'https://www.facebook.com/Moahmmed.s2'
u2 = 'https://t.me/+4jnnAedpstZhNDg6'
u3 = ''







def open2():
    webbrowser.open_new(u2)


def open3():
    webbrowser.open_new(u3)


def about_name():
    messagebox.showinfo('المطور', 'انجب حبي')


def about_App():
    messagebox.showinfo('App','اداره سوبر ماركت')


def log():
    user = En1.get()
    password = En2.get()
    if user == '1' and password == '1':
        messagebox.showinfo('Message','welcome to App market ')
    else:
        messagebox.showinfo('Message', 'Erorr')

def logout():
    exit()

# rect right!!

F1 = Frame(pro, width=230, height=420, bg='#0B2F3A')  # لتقسيم النافذه
F1.place(x=570, y=30)  # # مكان ظهور النافذه الجديده في الشاشه

# Label
Title1 = Label(F1 , text="مشروع سوبر ماركيت", bg='#0B2F3A', fg='white', font=('tajawal', 16, 'bold'))
Title1.place(x=42, y=10)
Title2 = Label(F1, text='المطور محمد سلام', bg='#0B2F3A', fg='white', font=('tajawal', 16, 'bold'))
Title2.place(x=68, y=50)
Title3 = Label(F1, text='وسائل الاتصال بنا', bg='#0B2F3A', fg='white', font=('tajawal', 16, 'bold'))
Title3.place(x=70, y=90)

# Button

B1 = Button(F1, text='حسابنا على الفيسبوك', width=22, bg='#DBA901', fg='black', font=('tajawal', 11, 'bold'))
B1.place(x=10, y=130)
B2 = Button(F1, text='قناتنا على التليكرام', width=22, bg='#DBA901', fg='black', font=('tajawal', 11, 'bold'), command=open2)
B2.place(x=10, y=170)
B3 = Button(F1, text='قناتنا على اليوتيوب', width=22, bg='#DBA901', fg='black', font=('tajawal', 11, 'bold'))
B3.place(x=10, y=210)
B4 = Button(F1, text='لمحه عن المطور', width=22, bg='#DBA901', fg='black', font=('tajawal', 11, 'bold'), command=about_name)
B4.place(x=10, y=250)
B5 = Button(F1, text='حوله البرنامج', width=22, bg='#DBA901', fg='black', font=('tajawal', 11, 'bold'),command=about_App)
B5.place(x=10, y=310)
B6 = Button(F1, text='اغلاق البرنامج', width=22, bg='#DBA901', fg='black', font=('tajawal', 11, 'bold'),command=logout)
B6.place(x=10, y=355)


# image

photo1 = PhotoImage(file='D:/super_Market_2022/imegs/face.png')
imo1 = Label(pro, image=photo1)
imo1.place(x=0, y=30, width=571, height=300)


# rect down!!
F2 = Frame(pro, width=570, height=120, bg='#0B2F3A')  # لتقسيم النافذه
F2.place(x=0, y=330)

# image !!!
#photo2 = PhotoImage(file='C:/Users/Moham/super_Market_2022/imegs/download (1).png')
#imo2 = Label(F2, image=photo2)
#imo2.place(x=380, y=3, width=180, height=112)

# label!!!
L1 = Label(F2, text='اسم المستخدم', bg='#0B2F3A', fg='#DBA901', font=('tajawal', 14, 'bold'))
L1.place(x=270, y=5)
L2 = Label(F2, text='كلمة المرور', bg='#0B2F3A', fg='#DBA901', font=('tajawal', 14, 'bold'))
L2.place(x=280, y=50)

# Entry حقل الادخال
En1 = Entry(F2, font=('tajawal', 12), justify='center')
En1.place(x=118, y=10, width=150)
En2 = Entry(F2, font=('tajawal', 12), justify='center')
En2.place(x=118, y=55, width=150)

# Button!!
B7 = Button(F2, text='تسجيل الدخول', width=22, bg='#DBA901', fg='black', font=('tajawal', 11, 'bold'),command=log)
B7.place(x=10, y=10, width=100, height=72)


pro.mainloop()