# Class Containing all methods required in main_menu()
# Class Containing all attributes required in main_menu()


import color as cl
import emojizz as em





class booking:
	book = {}



# Static Method to save the details of booked seat
	@staticmethod
	def save():
		fp = open('Screen_Booking.txt','r')
		sold = fp.readlines()
		for i in range(len(sold)):
			sold[i] = sold[i].split(' ')
			r=int(sold[i][0])
			s=int(sold[i][1])
			booking.book[(r,s)]= [sold[i][3],sold[i][4],sold[i][5],sold[i][6],sold[i][7]]
		fp.close()



# __init__() function that define object attributes and take value from modules
	def __init__(self):
		fp = open("config.txt", 'r')
		l = fp.read()
		l = l.split(' ')
		fp.close()
		self.rows = int(l[0])
		self.seats= int(l[1])
		self.booking = [['S' for j in range(self.seats)] for i in range(self.rows)]
		self.row = 1
		self.seat = 1
		self.i = 0
		self.total_seats = int(l[4])
		self.total_price = float(l[5])
		self.booked = int(l[2])
		self.price = int(l[3])
		


# object method to show booked seats
	def show_seats(self):
	    for i in range(self.rows+1):
	        if i==0:
	            print(' ',end=' ')
	        else:
	            print(i,' ',end = ' ')
	        for j in range(self.seats+1):
	            if j == 0 and i == 0:
	                print(' ',end = ' ')
	            elif i == 0 and j>=1:
	                print(j,' ',end=' ')
	            elif j>=1:
	            	fp = open('Screen_Booking.txt','r')
	            	l = fp.readlines()
	            	for a in range(len(l)):
	            		l[a] = l[a].split(' ')
	            		if int(l[a][0]) == i and int(l[a][1]) == j:
	            			self.booking[i-1][j-1] = 'B'
	            			break
	            	print(cl.red+self.booking[i-1][j-1], ' ', end= ' '+cl.reset)
	            	fp.close()
	        print('\n')
	    print('\n\n')



# Object method to calculate price of seat on basis of selection of house
	def seat_cost(self,row,seat,rows,seats):
	    if self.rows*self.seats<=60:
	        print(cl.green+'Price per seat is $10'+cl.reset)
	        return 10
	    elif self.rows*self.seats>60 and self.rows%2==0:
	        if self.row<=self.rows/2:
	            print(cl.green+'Price per seat is $10'+cl.reset)
	            return 10
	        else:
	            print(cl.green+'Price per seat is $8'+cl.reset)
	            return 8
	    else:
	        if self.row<self.rows/2:
	            print(cl.green+'Price per seat is $10'+cl.reset)
	            return 10
	        else:
	            print(cl.green+'Price per seat is $8'+cl.reset)
	            return 8



