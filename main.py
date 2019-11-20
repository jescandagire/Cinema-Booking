from models.store import SeatAssignment

print("\n\nWelcome! To Cinema Booking System\n")
restart = "Y"

while True:
    sell_seat = SeatAssignment()
    print("Number of seats available: " + str(sell_seat.count()) )
    print("Total sales: shs. 0")                    #need to use a function for this too

    print("\nChoose your preference...\n")
    print("1. Movie Schedule.")
    print("2. Seat Assignment.")
    print("3. Payments (for reserved seat).")
    print("4. Reset Seating Plan.")
    print("5. Exit.")
    option = int(input("\n--> "))

    if option == 1:
        print("\nChoose your prefered movie...\n")
        # movie schedule.readlines()
        print("1. Zootopia : 1:00pm")
        print("2. The Maze Runner : 3:00pm")
        print("3. Black panther : 5:00pm")
        print("4. Little : 7:00pm")
        opt = int(input("\n--> "))

        if opt == 1:
            
            print("\nWanna watch Zootopia..!\n")
            print("1. Book a ticket")
            print("2. Buy a ticket")
            opt = int(input("\n--> "))

            if opt == 1:
                try:
                    num_of_seats = int(input("Enter number of seats required: "))       #need to adjust the seating chart****
                
                except ValueError:
                    print("\nInteger value required.")

            elif opt == 2:
                try:
                    num_of_seats = int(input("Enter number of seats required: "))
                                
                except ValueError:
                    print("\nInteger value required.")
                seat_cat = str(input("Desired seat category(TWIN, VIP, VVIP, ECONOMY): "))
                seat_cat.lower()
                print(seat_cat.lower())

            #******RETURN THE SEATS OF THAT CATEGORY WITH THE CORRESPONDING PRICES*****
                print('Total Amount paid is : ')  #****NEED TO PICK THE PRICES FROM THE METHOD FOR SEAT CALCULATIONS****


            

    elif option == 2:
        print("\nChoose your preference...\n")
        print("1. Sell a ticket.")
        print("2. Display seating plan.")
        opt = int(input("\n--> "))
        
        if opt == 1:
            try:
                num_of_seats = int(input("Enter number of seats required: "))
                
            except ValueError:
                print("\nInteger value required.")
                
            seat_cat = str(input("Desired seat category: "))
            
            if sell_seat.category(seat_cat):
                seat_select = str(input("\n\nChoose seat: "))
                sell_seat.select(seat_select, num_of_seats, seat_cat)
                print("\n")
                
        elif opt == 2:
            sell_seat.printTable()
            
        else:
            print("\nIncorrect value entered!\n")
            
    elif option == 3:
        print("\nChoose your preference...\n")
        print("1. Sell a ticket.")
        print("2. Display seating plan.")
        opt = int(input("\n--> "))
        
        if opt == 1:
            num_of_seats = int(input("Enter number of seats required: "))
            seat_cat = str(input("Desired seat category: "))
            
            print("Availabel seats: ")
            sell_seat.cate(seat_cat)
            
            seat_select = str(input("\n\nChoose seat: "))
            sell_seat.select(seat_select, num_of_seats, seat_cat)
            print("\n")
            
        elif opt == 2:
            sell_seat.print()
            
        else:
            print("\nIncorrect value entered!\n")
            
    elif option == 4:
        pass
        
    elif option == 5:
        pass
        
    else:
        restart = "Y"
        print("\nIncorrect value entered!\n")


    list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
           ]
    output = " "
    
    def drawSeatChart(list):
        # col headings
        for number in list[0]:
            output += number
