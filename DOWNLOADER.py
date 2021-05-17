from tkinter import PhotoImage

from tkinter import *

from tkinter import ttk

from tkinter import messagebox

from tkinter import filedialog

import pafy

import threading

import youtube_dl

import time

import requests

import re

import sys

from threading import *


#<<--------------------You Tube Function to check the internet connection------------------->>

def connection1(url='http://www.google.com/', timeout=5):

    try:
        
        req = requests.get(url, timeout=timeout)
        
        req.raise_for_status()

        
        
        print("You're connected to internet\n")
        
        return True
    
    except requests.HTTPError as e:

        Label(tab1,text='Checking internet connection failed',fg='blue'
              ,font=('just',14,'bold')).place(x=50,y=390)

        
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
        
    except requests.ConnectionError:

        connnection__msg=Label(tab1,text='No Internet Connection Available'
                           ,fg='blue'  ,font=('just',14,'bold'))
        
        connnection__msg.place(x=50,y=390)
        
        #print("No internet connection available.")
        
    return False





#<<------------------------------dictionary of colors:----------------------------------->>

color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

#<<------------------------------setting screen window:------------------------------------>>

screen = Tk()

screen.title("Downloader")

screen.iconbitmap(r'./Image/down_arrow_0of_icon.ico')

screen.config(bg="gray17")

screen.geometry("418x680+850+60")


# setting switch state:

btnState = False

#<<---------------------------loading Navbar icon image:---------------------------------->>

navIcon = PhotoImage(file="./Image/menu.png")

closeIcon = PhotoImage(file="./Image/close.png")


SettingIcon = PhotoImage(file="./Image/gear.png")

DownloadIcon = PhotoImage(file="./Image/direct-download.png")

feedbackIcon = PhotoImage(file="./Image/chat-bubble.png")

homeIcon = PhotoImage(file="./Image/home.png")

How_to_use_Icon = PhotoImage(file="./Image/howtouse.png")

YouTube_Icon = PhotoImage(file="./Image/youtube.png")

bellIcon = PhotoImage(file="./Image/bell.png")


folder_Name=''

#<<--------------------------------file location for You Tube------------------------------>>

def openlocation():
    
    locationError=Label(tab1,text='Select folder',fg='orange',bg='black',font=('jost',10)
                        ,justify=CENTER)



    global folder_Name

    folder_Name=filedialog.askdirectory()

    if(len(folder_Name) > 1):
        
        locationError.config(text=folder_Name,fg='black',bg='yellow')
        
        locationError.place(x=80,y=210)

    else:
              
            locationError.config(text='Please Choose folder',fg='red',bg='yellow')

            locationError.place(x=145,y=210)







#<<-------------------------------setting switch function:--------------------------------->>

def switch():
    
    global btnState
    
    if btnState is True:
        
#<<--------------------create animated Navbar closing:------------------------------------->>
        
        #for x in range(301):
            
        navRoot.place(x=-301, y=0)

            
        topFrame.update()

        # resetting widget colors:
        
        brandLabel.config(bg="gray17", fg="green")
        
        homeLabel.config(bg=color["orange"])
        
        topFrame.config(bg=color["orange"])
        
        screen.config(bg="gray17")

        # turning button OFF:
        
        btnState = False
    else:
        
        # make root dim:
        
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        
        homeLabel.config(bg=color["nero"])
        
        topFrame.config(bg=color["nero"])
        
        screen.config(bg=color["nero"])

#<<-------------------------created animated Navbar opening:---------------------------->>
        
        for x in range(-301, 0):
            
            navRoot.place(x=x, y=0)
            
            topFrame.update()

        # turing button ON:
        
        btnState = True

#<<---------------------------------top Navigation bar:---------------------------------->>

topFrame = Frame(screen, bg=color["orange"])

topFrame.pack(side="top", fill=X)


#<<---------------------------------Header label text:----------------------------------->>

homeLabel = Label(topFrame, text="DOWNLOADER"
                  ,font=('jost',15,'bold'), bg=color["orange"], fg="gray17",
                  height=2, padx=120)

homeLabel.pack(side="right")

#Notification Button

Button(topFrame,image=bellIcon).place(x=360,y=10)

#<<-------------------------------Tab for You Tube and Instagran-------------------------->>

note_book=ttk.Notebook(screen)

tab1 =ttk.Frame(note_book)

tab2 =ttk.Frame(note_book)

tab3 =ttk.Frame(note_book)

tab4 =ttk.Frame(note_book)

note_book.add(tab1,text='      You Tube         ')

note_book.add(tab2,text='     Instagram         ')

note_book.add(tab3,text='     FaceBook          ')

note_book.add(tab4,text='     Converter_V->A          ')


note_book.place(x=10,y=30)

note_book.pack(expand=True,fill='both')
#<<-------------------------------Speech Search---------------------------->>
import pyttsx3

import speech_recognition as sr

