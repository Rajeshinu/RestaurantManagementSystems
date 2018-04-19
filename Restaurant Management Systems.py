from tkinter import*
from random import randint
import time;


root=Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant")


text_Input=StringVar()
operator= ""

tops=Frame(root, width=1600,height=50, bg="steel blue", relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)


lblinfo=Label(tops, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="blue",bd=10,anchor='w')
lblinfo.grid(row=0, column=0)

#-----------LOCAL TIME-------------
localtime= time.strftime("%c")
lblinfo=Label(tops, font=('arial', 20, 'bold'), text=localtime, fg="blue",bd=10,anchor='w')
lblinfo.grid(row=1, column=0)

#-------------CALACULATOR----------------

def btnClick(numbers):
    global operator
    operator= operator+str(numbers)
    text_Input.set(operator)

def btncleardisplay():
    global operator
    operator=""
    text_Input.set("")

def btnequalsdisplay():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""


def Ref():
    x=randint(17000,18000)
    randomref=x
    rand.set(randomref)


    cofIdliVada = float(IdliVada.get())
    cofMeals=float(Meals.get())
    cofMasalDoas= float(MasalDoas.get())
    cofdrinks=float(Drinks.get())
    cofChickenBiryani=float(ChickenBiryani.get())
    cofMuttonBiryani=float(MuttonBiryani.get())


    cofIdliVada = cofIdliVada*25.00
    cofMeals=cofMeals*50.0
    cofMasalDoas=cofMasalDoas*35.0
    cofdrinks=cofdrinks*20.0
    cofChickenBiryani=cofChickenBiryani*50.0
    cofMuttonBiryani=cofMuttonBiryani*75.0

    costofmeal1=(cofIdliVada+cofMeals+cofMasalDoas+cofdrinks+cofChickenBiryani+cofMuttonBiryani)

    Servicecharge1=((cofIdliVada+cofMeals+cofMasalDoas+cofdrinks+cofChickenBiryani+cofMuttonBiryani)*0.1)

    Subtotal1=costofmeal1+Servicecharge1

    Tax1=Subtotal1+0.5

    Total1=Subtotal1+Tax1



    costofmeal.set(str(costofmeal1))
    Servicecharge.set(Servicecharge1)
    Subtotal.set(Subtotal1)
    Tax.set(Tax1)
    Total.set(Total1)






def Exit():
    root.destroy()

def Reset():
    rand.set("")
    IdliVada.set(0)
    MasalDoas.set(0)
    Meals.set(0)
    Subtotal.set("")
    Total.set("")
    Servicecharge.set("")
    Drinks.set(0)
    costofmeal.set("")
    Tax.set("")
    Cost.set("")
    ChickenBiryani.set(0)
    MuttonBiryani.set(0)

txtDisplay=Entry(f2,font=('arial',20, 'bold'), textvariable=text_Input,bd=30, insertwidth=4,bg="powder blue", justif="right")
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="7",bg="powder blue", command=lambda : btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="8",bg="powder blue", command=lambda : btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="9",bg="powder blue", command=lambda : btnClick(9)).grid(row=2,column=2)

addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="+",bg="powder blue", command=lambda : btnClick("+")).grid(row=2,column=3)

#---------------------------------------------------------

btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="4",bg="powder blue", command=lambda : btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="5",bg="powder blue", command=lambda : btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="6",bg="powder blue", command=lambda : btnClick(6)).grid(row=3,column=2)

subtracation=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="-",bg="powder blue", command=lambda : btnClick("-")).grid(row=3,column=3)

#---------------------------------------------------------

btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="1",bg="powder blue", command=lambda : btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="2",bg="powder blue", command=lambda : btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="3",bg="powder blue", command=lambda : btnClick(3)).grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="*",bg="powder blue", command=lambda : btnClick("*")).grid(row=4,column=3)

#---------------------------------------------------------

btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="0",bg="powder blue", command=lambda : btnClick(0)).grid(row=5,column=0)

btnclear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="C",bg="powder blue", command=btncleardisplay).grid(row=5,column=1)

btnequals=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="=",bg="powder blue", command=btnequalsdisplay).grid(row=5,column=2)

btndivison=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial", 20,'bold'),
            text="/",bg="powder blue", command=lambda : btnClick("/")).grid(row=5,column=3)

#----------------------------------Restaurant info1------------------------------------

rand=StringVar()
IdliVada=StringVar()
MasalDoas=StringVar()
Meals=StringVar()
Subtotal=StringVar()
Total=StringVar()
Servicecharge=StringVar()
Drinks=StringVar()
costofmeal=StringVar()
Tax=StringVar()
Cost=StringVar()
ChickenBiryani=StringVar()
MuttonBiryani=StringVar()

