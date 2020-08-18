import  datetime
from DatabaseExecutions import database
from tkinter import *
import tkinter.messagebox
import random
class Software:
    def __init__(self,root):

        self.root=root
        self.root.title("Super Store")
        self.root.state("zoomed")
        bg_color="light blue"
        #############COSMETICS#######################
        self.fairnesscream=IntVar()
        self.Haircream=IntVar()
        self.Hairjel=IntVar()
        self.Hairspray=IntVar()
        self.VaxCream=IntVar()
        self.Cobraperfume=IntVar()
        ###########GROCERRY==================
        self.overallprize=IntVar()
        self.Rice=IntVar()
        self.Oil=IntVar()
        self.Dal=IntVar()
        self.Wheats=IntVar()
        self.Biscuits=IntVar()
        self.Milk=IntVar()
        ##################COLD DRINKS#################

        self.Coke=IntVar()
        self.sevenup=IntVar()
        self.Mirinda=IntVar()
        self.Sting=IntVar()
        self.Pepsi=IntVar()
        self.Sprite=IntVar()
        ##########TOTAL BILL Price and TAX
        self.cosmeticsTo=DoubleVar()
        self.GrocerryTo=DoubleVar()
        self.DrinksTo=DoubleVar()
        self.cosmeticsTax=DoubleVar()
        self.GrocerryTax=DoubleVar()
        self.DrinksTax=DoubleVar()

        ###########Customer Infomation############
        self.cname=StringVar()
        self.cuContact=StringVar()
        self.Search = StringVar()
        self.cuBill=IntVar()






    # +++++++++++++++++++CUSTOMER INFORMATION FRAME+++++++++++++++++++++++++

        self.lbl_title = Label(self.root, text="Super United Store",bg="Light Blue" ,fg="black", font=(("times new roman"),32,"bold"),bd=12, relief=GROOVE)
        self.lbl_title.pack(fill=X,pady=6)
        self.lbl_customer_info=LabelFrame(self.root,bd=12,relief=GROOVE,text="Customer Information",bg=bg_color ,fg="purple",font=(("times new roman") ,16, "bold" ),padx=20,pady=5)
        self.lbl_customer_info.place(x=0,y=80,relwidth=1)
        self.lbl_customer_name = Label(self.lbl_customer_info, text="Customer Name" ,fg="black", bg=bg_color,font=(("times new roman"),16,"bold"))
        self.lbl_customer_name.grid(row=0,column=0)
        self.Entry_customer_name = Entry(self.lbl_customer_info,textvariable=self.cname,width=20,font=("times new roman",16,"bold"),relief=SUNKEN,bd=7)
        self.Entry_customer_name.grid(row=0, column=5,padx=10,pady=5)
        self.lbl_Contactno = Label(self.lbl_customer_info, text="Contact No", fg="black", bg=bg_color, font=(("times new roman"), 16, "bold"))
        self.lbl_Contactno.grid(row=0, column=7)
        self.Entry_Customer_Contact = Entry(self.lbl_customer_info,textvariable=self.cuContact, width=20,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        self.Entry_Customer_Contact.grid(row=0, column=9, padx=10, pady=5)
        self.lbl_Bill = Label(self.lbl_customer_info, text="Bill No", fg="black", bg=bg_color, font=(("times new roman"), 16, "bold"))
        self.lbl_Bill.grid(row=0, column=11)
        self.Entry_lbl_CU_BILL = Entry(self.lbl_customer_info, width=20,textvariable=self.cuBill, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        self.Entry_lbl_CU_BILL.grid(row=0, column=13, padx=10, pady=5)
        Button1 = Button(self.lbl_customer_info, text="Search", fg="black", bg="white", font=(("times new roman"), 16, "bold"),bd=7,command=lambda:[self.text.delete(1.0,END),
                         self.text.insert(END,database.createdStringofSearch(self.Entry_lbl_CU_BILL.get()))])
        Button1.grid(row=0, column=14,padx=60,pady=3)


        ############ Cosmetic Frame################

        frame2 = LabelFrame(self.root, text="Cosmetics", bg=bg_color, fg="purple",
                            font=(("times new roman"), 16, "bold"), padx=20, pady=5,bd=7,relief=SUNKEN)
        frame2.place(x=5, y=180, width=325,height=350)

        lbl_Fairnesscream = Label(frame2, text="Fair Cream", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Fairnesscream.grid(row=0, column=0,sticky="w")
        Entry_fairnesscream = Entry(frame2, width=11,textvariable=self.fairnesscream ,font=("times new roman",16,"bold"),relief=SUNKEN, bd=7)
        Entry_fairnesscream.grid(row=0, column=13, padx=10, pady=5)
        lbl_HairCream = Label(frame2, text="Hair Cream", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_HairCream.grid(row=1, column=0,sticky="w")
        Entry_haircream = Entry(frame2, width=11,textvariable=self.Haircream ,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_haircream.grid(row=1, column=13, padx=10, pady=5)
        lbl_Hairjel = Label(frame2, text="Hair Jel", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Hairjel.grid(row=2, column=0,sticky="w")
        Entry_hairjel = Entry(frame2, width=11,textvariable=self.Hairjel ,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_hairjel.grid(row=2, column=13, padx=10, pady=5)
        lbl_Hairspray = Label(frame2, text="Hair Spray", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Hairspray.grid(row=3, column=0,sticky="w")
        Entry_hairspray = Entry(frame2, width=11 ,textvariable=self.Hairspray,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_hairspray.grid(row=3, column=13, padx=10, pady=5)
        lbl_VaxCream = Label(frame2, text="Vax Cream", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_VaxCream.grid(row=4, column=0,sticky="w")
        Entry_Vaxcream = Entry(frame2, width=11,textvariable=self.VaxCream ,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_Vaxcream.grid(row=4, column=13, padx=10, pady=5)
        lbl_perfume = Label(frame2, text="Perfume", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_perfume.grid(row=5, column=0,sticky="w")
        Entry_perfume = Entry(frame2, width=11,textvariable=self.Cobraperfume, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_perfume.grid(row=5, column=13, padx=10, pady=5)
        ########## Grocerry Frame333333333333

        frame3 = LabelFrame(self.root, text="Grocerry", bg=bg_color, fg="purple",
                            font=(("times new roman"), 16, "bold"), padx=20, pady=5, bd=7, relief=SUNKEN)
        frame3.place(x=340, y=180, width=325, height=350)
        lbl_rice = Label(frame3, text="Rice", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_rice.grid(row=0, column=0,sticky="w")
        Entry_rice = Entry(frame3, width=11,textvariable=self.Rice ,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_rice.grid(row=0, column=13, padx=10, pady=5)
        lbl_Oil = Label(frame3, text="Oil", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Oil.grid(row=1, column=0,sticky="w")
        Entry_oil = Entry(frame3, width=11, textvariable=self.Oil,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_oil.grid(row=1, column=13, padx=10, pady=5)
        lbl_Dal = Label(frame3, text="Dal", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Dal.grid(row=2, column=0,sticky="w")
        Entry_Dal = Entry(frame3, width=11,textvariable=self.Dal, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_Dal.grid(row=2, column=13, padx=10, pady=5)
        lbl_Wheat = Label(frame3, text="Wheat", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Wheat.grid(row=3, column=0,sticky="w")
        Entry_Wheat = Entry(frame3, width=11, textvariable=self.Wheats,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_Wheat.grid(row=3, column=13, padx=10, pady=5)
        lbl_Biscuit = Label(frame3, text="Biscuits", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Biscuit.grid(row=4, column=0,sticky="w")
        Entry_biscuit = Entry(frame3, width=11,textvariable=self.Biscuits, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_biscuit.grid(row=4, column=13, padx=10, pady=5)
        lbl_Milk = Label(frame3, text="Milk", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Milk.grid(row=5, column=0,sticky="w")
        Entry_Milk = Entry(frame3, width=11,textvariable=self.Milk, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_Milk.grid(row=5, column=13, padx=10, pady=5)

        #############Cold drinks Frame#################33333

        frame4 = LabelFrame(self.root, text="Cold Drinks", bg=bg_color, fg="purple",
                            font=(("times new roman"), 16, "bold"), padx=20, pady=5, bd=7, relief=SUNKEN)
        frame4.place(x=675, y=180, width=325, height=350)
        lbl_coke = Label(frame4, text="Coke", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"),pady=9)
        lbl_coke.grid(row=0, column=0,sticky="w")
        Entry_Coke = Entry(frame4, width=11,textvariable=self.Coke, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_Coke.grid(row=0, column=13, padx=10, pady=5)

        lbl_7up = Label(frame4, text="7-up", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"),pady=9)
        lbl_7up.grid(row=1, column=0,sticky="w")
        Entry_7up = Entry(frame4, width=11, textvariable=self.sevenup,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_7up.grid(row=1, column=13, padx=10, pady=5)
        lbl_Mirinda = Label(frame4, text="Mirinda", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"),pady=9)
        lbl_Mirinda.grid(row=2, column=0,sticky="w")
        Entry_Mirinda = Entry(frame4, width=11,textvariable=self.Mirinda, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_Mirinda.grid(row=2, column=13, padx=10, pady=5)
        lbl_Sting = Label(frame4, text="Sting", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"),pady=9)
        lbl_Sting.grid(row=3, column=0,sticky="w")
        Entry_sting = Entry(frame4, width=11, textvariable=self.Sting,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_sting.grid(row=3, column=13, padx=10, pady=5)
        lbl_pepsi = Label(frame4, text="Pepsi", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"),pady=9)
        lbl_pepsi.grid(row=4, column=0,sticky="w")
        Entry_pepsi = Entry(frame4, width=11,textvariable=self.Pepsi, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_pepsi.grid(row=4, column=13, padx=10, pady=5)
        lbl_sprite = Label(frame4, text="Sprite", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"),pady=9)
        lbl_sprite.grid(row=5, column=0,sticky="w")
        Entry_sprite = Entry(frame4, width=11,textvariable=self.Sprite, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_sprite.grid(row=5, column=13, padx=10, pady=5)

    ############BILL AREA##################################
        frame5 =Frame(self.root,padx=5,pady=5, bd=10, relief=GROOVE)
        frame5.place(x=1010, y=180, width=360, height=350)
        lbl_Billarea=Label(frame5,bd=7,text="Bill Area",fg="black",relief=GROOVE,bg="white", font=(("times new roman"), 16, "bold"))
        lbl_Billarea.pack(fill=X)
        scroll=Scrollbar(frame5,orient=VERTICAL)
        scroll.pack(side=RIGHT, fill=Y)


        self.text = Text(frame5,yscrollcommand=scroll.set)
        self.text.pack(fill=BOTH, expand=1)
        scroll.config(command=self.text.yview)

        self.Welcome()
        #                                     =======# LastFrame
        frame6 = LabelFrame(self.root, bd=12, relief=GROOVE, text="Billing Menu", bg=bg_color, fg="purple",
                            font=(("times new roman"), 15, "bold"),padx=5)
        frame6.place(x=1, y=537, relwidth=1,height=175)
        lbl_TotalCosmetics = Label(frame6, text="Total Cosmetics Price", fg="brown", bg=bg_color, font=("times new roman", 16, "bold"))
        lbl_TotalCosmetics.grid(row=0, column=0,sticky="w")
        Entry_CosmeticsTotal = Entry(frame6, width=11,textvariable=self.cosmeticsTo, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_CosmeticsTotal.grid(row=0, column=5, padx=10,pady=2)
        lbl_Grocry_price = Label(frame6, text="Total Groccery Price", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Grocry_price.grid(row=1, column=0,sticky="w")
        Entry_GroceryTotal = Entry(frame6, width=11,textvariable=self.GrocerryTo, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_GroceryTotal.grid(row=1, column=5, padx=10,pady=2 )
        lbl_Colddrinktotal = Label(frame6, text="Total Cold Drinks Price", fg="brown", bg=bg_color, font=(("times new roman"), 16, "bold"))
        lbl_Colddrinktotal.grid(row=2, column=0,sticky="w")
        Entry_colddrink_total = Entry(frame6, width=11,textvariable=self.DrinksTo, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_colddrink_total.grid(row=2, column=5, padx=10 ,pady=4)
        lbl_Colddrink_Tax = Label(frame6, text="Cold Drink Tax", fg="brown", bg=bg_color,
                       font=(("times new roman"), 16, "bold"))
        lbl_Colddrink_Tax.grid(row=2, column=7,sticky="w")
        Entry_colddrink_tax = Entry(frame6, width=11,textvariable=self.DrinksTax, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_colddrink_tax.grid(row=2, column=10, padx=10, pady=4)
        lbl_grocery_tax = Label(frame6, text="Grocerry Tax", fg="brown", bg=bg_color,
                       font=(("times new roman"), 16, "bold"))
        lbl_grocery_tax.grid(row=1, column=7,sticky="w")
        Entry_grocery_tax = Entry(frame6, width=11, textvariable=self.GrocerryTax,font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_grocery_tax.grid(row=1, column=10, padx=10, pady=4)
        lbl_cosmetics_tax = Label(frame6, text="Cosmetics Tax", fg="brown", bg=bg_color,
                       font=(("times new roman"), 16, "bold"))
        lbl_cosmetics_tax.grid(row=0, column=7,sticky="w")
        Entry_cosmetics_tax = Entry(frame6, width=11,textvariable=self.cosmeticsTax, font=("times new roman",16,"bold"), relief=SUNKEN, bd=7)
        Entry_cosmetics_tax.grid(row=0, column=10, padx=10)
        ##########BUTTONS##############

        frame7 = Frame(frame6, bd=12, relief=GROOVE,bg="white")
        frame7.place(x=670,width=665,height=138)
        button_total=Button(frame7,text="Total",width=7,fg="black",bg="cadetblue",font=("times new roman",20,"bold"),bd=11,relief=GROOVE,command=self.Total)
        button_total.grid(row=0,column=0,padx=11,pady=25)
        button_showBill = Button(frame7, text="Show Bill",width=7, fg="black", bg="cadetblue",relief=GROOVE ,font=("times new roman", 20, "bold"), bd=11,command=lambda:[self.BillArea(),
                     self.reset()])

        button_showBill.grid(row=0,column=1,padx=6,pady=10)
        button_saveBill = Button(frame7, width=7,text="Save Bill", fg="black", bg="cadetblue", relief=GROOVE,font=("times new roman", 20, "bold"), bd=11,
                     command=lambda:[database.createDatabse(self.text.get("1.0",END),
                self.cuBill.get()),tkinter.messagebox.showinfo("Saved","Your Data has been saved successfully!"),self.inserted()])
        button_saveBill.grid(row=0,column=2, padx=7,pady=10)

        button_ALLDATA = Button(frame7, width=7,text="All Data", fg="black",relief=GROOVE, bg="cadetblue", font=("times new roman", 20, "bold"), bd=11,command=lambda :
        [
            self.nextwindow()])
        button_ALLDATA.grid(row=0, column=4,padx=7,pady=10)





    def reset(self):
        self.fairnesscream.set("0")
        self.Haircream.set("0")
        self.Hairjel.set("0")
        self.Hairspray.set("0")
        self.VaxCream.set("0")
        self.Cobraperfume.set("0")
        ###########GROCERRY==================
        # self.overallprize.set("0")
        self.Rice.set("0")
        self.Oil.set("0")
        self.Dal.set("0")
        self.Wheats.set("0")
        self.Biscuits.set("0")
        self.Milk.set("0")
        ##################COLD DRINKS#################

        self.Coke.set("0")
        self.sevenup.set("0")
        self.Mirinda.set("0")
        self.Sting.set("0")
        self.Pepsi.set("0")
        self.Sprite.set("0")
        ##########TOTAL BILL Price and TAX
        self.cosmeticsTo.set("0.0")
        self.GrocerryTo.set("0.0")
        self.DrinksTo.set("0.0")
        # Tax
        self.cosmeticsTax.set("0.0")
        self.GrocerryTax.set("0.0")
        self.DrinksTax.set("0.0")
        self.Entry_customer_name.delete(0,END)
        self.Entry_Customer_Contact.delete(0,END)

    def Total(self):
        self.c_fc_p=(self.fairnesscream.get()*80)
        self.c_hc_p=(self.Haircream.get()*220)
        self.c_hj_p=(self.Hairjel.get()*340)
        self.c_hs_p=(self.Hairspray.get()*270)
        self.c_vc_p=(self.VaxCream.get()*180)
        self.c_cp_p=(self.Cobraperfume.get()*130)

        self.Total_Cosmetics_Price=(self.c_fc_p+self.c_hc_p+self.c_hj_p+self.c_hs_p+self.c_vc_p+self.c_cp_p)
        self.cosmeticsTo.set(str(self.Total_Cosmetics_Price)+" "+"Rs")
        self.cosmetics_Tax=((self.Total_Cosmetics_Price*0.05))
        self.cosmeticsTax.set((self.cosmetics_Tax))

        self.g_re_p=(self.Rice.get()*80)
        self.g_dl_p=(self.Dal.get()*110)
        self.g_ws_p=(self.Wheats.get()*165)
        self.g_ol_p=(self.Oil.get()*310)
        self.g_bs_p=(self.Biscuits.get()*20)
        self.g_mk_p=(self.Milk.get()*100)
        self.Total_Groccery_Price=(self.g_re_p+self.g_dl_p+self.g_ws_p+self.g_ol_p+self.g_bs_p+self.g_mk_p)
        self.GrocerryTo.set(str(self.Total_Groccery_Price)+" "+"Rs")
        self.groccery_tax=((self.Total_Groccery_Price * 0.05))
        self.GrocerryTax.set((self.groccery_tax))
        self.c_ce_p=(self.Coke.get() * 100)
        self.c_sp_p=(self.sevenup.get() * 80)
        self.c_ma_p=(self.Mirinda.get() * 90)
        self.c_se_p=(self.Sprite.get() * 80)
        self.c_pi_p=(self.Pepsi.get() * 60)
        self.c_sg_p=(self.Sting.get() * 70)
        self.Total_Drinks_Price =(self.c_ce_p  +self.c_sp_p  + self.c_ma_p + self.c_se_p + self.c_pi_p + self.c_sg_p)
        self.DrinksTo.set(str(self.Total_Drinks_Price) + " " + "Rs")
        self.drinks_tex=((self.Total_Drinks_Price * 0.05))
        self.DrinksTax.set((self.drinks_tex))
        ###################OVERALLPRODUCT PRICE
        self.overallprize=self.Total_Cosmetics_Price+self.Total_Groccery_Price+self.Total_Drinks_Price



    def Welcome(self):
        self.text.delete("1.0", END)
        self.text.insert(END, "\t"+" "+"Welcome Bill Retail")
        x = random.randint(1000, 9999)
        self.cuBill.set((x))
        self.text.insert(END, "\n\n"+" "+"Bill No:" + str(self.cuBill.get()))
        self.text.insert(END, "\n"+" "+"Customer Name:" + str(self.cname.get()))
        self.text.insert(END, "\n"+" "+"Contact No:" + str(self.cuContact.get()))
        self.text.insert(END, "\n======================================")
        self.text.insert(END, "\n"+" "+"Products\t\t"+" "+"QTY"+"\t\t""Price\n")
        self.text.insert(END, "======================================")

    def BillArea(self):
        if self.cname.get()=="" or self.cuContact.get()=="":
            tkinter.messagebox.showerror("Error","Customer Information is Valid!")
        else:
            self.Welcome()
            if self.fairnesscream.get()!=0:
                self.text.insert(END, "\t"+" "+"Fair Cream:\t\t"+" "+" "+str(self.fairnesscream.get())+"\t\t"+" "+str(self.c_fc_p)+"RS")
            if self.Haircream.get()!=0:
                self.text.insert(END, "\t"+" "+"Hair Cream:\t\t"+" "+" "+str(self.Haircream.get())+"\t\t"+" "+str(self.c_hc_p)+"RS")
            if self.Hairjel.get()!=0:
                self.text.insert(END, "\t"+" "+"Hair Jel:\t\t"+" "+" "+str(self.Hairjel.get())+"\t\t"+" "+ str(self.c_hj_p)+"RS")
            if self.Hairspray.get()!=0:
                self.text.insert(END, "\t"+" "+"Hair Spray:\t\t"+" "+" "+str(self.Hairspray.get())+"\t\t"+" "+str(self.c_hs_p)+"RS")
            if self.VaxCream.get()!=0:
                self.text.insert(END, "\t"+" "+"VaxCream:\t\t"+" "+" "+str(self.VaxCream.get())+"\t\t"+" "+str(self.c_vc_p)+"RS")
            if self.Cobraperfume.get()!=0:
                self.text.insert(END, "\t"+" "+"Cobraperfume:\t\t"+" "+" "+str(self.Cobraperfume.get())+"\t\t"+" "+str(self.c_cp_p)+"RS")
            if self.Rice.get()!=0:
                self.text.insert(END, "\t"+" "+"Rice:\t\t"+" "+" "+str(self.Rice.get())+"\t\t"+" "+str(self.g_re_p)+"RS")
            if self.Oil.get()!=0:
                self.text.insert(END, "\t"+" "+"Oil:\t\t"+" "+" "+str(self.Oil.get())+"\t\t"+" "+str(self.g_ol_p)+"RS")
            if self.Dal.get()!=0:
                self.text.insert(END, "\t"+" "+"Dal:\t\t"+" "+" "+str(self.Dal.get())+"\t\t"+" "+ str(self.g_dl_p)+"RS")
            if self.Wheats.get()!=0:
                self.text.insert(END, "\t"+" "+"Wheats:\t\t"+" "+" "+str(self.Wheats.get())+"\t\t"+" "+str(self.g_ws_p)+"RS")
            if self.Biscuits.get()!=0:
                self.text.insert(END, "\t"+" "+"Biscuits:\t\t"+" "+" "+str(self.Biscuits.get())+"\t\t"+" "+str(self.g_bs_p)+"RS")
            if self.Milk.get()!=0:
                self.text.insert(END, "\t"+" "+"Milk:\t\t"+" "+" "+str(self.Milk.get())+"\t\t"+" "+str(self.g_mk_p)+"RS")
            if self.Coke.get()!=0:
                self.text.insert(END, "\t"+" "+"Coke:\t\t"+" "+" "+str(self.Coke.get())+"\t\t"+" "+str(self.c_ce_p)+"RS")
            if self.sevenup.get()!=0:
                self.text.insert(END, "\t"+" "+"7-up:\t\t"+" "+" "+str(self.sevenup.get())+"\t\t"+" "+str(self.c_sp_p)+"RS")
            if self.Mirinda.get()!=0:
                self.text.insert(END, "\t"+" "+"Mirinda:\t\t"+" "+" "+str(self.Mirinda.get())+"\t\t"+" "+str(self.c_ma_p)+"RS")
            if self.Sting.get()!=0:
                self.text.insert(END, "\t"+" "+"Sting:\t\t"+" "+" "+str(self.Sting.get())+"\t\t"+" "+str(self.c_sg_p)+"RS")
            if self.Sprite.get()!=0:
                self.text.insert(END, "\t"+" "+"Sprite:\t\t"+" "+" "+str(self.Sprite.get())+"\t\t"+" "+str(self.c_se_p)+"RS")
            if self.Pepsi.get()!=0:
                self.text.insert(END, "\t"+" "+"Pepsi:\t\t"+" "+" "+str(self.Pepsi.get()) + "\t\t"+" "+str((self.c_pi_p))+"RS")

            self.text.insert(END, "\n--------------------------------------")
            if self.cosmeticsTax.get()!="0.0":
                self.text.insert(END, "\n" + " " + "Cosmetics Tax:\t\t\t\t" +" "+ str(self.cosmeticsTax.get()))
            if self.GrocerryTax.get() != "0.0":
                self.text.insert(END, "\n" + " " + "Grocerry Tax:\t\t\t\t" + " " + str(self.GrocerryTax.get()))
            if self.DrinksTax.get() != "0.0":
                self.text.insert(END, "\n" + " " + "Cold Drink Tax:\t\t\t\t" + " " + str(self.DrinksTax.get()))
            self.text.insert(END, "\n--------------------------------------")
            self.text.insert(END,"\t"+" "+"Total Price:\t\t\t\t"+ " " +str(self.overallprize)+"RS")
            self.text.insert(END, "\n--------------------------------------")

            self.text.insert(END,"\n============================")
            now = datetime.datetime.now()
            self.text.insert(END, now.strftime("\t\n"+" "+"Time:"+" "+"%H:%M:%S"))
            self.text.insert(END, "\n============================")
            self.text.insert(END,"\n"+"\t"+" "+"Thanks for Visiting.")




    def inserted(self):
        self.text.delete(8.38,END)
        self.Entry_lbl_CU_BILL.delete(0,END)

###############ALL DATA ON NEXT WINDOW###############################################################

    def nextwindow(self):

        self.root3 = Tk()
        self.root3.title("Super United Store")
        self.root3.state('zoomed')

        frame_tile = Frame(self.root3, bg="#675d50")
        frame_tile.pack(side=TOP, fill=X)

        frame_upper = Frame(self.root3, bg="ghost white", bd=10, relief=RIDGE)
        frame_upper.pack(side=TOP, fill=BOTH, expand=1)

        frame_left_inUpper = Frame(frame_upper, bg="#675d50", bd=10, relief=RIDGE)
        frame_left_inUpper.pack(side=RIGHT, fill=Y, padx=20, pady=20)

        frame_right_inUpper = Frame(frame_upper, bg="#675d50", bd=10, relief=RIDGE)
        frame_right_inUpper.pack(side=LEFT, fill=BOTH, expand=1, padx=20, pady=20)

        frame_bottom_inRight = Frame(frame_right_inUpper, bg="#675d50")
        frame_bottom_inRight.pack(side=BOTTOM)

        # def iExist():
        #     iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to Exit")
        #     if iExit > 0:
        #         root3.destroy()
        #         return

        # def reset():
        #     self.text_ViewRecords.delete("1.0", END)

        lbl_title = Label(frame_tile, font=('times new roman', 30, 'bold'), text="Record of Super United Store",
                          bd=10, relief=RIDGE,
                          bg='ghost white', fg='Slate Gray4', justify=CENTER, width=40)
        lbl_title.pack(side=TOP, padx=10, pady=10)

        lbl_searchBill = Label(frame_bottom_inRight, text="Search Bill: ", font=('times new roman',16,"bold"),
                               bg="#675d50", fg="ghost white")
        lbl_searchBill.pack(side=LEFT, padx=10, pady=10)


        self.entry_searchBILL = Entry(frame_bottom_inRight, font=('times new roman',16,"bold"), width=22,bd=5,relief=GROOVE)
        self.entry_searchBILL.pack(side=LEFT, padx=20)
        lbl_DeleteBill = Label(frame_bottom_inRight, text="Delete Bill: ", font=('times new roman', 16, 'bold'),
                               bg="#675d50", fg="ghost white")
        lbl_DeleteBill.pack(side=LEFT, padx=20, pady=20)
        self.entry_DeleteBILL = Entry(frame_bottom_inRight, font=('times new roman',16,"bold"), width=22,bd=5,relief=GROOVE)
        self.entry_DeleteBILL.pack(side=LEFT, padx=20)


        button_view_Data = Button(frame_left_inUpper, text="View Data", bd=7, fg="Black", font=('times new roman', 16, 'bold'),
                                  width=20,
                                  command=lambda: [
                                      self.text_ViewRecords.delete('1.0', 'end'),
                                      self.text_ViewRecords.insert("1.0",database.createdStringofShowDataAll())
                                  ])
        button_view_Data.pack(padx=20, pady=20)


        button_Search = Button(frame_left_inUpper, text="Search", bd=7, fg="Black", font=('times new roman', 16, 'bold'),
                               width=20, command=lambda: [
                self.text_ViewRecords.delete('1.0', 'end'),
                self.text_ViewRecords.insert('1.0',database.createdStringofSearch(self.entry_searchBILL.get())),self.resetedsearchEntry()
                # tkinter.messagebox.showinfo("Search", "Record Searched")

            ])
        button_Search.pack(padx=30, pady=20)

        button_Delete = Button(frame_left_inUpper, text="Delete", bd=7, fg="Black", font=('times new roman', 16, 'bold'),
                               width=20, command=lambda: [

                database.createdStringofDelete(self.entry_DeleteBILL.get()),self.text_ViewRecords.delete('0.1','end'),
                tkinter.messagebox.showinfo("DELTE", "Record Deleted Successfully"),self.resetedDelEntry()

            ])
        button_Delete.pack(padx=30, pady=20)

        button_Reset = Button(frame_left_inUpper, text="Reset", bd=7, fg="Black", font=('times new roman', 16, 'bold'), width=20,
                              command=self.reseted)
        button_Reset.pack(padx=30, pady=20)

        button_Exit = Button(frame_left_inUpper, text="Exit", bd=7, fg="Black", font=('times new roman', 16, 'bold'), width=20,
                             command=self.iExist)
        button_Exit.pack(padx=30, pady=20)

        scrollbar = Scrollbar(frame_right_inUpper, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_ViewRecords = Text(frame_right_inUpper, yscrollcommand=scrollbar.set)
        self.text_ViewRecords.pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=10)
        scrollbar.configure(command=self.text_ViewRecords.yview)

    def iExist(self):
        iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to Exit")
        if iExit > 0:
            self.root3.destroy()
            return
    def reseted(self):
        self.text_ViewRecords.delete("1.0", END)
    def resetedsearchEntry(self):
        self.entry_searchBILL.delete(0,END)
    def resetedDelEntry(self):
        self.entry_DeleteBILL.delete(0,END)



root=Tk()
software=Software(root)
root.mainloop()


