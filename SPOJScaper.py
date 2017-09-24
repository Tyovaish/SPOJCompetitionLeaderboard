import urllib.request
from bs4 import BeautifulSoup
from threading import Thread

def SPOJScraperT(username,userData,problemName):
    print('Working on '+username)
    url = "http://www.spoj.com/users/"+username+"/"
    while True:
        try:
            htmlfile = urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            continue
        break
    soup = BeautifulSoup(htmlfile, 'html.parser')
    everything=soup.find_all('table',{"class":"table table-condensed"})
    if not everything:
        return
    solvedProblemTags=everything[0].find_all('a')
    for solvedProblemName in solvedProblemTags:
        if (problemName not in userData[username] or userData[username][problemName]==False) and solvedProblemName.text==problemName:
            userData[username]['points']+=10
            userData[username][problemName]=True

def addPointsToUsersT(userList,userData,problemName):
    threads=[]
    for user in userList:
        t1=Thread(target=SPOJScraperT,args=(user,userData,problemName))
        threads.append(t1)
        t1.start()
    for t in threads:
        t.join()