IdliVada.set(0)
MasalDoas.set(0)
Meals.set(0)
Drinks.set(0)
ChickenBiryani.set(0)
MuttonBiryani.set(0)


lblreference = Label(f1, font=('arial',16 ,'bold'), text="Bill No", bd=16, anchor='w')
lblreference.grid(row=0,column=0)
txtreference=Entry(f1, font=("arial", 16, 'bold'), textvariable=rand,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtreference.grid(row=0,column=1)


lblIdliVada = Label(f1, font=('arial',16 ,'bold'), text="Idli, Vada", bd=16, anchor='w')
lblIdliVada.grid(row=1,column=0)
txtIdliVada=Entry(f1, font=("arial", 16, 'bold'), textvariable=IdliVada,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtIdliVada.grid(row=1,column=1)

lblMasalDoas = Label(f1, font=('arial',16 ,'bold'), text="Masal Doas", bd=16, anchor='w')
lblMasalDoas.grid(row=2,column=0)
txtMasalDoas=Entry(f1, font=("arial", 16, 'bold'), textvariable= MasalDoas,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtMasalDoas.grid(row=2,column=1)

lblMeals = Label(f1, font=('arial',16 ,'bold'), text="Meals", bd=16, anchor='w')
lblMeals.grid(row=3,column=0)
txtMeals=Entry(f1, font=("arial", 16, 'bold'), textvariable= Meals, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtMeals.grid(row=3,column=1)

lblChickenBiryani = Label(f1, font=('arial',16 ,'bold'), text="Chicken Biryani", bd=16, anchor='w')
lblChickenBiryani.grid(row=4,column=0)
txtChickenBiryani=Entry(f1, font=("arial", 16, 'bold'), textvariable= ChickenBiryani,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtChickenBiryani.grid(row=4,column=1)

lblMuttonBiryani = Label(f1, font=('arial',16 ,'bold'), text="Mutton Biryani", bd=16, anchor='w')
lblMuttonBiryani.grid(row=5,column=0)
txtMuttonBiryani=Entry(f1, font=("arial", 16, 'bold'), textvariable= MuttonBiryani,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtMuttonBiryani.grid(row=5,column=1)

#----------------------------------Restaurant info 2 ------------------------------------


lblDrinks = Label(f1, font=('arial',16 ,'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1, font=("arial", 16, 'bold'), textvariable=Drinks,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtDrinks.grid(row=0,column=3)


lblcostofmeal = Label(f1, font=('arial',16 ,'bold'), text="Cost of Meal", bd=16, anchor='w')
lblcostofmeal.grid(row=1,column=2)
txtcostofmeal=Entry(f1, font=("arial", 16, 'bold'), textvariable=costofmeal,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtcostofmeal.grid(row=1,column=3)

lblServicecharge = Label(f1, font=('arial',16 ,'bold'), text="Service charge", bd=16, anchor='w')
lblServicecharge.grid(row=2,column=2)
txtServicecharge=Entry(f1, font=("arial", 16, 'bold'), textvariable=Servicecharge,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtServicecharge.grid(row=2,column=3)

lblSubtotal = Label(f1, font=('arial',16 ,'bold'), text="Sub Total", bd=16, anchor='w')
lblSubtotal.grid(row=3,column=2)
txtSubtotal=Entry(f1, font=("arial", 16, 'bold'), textvariable=Subtotal,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtSubtotal.grid(row=3,column=3)

lblTax = Label(f1, font=('arial',16 ,'bold'), text="State Tax", bd=16, anchor='w')
lblTax.grid(row=4,column=2)
txtTax=Entry(f1, font=("arial", 16, 'bold'), textvariable=Tax,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtTax.grid(row=4,column=3)



lblTotal = Label(f1, font=('arial',16 ,'bold'), text="Total Cost", bd=16, anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1, font=("arial", 16, 'bold'), textvariable=Total,bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtTotal.grid(row=5,column=3)

#----------------------------------Restaurant info 3 ------------------------------------


btnTotal = Button(f1,padx=16, pady=8, fg='black', font=('arial',16 ,'bold'), width = 10,
            text="Total", bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset = Button(f1,padx=16, pady=8, fg='black', font=('arial',16 ,'bold'), width = 10,
            text="Reset", bg="powder blue", command=Reset).grid(row=7, column=2)

btnExit = Button(f1,padx=16, pady=8, fg='black', font=('arial',16 ,'bold'), width = 10,
            text="Exit", bg="powder blue", command=Exit).grid(row=7, column=3)



root.mainloop()
