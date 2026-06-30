# Final project:
# Design and write a Python program to perform the following operations:
# - get access to a file in a remote location
# - get the n (n is provided at run time by the user) most common words in the file
# - compute the average the of the X-DSPAM-Confidence in the file and send the result to the standard output
# - determine on which week day most of the messages were received
# - write code to insert in a database the following information retrieved from the remote file:
     # * sender
     # * week day
     # * hour
     # * minute
     # * second
     # * year
# - write code to retrive information on messages received on a given day, at a given time provided by the user at run time
# - design a menu to provide the user with options on how to run the program

# import necessary modules needed in this project
import os
import urllib.request, urllib.parse, urllib.error
import re
import json
import sqlite3

# display menu function
def display_menu():
   print('File processing software:')
   print('[1] - retrieve file from the remote end')
   print('[2] - print n most common words')
   print('[3] - print the average x-dspam-confidence')
   # continue with remaining options
   print('[4] - print the weekday most messages were received')
   print("[5] - create a databse")
   print('[q/Q] - exit')

# get user input (to grab the chosen menu option)
def get_input():
   return (input('Option chosen: '))

# prompts for URL and fetches the content from the remote end
def fetch_data_from_remote():
    usr_input = input('Enter URL: ')
    fhand = urllib.request.urlopen(usr_input)
    for line in fhand:
        data.append(line.decode().strip())
   # use urllib to request the remote file

# prompts the user for the number of most words and displays
def print_most_common_words():
    # prompt for necessary
    n=input("Enter the number (use digits): hit Enter key to continue... ")
    n=int(n)
    sdata=[]
    # counting
    for i in data:
        temp=i.split()
        sdata.append(temp)
    temp={}
    for i in sdata:
        for j in i:
            temp[j]=temp.get(j,0)+1
    # print n most common words
    li=list()
    for key, val in temp.items():
        li.append((val,key)) 
    li=sorted(li, reverse=True)
    temp=0
    while(n>0):
        print(li[temp])
        n=n-1
        temp=temp+1
# prints average dspam confidence
def print_avg_dspam_confidence():
   # process file to extract dspam confidence values and compute average 
    y=list()
    for i in data:
        n=re.findall("X-DSPAM-Confidence: ([0-9]+)",i)
        if len(n)>0:
            y.append(n)
    nums=list()
    for i in y:
        for q in i:
            q=int(q)
            nums.append(q)
    sums=0
    total=len(nums)
    for i in nums:
        sums=sums+i
    average=sums/total
    print(average)

def print_most_weekday():
    temp={}
    for z in data:
        if z.startswith("From "):
            words=z.split()
            temp[words[2]]=temp.get(words[2],0)+1
    del temp["Sun"]
    del temp["Sat"]
    li=list()
    for key, val in temp.items():
       li.append((val,key)) 
    li=sorted(li, reverse=True)
    print(li[0])

def create_databse():
    sdata=[]
    for i in data:
        if i.startswith("From "):
            temp=i.split()
            sdata.append()
            
    conn = sqlite3.connect('rosterdb.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS Message;

    CREATE TABLE Message (
        sender TEXT,
        day   TEXT,
        time TEXT,
        year TEXT,
    );

    ''')
    fname = input('Enter file name: ')
    if len(fname) < 1:
        fname = 'roster_data_sample.json'

    str_data = open(fname).read()
    json_data = json.loads(str_data)
    
    for i in sdata:
        for sdata in json_data:
            sender=sdata[1]
            day=sdata[2]
            time=sdata[5]
            year=sdata[6]
            
            cur.execute('''INSERT OR REPLACE INTO Message
            (sender,day,time,year) VALUES ( ?, ? )''',
            ( sender, day, time, year ) )

    conn.commit()
    
    
data=[]
while True:
   os.system('cls')
   display_menu()
   usr_input = get_input()

   # match construct: process the user input and run the corresponding code
   match usr_input.lower():
      case '1':
         fetch_data_from_remote()
         #print('option 1 chosen; hit Enter key to continue...')
         usr_input = input('option 1 chosen; hit Enter key to continue...')
      case '2':
         # You need to verify that you have data read already (from option 1)
         print_most_common_words()
         #print('option 2 chosen; hit Enter key to continue...')
         usr_input = input('option 2 chosen; hit Enter key to continue...')
      case '3':
         # You need to verify that you have data read already (from option 1)
         print_avg_dspam_confidence()
         #print('option 3 chosen; hit Enter key to continue...')
         usr_input = input('option 3 chosen; hit Enter key to continue...')
      case '4':
         # You need to verify that you have data read already (from option 1)
         print_most_weekday()
         #print('option 4 chosen; hit Enter key to continue...')
         usr_input = input('option 4 chosen; hit Enter key to continue...')
      case '5':
         # You need to verify that you have data read already (from option 1)
         create_databse()
         #print('option 4 chosen; hit Enter key to continue...')
         usr_input = input('option 5 chosen; hit Enter key to continue...')

      case 'q':
         #print('option q/Q chosen; hit Enter key to continue...')
         usr_input = input('option q/Q chosen; hit Enter key to continue...')
         quit()





