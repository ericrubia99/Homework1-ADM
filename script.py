# Ex Say Hello, World! With Python
if __name__ == '__main__':
    text='Hello, World!'
    print(text)


#Ex Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print('Weird')
    else:
        if 2<=n<=5:
            print('Not Weird')
        elif 6<=n<=20:
            print('Weird')
        elif n>20:
            print('Not Weird')


#Ex Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#Ex Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Ex Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

#Ex Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
        else:
            leap=True
    return leap

#Ex Print Function
if __name__ == '__main__':
    n = int(input())
    s=''
    for i in range(1,n+1):
        s+=str(i)
    print(s)

#Ex List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                l.append([i,j,k])
    k=[]
    for i in l:
        if i[0]+i[1]+i[2]!=n:
            k.append(i)
    print(k)

#Ex Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr=map(int, input().split())

    l=list(arr)
    l.sort()
    max=l[n-1]
    i=n-1
    while max==l[i]:
        i-=1
    print(l[i])
    
#Ex Nested Lists
if __name__ == '__main__':
    std=[]
    grades=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        std.append([name,score])
        grades.append(score)

    for i in std:
        grades.append(i[1]) # Make a list of the grades

    for g in grades:    #Remove the duplicates
        while(grades.count(g)>1):
            grades.remove(g)
            
    x=min(grades)      #Compute the minimum and remove it
    for i in grades:
        if i==x:
            grades.remove(i)
    x=min(grades)    #Compute the new minimum and print the names
    std.sort()
    for i in std:
        if i[1]==x:
            print(i[0])

#Ex Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    x=0
    for i in student_marks[query_name]:
        x+=i
    x/=3
    format_x = "{:.2f}".format(x)
    print(format_x)

#Ex Lists
if __name__ == '__main__':
    N = int(input())
    c=[]
    arr=[]
    for i in range(N):
        c+=list(input().split())
    for i in range(len(c)):
        if c[i]=='insert':
            arr.insert(int(c[i+1]),int(c[i+2]))
            i+=2
        elif c[i]=='print':
            print(arr)
        elif c[i]=='remove':
            arr.remove(int(c[i+1]))
            i+=1
        elif c[i]=='append':
            arr.append(int(c[i+1]))
            i+=1
        elif c[i]=='sort':
            arr.sort()
        elif c[i]=='pop':
            arr.pop()
        elif c[i]=='reverse':
            arr.reverse()
    
        
#Ex Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t=tuple(integer_list)
    print(hash(t))

#Ex sWAP cASE
def swap_case(s):
    t=''
    for i in s:
        if i.isupper():
            t+=i.lower()
        else:
            t+=i.upper()
            
    return t

#Ex String Split and Join

def split_and_join(line):
    # write your code here
    a=line.split(' ')
    a='-'.join(a)
    return(a)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#Ex Whats Your Name?
def print_full_name(first, last):
    # Write your code here
    print('Hello',first,last+'!','You just delved into python.')

#Ex Mutations
def mutate_string(string, position, character):
    s=''
    s+=string[:position]+character+string[position+1:]
    return s

#Ex Find a string
def count_substring(string, sub_string):
    x=0
    for i in range(len(string)-len(sub_string)+1):
        k=0
        if string[i]==sub_string[0]:
            k=1
            for j in range(1,len(sub_string)):
                if string[i+j]==sub_string[j]:
                    k+=1
        if k==len(sub_string):
            x+=1
    return x

#Ex String Validators
if __name__ == '__main__':
    s = input()
    an,al,d,l,u=0,0,0,0,0
    for i in s:
        if i.isalnum():
            an+=1
        if i.isalpha():
            al+=1
        if i.isdigit():
            d+=1
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
    
    if an>0:
        print(True)
    else:
        print(False)
    
    if al>0:
        print(True)
    else:
        print(False)
    if d>0:
        print(True)
    else:
        print(False)
    if l>0:
        print(True)
    else:
        print(False)
    if u>0:
        print(True)
    else:
        print(False)

