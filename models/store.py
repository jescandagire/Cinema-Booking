from tabulate import tabulate

# list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][ A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]]
# def drawSeatChart(list):
#     # col headings
#     for number in list[0]:



alphabet = [
    {'row': 'A'},
    {'row': 'B'},
    {'row': 'C'},
    {'row': 'D'},
    {'row': 'E'},
    {'row': 'F'},
    {'row': 'G'}, 
    {'row': 'H'},
    {'row': 'I'},
    {'row': 'J'},
    {'row': 'K'},
    {'row': 'L'},
    {'row': 'M'},
    {'row': 'N'},
    {'row': 'O'},
    {'row': 'P'}
]
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
seat_list = []
available_seats = []
taken_seats = []

count = 0
for i in range(16):
    seat_list.append(alphabet[i])

for seat in seat_list:
    for i in range(1, 21):
        seat_list[count][i] = "x"
    count = count + 1

class SeatAssignment:

#    def __init__(self, available, timer, level):
#        self.available = available
#        self.timer = timer
#        self.level = level

    @classmethod
    def count(cls):
        seats=[]
        cnt = 0
        for seat in seat_list:                                      #seat and seats???
            for i in range(1, 21):
                if seat_list[cnt][i] == "x":
                    seats.append(seat_list[cnt][i])
            cnt = cnt + 1

        return len(seats)

    @classmethod
    def category(cls, level):
        cnt = 0
        if level in ('Twin', 'twin', 'TWIN', 'VVIP', 'vvip', 'Vvip', 'VIP', 'vip', 'Vip', 'Economy', 'economy', 'ECONOMY'):
            print("Available seats: ")
            if level in ('Twin', 'twin', 'TWIN'):
                for n in range(0, 2):
                    for i in range(5, 17):
                        if seat_list[n][i] == "x":
                            print(alphabet_list[n] + str(i))
                            available_seats.append(alphabet_list[n] + str(i))

            elif level in ('VVIP', 'vvip', 'Vvip'):
                for n in range(0, 5):
                    for i in range(1, 5):
                        if seat_list[n][i] == "x":
                            print(alphabet_list[n] + str(i))
                            available_seats.append(alphabet_list[n] + str(i))

                    for i in range(17, 21):
                        if seat_list[n][i] == "x":
                            print(alphabet_list[n] + str(i))
                            available_seats.append(alphabet_list[n] + str(i))

                for n in range(3, 6):
                    for i in range(5, 17):
                        if seat_list[n][i] == "x":
                            print(alphabet_list[n] + str(i))
                            available_seats.append(alphabet_list[n] + str(i))

            elif level in ('VIP', 'vip', 'Vip'):
                for n in range(6, 12):
                    for i in range(1, 21):
                        if seat_list[n][i] == "x":
                            print(alphabet_list[n] + str(i))
                            available_seats.append(alphabet_list[n] + str(i))

            elif level in ('Economy', 'economy', 'ECONOMY'):
                for n in range(12, 16):
                    for i in range(1, 21):
                        if seat_list[n][i] == "x":
                            print(alphabet_list[n] + str(i))
                            available_seats.append(alphabet_list[n] + str(i))

            return True
            
        else:
            print("Desired seat category entered was incorrect!!!\n")
            return False
#****** this is for booking a seat*******
    @classmethod
    def select(cls, selection, num_seats, seat_level):
        i = 1
        print(available_seats)
        if selection in available_seats:
            for x in range(len(available_seats)):
                if available_seats[x] == selection:
                    try:
                        while i <= num_seats:
                            print(available_seats[x])
                            taken_seats.append(available_seats[x])
                            x = x + 1
                            i = i + 1
                    except IndexError:
                        print("\nAvailable seats: None \nPlease try again!")
                        break
        else:
            print("\nChoice is out of range. \nPlease try again!")

        print("taken_seats = " + str(taken_seats))
        for i in range(len(seat_list)):
            for v in seat_list[i].values():
                for n in range(len(taken_seats)):
                    if taken_seats[n] in seat_list[i].values():
                        print(v)
