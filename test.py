import PySimpleGUI as sg
import sys,random,glob,os
sg.theme("DarkGreen")
kir=["print(\"Hello,world!\")"]
tab=0
widths=800
heights=600
sda=0
file_list = glob.glob('*', recursive=True)
name_list = [os.path.basename(file) for file in file_list]
fl="\n".join(name_list)
file_list2 = glob.glob('templates/*.py', recursive=True)
name_list2 = [os.path.basename(file) for file in file_list2]
fl2=tuple(name_list2)

t1=sg.Tab("TextEditor",[[sg.InputText(default_text="tmp.py",key="fnam1",size=(20,10)),sg.Button(button_text="Save",key="save",size=(10,1)),sg.Button(button_text="Read",key="read",size=(10,1)),sg.Button(button_text="->",key="Next",size=(10,1)),sg.Button(button_text="<-",key="Back",size=(10,1))],[sg.Multiline(size=(widths-10,heights-20),font=("Arial",15),key="ftex1")]]) 
t2=sg.Tab("filelist",[[sg.Text(text=fl)]])
t3=sg.Tab("recipe",[[sg.Button(button_text="Import Module",key="c1"),sg.Button(button_text="AllClear",key="c2")],[sg.Button(button_text="Sample Load",key="c3")],[sg.Listbox(values=fl2,size=(widths,heights),key="kisc")]])
layout=[
    [sg.TabGroup([[t1,t2,t3]])]
]
window=sg.Window("KSW Proglarks2",layout,size=(widths,heights))
while True:
    if os.path.exists("templates")==False:
        sg.PopupError("The Templates folder does not exist. \n")
        break
    event,values=window.read()
    if event is None:
        break
    if event == "save":
        f=open(values["fnam1"],"w")
        f.write(values["ftex1"])
        kir.append(values["ftex1"])
    if event == "read":
        window["ftex1"].update("")
        for line in open(values["fnam1"],"r").readlines():
            window["ftex1"].print(line)
    if event == "Next" and sda <= len(kir)-2:
        sda+=1
        window["ftex1"].update(kir[sda])
    if event == "Back" and sda >= 2:
        sda-=1
        window["ftex1"].update(kir[sda])
    if event == "c1":
        window["ftex1"].print("import random,hashlib,msvcrt,cv2,os,sys,time\nkeyget=msvcrt.getwch()\n")
        window["ftex1"].print("rn=random.randint(0,100)\n")
    if event == "c2":
        window["ftex1"].update("")
    if event == "c3":
        for line2 in open("templates/"+values["kisc"][0],"r").readlines():
            window["ftex1"].print(line2.replace("\n",""))