import numpy as np
import pandas as pd


def EX1():
    a = np.array[0,1,2,3,4,5,6,7,8,9]
    print(np.max(a))
    print(np.min(a))
    print(np.mean(a))
    print(np.shape(a))


def EX2():
    mylist=[1,2,3,4,5]
    mylist.append(6)
    for i in range(7,100):
        mylist.append(i)
    print (type(mylist))
    newarray = np.array(mylist)
    print(type(newarray)) 


def EX3():
   
   one=np.ones([1,1000])
   empty=np.zeros([1,1000])
   
 
 

def EX4():
    myarray=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,30,15],[16,17,18,19,20]])

    print('shape of array ')
    print(np.shape(myarray))

    #4 rows 5 cols

    print('max of array ')
    print(np.max(myarray))

    print('min of each col ')
    print(np.amin(myarray,axis=0))
    print('max of each col ')
    print(np.amax(myarray,axis=0))
    print ("mean of each col ")
    print(np.mean(myarray,axis=0))

    print('max of each row ')
    print(np.amin(myarray,axis=1))
    print ('max of each row')
    print(np.amax(myarray,axis=1))
    print ('mean of each row ')
    print(np.mean(myarray,axis=1))

    myarrayreshape=myarray.reshape([2,10])
    print(myarrayreshape)
    

EX4()
def EX5():
    myarray=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
    lastcol=myarray[:,-1:]
    print(lastcol)


def EX6():
    myarray=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
    lastcol=myarray[:,-1:]
    newarray=np.hstack((myarray,lastcol))
    print(newarray)



def EX7():
    file1 = open('Desktop\Programming 2\labs\TEXT.txt')
    newtext=file1.read()
    print(newtext.count("the"))
    print(newtext.count("a"))
    file1.close()

    #have to close and reopen file 
    #i have no idea why but it works now

    file2 = open('Desktop\Programming 2\labs\TEXT.txt')
    
    lines=file2.readlines()
    
    
    #for line in lines:
    #    counter =+ 1 
    #    print(f""" line{counter}: the {line.count('the')} a's {line.count('a')}   """)
    
    #METHOD 1 
    counter = 0
    for line in lines:
        counter = counter + 1
        print("line{}: the's {} a's {}".format(counter,line.count('the'),line.count('a')))
    
    #METHOD 2
    #counter = 0 
    #for line in lines:
    #    counter =+ 1 
    #    print(f""" line {counter}: the {repr(line.count('the'))} a's {repr(line.count('a'))}   """)

