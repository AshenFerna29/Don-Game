#importing the packages
import random
import datetime

#creating the variables
name = 0
attempt = 1

#creating a function to add the date and time

def file_name():
    ''' To get the date and time'''
    date = datetime.datetime.now().strftime("%Y_%m_%d")
    time = datetime.datetime.now().strftime("%H_%M_%S")
    text_ID = random.randint(0,9999)
    text_ID = f"{text_ID:04d}"
    f_name = f"{date}_{time}_{text_ID}"
    return f_name

#openning the file 
fo = open(f"{file_name()}.txt","w")




#intializing the variablles
name = input("Player name:")
fo.write(f"Player name: {name}")
life = random.randint(100,500)

#creating an empty list
l=[]

#making a loop to go for 20 attempts
for x in range(20):
    attempt = x+1 #increasing the atempt by 1
    #giving the print statements
    print("\nAttempt",attempt)
    fo.write(f"\n\nAttempt : {attempt}")
    print("your life score is",life)
    fo.write(f"\nLife score is {life}\n")
             
    

    #creating the condition for the  first 5 attempts
    if attempt >= 1 and attempt <= 5:
        #giving the range to print the random numbers
        for _ in range (5):
            rand = random.randint(15,100)#impiorting the random numbers with range 
            print(rand,end=' ')
            fo.write(str(rand)+' ')
            l.append(rand)#appending them to the list
        
#getting a user input to fight with the given random numbers
        try:
            num = int(input('Enter : '))
            fo.write(f"\nEnter a number: {num}")
        except ValueError:
            print("Invalid input Game Over")
            break
        
            
        #cheackin wether the numbe in the created list
        if num in l:
            #giving the coditions acording to the senario
            if life == num :
                print(name, 'killed', num)
                fo.write(f"\n{name} killed {num}")
                print()
            elif life<num:
                print(num,'killed',name)
                fo.write(f"\n{num} killed {name}")
                break
            elif num<life:
                print(name,'killed',num)
                fo.write(f"\n{name} killed {num}")
       #ending the game if the user gives a invzlid input         
        elif num not in l:
            print('Out of range')
            fo.write("\nout of range")
            break
        #adding the user input number to the life score 
        life+= num

        
#creating the condition to the attempts between 6 and 10
    if 6<= attempt <=10:
        for _ in range(5):#creating the range
            rand1 = random.randint(250,2000)#importing the random numbers with range
            print(rand1,end=" ")
            fo.write(str(rand1)+' ')
            l.append(rand1)#appending the numbers to the given list
        #gettng the user inputs
        num = int(input('\nEnter : '))
        fo.write(f"\nEnter a number{num}")

        #getting the conditions 
        if num in l:
            if life == num :
                #givving the print statements and cheacking the conditions
                print(name, 'killed', num)
                fo.write(f"\n{name} killed {num}")
                print()
            elif life<num:
                print(num,'killed',name)
                fo.write(f"\n{num} killed {name}")
                break
            elif num<life:
                print(name,'killed',num)
                fo.write(f"\n{name} killed {num}")
         #cheaking wether the numbers is in the above list which was created        
        elif num not in l:
            print('Out of range')
            fo.write("\nout of range")
            break
        #adding the user input number to the life score 
        life += num
#creating the condition to the attempts between 11 and 15        
    if 11<= attempt <=15:
        #creating the range 
        for _ in range(5):
            rand2 = random.randint(3000,10000) #importing random numbers with rannge 
            print(rand2,end=" ")
            fo.write(str(rand2)+' ')
            l.append(rand2) #appending the numbers to the list which was created 

        #getting the user inputs
        num = int(input('\nEnter : '))
        fo.write(f"\nEnter a number{num}")
        #getting the printing outputs
        if num in l:
            if life == num :
                print(name, 'killed', num)
                fo.write(f"\n{name} killed {num}")
                print()
            elif life<num:
                print(num,'killed',name)
                fo.write(f"\n{num} killed {name}")
                break
            elif num<life:
                print(name,'killed',num)
                fo.write(f"\n{name} killed {num}")
                
        elif num not in l:
            print('Out of range')
            fo.write("\nout of range")
            break
        life  +=num
    if 16<= attempt<=20:
        for _ in range(5):
            rand3 = random.randint(20000,100000)
            print(rand3,end=" ")
            fo.write(str(rand3)+' ')
            
            l.append(rand3)

        num = int(input('\nEnter : '))
        fo.write(f"\nEnter a number{num}")
        if num in l:
            if life == num :
                print(name, 'killed', num)
                fo.write(f"\n{name} killed {num}")
                print()
            elif life<num:
                print(num,'killed',name)
                fo.write(f"\n{num} killed {name}")
                break
            elif num<life:
                print(name,'killed',num)
                fo.write(f"\n{name} killed {num}")
                
        elif num not in l:
            print('Out of range')
            fo.write("\nout of range")
            break
        life +=num
#printing the game ststus 
print("\n\n***Game Status***")
fo.write(f"\n\n***Game Status***")#adding the printing status in to file 
print("Player Name:",name)
fo.write(f"\nPlayer Name: {name}")
print("Total Attempts:",attempt)
fo.write(f"\nTotale Attempts: {attempt}")
print("Finale life score:",life)
fo.write(f"\nFinale Life Score: {life}")
if attempt ==20: # checking wether the user has completed all the attempts 
    print(f"{name} saved letter kind")
    fo.write(f"\n{name} saved letter kind")
else:
    print(f"{name} was defeted!!!")
    fo.write(f"\n{name} was defeted!!!")




#closng the text file 
fo.close()



        

    

        
            
        

            
        
            
        
    
            
    
    

