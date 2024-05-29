from tkinter import *
import random


class Super:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1050x600+30+10')
        self.root.title('Super Market')
        self.root.resizable(False,False)
        #self.root.iconbitmap('C:/Users/Moham/super_Market_2022/imegs/12.ico')
        # ====App the name====
        title = Label(self.root ,text='Electronic market', fg='gold', bg='#0B2F3A', font=('tajawal', 16, 'bold'),width=82)
        title.place(x=-8)


        # ======= variable  to Entry Frame 5 ===========
        self.E1F5 = IntVar()
        self.E2F5 = IntVar()
        self.E3F5 = IntVar()
        self.E4F5 = IntVar()
        self.E5F5 = IntVar()
        self.E6F5 = IntVar()
        self.E7F5 = IntVar()
        self.E8F5 = IntVar()
        self.E9F5 = IntVar()
        # ======= variable  to Entry Frame 6 ===========
        self.E1F6 = IntVar()
        self.E2F6 = IntVar()
        self.E3F6 = IntVar()
        self.E4F6 = IntVar()
        self.E5F6 = IntVar()
        self.E6F6 = IntVar()
        self.E7F6 = IntVar()
        self.E8F6 = IntVar()
        self.E9F6 = IntVar()
        # ======= variable  to Entry Frame 7 ===========
        self.E1F7 = IntVar()
        self.E2F7 = IntVar()
        self.E3F7 = IntVar()
        self.E4F7 = IntVar()
        self.E5F7 = IntVar()
        self.E6F7 = IntVar()
        self.E7F7 = IntVar()
        self.E8F7 = IntVar()
        self.E9F7 = IntVar()

        # ======  متغيرات الفاتوره =========
        self.fatora = StringVar()
        x = random.randint(1000,9999)
        self.fatora.set(str(x))
        self.name = StringVar()
        self.name.set(str())

        self.phone = StringVar()

        # ======  متغيرات الحساب الكلي =========
        self.E1F4 = StringVar()
        self.E2F4 = StringVar()
        self.E3F4 = StringVar()

        # ====frame the information====
        F1 = Frame(root, bd=2, width=300, height=180, bg='#0B2F3A')
        F1.place(x=760, y=30)

        # ====label the information====
        title = Label(F1, text='بيانات المشتري', fg='gold', bg='#0B2F3A', font=('tajawal', 16, 'bold'))
        title.place(x=70, y=0)

        # ===information the man===
        the_name = Label(F1, text='اسم المشتري', fg='#FF8201', bg='#0B2F3A', font=('tajawal', 13, 'bold'))
        the_name.place(x=140, y=40)
        the_phone = Label(F1, text='رقم المشتري', fg='#FF8201', bg='#0B2F3A', font=('tajawal', 13, 'bold'))
        the_phone.place(x=140, y=80)
        the_num = Label(F1, text='رقم الفاتوره', fg='#FF8201', bg='#0B2F3A', font=('tajawal', 13, 'bold'))
        the_num.place(x=140, y=120)

        # =====rect to the input information the man===
        enter_name = Entry(F1, textvariable=self.name,font=('tajawal', 9), justify='center')
        enter_name.place(x=20, y=42, width=110)
        enter_phone = Entry(F1, textvariable=self.phone,font=('tajawal', 9), justify='center')
        enter_phone.place(x=20, y=82, width=110)
        enter_num = Entry(F1, textvariable=self.fatora,font=('tajawal', 9), justify='center')
        enter_num.place(x=20, y=122, width=110)

        # ======button search======
        #bot_search = Button(F1, text='بحث',width=23, bg='gold',font=('tajawal', 10) )
        #bot_search.place(x=20, y=150)

        # ==== Fatora: bill ========
        F2 = Frame(root, width=300, height=30, bg='#0B2F3A')
        F2.place(x=760, y=210)
        title_bill = Label(F2, text='[~~~~ الفواتير ~~~~]', bg='#0B2F3A', font=('tajawal', 12, 'bold'), fg='white')
        title_bill.place(x=60, y=2)

        # ===== Frame - Scrollbar====
        F3 = Frame(root, width=250, height=285, bg='#0B2F3A')
        F3.place(x=760, y=240)
        scorll_y = Scrollbar(F3, orient=VERTICAL)  # تكوين عمود للنزول بلنص بشكل عمودي
        self.textarea= Text(F3, yscrollcommand=scorll_y.set, width=28 , height=22.4)
        scorll_y.pack(side=LEFT,fill=Y)   # ملئها بشكل كامل عموديا ووضعه على اليسار
        scorll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)


        # ======== Price ============
        F4 = Frame(root, bd = 2, width = 657, height=112, bg="#0B2F3A")
        F4.place(x=0, y=488)
        F44 = Frame(root, bd=2, width=103, height=112, bg="#0B2F3A")
        F44.place(x=657, y=488)

        # ======= Button of the frame 4 =======
        hesab = Button(F4, text='الحساب', width=13, height=1, font='tajawal', bg='#DBA901',command=self.total_prise)
        hesab.place(x=490, y=5)
        fatora = Button(F4, text='تصدير الفاتوره', width=13, height=1, font='tajawal', bg='#DBA901',command=self.welcome)
        fatora.place(x=490, y=55)
        clear = Button(F4, text='افراغ الحقول', width=13, height=1, font='tajawal', bg='#DBA901',command=self.deleted_count)
        clear.place(x=330, y=5)
        exit = Button(F4, text='اغلاق البرنامج', width=13, height=1, font='tajawal', bg='#DBA901',command=self.close)
        exit.place(x=330, y=55)

        # ======= label of the frame 4 ======
        label1 = Label(F4, text='حساب اجهزه الكهربائيه', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label1.place(x=195, y=10)
        label2 = Label(F4, text='حساب  الهواتف', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label2.place(x=195, y=40)
        label3 = Label(F4, text='حساب مواد المنزليه ', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label3.place(x=195, y=70)

        # ======== rect to the show prise ========
        entry1 = Entry(F4, textvariable=self.E1F4, font=('tajawal', 9), justify='center')
        entry1.place(x=40, y=15, width=110)
        entry2 = Entry(F4, textvariable=self.E2F4, font=('tajawal', 9), justify='center')
        entry2.place(x=40, y=45, width=110)
        entry3 = Entry(F4, textvariable=self.E3F4, font=('tajawal', 9), justify='center')
        entry3.place(x=40, y=75, width=110)

        # ============ frame to legumes =======
        F5 = Frame(root, bd=2, width=250, height=457, bg="#0B2F3A")
        F5.place(x=0, y=30)

        # ======= label in frame 5 ========
        label5_1 = Label(F5, text='اجهزه كهربائية', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_1.place(x=80, y=0)

        label5_1 = Label(F5, text='الاسم', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_1.place(x=210, y=25)
        label5_2 = Label(F5, text='العدد', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_2.place(x=120, y=25)
        label5_3 = Label(F5, text='السعر', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_3.place(x=30, y=25)

        label5_4 = Label(F5, text='مكنسه',font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_4.place(x=205, y=80)
        label5_5 = Label(F5, text='مبرده', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_5.place(x=209, y=110)
        label5_6 = Label(F5, text='غساله', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_6.place(x=206, y=140)
        label5_7 = Label(F5, text='ميكرويف', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_7.place(x=190, y=170)
        label5_8 = Label(F5, text='خلاط', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_8.place(x=210, y=200)
        label5_9 = Label(F5, text='مكواة', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_9.place(x=206, y=230)
        label5_10 = Label(F5, text='مقلاة كهربائيه', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_10.place(x=165, y=260)
        label5_11 = Label(F5, text='فرن', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_11.place(x=216, y=290)
        label5_12= Label(F5, text='فلتر ماء', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_12.place(x=192, y=320)

        # ================entry in frame 5 =================
        entry5_1 = Entry(F5, textvariable=self.E1F5 ,font=('tajawal', 9), justify='center')
        entry5_1.place(x=100, y=80, width=50)
        entry5_2 = Entry(F5, textvariable=self.E2F5,font=('tajawal', 9), justify='center')
        entry5_2.place(x=100, y=110, width=50)
        entry5_3 = Entry(F5, textvariable=self.E3F5,font=('tajawal', 9), justify='center')
        entry5_3.place(x=100, y=140, width=50)
        entry5_4 = Entry(F5, textvariable=self.E4F5,font=('tajawal', 9), justify='center')
        entry5_4.place(x=100, y=170, width=50)
        entry5_5 = Entry(F5, textvariable=self.E5F5,font=('tajawal', 9), justify='center')
        entry5_5.place(x=100, y=200, width=50)
        entry5_6 = Entry(F5, textvariable=self.E6F5,font=('tajawal', 9), justify='center')
        entry5_6.place(x=100,y=230, width=50)
        entry5_7 = Entry(F5, textvariable=self.E7F5,font=('tajawal', 9), justify='center')
        entry5_7.place(x=100, y=260, width=50)
        entry5_8 = Entry(F5, textvariable=self.E8F5,font=('tajawal', 9), justify='center')
        entry5_8.place(x=100, y=290, width=50)
        entry5_9 = Entry(F5, textvariable=self.E9F5,font=('tajawal', 9), justify='center')
        entry5_9.place(x=100, y=320, width=50)

        # ====== label in prise to frame 5 ==========
        label5_1_1 = Label(F5, text='20$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_1_1.place(x=20, y=80)
        label5_2_2 = Label(F5, text='30$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_2_2.place(x=20, y=110)
        label5_3_3 = Label(F5, text='40$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_3_3.place(x=20, y=140)
        label5_4_4 = Label(F5, text='50$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_4_4.place(x=20, y=170)
        label5_5_5 = Label(F5, text='20$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_5_5.place(x=20, y=200)
        label5_6_6 = Label(F5, text='15$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_6_6.place(x=20, y=230)
        label5_7_7 = Label(F5, text='12$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_7_7.place(x=20, y=260)
        label5_8_8 = Label(F5, text='40$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_8_8.place(x=20, y=290)
        label5_9_9 = Label(F5, text='120$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_9_9.place(x=20, y=320)


        # ========== frame 6 =========
        F6 = Frame(root, bd=2, width=255, height=457, bg="#0B2F3A")
        F6.place(x=251, y=30)

        # ======= label in frame 6 ========
        label6_1 = Label(F6, text='هواتف ', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label6_1.place(x=100, y=0)

        label5_1 = Label(F6, text='الاسم', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_1.place(x=210, y=25)
        label5_2 = Label(F6, text='العدد', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_2.place(x=120, y=25)
        label5_3 = Label(F6, text='السعر', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_3.place(x=30, y=25)

        label5_4 = Label(F6, text='NOT9', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_4.place(x=195, y=80)
        label5_5 = Label(F6, text='NOT10', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_5.place(x=195, y=110)
        label5_6 = Label(F6, text='NOT20', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_6.place(x=195, y=140)
        label5_7 = Label(F6, text='S8', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_7.place(x=195, y=170)
        label5_8 = Label(F6, text='S9', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_8.place(x=195, y=200)
        label5_9 = Label(F6, text='S10', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_9.place(x=195, y=230)
        label5_10 = Label(F6, text='S21', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_10.place(x=195, y=260)
        label5_11 = Label(F6, text='A51', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_11.place(x=195, y=290)
        label5_12 = Label(F6, text='A70', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_12.place(x=195, y=320)

        # ===============  entry in frame 6 ==============
        entry6_1 = Entry(F6, textvariable=self.E1F6,font=('tajawal', 9), justify='center')
        entry6_1.place(x=100,y=80, width=50)
        entry6_2 = Entry(F6, textvariable=self.E2F6,font=('tajawal', 9), justify='center')
        entry6_2.place(x=100, y=110, width=50)
        entry6_3 = Entry(F6, textvariable=self.E3F6,font=('tajawal', 9), justify='center')
        entry6_3.place(x=100, y=140, width=50)
        entry6_4 = Entry(F6, textvariable=self.E4F6,font=('tajawal', 9), justify='center')
        entry6_4.place(x=100, y=170, width=50)
        entry6_5 = Entry(F6, textvariable=self.E5F6,font=('tajawal', 9), justify='center')
        entry6_5.place(x=100, y=200, width=50)
        entry6_6 = Entry(F6, textvariable=self.E6F6,font=('tajawal', 9), justify='center')
        entry6_6.place(x=100, y=230, width=50)
        entry6_7 = Entry(F6, textvariable=self.E7F6,font=('tajawal', 9), justify='center')
        entry6_7.place(x=100, y=260, width=50)
        entry6_8 = Entry(F6, textvariable=self.E8F6,font=('tajawal', 9), justify='center')
        entry6_8.place(x=100, y=290, width=50)
        entry6_9 = Entry(F6, textvariable=self.E9F6,font=('tajawal', 9), justify='center')
        entry6_9.place(x=100, y=320, width=50)

        # ====== label in prise to frame 6 ==========
        label6_1_1 = Label(F6, text='200$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_1_1.place(x=20, y=80)
        label6_2_2 = Label(F6, text='300$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_2_2.place(x=20, y=110)
        label6_3_3 = Label(F6, text='400$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_3_3.place(x=26, y=140)
        label6_4_4 = Label(F6, text='500$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_4_4.place(x=20, y=170)
        label6_5_5 = Label(F6, text='560$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_5_5.place(x=20, y=200)
        label6_6_6 = Label(F6, text='1500$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_6_6.place(x=20, y=230)
        label6_7_7 = Label(F6, text='120$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_7_7.place(x=20, y=260)
        label6_8_8 = Label(F6, text='300$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_8_8.place(x=20, y=290)
        label6_9_9 = Label(F6, text='400$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label6_9_9.place(x=20, y=320)

        # ========== frame to 7 ==================
        F7 = Frame(root, bd=2, width=252, height=457, bg="#0B2F3A")
        F7.place(x=507, y=30)

        # ======= label in frame 7 ========
        label7_1 = Label(F7, text='مواد منزليه', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label7_1.place(x=95, y=0)

        label5_1 = Label(F7, text='الاسم', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_1.place(x=210, y=25)
        label5_2 = Label(F7, text='العدد', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_2.place(x=120, y=25)
        label5_3 = Label(F7, text='السعر', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='gold')
        label5_3.place(x=30, y=25)

        label5_4 = Label(F7, text='فلاش', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_4.place(x=210, y=80)
        label5_5 = Label(F7, text='قاصر', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_5.place(x=205, y=110)
        label5_6 = Label(F7, text='زاهي', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_6.place(x=209, y=140)
        label5_7 = Label(F7, text='عملاق', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_7.place(x=209, y=170)
        label5_8 = Label(F7, text='صابون', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_8.place(x=209, y=200)
        label5_9 = Label(F7, text='تايت', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_9.place(x=209, y=230)
        label5_10 = Label(F7, text='ديتول', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_10.place(x=209, y=260)
        label5_11 = Label(F7, text='منظف', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_11.place(x=209, y=290)
        label5_12 = Label(F7, text='سيترو', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label5_12.place(x=209, y=320)

        # ======== entry in frame 7 ===========
        entry5_1 = Entry(F7, textvariable=self.E1F7,font=('tajawal', 9), justify='center')
        entry5_1.place(x=100,y=80, width=50)
        entry5_2 = Entry(F7, textvariable=self.E2F7,font=('tajawal', 9), justify='center')
        entry5_2.place(x=100, y=110, width=50)
        entry5_3 = Entry(F7, textvariable=self.E3F7,font=('tajawal', 9), justify='center')
        entry5_3.place(x=100, y=140, width=50)
        entry5_4 = Entry(F7, textvariable=self.E4F7,font=('tajawal', 9), justify='center')
        entry5_4.place(x=100, y=170, width=50)
        entry5_5 = Entry(F7, textvariable=self.E5F7,font=('tajawal', 9), justify='center')
        entry5_5.place(x=100, y=200, width=50)
        entry5_6 = Entry(F7, textvariable=self.E6F7,font=('tajawal', 9), justify='center')
        entry5_6.place(x=100, y=230, width=50)
        entry5_7 = Entry(F7, textvariable=self.E7F7,font=('tajawal', 9), justify='center')
        entry5_7.place(x=100, y=260, width=50)
        entry5_8 = Entry(F7, textvariable=self.E8F7,font=('tajawal', 9), justify='center')
        entry5_8.place(x=100, y=290, width=50)
        entry5_9 = Entry(F7, textvariable=self.E9F7,font=('tajawal', 9), justify='center')
        entry5_9.place(x=100, y=320, width=50)

        # ====== label in prise to frame 7 ==========
        label7_1_1 = Label(F7, text='2$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_1_1.place(x=20, y=80)
        label7_2_2 = Label(F7, text='3$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_2_2.place(x=20, y=110)
        label7_3_3 = Label(F7, text='4$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_3_3.place(x=20, y=140)
        label7_4_4 = Label(F7, text='5$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_4_4.place(x=20, y=170)
        label7_5_5 = Label(F7, text='2$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_5_5.place(x=20, y=200)
        label7_6_6 = Label(F7, text='10$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_6_6.place(x=20, y=230)
        label7_7_7 = Label(F7, text='1$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_7_7.place(x=20, y=260)
        label7_8_8 = Label(F7, text='4$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_8_8.place(x=20, y=290)
        label7_9_9 = Label(F7, text='2$', font=('tajawal', 12, 'bold'), bg='#0B2F3A', fg='white')
        label7_9_9.place(x=20, y=320)

    def close(self):
        exit(root)

    def deleted_count(self):
         self.E1F5.set(str("0"))
         self.E2F5.set(str("0"))
         self.E3F5.set(str("0"))
         self.E4F5.set(str("0"))
         self.E5F5.set(str("0"))
         self.E6F5.set(str("0"))
         self.E7F5.set(str("0"))
         self.E8F5.set(str("0"))
         self.E9F5.set(str("0"))
         self.E1F6.set(str("0"))
         self.E2F6.set(str("0"))
         self.E3F6.set(str("0"))
         self.E4F6.set(str("0"))
         self.E5F6.set(str("0"))
         self.E6F6.set(str("0"))
         self.E7F6.set(str("0"))
         self.E8F6.set(str("0"))
         self.E9F6.set(str("0"))
         self.E1F7.set(str("0"))
         self.E2F7.set(str("0"))
         self.E3F7.set(str("0"))
         self.E4F7.set(str("0"))
         self.E5F7.set(str("0"))
         self.E6F7.set(str("0"))
         self.E7F7.set(str("0"))
         self.E8F7.set(str("0"))
         self.E9F7.set(str("0"))

    def total_prise(self):
    # ==========  the total prises in F5 ========
        self.p1 = self.E1F5.get()*20
        self.p2 = self.E2F5.get()*30
        self.p3 = self.E3F5.get()*40
        self.p4 = self.E4F5.get()*50
        self.p5 = self.E5F5.get()*20
        self.p6 = self.E6F5.get()*15
        self.p7 = self.E7F5.get()*12
        self.p8 = self.E8F5.get()*40
        self.p9 = self.E9F5.get()*120
        self.tol = float(self.p1+self.p2+self.p3+self.p4+self.p5+self.p6+self.p7+self.p8+self.p9)
        self.E1F4.set(str(self.tol)+' $')

        # ==========  the total prises in F6 ========
        self.p11 = self.E1F6.get() * 200
        self.p22 = self.E2F6.get() * 300
        self.p33 = self.E3F6.get() * 400
        self.p44 = self.E4F6.get() * 500
        self.p55 = self.E5F6.get() * 560
        self.p66 = self.E6F6.get() * 1500
        self.p77 = self.E7F6.get() * 120
        self.p88 = self.E8F6.get() * 300
        self.p99 = self.E9F6.get() * 400
        self.tol1 = float(self.p11 + self.p22 + self.p33 + self.p44 + self.p55 + self.p66 + self.p77 + self.p88 + self.p99)
        self.E2F4.set(str(self.tol1) + ' $')

        # ==========  the total prises in F7 ========
        self.p111 = self.E1F7.get() * 2
        self.p222 = self.E2F7.get() * 3
        self.p333 = self.E3F7.get() * 4
        self.p444 = self.E4F7.get() * 5
        self.p555 = self.E5F7.get() * 2
        self.p666 = self.E6F7.get() * 10
        self.p777 = self.E7F7.get() * 1
        self.p888 = self.E8F7.get() * 4
        self.p999 = self.E9F7.get() * 2
        self.tol11 = float(self.p111 + self.p222 + self.p333 + self.p444 + self.p555 + self.p666 + self.p777 + self.p888 + self.p999)
        self.E3F4.set(str(self.tol11) + ' $')

    def welcome(self):

        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "اهلا بكم في سوبر ماركيت")
        self.textarea.insert(END, "\n============================")
        self.textarea.insert(END, f'\n B.NUM    :{self.fatora.get()}')
        self.textarea.insert(END, f'\n NAME     :{self.name.get()}')
        self.textarea.insert(END, f'\n PHONE    :{self.phone.get()}')
        self.textarea.insert(END, "\n============================")
        self.textarea.insert(END, f'\nPrise\t  count\t  Purchases')
        self.textarea.insert(END, "\n============================")

        # ========== frame 5 ============
        if self.E1F5.get() != 0:
            self.p1 = self.E1F5.get() * 20
            x = "مكنسه"
            self.textarea.insert(END,f'{self.p1}$\t    {self.E1F5.get()}\t    {x}\t  ')
        if self.E2F5.get() != 0:
            self.p2 = self.E2F5.get() * 30
            x = "مبرده"
            self.textarea.insert(END,f'{self.p2}$\t    {self.E2F5.get()}\t    {x}   ')
        if self.E3F5.get() !=0:
            self.p3 = self.E3F5.get() * 40
            x = "غساله"
            self.textarea.insert(END, f'{self.p3}$\t    {self.E3F5.get()}\t    {x}   ')
        if self.E4F5.get() != 0:
            self.p4 = self.E4F5.get() * 50
            x = "ميكرويف"
            self.textarea.insert(END, f'{self.p4}$\t    {self.E4F5.get()}\t    {x} ')
        if self.E5F5.get() != 0:
            self.p5 = self.E5F5.get() * 20
            x = "خلاط  "
            self.textarea.insert(END, f'{self.p5}$\t    {self.E5F5.get()}\t    {x}   ')
        if self.E6F5.get() != 0:
            self.p6 = self.E6F5.get() * 15
            x = "مكواة"
            self.textarea.insert(END, f'{self.p6}$\t    {self.E6F5.get()}\t    {x}   ')
        if self.E7F5.get() != 0:
            self.p7 = self.E7F5.get() * 50
            x = "مقلاة "
            self.textarea.insert(END, f'{self.p7}$\t    {self.E7F5.get()}\t    {x}   ')
        if self.E8F5.get() != 0:
            self.p8 = self.E8F5.get() * 50
            x = "فرن  "
            self.textarea.insert(END, f'{self.p8}$\t    {self.E8F5.get()}\t    {x}   ')
        if self.E9F5.get() != 0:
            self.p9 = self.E9F5.get() * 50
            x = "فلترماء"
            self.textarea.insert(END, f'{self.p9}$\t    {self.E9F5.get()}\t    {x}   ')
        # ========== frame 6 ============
        if self.E1F6.get() != 0:
            self.p10 = self.E1F6.get() * 200
            x = "NOT9"
            self.textarea.insert(END,f'{self.p10}$\t    {self.E1F6.get()}\t    {x}\t   ')
        if self.E2F6.get() != 0:
            self.p12 = self.E2F6.get() * 300
            x = "NOT10"
            self.textarea.insert(END,f'{self.p12}$\t    {self.E2F6.get()}\t    {x}   ')
        if self.E3F6.get() !=0:
            self.p13 = self.E3F6.get() * 400
            x = "NOT20"
            self.textarea.insert(END, f'{self.p13}$\t    {self.E3F6.get()}\t    {x}   ')
        if self.E4F6.get() != 0:
            self.p14 = self.E4F6.get() * 500
            x = "S8   "
            self.textarea.insert(END, f'{self.p14}$\t    {self.E4F6.get()}\t    {x}   ')
        if self.E5F6.get() != 0:
            self.p15 = self.E5F6.get() * 560
            x = "S9   "
            self.textarea.insert(END, f'{self.p15}$\t    {self.E5F6.get()}\t    {x}   ')
        if self.E6F6.get() != 0:
            self.p16 = self.E6F6.get() * 1000
            x = "S10  "
            self.textarea.insert(END, f'{self.p16}$\t    {self.E6F6.get()}\t    {x}   ')
        if self.E7F6.get() != 0:
            self.p17 = self.E7F6.get() * 120
            x = "S21  "
            self.textarea.insert(END, f'{self.p17}$\t    {self.E7F6.get()}\t    {x}   ')
        if self.E8F6.get() != 0:
            self.p18 = self.E8F6.get() * 300
            x = "A51  "
            self.textarea.insert(END, f'{self.p18}$\t    {self.E8F6.get()}\t    {x}   ')
        if self.E9F6.get() != 0:
            self.p19 = self.E9F6.get() * 400
            x = "A70"
            self.textarea.insert(END, f'{self.p19}$\t    {self.E9F6.get()}\t    {x}   ')
        # ========== frame 7 ============
        if self.E1F7.get() != 0:
            self.p20 = self.E1F7.get() * 2
            x = "فلاش"
            self.textarea.insert(END,f'{self.p20}$\t    {self.E1F7.get()}\t    {x}\t    ')
        if self.E2F7.get() != 0:
            self.p21 = self.E2F7.get() * 3
            x = "قاصر"
            self.textarea.insert(END,f'{self.p21}$\t    {self.E2F7.get()}\t    {x}    ')
        if self.E3F7.get() !=0:
            self.p22 = self.E3F7.get() * 4
            x = "زاهي"
            self.textarea.insert(END, f'{self.p22}$\t    {self.E3F7.get()}\t    {x}    ')
        if self.E4F7.get() != 0:
            self.p23 = self.E4F7.get() * 5
            x = "عملاق"
            self.textarea.insert(END, f'{self.p23}$\t    {self.E4F7.get()}\t    {x}    ')
        if self.E5F7.get() != 0:
            self.p24 = self.E5F7.get() * 2
            x = "صابون"
            self.textarea.insert(END, f'{self.p24}$\t    {self.E5F7.get()}\t    {x}    ')
        if self.E6F7.get() != 0:
            self.p25 = self.E6F7.get() * 1
            x = "تايت"
            self.textarea.insert(END, f'{self.p25}$\t    {self.E6F7.get()}\t    {x}     ')
        if self.E7F7.get() != 0:
            self.p26 = self.E7F7.get() * 5
            x = "ديتول"
            self.textarea.insert(END, f'{self.p26}$\t    {self.E7F7.get()}\t    {x}   ')
        if self.E8F7.get() != 0:
            self.p27 = self.E8F7.get() * 5
            x = "سيترو"
            self.textarea.insert(END, f'{self.p27}$\t    {self.E8F7.get()}\t    {x}   ')
        if self.E9F7.get() != 0:
            self.p28 = self.E9F7.get() * 1
            x = "منظف"
            self.textarea.insert(END, f'{self.p28}$\t    {self.E9F7.get()}\t    {x}   ')

        self.textarea.insert(END, "\n============================")
        x = self.tol1 + self.tol + self.tol11
        self.textarea.insert(END,f'The total amount ~~{x}~~')


root = Tk()
ob = Super(root)
root.mainloop()