import re

# find the word pretty
def hasPretty(inp):
    return re.search(r'pretty', inp) != None
print hasPretty('i am pretty so yeah')
print hasPretty('i am not that ahhh')
    
def whichPet(inp):
    result = re.search(r'pet (cat|dog)', inp)
    if result == None:
        return None
    return result.group(1)
print whichPet('my pet cat')
print whichPet('my pet dog was cool')
print whichPet('my pet donkey')


def getAdjs(inp):
    return re.findall(r'\w+y', inp)
    #return re.findall(r'[a-zA-Z0-9_]+y', inp) # the same thing
    #return re.findall(r'\w{1,}y', inp) # the same thing
print getAdjs('the funny book was goofy')



##
print '\n\n NUMBER 3'
print '**************'


def isEmail(inp):
    return re.match('(\w)+@\w+(\.\w)+',inp) != None

print isEmail('sd$sd@hello.com')
##  nanab@aiti-kace.com.gh
##  nanagalore@aol.com
##  nana12345@yahoo.com
##  nana_smiles@ovi.com
##  sd$sd@hello.com



##
print '\n\n NUMBER 4'
print '**************'


def getTxts(files):
    return re.findall(r'\w+\.txt',files)

print getTxts('yo.html blah.txt woah.txt he ')



print '\n\n NUMBER 5'
print '**************'

def percAwesome(inp):
    num = float(len(re.findall('(\w)+',inp))) #finding number of words
    aw_num = float(len(re.findall('awes[o|0]me',inp))) #finding number of 'awes[o|0]me'
    return round(((aw_num/num)*100),1)#returning percentage of awes[o|0]me

print percAwesome('iamawesomeblah and awes0me is as awesomeo does')

## iamawesomeblah and awes0me is as awesomeo does
## hello my name is wayawesomedude