import os

global search_result


def search():
    global search_result
    search_result=[]
    def take_commands():
        r = sr.Recognizer()
    
        with sr.Microphone() as source:
            print('Listening')
            r.pause_threshold = 0.7
            # storing audio/sound to audio variable
            audio = r.listen(source)
            try:
                print("Recognizing")
                # Recognizing audio using google api
                Query = r.recognize_google(audio)
                print("the query is printed='", Query, "'")
                search_result.append(Query)
                print(search_result)
            except Exception as e:
                print(e)
                print("Say that again sir")
                # returning none if there are errors
                return "None"
        # returning audio as text
        ytdEntry1.delete(0, 'end')
        ytdEntry1.insert(0,str(search_result[0]))
        import time
        time.sleep(2)
        return Query



    command = take_commands()
listenIcon = PhotoImage(file="./Image/listener.png")

Button(tab1,image=listenIcon,command=search).place(x=377,y=45)
#<<-----------------------------------YOU TUBE ICON---------------------------------------->>

Label(tab1,image=YouTube_Icon,bd=2).place(x=160,y=1)

p=Label(tab1,text='YOU TUBE',font=('just',14,'bold'))

p.place(x=306,y=6)

#<<-----------------------------------Entry Box--------------------------------------------->>

ytdEntryVar1=StringVar()

ytdEntry1=Entry(tab1,width=24,textvariable=ytdEntryVar1,bd=4
               ,font=('Arial',20))

ytdEntry1.place(x=10, y=45)

ytdEntry1.focus()

ytdEntry1.insert(0,'Enter Songs Name')

# padx = padding for left side  pady= padding for right side ipady=Height of the padding
linkVar1=StringVar()


#<<-----------------------------Button to save the file------------------------->

save_Entry=Button(tab1,width=14,command=openlocation
                  ,bg='red',fg='white',text='SELECT FOLDER',bd=8,font=('jost',10,'bold'))

save_Entry.place(x=238,y=160)

#<<------------------------------Link Entry------------------------------------->>

#search youtube video link & open a video in browser
from youtube_search import YoutubeSearch

import webbrowser

global link_Entry
ll=[]
l=[]
global URL
def show_link():

    def Entrylink():
        
        l=ytdEntry1.get()
        vid=l
        print(vid)
        l=[ ]
        #10 video link is generated max_result=10 we can also change the range
        results = YoutubeSearch(vid, max_results=3).to_dict()
        for v in results:
            l.append(v['url_suffix'])
            ll.append('https://www.youtube.com' + v['url_suffix'])
            print('https://www.youtube.com' + v['url_suffix'])
    Entrylink()

    linkEntry1=Entry(tab1,width=28,text='',bd=2
               ,font=('Arial',14))
    
    linkEntry1.place(x=6,y=420)
    
    linkEntry1.insert(0,ll[0])

    linkEntry1=Entry(tab1,width=28,text='',bd=2
               ,font=('Arial',14))

    linkEntry1.place(x=6,y=450)
    
    linkEntry1.insert(0,ll[1])

    linkEntry1=Entry(tab1,width=28,text='',bd=2
               ,font=('Arial',14))

    linkEntry1.place(x=6,y=480)
    
    linkEntry1.insert(0,ll[2])

    def copy():
        global URL
        URL=linkEntry1.get()
        print(URL)
    def play():
        n=linkEntry1.get()
        print(n)
        if(n!=""):
            try:
                webbrowser.open(n)
                l= linkEntry1.get()
            except:
                print('Some thing Went Wrong..')
        else:
            print('Error')
    link_Entry=Button(tab1,width=5,command=play
                  ,bg='red',fg='white',text='Play',bd=4,font=('jost',7,'bold'))

    link_Entry.place(x=322,y=421)


    link_Entry=Button(tab1,width=5,command=play
                  ,bg='red',fg='white',text='Play',bd=4,font=('jost',7,'bold'))

    link_Entry.place(x=322,y=451)
    
    link_Entry=Button(tab1,width=5,command=play
                  ,bg='red',fg='white',text='Play',bd=4,font=('jost',7,'bold'))

    link_Entry.place(x=322,y=481)

    link_Entry=Button(tab1,width=5,command=copy
                  ,bg='red',fg='white',text='Copy',bd=4,font=('jost',7,'bold'))

    link_Entry.place(x=371,y=421)


    link_Entry=Button(tab1,width=5,command=copy
                  ,bg='red',fg='white',text='Copy',bd=4,font=('jost',7,'bold'))

    link_Entry.place(x=371,y=451)

    link_Entry=Button(tab1,width=5,command=copy
                  ,bg='red',fg='white',text='Copy',bd=4,font=('jost',7,'bold'))

    link_Entry.place(x=371,y=481)



#<<-------------------------Search Button--------------------------------------->>

