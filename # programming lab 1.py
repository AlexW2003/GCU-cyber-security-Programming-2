# programming lab 1 


def Ex1():
    name= input("what is your name ")
    print (name)

def Ex2():
    name= input("what is your name ")
    print (name)
    print ('first letter only')
    print(name[0])
    print("first name only: ")
    print(name.split(' ')[0])
    print("last letter full name: ")
    print(name[-1])
    print('last name: ')
    print(name.split(' ')[-1])
    print ('first 3 letters of full name')
    print(name[0:3])
    print("last four letters of fist name: ")
    print (name.split(' ')[0][-4:])
    print (' letters 3 and 4 of the last name ')
    print (name.split(' ')[1][2:4])
   
def Ex2redo():
    name=input('enter your name: ')
    print(f""" 
 2.a {name}
 2.b first letter only {name[0]}
 2.c first name only {name.split(' ')[0]}
 2.d last letter fullname {name[-1]}
 2.e last name {name.split(' ')[-1]}
 2.f first 3 letters full name {name[0:3]}
 2.g last four letters first name {name.split(' ')[0][-4:]}
 2.h letters 3 and 4 last name {name.split(' ')[1][2:4]}
""")
    



def Ex3():
    fullname=input('enter your full name ')
    done=""
    for i in range(0, len(fullname),2):
        done=done+fullname[i]
    
    #second method
    print(fullname[0::2])
    print (done)
Ex3()
def Ex4():
    name= input("what is your name ")
    reversedname = name[::-1]
    print(reversedname)


def Ex5():
    fullname = input("what is your full name ")
    firstname=fullname.split(" ")[0]
    secondname=fullname.split(" ")[1]
    print(firstname)
    print(secondname)

def Ex6():
    counter=0
    name=input("enter your name ")
    for i in range(len(name)-1):
        if name[i]=='a' or name[i]=='b':
            counter += 1 
    print (counter)

def Ex7():
    namelist=[]
    for i in range(5):
        name=input('enter a name ')
        namelist.append(name)
    for n in range(5):
        print (namelist[n])


def OOPrev():

    class person:
        def init(self,age):
            name= input('give me you name now ')
            self.age= age
        def run():
            print('i am running you mong ')    


    jack=person()