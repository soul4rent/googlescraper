import urllib.request
url = "http://stackoverflow.com"
f = urllib.request.urlopen(url)
test = f.read()
if (b'Stack' in test):
    print ("success")
