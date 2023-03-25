
Author="高二(5)班巫嘉雄"
Time="2022.11.22"
Version="1.0"



import  os
import shutil 


import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import Scrollbar,Canvas
from tkinter import DISABLED, NORMAL,WORD,Tk,ttk
from random import randint
import sys
import sqlite3
import re

appdata_path=r"C://appdata//appdata.db"
subjects=("语文","英语","数学","物理","历史","地理","生物","化学","政治")

class Init():
    def __init__(self,pwd='202110'):
        
        if not os.path.exists("C://appdata"):
            os.mkdir("C://appdata")
        filepath="\\".join((sys.argv[0]).split("\\")[:-1])+"\\name.txt"
        #print(filepath)
        namefile_exists=os.path.exists(filepath)
        
        if namefile_exists:
            with open(filepath,"r") as file:
                namelist=list()
                for i in file.read().split():
                    if not((i=="") and (i in namelist)):
                        namelist.append((i,))
        else:
            print("Not file 'name.txt'")
            sys.exit()
        
        if len(namelist)<1:
            print("Please keep enough value in file 'name.txt'")
            sys.exit()
        
        if os.path.exists(appdata_path):
            os.remove(appdata_path)
        
        pattern=r"[0-9]{6}"
        if re.search(pattern,pwd):
            password=(re.findall(pattern,pwd)[0])
            
        else:
            print("password must be type int ")
            sys.exit()
        
        db=sqlite3.connect(appdata_path)
        cs=db.cursor()
        cs.execute("create table random(name varchar(10),%s)"%(",".join(["%s int(1)"%s for s in subjects]),))
        cs.executemany("insert into random(name,%s,%s,%s,%s,%s,%s,%s,%s,%s) values(?,0,0,0,0,0,0,0,0,0)"%subjects,namelist)
        cs.execute("create table app(name varchar(10),password int(6))")
        cs.execute("insert into app(name,password) values(?,?)",("random",password))
        db.commit()
        cs.close()
        db.close()

class Uninstall():
    def __init__(self,filename):
        if os.path.exists("C://appdata"):
            shutil.rmtree("C://appdata")
            
        if os.path.exists("C://appdata"):
            print("dir 'C://appdata' can not remove")
            sys.exit()

        os.remove(filename)

        if os.path.exists(filename):
            print("file '%s' can not remove"%(filename,))
            sys.exit()

        print("Uninstall prosess is finish")

class Reset():
    def __init__(self,subject):
        if (subject in subjects):
            with sqlite3.connect(appdata_path) as db:
                cs=db.cursor()
                cs.execute("update random set %s=0"%(subject,))
        else:
            print("Fail")
        


class Main():
    def __init__(self):
        if os.path.exists(appdata_path):
            MainWindow()
        else:
            print("The database did not init! Please use command'%s init'")
            sys.exit()
#===================================================================================================

class Input_area():
  def __init__(self,father=None,control=print,arg=None,tip='',x=0,y=100,height=300,width=200):
    self.arg=arg
    self.control=control
    self.num="0"
    if not father:
      father=Tk()
      self.block=ttk.Frame(father)
      print("not father")
    else:
      self.block=ttk.Frame(father)
    

    self.block.place(x=x,y=y,height=height,width=width)
      
    self.lbl=ttk.Label(self.block,text=self.num)
    self.list=[]  
    btn=ttk.Button(self.block,text="确定",command=self.rt)
    for i in range(1,10):
      self.list.append(ttk.Button(self.block,text=i,command=lambda loadnum=i:self.fm(loadnum)))
    btn0=ttk.Button(self.block,text="0",command=self.num0)
    btn_b=ttk.Button(self.block,text="<-",command=self.bksp)
    btn_c=ttk.Button(self.block,text="C",command=self.clear)
    self.lbl.place(x=60,y=0,width=60,height=30)  
    btn.place(x=60,y=30,width=60,height=30)
    self.placebtn()
    btn_c.place(x=0,y=150,width=60,height=30)
    btn0.place(x=60,y=150,width=60,height=30)
    btn_b.place(x=120,y=150,width=60,height=30) 
    

  def rt(self):
    num=self.num
    self.clear()
    self.control(int(num),arg=self.arg)
  
  def fm(self,num):
    if len(str(self.num))<3:
      self.num=str(int(self.num))
      self.num=self.num+str(num)
      self.lbl.configure(text=self.num)
    
    
  def num0(self):
    if len(str(self.num))<3:
      self.num=str(int(self.num))
      self.num=self.num+"0"
      self.lbl.configure(text=self.num)
      
    
  def bksp(self):    
    self.num=self.num[:-1]
    if len(self.num)==0:
      self.num="0"
    self.lbl.configure(text=self.num)
  
  def clear(self):   
    self.num="0"
    self.lbl.configure(text=self.num)
    
  def placebtn(self):
    local_column=0
    local_row=2
    for i in self.list:
      i.place(x=local_column*60,y=local_row*30,width=60,height=30)
      local_column+=1
      if local_column==3:
        local_column=0
        local_row+=1
