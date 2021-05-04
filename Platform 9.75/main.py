# *****************Welcome To THE OTHER SIDE*****************

# Created on:   time: 00:13     Date: 1/5/2021
# Programmer: Himanshi


# Importing Global File For working of font Color in Console/Shell 
import os
os.system("cls")

# Importing local modules
import color as cl
import emojizz as em

# Importing local module from package Booking
from Booking import book



print(cl.white+cl.bold+'Welcome to Platform 9 3/4'+cl.reset+em.wizard+'\n\n\n')


screen = 0


# Function only when user choose to make own seating provision
def new_seats():
    flag = 1
    while(flag):
        try:
            print("Enter the Number of Rows:")
            rows = int(input())
            print("Enter the Number of seats in each Rows:")
            seats = int(input())
            if rows>0 and rows<101 and seats>0 and seats<101:     
                print('\n\n\n'+cl.gold+'ACCIO SEATS  '+em.chair+cl.reset+'\n\n\n')
                return rows, seats
            else:
                print(cl.red+"Enter value between 1 and 100!!"+em.w_i+cl.reset)
        except ValueError:
            print(cl.red+"Enter a digit value"+em.w_i+cl.reset)



#Loop will run till user choose one of the screen
while(True):
    print(cl.green+'Choose The Screen:\n\n'+cl.gold+'1. Prisoner of Azkaban(Fixed Seats)\n2. Deathly Hollows(Changing Seats)\n\n\n'+cl.reset)
    try:
        screen = int(input())
    except:
        print(cl.red+'Wrong Input. Please enter a digit'+em.w_i+cl.reset)
        continue
    if screen == 2:
        print(cl.cyan+'Do you want to change number of seats?')
        print("Enter 'Y/y' for yes and 'N/n' for no."+cl.reset)
        choice = input()
        choice = choice.upper()
        if choice == 'Y':
            rows, seats = new_seats()
            break
        elif choice == 'N':
            rows = 10
            seats = 10
            break
        else:
            print(cl.red+'Wrong Input!! Try Again.'+em.w_i+cl.reset)
    elif screen == 1:
        rows = 10
        seats = 10
        break
    else:
        print(cl.red+'Wrong Input!! Try Again!'+em.w_i+cl.reset)



#Global variables to stored in text file
booked = 0
price = 0
fp = open('Screen_Booking.txt','r')
l = fp.readlines()
for i in range(len(l)):
    l[i] = l[i].split(' ')
    if int(l[i][0])<=rows and int(l[i][1])<=seats:
        booked +=1
        if rows%2==0 and rows*seats>60:
            if int(l[i][0])<=rows/2:
                price = price = price+10
            else:
                price = price = price+8
        elif rows*seats<=60:
            price = price+10
        else:
            if int(l[i][0])<=(rows-1)/2:
                price = price = price+10
            else:
                price = price = price+8
fp.close()


total_seats = rows*seats
total_price = 0
if rows%2==0 and rows*seats>60:
    total_price = total_price+rows*seats/2*10+rows*seats/2*8
elif rows*seats<=60:
    total_price = total_price+rows*seats*10
else:
    total_price = total_price+((rows-1))*seats/2*10+((rows+1)*seats/2*8)


fp = open("config.txt", 'w')
fp.write(str(rows)+' '+str(seats)+' '+str(booked)+' '+str(price)+' '+str(total_seats)+' '+str(total_price))
fp.close()



# Function that will run in loop until user exits
def main_menu():
    while(True):
            print(cl.cyan+'\n\n\n1. Show the seats  '+em.sit)
            print('2. Buy a Ticket  '+em.ticket)
            print('3. Statistics   '+em.stat)
            print('4. Show Booked Ticket User Information  '+em.info)
            print('0. Exit\n\n\n'+cl.reset)
            viewer = book.booking() #Making an object of booking class
            viewer.save()
            option = input()
            if option == '1':
                print(cl.gold+'\n\nWINGARDIUM LEVIOSA  '+em.herm+'\n'+cl.reset)
                viewer.show_seats() #Calling function to show seat booking
            elif option == '2':
                viewer.buy_ticket() #calling function to buy tickets
            elif option == '3':
                viewer.statistics() #calling function to view the house details
            elif option == '4':
                viewer.user_info() #calling function to view booked seats details
            elif option == '0':
                print(cl.gold+'\n\nMISCHIEF MANAGED  '+em.mapp+'\n'+cl.reset)
                break
            else:
                print(cl.red+'Enter a digit between 0 and 4'+em.w_i+cl.reset)


main_menu()