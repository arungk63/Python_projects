from tkinter import*

#window
root = Tk()
root.title('Calculation tool')
root.geometry('350x200')
root.resizable(False,False)

#function
def thickness():
    s3_minwall = float(e1.get())
    s2_minally = 0
    tol =0
    if s3_minwall <= 1.4:
        mylabel9 = Label(root, text = 'Value should be > 1.4' )
        mylabel9.grid(row=3,column =1)
    else:
        if s3_minwall > 1.4 and s3_minwall<=2:
            s2_minally=0.15
            tol = 0.20
        elif s3_minwall > 2 and s3_minwall<=2.5:
            s2_minally=0.20
            tol = 0.22
        elif s3_minwall > 2.5 and s3_minwall<=3.0:
            s2_minally=0.20
            tol = 0.25
        elif s3_minwall > 3.0 and s3_minwall<=4.5:
            s2_minally=0.20
            tol = 0.30
        elif s3_minwall > 4.5:
            s2_minally=0.25
            tol = 0.40
        elif s3_minwall <= 1.4:
            mylabel9 = Label(root, text = 'Value should be > 1.4' )
            mylabel9.grid(row=6,column =1)
        steemax = s3_minwall - s2_minally
        steemin = steemax - tol
        steeavg = (steemax + steemin)/2
        mylabel6 = Label(root, text = round(steemin,2) )
        mylabel7 = Label(root, text = round(steemax,2) )
        mylabel8 = Label(root, text = round(steeavg,2) )
       
        mylabel6.grid(row=4,column =1,sticky = W)
        mylabel7.grid(row=5,column =1,sticky = W)
        mylabel8.grid(row=6,column =1,sticky = W)
   

#putting label
mylabel1 = Label(root, text = "Std number : X-X-XX-XX")
mylabel2 = Label(root, text = "Main Thickness :")
mylabel3 = Label(root, text = "Layer thickness minimum : ")
mylabel4 = Label(root, text = "Layer thickness maximum : ")
mylabel5 = Label(root, text = "Layer thickness average : ")
#create button
mybutton = Button(root, text = "CALCULATE",padx =28,command=thickness)
#grid the label
mylabel1.grid(row=0,column=0,sticky = W,padx=5,pady=5)
mylabel2.grid(row=1,column=0,sticky = E,padx=3,pady=3)
mybutton.grid(row=2,column=1)
mylabel3.grid(row=4,column=0,sticky = E,padx=3,pady=3)
mylabel4.grid(row=5,column=0,sticky = E,padx=3,pady=3)
mylabel5.grid(row=6,column=0,sticky = E,padx=3,pady=3)

#input field
e1 = Entry(root)
e1.grid(row=1,column=1)

#value input
e1.get()

#infinit loop
root.mainloop()