#+++++++++++++++++++++++++++++++++++++

class Password_Input():
  def __init__(self,master,command=print,x=340,y=125,height=120,width=120):
    self.size=20
    self.command=command
    self.num=""
    self.pattern="[0-9]"
    
    self.block=ttk.Frame(master)
    

    self.block.place(x=x,y=y,height=height,width=width)
      
    self.lbl=ttk.Label(self.block,text=self.num)
    self.list=[]  
    btn=ttk.Button(self.block,text="确定",command=self.rt)
    for i in range(1,10):
      self.list.append(ttk.Button(self.block,text=i,command=lambda loadnum=i:self.fm(loadnum)))
    btn0=ttk.Button(self.block,text="0",command=self.num0)
    btn_b=ttk.Button(self.block,text="<-",command=self.bksp)
    btn_c=ttk.Button(self.block,text="C",command=self.clear)
    self.lbl.place(x=40,y=0,width=40,height=20)  
    btn.place(x=40,y=20,width=40,height=20)
    self.placebtn()
    btn_c.place(x=0,y=100,width=40,height=20)
    btn0.place(x=40,y=100,width=40,height=20)
    btn_b.place(x=80,y=100,width=40,height=20) 
    '''
    ---xxx---0
    ---com---10
     1  2  3  20
     4  5  6  30
     7  8  9  40
     c  0 <-  50
     0  20 40
    '''
    

  def rt(self):
    num=self.num
    self.clear()
    self.command(num)
  
  def fm(self,num):
    
    if len(str(self.num))<6:
      self.num=str(self.num)
      self.num=self.num+str(num)
      self.lbl.configure(text=re.sub(self.pattern,"*",str(self.num)))
      
    
    
  def num0(self):
    if len(str(self.num))<6:
      pattern="[0-9]"
      self.num=str(self.num)
      self.num=self.num+"0"
      self.lbl.configure(text=re.sub(self.pattern,"*",str(self.num)))
      
    
  def bksp(self):    
    self.num=self.num[:-1]
    if len(self.num)==0:
      self.num=""
    self.lbl.configure(text=re.sub(self.pattern,"*",str(self.num)))
  
  def clear(self):   
    self.num=""
    self.lbl.configure(text=re.sub(self.pattern,"*",str(self.num)))
    
  def placebtn(self):
    local_column=0
    local_row=2
    for i in self.list:
      i.place(x=local_column*40,y=local_row*20,width=40,height=20)
      local_column+=1
      if local_column==3:
        local_column=0
        local_row+=1
#++++++++++++++++++++++++++++++++++++++++++++++    