#Object to store the information of User when new ticket booked
	def booking_info(self,i):
	    while(True):
	        while(True):
	            print('\nEnter the row Viewer',self.i+1,' wants:')
	            self.row = self.num_input()
	            if self.row>self.rows:
	                print(cl.red+'There are only ',self.rows,'rows in theater'+em.w_i+cl.reset)
	                continue 
	            break
	        while(True):
	            print('Enter the seat Viewer',self.i+1,' wants in this row:')
	            self.seat = self.num_input()
	            if self.seat>self.seats:
	                print(cl.red+'There are only ',self.seats,'seats in this row'+em.w_i+cl.reset)
	                continue
	            break
	        if (self.row,self.seat) in self.book.keys():
	            print(cl.red+'This seat is already booked. Try Again!!'+em.sad+cl.reset)
	            continue
	        break
	    while(True):
	    	cost = self.seat_cost(self.row,self.seat,self.rows,self.seats)
	    	print('\nDo you want to continue?')
	    	print("Type 'Y' for Yes and 'N' for No")
	    	choice = input()
	    	if choice == 'Y':
	    		print('\n\nEnter the First Name of Viewer',self.i+1,':')
	    		name = input()
	    		name = name.split(' ')
	    		name = name[0]
	    		print('Enter the Age of',name)
	    		age = self.num_input()
	    		print('Enter the Gender of',name)
	    		gender = input()
	    		print('Enter contact number of',name)
	    		mob = self.num_input()
	    		fp = open('Screen_Booking.txt','a+')
	    		fp.write('\n'+str(self.row)+' '+str(self.seat)+' : '+name+' '+gender+' '+str(age)+' '+str(mob)+' '+str(cost))
	    		fp.close()
	    		self.save()
	    		print(cl.gold+'\n\nTicket Sucessfully Booked!'+cl.reset)
	    		self.price = self.price+cost
	    		self.booked+=1
	    		fp = open('config.txt','w')
	    		fp.write(str(self.rows)+' '+str(self.seats)+' '+str(self.booked)+' '+str(self.price)+' '+str(self.total_seats)+' '+str(self.total_price)+'\n')
	    		fp.close()
	    		return True
	    	elif choice == 'N':
	    		print(cl.red+'Sorry Try Again'+em.w_i+cl.reset)
	    		return False
	    	else:
	    		print(cl.red+'Wront Input try Again'+em.w_i+cl.reset)



# Object method to book a new ticket
	def buy_ticket(self):
		while(True):
		    print('Enter the number of tickets you want: ')
		    ticket = self.num_input()
		    if ticket<= self.rows*self.seats:
		        for self.i in range(ticket):
		            ret = self.booking_info(self.i)
		            if ret:
		            	self.show_seats()
		            else:
		            	continue
		        break
		    else:
		        print(cl.red+'Number of tickets exceeds the total seating available here. Try Again.'+em.w_i+cl.reset)



#Object method to show House details
	def statistics(self):
		fp = open('config.txt','r+')
		l = fp.readlines()
		l = l[0].split(' ')
		self.booked = int(l[2])
		self.total_seats = int(l[4])
		self.price = int(l[3])
		self.total_price = float(l[5])
		fp.close()
		print(cl.blue+'Number of Purchased Ticket:',self.booked)
		formatted_float = "{:.2f}".format(self.booked/self.total_seats*100)
		print('Percent of Purchased Ticket:',formatted_float,'%')
		print('Current Income:',self.price)
		print('Total Income:'+str(self.total_price)+cl.reset+'\n\n')



#Object Method to show user info if seat booked
	def user_info(self):
		while(True):
			print('Enter the row number')
			r = self.num_input()
			if r>self.rows:
				print(cl.red+'Please enter row number that exists'+em.w_i+cl.reset)
				continue
			break
		while(True):
			print('Enter the seat number in this row')
			s = self.num_input()
			if s>self.seats:
				print(cl.red+'Please enter seat number that exists'+em.w_i+cl.reset)
				continue
			break
		self.save()
		if (r,s) in self.book:
			user = self.book[(r,s)]
			if user[1] in ['Male','M','m','MALE','male']:
				print('The viewer',"'s name is: Mr",user[0])
			elif user[1] in ['Female','F','f','female','FEMALE']:
				print('The viewer',"'s name is: Ms/Mrs",user[0])
			else:
				print('The viewer',"'s name is:",user[0])
			print(user[0],"'s age is:",user[2])
			print(user[0],"'s contact info is:",user[3])
			print(user[0],"'s ticket price is: $",user[4]+'\n\n')
		else:
			print('Seat is not yet booked\n\n')


# Static method to take only integer input
	@staticmethod
	def num_input():
	    while(True):
	        try:
	            num = int(input())
	            if num>0:
	            	return num
	            else:
	            	print(cl.red+'Enter a Natural Number'+em.w_i+cl.reset)
	            	continue
	        except ValueError:
	            print(cl.red+'Enter a digit Value. Try Again.'+em.w_i+cl.reset)



# **********************END OF SECRETS**********************