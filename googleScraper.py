import time
from googlesearch import search
import urllib.request

#one of my more major projects that I've worked on
#url = "https://paintwithbob.com"

#testing url opener with paintwithbob
#f = urllib.request.urlopen(url)
#test = f.read()
#if ("Paint".encode("utf-8") in test):
#    print (test)

searchterm = input("Search: ")
ctrlf = input("Find on Page: ")

botnolikey = 0 #keep track of number of no-bot websites

#get top 20 results for reddit
print("when google searching "+searchterm+", these websites contain the phrase "+ctrlf+" somewhere on the page")
for url in search(searchterm, stop=20):

    try: #if the website hates robots
        f = urllib.request.urlopen(url)
        webdata = f.read()
        if (ctrlf.encode("utf-8") in webdata): #ctrl-f the page
            print(url)


    except: #if there is ANY error

        
        for x in range (0,3): #try it again 3 times, see what happens.
            try:
                time.sleep(3) #attempting to fix most "too many requests" errors
                f = urllib.request.urlopen(url)
                webdata = f.read()
                if (ctrlf.encode("utf-8") in webdata): #ctrl-f the page
                    print(url)
                break; #if no errors after checking second time, exit for loop
            except:
                continue #keep trying if errors.
            
        botnolikey = botnolikey+1 #record number of websites with errors
        continue

print("This many websites didn't like bots:")
print(botnolikey)