class Set_Subject():
    def __init__(self,master,main_window,subject):
        self.master=master
        self.main_window=main_window
        self.subject=subject
 
        self.page=ttk.Frame(master=self.main_window)
        
        self.master.Hidden()
        self.De_Hidden()

        self.password_page=ttk.Frame(self.page)
        self.password_page.place(width=800,height=370,y=30)

        self.return_button=ttk.Button(master=self.page,text="<返回",command=self.return_suppage)
        self.return_button.place(x=0,y=0,height=30,width=60)

        self.password_label=ttk.Label(master=self.password_page,text="Please Enter Password")
        self.password_label.place(x=320,width=160,y=90,height=30)
        self.password_input=Password_Input(master=self.password_page,command=self.check_password)

        

        self.op_page=ttk.Frame(master=self.page)

        
        
    def save(self):
        will_rand_list=[]
        willnot_rand_list=[]
        for i in self.checkbox_list:
            if int(i.get_value())==1:
                will_rand_list.append(i.name)
            elif int(i.get_value())==0:
                willnot_rand_list.append(i.name)
            else:
                print("%s's value not in[0,1] ")
        print('will rand:',will_rand_list)
        print("will not rand:",willnot_rand_list)
        with sqlite3.connect(appdata_path) as db:
            cs=db.cursor()

            if len(will_rand_list)>=1:
                for i in will_rand_list:
                    cs.execute("update random set %s=0 where name=?"%(self.subject,),(i,))
        
            if len(willnot_rand_list)>=1:
                for i in willnot_rand_list:
                    cs.execute("update random set %s=1 where name=?"%(self.subject,),(i,))
  
            db.commit()
            cs.close()
        # for i in self.checkbox_list:
        #     i.checkbox.destroy()
        self.return_suppage()
        sys.exit()
        
        #os.system("start %s"%(sys.argv[0],))
        #sys.exit()

          
             
          
       
       


    def Hidden(self):
        self.page.place_forget()

    def check_password(self,password):
        password=str(password)
        with sqlite3.connect(appdata_path) as db:
            cs=db.cursor()
            cs.execute("select password from app where name='random'")
            right_password=str(cs.fetchone()[0])
            cs.close()
        if password==right_password:
            self.goto_op_page()

        

    def De_Hidden(self):
        self.page.place(width=800,height=400)

    def goto_op_page(self):
        self.password_page.place_forget()
        self.op_page.place(width=800,height=370,y=30)
        self.savebutton=ttk.Button(master=self.op_page,text="SAVE",command=self.save)
        self.savebutton.place(x=100,y=340,height=30,width=50)
        self.cancel_button=ttk.Button(master=self.op_page,text="CANCEL",command=self.return_suppage)
        self.cancel_button.place(x=250,y=340,height=30,width=50)


        self.get_name()
        self.palce_checkbox()
        
    def get_name(self):
        with sqlite3.connect(appdata_path) as db:
            cs=db.cursor()
            cs.execute("select name,%s from random"%(self.subject,))
            self.namelist=cs.fetchall()  #[(name,is_select),()]
            cs.close()
        #print(self.namelist)

    def palce_checkbox(self):
        self.checkbox_list=list()
        self.check_area=ttk.Frame(self.op_page)
        self.check_area.place(x=600,height=370,width=200)
        self.check_frame=canvas_scroll(master=self.check_area,upper=self)
         

        
        

    def return_suppage(self):
        self.page.destroy()
        self.master.De_Hidden()
        self.main_window.title(self.subject)
        sys.exit()

#+++++++++++++++++++++++++++++++++++++++++++++++++++
class canvas_scroll():

    def __init__(self,master,upper):
        self.upper=upper

        canvas = tk.Canvas(master)
        canvas.place( width=200, height=370)
        canvas.config(scrollregion=(0,0,100,len(self.upper.namelist)*30))#可操控（x1，y1，x2，y2）的矩形

        frame = tk.Frame(canvas)
        frame.place(width=180,height=800)

        scroll = ttk.Scrollbar(canvas, orient="vertical")
        scroll.place(x=180, y=0, width=30, height=370)#只能用place
        scroll.config(command=canvas.yview)

        canvas.config(yscrollcommand=scroll.set)
        canvas.create_window((0,0), window=frame, anchor="nw")
        y_num=0
        for name,is_select in self.upper.namelist:
            #print(name,is_select)
            self.upper.checkbox_list.append(CheckBox(master=frame,name=name,is_select=is_select,y=y_num))
            y_num+=1

    
        
#+++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++
class CheckBox():
    def __init__(self,master,name,is_select,height=20,width=100,x=0,y=0):
        self.pid=randint(0,10)
        self.master=master
        self.name=name
        self.is_select=int(is_select)
        self.checkbox=tk.Checkbutton(master=master,text=self.name,command=self.command)
        #print(self.name,self.is_select)
        
        
        if self.is_select==0:
            
            self.checkbox.select()
            self.command()
            
        else:
            self.is_select=not self.is_select
            
        self.place(height=height,width=width,x=x,y=y)

    def command(self):
        self.is_select=not self.is_select
        #print("name=%s is_select=%s pid=%s"%(self.name,str(not self.is_select),self.pid))
        

    def get_value(self):
        return self.is_select
        

    def place(self,x=0,y=0,height=60,width=60):
        self.checkbox.grid(row=y)