search_button=Button(tab1,text='Search',font=('jost',12,'bold'),bd=4,
                 fg='white',bg='red',command=show_link)

search_button.place(x=170,y=104)

#<<---------------------------------How To use-------------------------------->>
    
How_to_use_image=Label(tab1,image=How_to_use_Icon)

def click():

    How_to_use_image.place(x=0,y=450)


#<<-------------------------------How to Use Button---------------------------------------->>

How_to_use_btn=Button(tab1,text='HOW TO USE',width=13,bg='red',fg='white',
                   bd=8,font=('jost',10,'bold'),command=click)

How_to_use_btn.place(x=40,y=160)


#<<------------------------------Option for Quality------------------------------------->>

'''choices=[720,480,360,240]

ytdchoices = ttk.Combobox(tab1,values=choices,width=18)

ytdchoices.place(x=139,y=305)'''

'''Label(tab1,text='Developer Addhayayan Pandey',fg='orange',
      font=('Arial',14,'bold')).place(x=50,y=560)'''



variable1 = StringVar(tab1)

variable1.set("SELECT QUALITY") # default value

w1 = OptionMenu(tab1, variable1, "          Video            ","        Audio            ")

w1.config(width=15,activeforeground='black',font=('just',10,'bold'),
         bg='orange',fg='SystemButtonText', activebackground='yellow')

w1.place(x=125,y=250)

string="          Video            "

string1="        Audio            "
option_value1=""

global best

def ok2():

    global option_value1

    print ("value is:" +variable1.get())

    option_value1=variable1.get()

    def close_how_to_use_picture():

        How_to_use_image.place(x=-400,y=-400)

    close_how_to_use_picture()

def DOWNLOAD():

    def mycb(total, recvd, ratio, rate, eta):

        print(recvd, ratio, eta)


    def details():

        try:
            global URL

            url=URL

            print('URL:',url)
        
        except:
            
            print('Error:')

        global title

        try:

            video=pafy.new(url)

            #Label(tab1,text='Details:',font=('just',13,'bold'),fg='red').place(x=2,y=430)

            title=video.title

            print(video.title)

            print(video.rating)

            print(video.viewcount)

            print(video.author, video.length)

            '''Label(tab1,text='Title:',font=('just',10,'bold'),fg='red').place(x=2,y=455)

            Label(tab1,text=title,font=('just',9,'bold'),fg='Blue').place(x=40,y=455)

            Label(tab1,text='Duration:',font=('just',10,'bold'),fg='red').place(x=2,y=480)

            Label(tab1,text=video.duration,font=('just',10,'bold'),fg='Blue').place(x=66,y=480)


            Label(tab1,text='Author:',font=('just',10,'bold'),fg='red').place(x=2,y=510)

            Label(tab1,text=video.author,font=('just',10,'bold'),fg='Blue').place(x=50,y=510)

            Label(tab1,text='Length:',font=('just',10,'bold'),fg='red').place(x=2,y=540)

            Label(tab1,text=video.length,font=('just',10,'bold'),fg='Blue').place(x=56,y=540)

            print(video.title)'''
            
            p=Label(tab1,text='Download Succesfully..',font=('just',14,'bold'),fg='red')

            '''best = video.getbest()

            print(best.resolution, best.extension)

            best.download()
                    
            p.place(x=20,y=400)

            print('Video Download...')

            bestaudio=video.getbestaudio()
                    
            p.place(x=20,y=400)

            bestaudio.download()

            p.place(x=20,y=400)
    '''
            if(option_value1==string):
                try:
                    best = video.getbest()

                    print(best.resolution, best.extension)

                    best.download()
                    
                    p.place(x=50,y=390)

                    print('Video Download...')

                    
                except Exception as e:

                    Label(tab1,text='Something Goes Wrong..',
                          font=('just',14,'bold'),fg='red').p.place(x=20,y=400)
                    
                    print('Something went wrong..',e)
                    
            elif(option_value1==string1):

                try:

                    bestaudio=video.getbestaudio()

                    bestaudio.download()

                    p.place(x=50,y=390)
                except:
                    Label(tab1,text='Something Goes Wrong..',
                          font=('just',14,'bold'),fg='red').place(x=20,y=400)
        except Exception as e:
            print('Something went wrong..',e)
            Label(tab1,text='Something Wrong On URL..',
                          font=('just',14,'bold'),fg='red').place(x=20,y=400)

    if connection1() == True :

        try:
            details()
    
            
        except Exception as e:
            print('Something went wrong..',e)
    

#Combobox it help the users to select the according to the option of the list

#<<-------------------------------- Progess Bar------------------------------------------>>    
my_progress = ttk.Progressbar(tab1,orient=HORIZONTAL,length=155,mode='determinate')

my_progress.place(x=130,y=305)

my_label = Label(tab1,text='')

my_label.place(x=290,y=305)


#<<--------------------------------Option Menu---------------------------------------->>
        