#Ex Text Wrap

def wrap(string, max_width):
    s=string[0]
    k=1
    for i in string[1:]:
        if k%(max_width)==0:
            s+='\n'
        s+=i
        k+=1
    return s

#Ex Designer Door Mat

c='.|.'
w='WELCOME'
N, M = map(int, input().split())

for i in range(N//2):
    print((c*i).rjust(M//2-1,'-')+c+(c*i).ljust(M//2-1,'-'))
    
print(w.center(M,'-'))

for i in range(N//2):
    print((c*(N//2-i-1)).rjust(M//2-1,'-')+c+(c*(N//2-i-1)).ljust(M//2-1,'-'))

#Ex  String Formatting
def print_formatted(number):
    # your code goes here
    l=len(str(bin(number)))-2
    for i in range(1,number+1):
        d=str(i)
        o=str(oct(i))
        h=str(hex(i).upper())
        b=str(bin(i))
        print(d.rjust(l,' '),o[2:].rjust(l,' '),h[2:].rjust(l,' '),b[2:].rjust(l,' '))

#Ex Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    from string import ascii_lowercase as alpha
    for i in range(1,2*size):
        k = alpha[abs(size-i):size] #The letters from size-i to size
        k = k[-1:0:-1] + k #We write them backwards and the original way
        print( '-'.join(k).center(4*size-3,'-')) # Join them with -
    
    #To do this programme I looked through internet and fount the ascii_lowercase information and the idea for the command where it appears

#Ex Capitalize!
# Complete the solve function below.
def solve(s):
    l = list(s)
    ok = True
    for i in range(len(l)):
        if l[i] == ' ': #If we have a blank space
            ok = True
            continue
        if ok is True: #The next letter needs to be capital
            l[i] = l[i].upper()
        ok = False
    return ''.join(l)

# Ex Text Alignment
# I CANNOT MAKE THIS ONE WORK

t = int(input())
# Thickness
c = 'H'


     # First Part (Top)

for i in range(t):
    print((c*i).rjust(t-1)+c+(c*i).ljust(t-1))
                                            #The number of Hs grows at
                                               #At boths sides from the center

                                               
      # Second Part (2 columns)

for i in range(t+1):
    print((c*t).center(2*t-1)+(c*t).rjust((t-2)*(t+1)))
    # A columns of 5 centered in a space of 9 and another  in 20

    
      # Middle
for i in range(int((t+1)/2)):
    print((c*t**2).center(t**2+t-1))
    # 3 rows of 25 characters centered with 2 spaces of margin

      # Fourth Part (Same as the 2nd One)


for i in range(t+1):
    print((c*t).center(2*t-1)+(c*t).rjust((t+1)*(t-2)))
    # A columns of 5 centered in a space of 9 and another  in 20

      #Last Part
for i in range(t-1):
    print((c*(t-i-1)).rjust(t**2-1)+c+(c*(t-i-1)).ljust(t-i))
print(c.rjust(t**2)+'')


#Ex The Minion Game

def minion_game(string):
    # your code goes here
    x = zip(list(string), range(len(string), 0, -1))
    Stuart,Kevin=0,0
    vowels=['A','E','I','O','U']
    for e in x:
        if e[0] in vowels:
            Kevin+=e[1]
                        # I did look into the discussions for this
                        # I had done another one but got 4/16 or so
                        #for time exceeding error
        else:
            Stuart+=e[1]
    #Results
    if Kevin>Stuart:
        print(f'Kevin {Kevin}')
    elif Kevin<Stuart:
        print(f'Stuart {Stuart}')
    else:
        print('Draw')

#Ex Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    sub_n=n//k
    
    substrings=[]
    for i in range(1,n+1): #We move through all the letters
        if string[i-1] not in substrings:
            substrings.append(string[i-1])
            #We add it if it was not there
        if i%k==0:
        #And if we have reached maximum length, we put them together
        # and restrart from where we were
            print(''.join(substrings))
            substrings.clear()

#Ex Introduction to Sets

def average(array):
    # your code goes here
    s=set(array)
    k=len(s)
    x=0
    for i in s:
        x+=i
    return x/k

#Ex No Idea!

n,m=map(int, input().split())
array=list(map(int, input().split()))
a=set(map(int, input().split()))
b=set(map(int, input().split()))
s=0

for i in array:
    if i in a:
        s+=1
    elif i in b:
        s-=1
print(s)

#Ex Symmetric Difference

m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))

s=(a.union(b))-(a&b)
l=list(s)
l.sort()
for i in l:
    print(i)

#Ex Set .add()

n=int(input())
stamps=set()
for i in range(n):
    stamps.add(input())
print(len(stamps))

#Ex Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
k = int(input())

for i in range(k):
    c=input().split()
    if c[0]=='remove':
        s.remove(int(c[1]))
    elif c[0]=='discard':
        s.discard(int(c[1]))
    elif c[0]=='pop':
        s.pop()

print(sum(s))

#Ex Set .union() Operation

n=int(input())
eng=set(map(int,input().split()))
m=int(input())
fr=set(map(int,input().split()))

std=eng|fr
print(len(std))

#Ex Set .intersection() Operation

n=int(input())
eng=set(map(int,input().split()))
m=int(input())
fr=set(map(int,input().split()))

print(len(eng & fr))

#Ex Set .difference() Operation

a=int(input())
eng=set(map(int,input().split()))
b=int(input())
fr=set(map(int,input().split()))

print(len(eng-fr))

#Ex Set .symmetric_difference() Operation

n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))

print(len(a.symmetric_difference(b)))

#Ex Set Mutations

n=int(input())
a=set(map(int,input().split()))
k=int(input())

for i in range(k):
    c=list(input().split())
    b=set(map(int,input().split()))
    if c[0]=='update':
        a.update(b)
    elif c[0]=='intersection_update':
        a.intersection_update(b)
    elif c[0]=='difference_update':
        a.difference_update(b)
    elif c[0]=='symmetric_difference_update':
        a.symmetric_difference_update(b)
print(sum(a))

#Ex The Captains Room

from collections import Counter
k=int(input())
l=list(map(int,input().split()))
l=Counter(l)
#We use a dictionary where the numbers in l are counted
for i in l:
#For every number
    if l[i]!=k:
    #If it appears a different number than k times, it is the captain
        print(i)

#Ex Check Subset

k=int(input())

for i in range(k):
    n=int(input())
    a=set(map(int,input().split()))
    m=int(input())
    b=set(map(int,input().split()))
    k=0
    for i in a:
        if i not in b:
            k+=1
    if k>0:
        print(False)
    else:
        print(True)

#Ex Check Strict Superset

a=set(map(int,input().split()))
n=int(input())

k=0
for i in range(n):
    b=set(map(int,input().split())) #Read the set
    for i in b:
        if i not in a:
    #If an element is not in a, we increase k
            k+=1

if k>0:
    #If k has been modified, then false
    print(False)
else:
    print(True)

#Ex collections.Counter()

from collections import Counter
n=int(input())
l=list(map(int,input().split()))
k=int(input())
d=Counter(l)
m=0
for i in range(k):
    o=list(map(int,input().split()))
    if d[o[0]]>0:
        m+=o[1]
        d[o[0]]-=1
print(m)

#Ex DefaultDict Tutorial

from collections import defaultdict

n,m=list(map(int,input().split()))
d=defaultdict(list)

for i in range(1,n+1):
    d[input()].append(i)

for j in range(m):
    idx=d[input()]
    if idx==[]:
        print(-1)
    else:
        print(*idx)

#Ex Collections.namedtuple()

from collections import namedtuple

n=int(input())
student=namedtuple('student',input().rsplit())

print(sum([int(student(*input().rsplit()).MARKS) for _ in range(n)])/n)
    #We get all the Marks of the students and the the average

#Ex Collections.OrderedDict()

from collections import OrderedDict

order=OrderedDict()
n=int(input())
for i in range(n):
    *name, price = tuple(map(str, input().split()))
    name, price = " ".join(name), int(price)
    # I checked how to properly read the name in the discussion chat
    if name in order:
        order[name]+=int(price)
    else:
        order[name]=int(price)

for n,v in order.items():
    print(n,v)

#Ex Word Order

from collections import Counter, defaultdict

n=int(input())
    #I tried this but apparently it exceeds the time limit
    #l=[]
    #for i in range(n):
    #    l.append(input())

    #print(len(set(l)))
    #for i in Counter(l).keys():
    #    print(Counter(l)[i],end=' ')
d=defaultdict(list)
for i in range(n):
    d[input()].append(i)
print(len(d))
for i in d.keys():
    print(len(d[i]), end = " ")

#Ex Collections.deque()

from collections import deque

n=int(input())

d=deque()
for i in range(n):
    o=list(map(str,input().split()))
    if o[0]=='append':
        d.append(int(o[1]))
    elif o[0]=='appendleft':
        d.appendleft(int(o[1]))
    elif o[0]=='pop':
        d.pop()
    elif o[0]=='popleft':
        d.popleft()
    elif o[0]=='extend':
        d.extend(o[1])
    elif o[0]=='extedleft':
        d.extendleft(o[1])
    elif o[0]=='clear':
        d.clear()
    elif o[0]=='reverse':
        d.reverse()
    elif o[0]=='remove':
        d.remove(o[1])
    elif o[0]=='rotate':
        d.rotate(int(o[1]))
    elif o[0]=='count':
        d.count()
print(*d)
    
#Ex Company Logo
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    sort=Counter(sorted(s))
    for i,j in sort.most_common(3):
        print(i,j)

#Ex Piling Up!

from collections import deque
t=int(input())

for i in range(t):
    n=int(input())
    b=deque(list(map(int,input().split())))
    maximum=max(b)
    #We compute the maximum
    res='Yes'
    for i in range(n):
        if b[0]>=b[-1]:
            #Assign the maximum of the extrems to max_b and
            max_b=b[0]
            #remove it
            b.popleft()
        else:
            max_b=b[-1]
            b.pop()
        if maximum>=max_b:
            #If the new max_b>maximum, then we cannot do it
            maximum=max_b
        else:
            res='No'
            break
    print(res)

#Ex Calendar Module

import calendar as c
m,d,y=map(int,input().split())

x=c.weekday(y,m,d)
days=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(days[x])

#Ex Time Delta

import math
import os
import random
import re
import sys
import datetime as datet
# Complete the time_delta function below.
def time_delta(t1, t2):
    f = "%a %d %b %Y %H:%M:%S %z" #We stablish the format of the date
    dt1 = datet.datetime.strptime(t1, f)  #And make these new variables
    dt2 = datet.datetime.strptime(t2, f) #from the previous format
    return f"{round(abs((dt1-dt2).total_seconds()))}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Ex Exceptions
n=int(input())

for i in range(n):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print('Error Code:',e)

#Ex Zipped!

n,x=map(int,input().split())
l=[]

for _ in range(x):
    l.append(list(map(float,input().split())))

z=list(zip(*l)) #This way, we put all the grades of every student together
for i in range(n):
    print(sum(z[i])/x)


#Ex Athlete Sort

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    sorted_arr=sorted(arr,key=lambda x:x[k])
    #We use a lambda function to sort according to the k-th parameter
    for i in sorted_arr:
        print(*i)

#Ex Map and Lambda Function

cube = lambda x: x**3# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==1:
        l=[0]
    elif n==2:
        l=[0,1]
    elif n==0:
        l=[]
    else:
        l=[0,1]
        for i in range(2,n):
            l.append(l[i-1]+l[i-2])
    return l

#Ex Detect Floating Point Number

import re
t=int(input())
l=[]
for i in range(t):
    k=input()
    try:
        #x=(bool(re.match(r"[-+]?",k)) and #bool(re.search(r'[0-9]*\.[0-9]+$',k)))
        #I wanted to check if they start with +/-, and the digits
        x=bool(float(k))
        print(x)
    except:
        print(False)
        
#Ex Re.split()

regex_pattern = r"[.,]"    # Do not delete 'r'.

#Ex Group(), Groups() & Groupdict()

import re
s=input()
m=re.findall(r'([A-Za-z0-9])\1+',s)
    #This function returns, with the argument
    #given, the elements that are repeated
if len(m)>0:
    print(m[0])
else:
    print(-1)

#Ex Re.findall() & Re.finditer()

import re
s=input()
m=re.findall(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])", s)
#Now we have to specify that it must be between two consonants (opp of vowels)
# and that it must contain at least two vowels
if len(m)>0:
    for i in m:
        print(i)
else:
    print(-1)

#Ex Re.start() & Re.end()

import re
s=input()
k=re.compile(input())
results=k.search(s)
#We look for the first match
if results:
    while results:
        print(f'({results.start()}, {results.end()-1})')
        results = k.search(s,results.start()+1)
        #Then we look for a match  startingfrom the previous one's end+1
else:
    print('(-1, -1)')

#Ex Regex Substitution

import re
n=int(input())

for i in range(n):
    s=input()
    while ' && ' in s or ' || ' in s:
        s=s.replace(' && ',' and ').replace(' || ',' or ')
    print(s)

#Ex Validating Roman Numerals
t='M{0,3}' #Up to 3 Ms
h='(D?C{0,3}|C[DM])' #D? with at most 3 Cs #C before D or M
d='(L?X{0,3}|X[LC])'  #L? with at most 3 Xs #X before L or C
u='(V?I{0,3}|I[VX])'  #V? with at most 3 Is #I before V or X
regex_pattern = r"%s%s%s%s$"%(t,h,d,u)    # Do not delete 'r'.

#Ex Validating phone numbers
import re
form=r'^[789][0-9]{9}$' #Must begin with 7-8-9 and have 9 more digits
n=int(input())
for i in range(n):
    num=input()
    if len(num)<2 or len(num)>15 :
        print('NO')
        break
    if bool(re.match(form,num)):
        print('YES')
    else:
        print('NO')

#Ex Validating and Parsing Email Addresses
import re
n=int(input())
f=r'<[a-z][a-zA-Z0-9\-\.\_]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}>'
#email can contain those characters, then @ domain and then the extension (3 letters)
for i in range(n):
    name,email=list(map(str,input().split()))
    if bool(re.search(f,email)):
        print(name, email)

#Ex Hex Color Code

import re
f=r'#[0-9a-fA-F]{3,6}[,;\(\)]'
#We set the format of the code

n=int(input())
for _ in range(n):
    x=re.findall(f,input().strip())
    for correct in x:
        print(correct[:-1])

#Ex HTML Parser - Part 1
from html.parser import HTMLParser
    # create a subclass and override the handler methods
    #It is essentially a copy of the original one but we change the titles
    #and print the attributes for start and empty cases
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for i in attrs:
            print(f'-> {i[0]} > {i[1]}')
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for i in attrs:
            print(f'-> {i[0]} > {i[1]}')

n=int(input())
txt=''
for i in range(n): #we write all the text together
    s=input()
    txt+=s
parser=MyHTMLParser()
parser.feed(txt)

#Ex HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data!='\n':
                #We do not print if it is just a '\n'
            if '\n' in data:
                #More than one line
                print (">>> Multi-line Comment")
                print(data)
            else:
                #just one line
                print('>>> Single-line Comment')
                print(data)
    
    def handle_data(self, data):
        if '\n' not in data:
            #We do not print if it is just a '\n'
            print (">>> Data")
            print(data)
  
  
html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Ex Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser
# We do a little modification of the previously used functions
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print(f"-> {attr[0]} > {attr[1]}") for aid, attr in enumerate(attrs)]

    def handle_startendtag(self, tag, attrs):
        print(tag)
        [print(f"-> {attr[0]} > {attr[1]}") for attr in attrs]

n=int(input())
p = MyHTMLParser()
for _ in range(n):
    p.feed(input())

#Ex Validating UID

import re

f=r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$'
# The format asks for a capital letter at least 2 times
# at least 3 digits and no to characters that have appeared once
n=int(input())

for _ in range(n):
    ok=re.match(f,input())
    if ok:
        print('Valid')
    else:
        print('Invalid')

#Ex Validating Credit Card Numbers

import re
n=int(input())
#format one checks if starts with 4,5 or 6, 16 dig, and the hyphen cond.
f1=re.compile(r'^(?=[4|5|6])(\d{4}\-?){3}\d{4}$')
#format 2 checks the repetitions
f2=re.compile(r'(\d)\1{3,}')

for _ in range(n):
    #format
    k=input()
    ok=re.search(f1,k)
    if bool(ok):
        ok2=re.search(f2,k.replace('-',''))
        if not ok2:
            print('Valid')
            #If there are not reps
        else:
            print('Invalid')
            #If there are reps
    else:
        print('Invalid')

#Ex Validating Postal Codes

regex_integer_in_range = r'^[1-9][0-9]{5}$'
#Interval
regex_alternating_repetitive_digit_pair = r"(?=(([0-9]).)(?=\2))"
#Alt rep

#Ex Matrix Script

# I GET THE SAME RESULT BUT IS SAYS WRONG, I DO NOT KNOW HOW TO SORT THAT OUT
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

f=r'(?<=\w)[!@#$%& ]{1,}(?=\s*\w)'
# here we ask if there is one or more of these symbols between two words
text=''
# we put all the text in a string
for i in range(m):
    for j in range(n):
        c=str(matrix[j][i])
        text+=c
#Change all the cases included in f for ' '
print(re.sub(f,' ',text))

#Ex XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    r=len(node.attrib)
    for i in node.findall('.//'):
            # I did search for this on internet because I had not
            #worked with anythign similar before
        r+=len(i.attrib)
    return(r)

#Ex XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level+=1
    if level>maxdepth:
        #First we update the depth
        maxdepth=level
    for i in elem:
        depth(i,level)
            #And so will keep doing until we get to the bottom

#Ex Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        x= lambda t: '+91 '+t[-10:-5]+' '+t[-5:]
        #x will write l correctly
        f(map(x,l))
        #now l is sorted according to x
    return fun

#Ex Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        for x in people:
            x[2]=int(x[2])
            #We assigne to each its age (int) to sort them
        return (map(f,sorted(people,key=operator.itemgetter(2))))
    return inner


#Ex Arrays

import numpy as np
def arrays(arr):
    # complete this function
    # use numpy.array
    a=np.array(arr,float)
    a=a[::-1]
    return a
    
#Ex Shape and Reshape

import numpy as np
a=list(map(int,input().split()))
arr=np.array(a)
print( np.reshape(a,(3,3)))

#Ex Transpose and Flatten
import numpy as np
n,m=map(int,input().split())

arr=np.array([list(map(int,input().split())) for i in range(n)])

print(np.transpose(arr))
print(arr.flatten())

#Ex Concatenate

import numpy as np

n,m,p=map(int,input().split())

a=np.array([list(map(int,input().split())) for _ in range(n)])
b=np.array([list(map(int,input().split())) for _ in range(m)])

print(np.concatenate((a,b),axis=0))

#Ex Zeros and Ones

import numpy as np
dim=list(map(int,input().split()))
print(np.zeros((dim),dtype=np.int))
print(np.ones((dim),dtype=np.int))

#Ex Eye and Identity

import numpy as np
np.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
print(np.eye(n,m))

#Ex Array Mathematics
import numpy as np
n,m=map(int,input().split())

a=np.array([list(map(int,input().split())) for i in range(n)])
b=np.array([list(map(int,input().split())) for i in range(n)])

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(a//b)
print(a%b)
print(np.power(a,b))

#Ex Floor, Ceil and Rint

import numpy as np
np.set_printoptions(legacy='1.13')
a=list(map(float,input().split()))
arr=np.array(a,float)

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
    
#Ex Sum and Prod

import numpy as np
np.set_printoptions(legacy='1.13')

n,m=map(int,input().split())
a=np.array([list(map(int,input().split())) for i in range(n)])
b=np.sum(a,axis=0)
print(np.prod(b))

#Ex Min and Max

import numpy as np
np.set_printoptions(legacy='1.13')

n,m=map(int,input().split())
a=np.array([list(map(int,input().split())) for i in range(n)])
b=np.sum(a,axis=0)
print(np.prod(b))

#Ex Mean, Var, and Std

import numpy as np
n,m=map(int,input().split())
a=np.array([list(map(int,input().split())) for i in range(n)])

print(np.mean(a,axis=1))
print(np.var(a,axis=0))
print(round(np.std(a,axis=None),11))

#Ex Dot and Cross
import numpy as np
n=int(input())
a=np.array([list(map(int,input().split())) for i in range(n)])
b=np.array([list(map(int,input().split())) for i in range(n)])
c=np.zeros((n,n),int)
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]

print(c)

#Ex Inner and Outer

import numpy as np
a=np.array(list(map(int,input().split())))
b=np.array(list(map(int,input().split())))

print(np.inner(a,b))
print(np.outer(a,b))

#Ex Polynomials

import numpy as np
coef=np.array(list(map(float,input().split())))
x=float(input())
print(np.polyval(coef,x))

#Ex Linear Algebra

import numpy as np
n=int(input())

a=np.array([list(map(float,input().split())) for i in range(n)])
print(round(np.linalg.det(a),2))


###### EXERCISE 2

# Ex Candles


import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    m=max(candles)
    x=0
    for i in candles:
        if i==m:
            x+=1
    return(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#Ex Number Line Jumps

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    num_jumps=x2-x1
    #We get this from making x1+t*v1=x2+t*v2
    for i in range(num_jumps):
        x1+=v1
        x2+=v2
        if x1==x2:
            return('YES')
    return('NO')
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Ex Viral Advertising

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    x=5
    c=x//2
    l=c
    # x is shared=3*likes and the likes get stored in c
    for i in range(n-1):
        x=3*l
        l=x//2
        c+=l
    return(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Ex Recursive Digit Sum

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    aux=0
    if k==1 and len(n)==1:
        return(int(n))
    for i in range(len(n)):
        aux+=int(n[i])
    return(superDigit(str(k*aux),1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#For both insertion exercises I have checked my programming notes in C that I had
#from my uni in a course of cientific programming

#Ex Insertion Sort - Part 1

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    m=arr[n-1]
    #We keep the last digit
    #Let us move backwards along the array (n-1 to -1 = n times ok!)

    for i in range(n-1,-1,-1):
        #If the number is greater than m, we copy the number in front of itself
        if m<arr[i-1] and i>0:
            arr[i]=arr[i-1]
            print(' '.join(str(x) for x in arr))
        else:
            #If the number is smaller, we put m between that number and the one in front
            #Or if we have reached the last digit, we just put m there
            arr[i]=m
            print(' '.join(str(x) for x in arr))
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)





#Ex Insertion Sort - Part 2

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    #From the beggining
    for i in range(1,n):
        #We check every number against all the previous ones
        for j in range(i):
            #If it is smaller, we place it there and move all the cones at the right
            if arr[i]<arr[j]:
                aux=arr[j]
                arr[j]=arr[i]
                arr[i]=aux
        print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