class Random_Page():
    def __init__(self,master,main_window,subject):
        self.master=master
        self.main_window=main_window
        self.subject=subject
        self.main_window.title(self.subject)
        self.setpage=None

        self.page=ttk.Frame(master=self.main_window)

        self.master.Hidden()
        self.De_Hidden()

        self.return_button=ttk.Button(master=self.page,text="<返回",command=self.return_suppage)
        self.return_button.place(x=0,y=0,height=30,width=60)
        
        self.input_area=Input_area(father=self.page,control=self.start_rand,arg=None,tip='',x=0,y=200,height=300,width=200)

        self.print_area=ScrolledText(self.page,state=DISABLED)
        self.print_area.place(x=400,y=0,height=400,width=400)

        self.set_button=ttk.Button(master=self.page,text="Setting",command=self.setting)
        self.set_button.place(width=60,height=30,x=340,y=370)

    def setting(self):
        del self.setpage
        self.setpage=Set_Subject(master=self,main_window=self.main_window,subject=self.subject)

    def printdata(self,text):
        self.print_area.configure(state=NORMAL)
        if str(type(text))=="<class 'int'>":
            self.print_area.insert("end","%s%d%s"%(">>>",text,"\n\n"))
        else:
            self.print_area.insert("end","%s%s%s"%(">>>",str(text),"\n\n"))
        self.print_area.configure(state=DISABLED)
        


    
    def start_rand(self,num,arg):

        db=sqlite3.connect(appdata_path)
        cs=db.cursor()
        cs.execute("select name from random where %s=0"%(self.subject,))
        namelist=list([i[0] for i in cs.fetchall()])
        cs.close()
        db.close()

        randlist=list()
        while (len(randlist)<num) and (num<=self.get_studen_num()):
            if (len(namelist)==0):
                db=sqlite3.connect(appdata_path)
                cs=db.cursor()
                cs.execute("update random set %s=0"%(self.subject,))
                db.commit()
                cs.execute("select name from random where %s=0"%(self.subject,))
                namelist=list([i[0] for i in cs.fetchall()])
                
                cs.close()
                db.close()
            
            name=namelist[randint(0,len(namelist)-1)]
            
            if not(name in randlist):
                randlist.append(name)
                namelist.remove(name)

        if num==0 or num>self.get_studen_num():
            pass
        else:
            self.printdata(",".join(randlist))
            db=sqlite3.connect(appdata_path)
            cs=db.cursor()
            cs.executemany("update random set %s=1 where name=?"%self.subject,([i,] for i in randlist))
            db.commit()
            cs.close()
            db.close()

    def get_studen_num(self):
        db=sqlite3.connect(appdata_path)
        cs=db.cursor()
        cs.execute("select name from random")
        num=len(cs.fetchall())
        cs.close()
        db.close()
        return num


        

    def return_suppage(self):
        self.page.destroy()
        self.master.De_Hidden()
        self.main_window.title("主页")
        self=None
    
    def Hidden(self):
        self.page.place_forget()

    def De_Hidden(self):
        self.page.place(width=800,height=400)

class Button():

    def __init__(self,master,main_window,subject,posision):
        self.master=master
        self.subject=subject
        self.posision=posision
        self.main_window=main_window
        self.button=ttk.Button(master=master.page,text=self.subject,command=self.Rand) 
        self.button.place(x=posision[0]*200,y=self.posision[1]*100,width=100,height=50)


    def Rand(self):
        self.page=Random_Page(master=self.master,main_window=self.main_window,subject=self.subject)
    
class MainWindow():

    def __init__(self):
        self.window=Tk()
        self.screen_size=(self.window.winfo_screenwidth(),self.window.winfo_screenheight())
        self.window_size=(800,400)
        self.window.geometry("%dx%d+%d+%d"%self.getcenter())
        self.window.title("主页")

        self.page=ttk.Frame(self.window)
        self.De_Hidden()
        
        self.loadbutton()

        self.window.mainloop()
    
    def loadbutton(self):
        self.subject_list=subjects
        self.button_list=list()
        x=0
        y=0
        for subject in self.subject_list:
            self.button_list.append(Button(master=self,main_window=self.window,subject=subject,posision=(x,y)))
            x+=1
            if x==4:
                x=0
                y+=1

    def De_Hidden(self):
        self.page.place(x=0,y=0,width=800,height=600)
    
    def Hidden(self):
        self.page.place_forget()
        

    def getcenter(self):
        return(self.window_size[0],self.window_size[1],(self.screen_size[0]-self.window_size[0])/2,(self.screen_size[1]-self.window_size[1])/2)


if __name__=="__main__":
    argv=sys.argv[1:]
    file=sys.argv[0]
    longth=len(argv)
    if longth==0:
        MainWindow()

    

    elif longth==1:
        if argv[0]=="/?":
            help='''agrv :
                init                           #init
                init pwd=[password (type int)] #init and set password 
                uninstall                      #remove the tool from you computer
                /?                             #show this tip
            
            '''
            print(help)
        elif argv[0]=="uninstall":
            Uninstall(file)
        
        elif (argv[0]=="init"):
            Init()
    
    elif longth==2:
        if argv[0]=="init":
            Init(argv[1])
            