button1 = Button(tab1, text="OK", command=ok2,font=('just',10,'bold'),bg='red')

button1.place(x=277,y=252)
def clear():

    try:

        ytdEntry1.delete(0,'end')

        ytdEntry1.insert(0,'Enter Songs Name')

        linkEntry1.delete(0,'end')

        link_Entry.after(0,linkEntry1.destroy)

    except:
        pass
        




#<<--------------------------------clear Button---------------------------------------->>

clearbtn=Button(tab1,text='CLEAR',width=12,bg='red',fg='white',
            bd=6,font=('jost',11,'bold'),command=clear)

clearbtn.place(x=70,y=338)


#<<--------------------------------Download Button---------------------------------------->>

downloadbtn=Button(tab1,text='DOWNLOAD',width=12,bg='red',fg='white',
            bd=6,font=('jost',11,'bold'),command=DOWNLOAD )

downloadbtn.place(x=240,y=338)


#<<--------------------------------Main label text:---------------------------------------->>

brandLabel = Label(tab1, text="Pandey",
                      font="System 30", bg="gray17", fg="green")

brandLabel.place(x=100, y=600)

#<<--------------------------------Navbar button:------------------------------------------>>

navbarBtn = Button(topFrame, image=navIcon, bg=color["orange"],
                   activebackground=color["orange"], bd=1, padx=20, command=switch)

navbarBtn.place(x=8, y=8)

#<<-------------------------------setting Navbar frame:------------------------------------>>

navRoot = Frame(screen, bg="gray17", height=300, width=255)

navRoot.place(x=-300, y=0)

Label(navRoot, font="Bahnschrift 15", bg=color["orange"],
         fg="black", height=2, width=300, padx=20).place(x=0, y=0)

#<<--------------------------set y-coordinate of Navbar widgets:--------------------------->>

y = 70

#<<----------------------------option in the navbar:-------------------------------------->>

options = ["Home","Download list","Feedback","Settings"]

#<<-----------------------------Navbar Option Buttons:------------------------------------>>

for i in range(4):
    
    Button(navRoot, text=options[i], font="BahnschriftLight 15",
              bg="gray17", fg=color["orange"], activebackground="gray17",
              activeforeground="green", bd=0).place(x=45, y=y)
    y += 60

#<<------------------------------Navbar Close Button:------------------------------------->>

closeBtn = Button(navRoot, image=closeIcon, bg=color["orange"],
                     activebackground=color["orange"], bd=1, command=switch)

closeBtn.place(x=210, y=10)

#<<------------------------------Navbar Setting Button:------------------------------------->>

SettingBtn = Button(navRoot, image=SettingIcon, bg=color["orange"],
                     activebackground=color["orange"])

SettingBtn.place(x=10, y=258)

#<<------------------------------Navbar Download Button:----------------------------------->>


DownloadBtn = Button(navRoot, image=DownloadIcon, bg=color["orange"],
                     activebackground=color["orange"])

DownloadBtn.place(x=10, y=138)

#<<-----------------------------------Feedback---------------------------------------->>

closeIcon1 = PhotoImage(file="./Image/back.png")

def feedback():

    feed = Frame(screen, height=650, width=400,bg='green')

    feed.place(x=10, y=10)

    headerlabel = Label(feed, text='CUSTOMER FEEDBACK', foreground='orange',
                        font=('Arial', 20))

    headerlabel.place(x=30,y=30)

    messagelabel = Label(feed,
                         text='PLEASE TELL US WHAT YOU THINK',
                         foreground='purple', font=('Arial', 10))

    messagelabel.place(x=60, y=90)

    myvar = StringVar()

    var = StringVar()
    # cmnt= StringVar()

    namelabel = Label(feed, text='Name',font=('Arial',13))

    namelabel.place(x=5,y=132)

    entry_name = Entry(feed, width=26, font=('Arial', 16), textvariable=myvar)

    entry_name.place(x=70,y=130)


    emaillabel = Label(feed, text='Email',font=('Arial',13))
    
    emaillabel.place(x=5,y=172)
    
    entry_email = Entry(feed, width=26, font=('Arial', 16), textvariable=var)
    
    entry_email.place(x=70, y=170)

    commentlabel = Label(feed, text='Comment', font=('Arial', 13))

    commentlabel.place(x=5,y=210)

    textcomment = Text(feed, width=45, height=10)

    textcomment.place(x=15,y=245)

    textcomment.config(wrap ='word')

    def clear():

        global entry_name
        global entry_email
        global textcomment
        messagebox.showinfo(title='clear', message='Do you want to clear?')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)


    def submit():
        global entry_name
        global entry_email
        global textcomment
        print('Name:{}'.format(myvar.get()))
        print('Email:{}'.format(var.get()))
        print('Comment:{}'.format(textcomment.get(1.0, END)))

        messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)

    submitbutton = Button(feed, text='Submit', command=submit).place(x=150,y=420)
    clearbutton = Button(feed, text='Clear', command=clear).place(x=210,y=420)


    def closedButton():

        feed.place(x=-1000,y=0)

        feed.update()

    button=Button(feed,image=closeIcon1,bg='yellow',bd=1,activebackground=color["orange"]
                  ,command=closedButton)
    
    button.place(x=360,y=2)

    
