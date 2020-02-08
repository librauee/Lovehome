# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:06:15 2020

@author: Administrator
"""


import tkinter
import tkinter.messagebox
import time
import datetime
from PIL import ImageTk,Image
import os
import random

class App(object):
    
    def __init__(self):
        self.win=tkinter.Tk()
        self.i=0
        self.img_paths=os.listdir('pictures')
        self.path=[os.sep.join(['pictures',i]) for i in self.img_paths]     
        self.CHP=['近朱者赤，近你者甜。','我想我是爱着你的，被你点赞过的朋友圈叫做甜甜圈。','我宣布人间水蜜桃非你莫属。','说老实话，我在人间贩卖黄昏只为收集世间温柔去见你。','月亮被嚼碎变成了小星星，你就藏在漫天的星光里。','我要变成一颗小奶糖，夜深了提着星星灯悄悄的溜进你梦里说晚安，你一定不能想象。','当星河都在变迁，你我却仍天各一边，但请相信，纵使万水千山、日日夜夜我对你的爱与思念从未改变。']
        self.menu_list=['account_prompt1','account_prompt2','password_prompt1','password_prompt2']
        
    def set_win(self):
        self.win.title("Login")
        self.win.geometry("450x350")
        menubar=tkinter.Menu(self.win)
        self.win.config(menu=menubar)
        menu1=tkinter.Menu(menubar,tearoff=False)
        menu2=tkinter.Menu(menubar,tearoff=False)
        for item in self.menu_list[:2]:
            if item=='account_prompt1':
                menu1.add_separator()
                menu1.add_command(label=item,command=self.get_account1)
            else:
                menu1.add_command(label=item,command=self.get_account2)
        for item in self.menu_list[2:]:
            if item=='password_prompt1':
                menu2.add_separator()
                menu2.add_command(label=item,command=self.get_password1)
            else:
                menu2.add_command(label=item,command=self.get_password2)
        menubar.add_cascade(label='Love',menu=menu1)
        menubar.add_cascade(label='You',menu=menu2)
        

        
        canvas=tkinter.Canvas(self.win,height=270,width=450)
        imagefile=tkinter.PhotoImage(file='a.gif')
        canvas.create_image(0,0,anchor='nw',image=imagefile)
        canvas.pack()

        account=tkinter.Variable()
        password=tkinter.Variable()

        entry1=tkinter.Entry(self.win,textvariable=account)
        entry1.place(x=160,y=280)

        entry2=tkinter.Entry(self.win,textvariable=password,show='*')
        entry2.place(x=160,y=320)

        tkinter.Label(self.win,text='Account').place(x=100,y=280)
        tkinter.Label(self.win,text='Password').place(x=100,y=320)
    
        login_button=tkinter.Button(self.win, text="Login", command=lambda :self.login(entry1,entry2), width=5, height=3)
        login_button.place(x=320,y=280)

        self.win.mainloop()
        
    def get_account1(self):      
        tkinter.messagebox.showinfo(message='5位字母',title="Hint")
    def get_account2(self):      
        tkinter.messagebox.showinfo(message='你的英文名',title="Hint")
    
    def get_password1(self):
        tkinter.messagebox.showinfo(message='7位数字',title="Hint")
    def get_password2(self):
        tkinter.messagebox.showinfo(message='谐音数字组合，表达我的爱意',title="Hint")
        
    def pic_process(self,path):
        
        img=Image.open(path)
        img=img.resize((300,250))
        photo=ImageTk.PhotoImage(img)
        imgLabel=tkinter.Label(self.win2,image=photo)
        imgLabel.place(x=150,y=0)        
        imgLabel.after()

    def get_chp(self):
        
        chp=random.choice(self.CHP)
        text=tkinter.Text(self.win2,width=10,height=5)
        text.insert(tkinter.INSERT,chp)
        text.place(x=60,y=200)  
        
    def open_pic(self):
        self.i=0
        chp="管珍妮，\n我希望千年万年兵荒马乱，你还在，我还爱。"
        text=tkinter.Text(self.win2,width=10,height=5)
        text.insert(tkinter.INSERT,chp)
        text.place(x=60,y=200) 
        self.pic_process(self.path[self.i])


    def prev_pic(self):
        
        self.get_chp()
        self.i-=1
        self.pic_process(self.path[self.i])


  
    def next_pic(self):
        if self.i<40:
            self.get_chp()
            self.i+=1
            self.pic_process(self.path[self.i])
        else:
            tkinter.messagebox.showinfo(message='最后一张了喔~',title="Info")
 
    def cal(self):
    
        next_commemoration_day=datetime.datetime(2020,8,31)
        love_start=datetime.datetime(2017,8,31,20,00,00)
        next_birthday1=datetime.datetime(2020,10,9)
        next_birthday2=datetime.datetime(2020,12,16)

        now=datetime.datetime.now()
        today=now.strftime("%Y-%m-%d")
        interval1=now-love_start
        days=interval1.days+1
        total_seconds=interval1.total_seconds()
        text1='今天是{}\n是我们相爱的第{}天'.format(today,days)
        interval2=next_birthday1-now
        days2=interval2.days
        text2='离小肥的生日\n还有{}天'.format(days2)
        interval3=next_birthday2-now
        days3=interval3.days
        text3='离老肥的生日\n还有{}天'.format(days3)
        interval4=next_commemoration_day-now
        days4=interval4.days
        text4='离周年纪念日\n还有{}天'.format(days4)
        return text1,text2,text3,text4

    def login(self,entry1,entry2):
        account=entry1.get()
        password=entry2.get()
        if account=='jenny' and password=='5201314':
            tkinter.messagebox.showinfo(title='welcome',message='欢迎光临恋爱小屋!')
            self.get_win2()
        else:
            tkinter.messagebox.showerror(message='走错房间了喔，请重试！')
        
    def get_win2(self):
        self.win2=tkinter.Toplevel()
        self.win2.title("Memory")
        self.win2.geometry("450x300") 
        # 相册首图
        img=Image.open('b.jpg')
        img=img.resize((300,250))
        photo=ImageTk.PhotoImage(img)
        imgLabel=tkinter.Label(self.win2,image=photo)
        imgLabel.place(x=150,y=0)
        self.text1,self.text2,self.text3,self.text4=self.cal()
        tkinter.Label(self.win2,text=self.text1,font=("黑体",10),fg="red").place(x=10,y=10)
        
        start_button=tkinter.Button(self.win2, text="S\nt\na\nr\nt", command=self.open_pic, width=2, height=5,bg="pink")
        start_button.place(x=20,y=180)
        prev_button=tkinter.Button(self.win2,text="Prev",command=self.prev_pic,width=10)
        prev_button.place(x=180,y=260)
        next_button=tkinter.Button(self.win2,text="Next",command=self.next_pic,width=10)
        next_button.place(x=340,y=260)
        day_button=tkinter.Button(self.win2,text="D\na\ny",command=self.get_commemoration_day, height=5,width=2,bg="pink")
        day_button.place(x=20,y=60)
        self.win2.mainloop()
    
    def get_commemoration_day(self):
        
        tkinter.Label(self.win2,text=self.text2).place(x=60,y=50)
        tkinter.Label(self.win2,text=self.text3).place(x=60,y=90)
        tkinter.Label(self.win2,text=self.text4).place(x=60,y=130)

        
        
if __name__=='__main__':
    a=App()
    a.set_win()
    #a.get_win2()