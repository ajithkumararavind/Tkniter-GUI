#grabing time using time module

import time
dtime = time.asctime()
timelist  = dtime.split(' ')
distime = '{}{}{}{}{}'.format(timelist[0],'/',timelist[1],'-',timelist[2])
logtime = '{}{}{}'.format(timelist[3],'-',timelist[1])

from tkinter import *

#defining fonts in the tkinter
mfont = ('Ariel',25,'bold')
tfont = ('Ariel',15,'bold')
nfont = ('verdana',10,'bold')

root = Tk()
root.title('Prepared by: Mr.cool!')
root.geometry('515x240+0+0')

import csv
item = IntVar()
item2 = StringVar()


mframe = Frame(root, height = 100, width = 600,)
mframe.pack(side = 'top', fill = 'both')
eframe = Frame(root, height = 150, width = 600)
eframe.pack(side = 'top', fill = 'both')
tframe = Frame(root, height = 150, width = 600)
tframe.pack(side = 'top', fill = 'both')
bframe = Frame(root, height = 150,width = 600)
bframe.pack(side = 'bottom', fill = 'both')

mainlabel = Label(mframe,text = "Ponnu's Expense calculator",
                  font = mfont, fg = 'white', bg = 'grey')
mainlabel.grid(column = 0, row = 0)


timelabel = Label(mframe, text = distime, font = tfont)
timelabel.grid(column = 0, row = 1)


entry0 = Entry(eframe, textvariable = item )
entry0.grid(column = 1, row = 0, padx=20)



label0 = Label(eframe, text = "Expense", font = nfont,)
label0.grid(column = 0, row = 0)

label1 = Label(tframe, text = "Total", font = tfont)
label1.grid(column = 0, row = 2, rowspan = 2)

entry1 = Entry(tframe)
var = StringVar()
lis = ['Travel','Food','Grocery','Home','Other','Health','Entertainement','Fun']
var.set(lis[1])

Dropdown = OptionMenu(eframe, var, *lis)
Dropdown.grid(row = 0, column = 3)


def entrytime():
    total = 0
    category = var.get()
    
#this will write the headers
    with open('expense.csv','a') as logfile:
        
        item = entry0.get()
        writer = csv.writer(logfile)
        writer.writerow([logtime,category,item])

    with open ('expense.csv','r')as readfile:
        reader = csv.reader(readfile)
        reader.next()
        for line in reader:
            try:
                total += int(line[2])
                totlabel = Label(tframe, font = tfont, text = total)
                totlabel.grid(column = 1,ipadx =50, row = 2,rowspan = 2, ipady = 20)
            except:
                ValueError
def clearbutton():
    item2.set("")
    item.set("")
    
    
       
button0 = Button(bframe, text = "click here to enter", command = entrytime)
button0.grid(row = 4, column = 0 ,ipadx =50 , ipady = 5)

button1 = Button(bframe, text = "clear", command = clearbutton)
button1.grid(column = 1  ,ipadx =50, row = 4, ipady = 5)
root.mainloop()