#<<------------------------------Navbar feedback Button:----------------------------------->>

feedbackBtn = Button(navRoot, image=feedbackIcon, bg=color["orange"],
                     activebackground=color["orange"],command=feedback)

feedbackBtn.place(x=10, y=195)

#<<------------------------------Navbar Home Button:-------------------------------------->>


homeBtn = Button(navRoot, image=homeIcon, bg=color["orange"],
                     activebackground=color["orange"])

homeBtn.place(x=10, y=78)

#<<----------------------------END OF YOU TUBE TAB1--------------------------------------->>

#<<--------------------------------------------------------------------------------------->>
#<<--------------------------------------------------------------------------------------->>

#<<------------------------------- Instagram TAB2------------------------------------------>>


from datetime import datetime

from tqdm import tqdm

import requests

import re

import sys

Instagram_Icon = PhotoImage(file="./Image/instagram.png")

Label(tab2,image=Instagram_Icon,bd=2).place(x=160,y=2)

p=Label(tab2,text='INSTAGRAM',font=('just',14,'bold'))

p.place(x=285,y=10)


folder_Name_insta=''

#<<--------------------------------file location for You Tube------------------------------>>

def openlocation_insta():
    
    locationError=Label(tab2,text='Select folder',fg='orange',bg='black',font=('jost',10)
                        ,justify=CENTER)



    global folder_Name_insta

    folder_Name_insta=filedialog.askdirectory()

    if(len(folder_Name_insta) > 1):
        
        locationError.config(text=folder_Name_insta,fg='black',bg='yellow')
        
        locationError.place(x=80,y=200)

    else:
              
            locationError.config(text='Please Choose folder',fg='red',bg='yellow')

            locationError.place(x=145,y=200)






#<<--------------------------------Entry for the URL------------------------------------->>

ytdEntryVar_insta=StringVar()

ytdEntry_insta=Entry(tab2,width=25,textvariable=ytdEntryVar_insta,bd=4
               ,font=('Arial',20))

ytdEntry_insta.place(x=20, y=55)

ytdEntry_insta.insert(0,'PASTE THE URL')


#<<-----------------------------How To Use Picture Instgram-------------------------------->>
How_To_use_Insta = PhotoImage(file="./Image/How_To_use_Insta.png")

How_to_use_Insta=Label(tab2,image=How_To_use_Insta)

def click1():

    How_to_use_Insta.place(x=0,y=475)


#<<--------------------------------HOW TO USE BUTTON------------------------------------->>


How_to_use_btn=Button(tab2,text='HOW TO USE',width=13,bg='red',fg='white',
                   bd=8,font=('jost',10,'bold'),command=click1)

How_to_use_btn.place(x=40,y=140)


#<<-------------------------------Button to save the file----------------------------------->

save_Entry=Button(tab2,width=14,command=openlocation_insta
                  ,bg='red',fg='white',text='SELECT FOLDER',bd=8,font=('jost',10,'bold'))

save_Entry.place(x=238,y=140)


'''OPTIONS = [
"Profile Photo",
" Video ",
"Normal Post"
] #etc'''

variable = StringVar(tab2)

variable.set("SELECT TYPE") # default value

w = OptionMenu(tab2, variable, "Profile Photo"," Video ","Normal Post")

w.config(width=13,activeforeground='black',font=('just',11,'bold'),
         bg='orange',fg='SystemButtonText', activebackground='yellow')

w.place(x=130,y=230)

option_value=""

def ok1():

    global option_value
    
    print ("value is:" + variable.get())

    option_value=variable.get()
    

button = Button(tab2, text="OK", command=ok1,font=('just',10,'bold'),bg='red')

button.place(x=277,y=233)


#<<------------------------------Progress Bar ------------------------------------------>>

def download():

    def step1():

        my_progress2 = ttk.Progressbar(tab2,orient=HORIZONTAL,length=155,mode='determinate')

        my_progress2.place(x=130,y=290)

        my_label2= Label(tab2,text='')

        my_label2.place(x=290,y=290)


        for x in range(11):

            my_label2.config(text= my_progress2['value'],font=('just',10,'bold'))

            my_progress2['value']+=(10)

            tab1.update_idletasks()

            time.sleep(0.3)
        
        my_label2.config(text='Completed',fg='blue',font=('just',10,'bold'))


#<<----------------------------How to Use Pictures close --------------------------------->>
    def close_how_to_use_picture():
        
        How_to_use_Insta.place(x=-400,y=-400)

    close_how_to_use_picture()    

    ok() 

    step1()




