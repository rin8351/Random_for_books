import re
import random
from tkinter import *
import textwrap

class Application():
    def __init__(self,parent):
        self.char = self.zapoln('char.txt','Х')
        self.pers = self.zapoln('pers2.txt','Х')
        self.place = self.zapoln('place.txt','Х')
        self.word = self.zapoln('word2.txt',',')
        self.pril = self.zapoln('pril.txt','\n')
        self.sush = self.zapoln('sush.txt','\n')
        self.glag = self.zapoln('glag.txt','\n')
        self.uniq = self.zapoln('uniq.txt','\n')

        self.bg = PhotoImage(file = "f4.png")
        self.frame_main = Label(parent, image=self.bg)
        self.frame_main.image = self.bg
        self.frame_main.place(x=0,y=0)

        self.num = IntVar()
        nums = Entry(parent, width=5,textvariable=self.num,relief=RAISED)
        nums.insert(END,1)
        nums.place(x=30,y=33)
        self.lbl = Label(parent, text='',font=("Verdana Bold", 10),background='#EBD6BB') 
        self.lbl.place(x=140,y=33)
        btn = Button(parent,text="Характер!",command=self.clic,background='#D29A77',highlightcolor='#D0B4A2',foreground='#ffffff',font=("Verdana Bold", 10))
        btn.place(x=70,y=30)

        self.num1 = IntVar()
        nums1 = Entry(parent, width=5,textvariable=self.num1,relief=RAISED)
        nums1.insert(END,1)
        nums1.place(x=30,y=73)
        self.lbl1 = Label(parent, text='',font=("Verdana Bold", 10),background='#EBD6BB')  
        btn2 = Button(parent,text="Персонаж!",command=self.clic1,background='#D29A77',highlightcolor='#D0B4A2',foreground='#ffffff',font=("Verdana Bold", 10))
        btn2.place(x=70,y=70)    
        self.lbl1.place(x=140,y=70)

        self.num2 = IntVar()
        nums2 = Entry(parent, width=5,textvariable=self.num2,relief=RAISED)
        nums2.insert(END,1)
        nums2.place(x=30,y=113)   
        self.lbl2 = Label(parent, text='',font=("Verdana Bold", 10),background='#EBD6BB')
        btn3 = Button(parent,text="Слова!",command=self.clic2,background='#D29A77',highlightcolor='#D0B4A2',foreground='#ffffff',font=("Verdana Bold", 10))
        btn3.place(x=70,y=110)
        self.lbl2.place(x=140,y=110)

        self.num3 = IntVar()
        nums3 = Entry(parent, width=5,textvariable=self.num3,relief=RAISED)
        nums3.insert(END,1)
        nums3.place(x=30,y=153)
        self.lbl3 = Label(parent, text='',font=("Verdana Bold", 10),background='#EBD6BB')  
        btn4 = Button(parent,text="Локация!",command=self.clic3,background='#D29A77',highlightcolor='#D0B4A2',foreground='#ffffff',font=("Verdana Bold", 10))
        btn4.place(x=70,y=150)
        self.lbl3.place(x=140,y=150)

        self.lbl4 = Label(parent,text='',font=("Verdana Bold", 10),background='#EBD6BB')  
        self.lbl4.place(x=140,y=200)
        btn5 = Button(parent,text="Имя!",command=self.clic4,background='#D29A77',highlightcolor='#D0B4A2',foreground='#ffffff',font=("Verdana Bold", 10))  
        btn5.place(x=30,y=200) 

        btn6 = Button(parent,text="Предложение!",command=self.clic5,background='#D29A77',highlightcolor='#D0B4A2',foreground='#ffffff',font=("Verdana Bold", 10))  
        btn6.place(x=30,y=380)
        self.lbl5 = Label(parent,text='',font=("Verdana Bold", 10),background='#EBD6BB')  
        self.lbl5.place(x=140,y=380)

        self.lbl6 = Label(parent,text='',font=("Verdana Bold", 10),background='#EBD6BB')  
        self.lbl6.place(x=120,y=300)
        btn7 = Button(parent,text="Сокровища!",command=self.clic6,background='#D29A77',highlightcolor='#D0B4A2',foreground='#ffffff',font=("Verdana Bold", 10))  
        btn7.place(x=30,y=300)
        
        btn8 = Button(parent,text="Имя слогами!",command=self.clic7,background='#D29A77',highlightcolor='#D0B4A2',foreground='#ffffff',font=("Verdana Bold", 10))  
        btn8.place(x=30,y=250)
        self.lbl8 = Label(parent,text='',font=("Verdana Bold", 10),background='#EBD6BB')  
        self.lbl8.place(x=140,y=250)

    def clic6(self):
        t=self.wrap(' '.join(random.sample(self.uniq,1)))
        self.lbl6.configure(text=t)

    def clic5(self):
        t1=' '.join(random.sample(self.sush,1))
        t2=' '.join(random.sample(self.glag,1))
        t3=' '.join(random.sample(self.pril,1))
        t=self.wrap(t2+' '+t3+' '+t1)
        self.lbl5.configure(text=t)

    def wrap(self, string, lenght=40):
        return '\n'.join(textwrap.wrap(string, lenght))

    def clic(self):
        self.lbl.configure(text=(' '.join(random.sample(self.char,self.num.get()))))

    def clic1(self):
        self.lbl1.configure(text=(' '.join(random.sample(self.pers,self.num1.get()))))
    
    def clic2(self):
        self.lbl2.configure(text=(' '.join(random.sample(self.word,self.num2.get()))))

    def clic3(self):
        self.lbl3.configure(text=(' '.join(random.sample(self.place,self.num3.get()))))

    def zapoln(self,fl,steps):
        file=open(fl,'r',encoding="UTF-8")
        lst=[]
        for line in file.readlines():
            for i in re.split(steps, line.rstrip()):
                i = re.sub(r'\d+', '', i)
                i = re.sub(r'^\s+', '', i)
                if i != '':
                    if i not in lst:
                        lst.append(i)
        return lst

    def clic4(self):
        sog='б','в','г','д','ж','з','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ'
        gl='а','е','ё','и','о','у','э','ю','я'
        def slog():
            s=''.join(random.sample(sog,1))+''.join(random.sample(gl,1))
            return s
        name=[]
        for i in range(random.randint(2,6)):
            sl=random.choice([random.choice(sog),random.choice(gl),slog()])
            name.append(sl)  
        self.lbl4.configure(text=(''.join(name)))

    def clic7(self):
        sog='б','в','г','д','ж','з','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ'
        gl='а','е','ё','и','о','у','э','ю','я'
        name=[]
        for i in range(random.randint(2,3)):
            name.append(random.choice(sog) + random.choice(gl)) 
        self.lbl8.configure(text=(''.join(name))) 
        

if __name__ == "__main__":
    root = Tk()
    example = Application(root)
    root.geometry("810x600")
    root.title('Рандом для книг')
    root.mainloop()