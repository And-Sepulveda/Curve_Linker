from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox

def Pointer(x,y):
   P = []
   for i in range(x):
      P.append(pos)
   return P

def Close_all():
   root.destroy()
   
def Plot(X,Y):
   print("Ploting...")
   root = Tk()
   root.title("Two Dimensional Graph")
   root.geometry("1000x640+0+0")
   root.config(bg="cadet blue")

   MainFrame = Frame(root, bg="powder blue")
   MainFrame.grid()

   DataFrame2 = Frame(MainFrame, bd=1, width=1000, height=600, padx=40, pady=30, relief=RIDGE, bg="cadet blue")
   DataFrame2.grid()

   K = Label(DataFrame2, font=('Arial',14,'bold'), text="Data Science", bg="cadet blue", fg="white")
   K.grid(row = 0, column=0, sticky=W)

   canvas = Canvas(DataFrame2, width=900, height=510, bg = 'white')
   canvas.grid(row=1, column=0)

   canvas.create_line(100,450,800,450, width=4)
   canvas.create_line(100,450,100,50, width=4)

   for k in range(len(X)):
      x = X[k]
      y = Y[k]
##      x = (100 + 900*x)
##      y = (200 - 50*y/5)
      #x = (50 + 7*x)
      #y = (450 - (4*y)/5)
      print(x,y)
      canvas.create_oval(x-6,y-6,x+6,y+6,width=2,outline='red', fill='yellow')

   def iExit():
       qExit = tkinter.messagebox.askyesno("Quit System","Do you want to quit?")
       if qExit > 0:
          root.destroy()
          return
         
   b = Button(root,text='Exit',font=('arial',12,'bold'),width=16,bd=2,padx=8,bg='cadet blue',fg='white',command=iExit).grid()
   print("Ok")
   root.mainloop()


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

   
def filecatcher(a):
    s11 = []
    I11 = []
    Q11 = open(a,'r')
    i_11 = Q11.readline()
    print("Reading file...")
    for i_11 in Q11:
       d11 = i_11.split()
       s11.append(float(d11[0]))        
       I11.append(float(d11[1]))
    print("Ok")
    return s11, I11
   
def catcher1():
   #points = []
   X1 = []
   Y1 = []
   Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
   filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   resultStr.set(filename)
   print("Choosen file...")
   print(filename)
   try:
      x, y = filecatcher(filename)
      X1.append(x)
      Y1.append(y)
      Plot(X1,Y1)      
   except Exception:
       print("Invalid file!")
       tkinter.messagebox.showerror("Error","Invalid file!")
       return
   

def catcher2():
   #points = []
   X2 = []
   Y2 = []
   Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
   filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   resultStr.set(filename)
   print("Choosen file...")
   print(filename)
   try:
      x, y = filecatcher(filename)
      X2.append(x)
      Y2.append(y)
      Plot(X2,Y2)
      #Plot(X1+X2,Y1+Y2)
   except Exception:
       print("Invalid file!")
       tkinter.messagebox.showerror("Error","Invalid file!")
       return

root = Tk()
root.title('Curve_Linker 2.0')
root.geometry("350x150+30+30")
root.config(bg = "powder blue")
print("================================================================================")
print("Welcome to Curve_Linker")
print("================================================================================")
print("This software is intended to join two different data files from Small-angle scattering measurements,\nfilling the gap between them with points calculated by curve fitting.")
print("================================================================================")
print("Created by Anderson Ferreira Sepulveda (2019)")
print("Federal University of ABC")
print("================================================================================")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Data 1", command=donothing)
filemenu.add_command(label="Data 2", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=Close_all)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)


editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)


plotmenu = Menu(menubar,tearoff=0)
plotmenu.add_command(label = "Plot",command=Plot)
plotmenu.add_command(label = "Exponential fit",command=donothing)
plotmenu.add_command(label = "Linear fit",command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label = "Plot", menu=plotmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

plotmenu.add_separator()

root.config(menu=menubar)

   
labelframe = LabelFrame(root, text="Curve linker: SAXS and SANS data",bg="powder blue")

labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Choose two data from different measures: file #1 and file #2",bg="powder blue")

resultStr= StringVar()
resultStr.set("Enter file names:")

resultLabel = Label(textvariable=resultStr,bg="powder blue")
resultLabel.pack()

left.pack()

X1 = []
Y1 = []
X2 = []
Y2 = []
points = []

def catcher1():
   #points = []
   #X1 = []
   #Y1 = []
   Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
   filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   resultStr.set(filename)
   print("Choosen file...")
   print(filename)
   try:
      x, y = filecatcher(filename)
      X1.append(x)
      Y1.append(y)
      #print(X1)
      #print(Y1)
      Plot(X1,Y1)      
   except Exception:
      print("Invalid file!")
      tkinter.messagebox.showerror("Error","Invalid file!")
      return 

print(X1)   

def catcher2():
   X2 = []
   Y2 = []
   Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
   filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   resultStr.set(filename)
   print("Choosen file...")
   print(filename)
   try:
      x, y = filecatcher(filename)
      X2.append(x)
      Y2.append(y)
      #Plot(X2,Y2)
      Plot(X1+X2,Y1+Y2)
   except Exception:
      print("Invalid file!")
      tkinter.messagebox.showerror("Error","Invalid file!")
      return

def Plot(X,Y):
   print("Ploting...")
   root = Tk()
   root.title("Two Dimensional Graph")
   root.geometry("1000x640+0+0")
   root.config(bg="cadet blue")

   MainFrame = Frame(root, bg="powder blue")
   MainFrame.grid()

   DataFrame2 = Frame(MainFrame, bd=1, width=1000, height=600, padx=40, pady=30, relief=RIDGE, bg="cadet blue")
   DataFrame2.grid()

   K = Label(DataFrame2, font=('Arial',14,'bold'), text="Data Science", bg="cadet blue", fg="white")
   K.grid(row = 0, column=0, sticky=W)

   canvas = Canvas(DataFrame2, width=900, height=510, bg = 'white')
   canvas.grid(row=1, column=0)

   canvas.create_line(100,450,800,450, width=4)
   canvas.create_line(100,450,100,50, width=4)

   for k in range(len(X[0])):
      x = X[0][k]
      y = Y[0][k]
##      x = (100 + 900*x)
##      y = (200 - 50*y/5)
      #x = (50 + 7*x)
      #y = (450 - (4*y)/5)
      #print(x,y)
      canvas.create_oval(x-6,y-6,x+6,y+6,width=2,outline='red', fill='yellow')

   def iExit():
       qExit = tkinter.messagebox.askyesno("Quit System","Do you want to quit?")
       if qExit > 0:
          root.destroy()
          return
         
   b = Button(root,text='Exit',font=('arial',12,'bold'),width=16,bd=2,padx=8,bg='cadet blue',fg='white',command=iExit).grid()
   print("Ok")
   root.mainloop()
    
B1 = Button(root, text = "Data 1", width = 40, command = catcher1)
B1.pack()

B2 = Button(root, text = "Data 2", width = 40, command = catcher2)
B2.pack()


    

        
#dif_s = s2[0] - s11[len(s11)-1]
#dif_I = I11[len(I11)-1] - I2[0]

root.mainloop()
