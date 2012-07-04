import urllib
import re

# Get a file-like object for the Python Web site's home page.
f = urllib.urlopen("http://www.wunderground.com/global/stations/65432.html")
# Read from the object, storing the page's contents in 's'.
s = f.read()
match=re.search(r'<div id="tempActual">.*?>(<span\sclass="b">)(\d*?)<',s,re.DOTALL)
if match!=None:
    print 'THE TEMPERATURE NOW IS', match.group(2),'°C'
else:
    print 'Nothing yet'
f.close()