#******this method is for modifying the seat list******* 
    @classmethod
    def modifyList(cls):
        row = selection[0]
        print("Row = " + row)
#        for seat in seats:
#            seat_list[seat][]
        """count = 0
                                i = 0
                                r = 0
                                dummy_i = 0
                                dummy_r = 0
                                for seat in seats:
                                    if (seat['seat_id'] == selection) and (seat['status'] == "available"):       
                                        while dummy_i < num_seats:
                                            try:
                                                if seats[count + dummy_r]['level'] in ('VVIP', 'VIP', 'Economy'):
                                                    if seats[count + dummy_r]['level'] == seat_level:
                                                        dummy_i = dummy_i + 1
                                                        dummy_r = dummy_r + 1
                                                    else:
                                                        dummy_r = dummy_r + 1
                                                else:
                                                    if seats[count + dummy_r]['level'] == seat_level:
                                                        dummy_i = dummy_i + 1
                                                        dummy_r = dummy_r + 2
                                                    else:
                                                        dummy_r = dummy_r + 2
                        
                                            except IndexError:
                                                print("\nAvailable seats: None")
                                                print("Please try again!")
                                                break
                        
                                        if dummy_i == num_seats:
                                            while i < num_seats:
                                                if seats[count + dummy_r]['level'] in ('VVIP', 'VIP', 'Economy'):
                                                    if seats[count + r]['level'] == seat_level:
                                                        seats[count + r]['status'] = "taken"
                        
                                                    #    print(seats[count + r])
                                                    #    print(seats[count + r]['status'])
                                                        i = i + 1
                                                        r = r + 1
                                                    else:
                                                        r = r + 1
                                                else:
                                                    if seats[count + r]['level'] == seat_level:
                                                        seats[count + r]['status'] = "taken"
                                                        seats[count + r + 1]['status'] = "taken"
                                                    #    print(seats[count + r])
                                                    #    print(seats[count + r]['status'])
                                                    #    print(seats[count + r + 1])
                                                    #    print(seats[count + r + 1]['status'])
                                                        
                                                        i = i + 1
                                                        r = r + 2
                                                    else:
                                                        r = r + 2
                        
                                    count = count + 1
                                return True"""
#*******this method is for printing the seating chart********
    @classmethod
    def printTable(cls):
        i = 1
        new_list = []
        alphabet = [
            {' ': 'A'},
            {' ': 'B'},
            {' ': 'C'},
            {' ': 'D'},
            {' ': 'E'},
            {' ': 'F'},
            {' ': 'G'}, 
            {' ': 'H'},
            {' ': 'I'},
            {' ': 'J'},
            {' ': 'K'},
            {' ': 'L'},
            {' ': 'M'},
            {' ': 'N'},
            {' ': 'O'},
            {' ': 'P'}
        ]

       # for i in range(16):
            
       #     new_list.append(alphabet[i])
       #     i = i + 1

    
    #    for seat in seat_list:

     #       i = i + 1

      #      if seat['status'] == "available":
       #         seat['status'] = 'x'
        #        new_list.append(seat)

        header = seat_list[0].keys()
        rows = [x.values() for x in seat_list]
        print("\nSeating Chart")
        print (tabulate.tabulate(rows, header, tablefmt='github'))
#******this is the method for the type of seat prices*******
    @classmethod
    def print(cls):
        header = dataset[0].keys()
        rows =  [x.values() for x in dataset]
        print (tabulate.tabulate(rows, header, tablefmt='github'))
        print("\n\n")
#*******this method is for the adding the available seats to the seat list in the respective categories*******
    @classmethod
    def cate(cls, level):
        available_seats =[]
        if level in ('Twin','VVIP', 'VIP', 'Economy'):
            for seat in dataset.values():
                if (seat['level'] == level) and (seat['status'] == "available"):
                    seat_list.append(seat)
                    print(seat['seat_id'])

            return True
            
        else:
            print("Desired seat category entered was incorrect!!!")
            return False