#Function to check the internet connection

def connection(url='http://www.google.com/', timeout=5):

    try:
        
        req = requests.get(url, timeout=timeout)
        
        req.raise_for_status()

        
        
        print("You're connected to internet\n")
        
        return True
    
    except requests.HTTPError as e:

        Label(tab2,text='Checking internet connection failed',fg='blue'
              ,font=('just',14,'bold')).place(x=50,y=385)

        
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
        
    except requests.ConnectionError:

        connnection__msg=Label(tab2,text='No internet connection available'
                           ,fg='blue'  ,font=('just',14,'bold'))
        
        connnection__msg.place(x=50,y=380)
        
        #print("No internet connection available.")
        
    return False


#<<------------------------------Connection-------------------------------------------->>

#<<-----------------------Function to download an instagram photo or video------------->>
def ok():

    print_msg_on_screen=Label(tab2,text='Image downloaded successfully',font=('just',14,'bold')
                          ,fg='orange')
    def download_image_video():
        
        url = ytdEntry_insta.get()
        print(url)
        
        #url = input("Please enter image URL: ")
        
        x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)

        try:

            if x:
                request_image = requests.get(url)

                src = request_image.content.decode('utf-8')
            
                check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
            
                check_type_f = check_type.group()
            
                final = re.sub('<meta name="medium" content="', '', check_type_f)

                print('A:',final)

                if final == "image":

                    print("\nDownloading the image...")
                
                    extract_image_link = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)', src)
                    image_link = extract_image_link.group()
                    final = re.sub('meta property="og:image" content="', '', image_link)
                    _response = requests.get(final).content
                    file_size_request = requests.get(final, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024 
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    Label(tab2,text='Size : '+str(file_size//1000)+' KB',font=('just',12,'bold')
                          ,fg='red').place(x=10,y=380)
                    
                    #Label(tab2,text=file_size//1000,font=('just',11,'bold')).place(x=10,y=480)
                    

                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)

                    p=Label(tab2,text=t)
                    p.place(x=10,y=490)
                    with open(filename + '.jpg', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            time.sleep(0.2)
                            p.config(text=t)
                            time.sleep(0.3)
                            t.update(len(data))
                    t.close()
                
                    print_msg_on_screen.place(x=75,y=430) #label for print sucessfull msg
                
                    print("Image downloaded successfully")
                    
                if final == "video":
                    
                    #msg = input("You are trying to download a video. Do you want to continue? (Yes or No): ".lower())
                    msg='yes'

                    print(final)

                    if msg == "yes":

                        print("Downloading the video...")
                    
                        extract_video_link = re.search(r'meta property="og:video" content=[\'"]?([^\'" >]+)', src)
                        video_link = extract_video_link.group()
                    
                        final = re.sub('meta property="og:video" content="', '', video_link)
                        _response = requests.get(final).content
                        file_size_request = requests.get(final, stream=True)
                        file_size = int(file_size_request.headers['Content-Length'])
                        block_size = 1024 
                        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                        t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                        
                        with open(filename + '.mp4', 'wb') as f:
                            for data in file_size_request.iter_content(block_size):
                                t.update(len(data))
                                f.write(data)
                            t.close()
                        Label(tab2,text='Video downloaded successfully',font=('just',10,'bold')
                          ,fg='green').place(x=70,y=430)
                        print("Video downloaded successfully")

                    if msg == "no":
                        exit()  
            else:

                Label(tab2,text='Entered URL is not an instagram.com URL',font=('just',10,'bold')
                          ,fg='green').place(x=40,y=430)
                print("Entered URL is not an instagram.com URL.")
            
        except AttributeError:
            
            Label(tab2,text='Unknown URL',font=('just',10,'bold')
                          ,fg='green').place(x=80,y=430)
            print("Unknown URL")

#<<-------------------Function to download profile picture of instagram accounts------------>>
    def pp_download():
        
        url = ytdEntry_insta.get()
        
        print(url)
        
        #url = input("Please enter the URL of the profile: ")

        x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)
    
        if x:
            check_url1 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/].*\?hl=[a-z-]{2,5}', url)
            check_url2 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com$|^(https:)[/][/]www.([^/]+[.])*instagram.com/$', url)
            check_url3 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/][a-zA-Z0-9_]{1,}$', url)
            check_url4 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/][a-zA-Z0-9_]{1,}[/]$', url)

            if check_url3:
                
                final_url = url + '/?__a=1'
                
            if check_url4:
                
                final_url = url + '?__a=1'

            if check_url2:
                
                Label(tab2,text='Please enter an URL related to a profile',font=('just',10,'bold')
                          ,fg='green').place(x=30,y=430)

                final_url = print("Please enter an URL related to a profile")

                exit()
            if check_url1:
                alpha = check_url1.group()
                final_url = re.sub('\\?hl=[a-z-]{2,5}', '?__a=1', alpha)
            
        try:
            if check_url3 or check_url4 or check_url2 or check_url1:
                req = requests.get(final_url)
                get_status = requests.get(final_url).status_code
                get_content = req.content.decode('utf-8')

                if get_status == 200:

                    print("\nDownloading the image...")

                    find_pp = re.search(r'profile_pic_url_hd\":\"([^\'\" >]+)', get_content)
                    pp_link = find_pp.group()
                    pp_final = re.sub('profile_pic_url_hd":"', '', pp_link)
                    file_size_request = requests.get(pp_final, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024 
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)

                    with open(filename + '.jpg', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            print(data)
                            t.update(len(data))
                            f.write(data)
                    t.close()

                    Label(tab2,text='Profile picture downloaded successfully',font=('just',14,'bold')
                          ,fg='green').place(x=70,y=430)
                
                    print("Profile picture downloaded successfully")

        except Exception:
            
            Label(tab2,text='error',font=('just',14,'bold')
                          ,fg='green').place(x=100,y=430)

            print('error')

    if connection() == True:
        
        try:
            
            a=option_value
            
            print('AA:',a)

            try:
                
                if a=='Profile Photo':
                    t=Thread(target=pp_downlaod)
                    t.start()
                    #pp_download()

                if a=='Video' or a=='Normal Post':
                    #if select == 'B':
                            
                    download_image_video()
                        
                else:
                        
                    sys.exit()
                            
            except (KeyboardInterrupt):
                        
                Label(tab2,text='Programme Interrupted').place(x=100,y=480)

                print("Programme Interrupted")
                        
        except(KeyboardInterrupt):
                        
            Label(tab2,text='\nProgramme Interrupted').place(x=100,y=480)

            print("\nProgramme Interrupted")

    else:

        sys.exit()


#button = Button(tab2, text=" OK ", command=ok)

#button.place(x=280,y=230)



#<<----------------------------Download Button for Instagram---------------------------->>

downloadbtn=Button(tab2,text='DOWNLOAD',width=12,bg='red',fg='white',
                   bd=6,font=('jost',11,'bold'),command=download)

downloadbtn.place(x=145,y=320)


#<<--------------------------------------------------------------------------------------->>

#<<--------------------------------------------------------------------------------------->>

#<<--------------------------------Facebook---------------------------------------------->>

import re
import requests
import urllib.request



faceBook_Icon = PhotoImage(file="./Image/facebook.png")

Label(tab3,image=faceBook_Icon,bd=2).place(x=160,y=2)

p=Label(tab3,text='FACEBOOK',font=('just',14,'bold'))

p.place(x=285,y=10)




ytdEntryVar_fb=StringVar()

ytdEntry_fb=Entry(tab3,width=25,textvariable=ytdEntryVar_fb,bd=4
               ,font=('Arial',20))

ytdEntry_fb.place(x=20, y=55)

ytdEntry_fb.insert(0,'PASTE THE URL')

def openlocationFB():
    
    locationError=Label(tab3,text='Select folder',fg='orange',bg='black',font=('jost',10)
                        ,justify=CENTER)



    global folder_Name1

    folder_Name1=filedialog.askdirectory()

    if(len(folder_Name1) > 1):
        
        locationError.config(text=folder_Name1,fg='black',bg='yellow')
        
        locationError.place(x=80,y=210)

    else:
              
            locationError.config(text='Please Choose folder',fg='red',bg='yellow')

            locationError.place(x=145,y=210)





#<<--------------------FACABOOK Function to check the internet connection------------------->>

def connectionFB(url='http://www.google.com/', timeout=5):

    try:
        
        req = requests.get(url, timeout=timeout)
        
        req.raise_for_status()

        
        
        print("You're connected to internet\n")
        
        return True
    
    except requests.HTTPError as e:

        Label(tab3,text='Checking internet connection failed',fg='blue'
              ,font=('just',14,'bold')).place(x=50,y=390)

        
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
        
    except requests.ConnectionError:

        connnection__msg=Label(tab3,text='No Internet Connection Available'
                           ,fg='blue'  ,font=('just',14,'bold'))
        
        connnection__msg.place(x=50,y=390)
        
        #print("No internet connection available.")
        
    return False




#<<-----------------------------How To Use Picture Facebook-------------------------------->>
How_To_use_fb = PhotoImage(file="./Image/FB_HOW.png")

How_to_use_fb=Label(tab3,image=How_To_use_fb)

def click2():

    How_to_use_fb.place(x=0,y=475)


#<<--------------------------------HOW TO USE BUTTON------------------------------------->>


How_to_use_btn2=Button(tab3,text='HOW TO USE',width=13,bg='red',fg='white',
                   bd=8,font=('jost',10,'bold'),command=click2)

How_to_use_btn2.place(x=40,y=140)

#<<-------------------------------Button to save the file----------------------------------->

save_Entry2=Button(tab3,width=14,command=openlocationFB
                  ,bg='red',fg='white',text='SELECT FOLDER',bd=8,font=('jost',10,'bold'))

save_Entry2.place(x=238,y=140)



def fb():

    if connectionFB() == True:

        link=ytdEntry_fb.get()
        print(link)
        html=requests.get(link)
        #parse url

        try:

            url=re.search('hd_src:"(.+?)"',html.text)[1]#hd video

            print("hd video")
        except:
            url=re.search('sd_src:"(.+?)"',html.text)[1]#sd video

            print("sd video")

        print("downloading...")

        #download & giving name

        urllib.request.urlretrieve(url, "facebook video.mp4")

        print("download sucessfull!")
        
        Label(tab3,text='Download Successfull!',font=('Arial',10,'Bold'),
              color='orange').place(x=50,y=390)
            
#<<----------------------------Download Button for facebook---------------------------->>

downloadbtn=Button(tab3,text='DOWNLOAD',width=12,bg='red',fg='white',
                   bd=6,font=('jost',11,'bold'),command=fb)

downloadbtn.place(x=145,y=245)

#<<------------------------------------Converter----------------------------------------->>

import os

#from moviepy.editor import *

Converter_Icon = PhotoImage(file="./Image/Convert.png")

Label(tab4,image=Converter_Icon ,bd=4).place(x=170,y=2)

p=Label(tab4,text='CONVERTER',font=('just',14,'bold'))

p.place(x=285,y=10)

ytdEntryVar_CV=StringVar()

ytdEntry_CV=Entry(tab4,width=25,textvariable=ytdEntryVar_CV,bd=4
               ,font=('Arial',20))

ytdEntry_CV.place(x=20, y=75)

ytdEntry_CV.insert(0,'ENTER THE SONG NAME')


def openlocationCV():
    
    locationError=Label(tab4,text='Select folder',fg='orange',bg='black',font=('jost',10)
                        ,justify=CENTER)

    global folder_Name1

    folder_Name1=filedialog.askdirectory()

    if(len(folder_Name1) > 1):
        
        locationError.config(text=folder_Name1,fg='black',bg='yellow')
        
        locationError.place(x=80,y=210)

    else:
              
            locationError.config(text='Please Choose folder',fg='red',bg='yellow')

            locationError.place(x=145,y=210)


#<<--------------------FACABOOK Function to check the internet connection------------------->>

def connectionCV(url='http://www.google.com/', timeout=5):

    try:
        
        req = requests.get(url, timeout=timeout)
        
        req.raise_for_status()
  
        print("You're connected to internet\n")
        
        return True
    
    except requests.HTTPError as e:

        Label(tab3,text='Checking internet connection failed',fg='blue'
              ,font=('just',14,'bold')).place(x=50,y=390)

        
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
        
    except requests.ConnectionError:

        connnection__msg=Label(tab3,text='No Internet Connection Available'
                           ,fg='blue'  ,font=('just',14,'bold'))
        
        connnection__msg.place(x=50,y=390)
        
        #print("No internet connection available.")
        
    return False

#<<---------------------------Function For Converter-------------------------------------->>

import os
from moviepy.editor import *
def Convert():

     if connectionCV() == True:
         try:
             link=str(ytdEntry_CV.get())+'.mp4'
             video=VideoFileClip(link)#video name or video pat
             aud=video.audio
             aud.write_audiofile("m_song.mp3")#name of mp3
             aud.close()
             video.close()
             Label(tab3,text='Download Successfull!',font=('Arial',10,'bold'),
              fg='yellow').place(x=50,y=390)
         except:
             Label(tab4,text='Somthing Goes Wrong',font=('Arial',22,'bold'),
                   fg='red').place(x=50,y=300)
             
#<<-----------------------------How To Use Picture Facebook-------------------------------->>
How_To_use_fb = PhotoImage(file="./Image/FB_HOW.png")

How_to_use_fb=Label(tab4,image=How_To_use_fb)

def click2():
    How_to_use_fb.place(x=0,y=475)


#<<--------------------------------HOW TO USE BUTTON------------------------------------->>


How_to_use_btn2=Button(tab4,text='HOW TO USE',width=13,bg='red',fg='white',
                   bd=8,font=('jost',10,'bold'),command=click2)

How_to_use_btn2.place(x=40,y=140)


#<<-------------------------------Button to save the file----------------------------------->

save_Entry2=Button(tab4,width=14,command=openlocationCV
                  ,bg='red',fg='white',text='SELECT FOLDER',bd=8,font=('jost',10,'bold'))

save_Entry2.place(x=238,y=140)

downloadbtn=Button(tab4,text='CONVERT',width=12,bg='red',fg='white',
                   bd=6,font=('jost',11,'bold'),command=Convert)

downloadbtn.place(x=145,y=245)

#<<---------------------------Developer SAAR-------------------------------->>

