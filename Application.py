import bs4
import collections

import SPOJScaper
from tkinter import *
def addUser(top,userList,userData,newUser,labels):
    userList.append(newUser)
    userData[newUser]={'username': newUser, 'points': 0}
    top.destroy();
    display(root,userList,userData,labels)
def displayAddUserBox(userList,userData,labels):
    top = Toplevel(root)
    Label(top, text="Add User:").grid(row=0)
    addUserName=Entry(top)
    addUserName.grid(row=0, column=1)
    Button(top,text="Done",command=lambda: addUser(top,userList,userData,addUserName.get(),labels)).grid(row=1,column=1)
def removeUser(top,userList,userData,removeUserName,labels):
    userList.remove(user)
    del userData[removeUserName]
    top.destroy()
    display(root,userList,userData,labels)
def displayRemoveUserBox(userList,userData,labels):
    top = Toplevel(root)
    Label(top, text="Remove User:").grid(row=0)
    removeUserName=Entry(top)
    removeUserName.grid(row=0, column=1)
    Button(top,text="Done",command=lambda: removeUser(top,userList,userData,removeUserName.get(),labels)).grid(row=1,column=1)
def update(userList,userData,problemName,labels):
    SPOJScaper.addPointsToUsersT(userList,userData,problemName)
    for label in labels:
        label.destroy()
    display(root,userList,userData,labels)
def displayMenu(root,userList,userData,labels):
    menubar = Menu()
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Add User", command=lambda: displayAddUserBox(userList,userData,labels))
    filemenu.add_command(label="Remove User", command=lambda: displayRemoveUserBox(userList,userData,labels))
    menubar.add_cascade(label="Manage Users", menu=filemenu)
    root.config(menu=menubar)
def display(root,userList,userData,labels):
    for label in labels:
        label.destroy()
    rankings = sorted(userData.values(), key=lambda k: k['points'], reverse=True)
    i=1
    labels=[]
    for user in rankings:
        if i==1:
            first=Label(root, text=str(i)+". "+user['username']+": "+str(user['points']),fg='gold',font=("Helvetica", 50))
            first.pack()
            labels.append(first)
        elif i==2:
            second=Label(root, text=str(i)+ ". " + user['username'] + ": " + str(user['points']), fg='silver',font=("Helvetica", 50))
            second.pack()
            labels.append(second)
        elif i==3:
            third=Label(root, text=str(i) + ". " + user['username'] + ": " + str(user['points']), fg='saddle brown',font=("Helvetica", 50))
            third.pack()
            labels.append(third)
        else:
            other=Label(root, text=str(i) + ". " + user['username'] + ": " + str(user['points']),font=("Helvetica", 20))
            other.pack()
            labels.append(other)
        i+=1
    displayMenu(root, userList,userData,labels)
    problemName= Entry(root)
    problemName.pack()
    refresh=Button(root,text="Check",command=lambda:update(userList,userData,problemName.get(),labels))
    refresh.pack()
    labels.append(problemName)
    labels.append(refresh)

root = Tk()
root.title('SPOJ Competition')
userList = []
userData = {}
for user in userList:
    userData[user] = {'username': user, 'points': 0}
labels=[]
display(root,userList,userData,labels)

mainloop()