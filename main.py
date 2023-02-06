class BikeRental:

    def __init__(self) :
        
        self.stocks = 100
        self.menu()




    def menu(self):
        self.user_input = input('''
        1. Display available Stocks
        2. Request a bike for rent(100BDT-1qty)
        3. Exit 
        ''')
        
        


        if self.user_input == '1':
            print('Total Available Stock :-', self.stocks)
            self.menu()

        

        elif self.user_input == '2':
            self.requestAbike()

        
        else:
            exit()



    def requestAbike(self):
        if self.stocks > 0:
            qtyOfByke = int(input('Enter the qty would you like to rent : '))

            if qtyOfByke <= self.stocks:
                self.stocks = self.stocks - qtyOfByke
                print('Done. Avable able bike :- ', self.stocks)
                print('Total Price :- ', qtyOfByke * 100)

            else:
                print(qtyOfByke, 'Is not avable avable')

        else:
            print('Bike is not availablel for rent')
            


        self.menu()

    
a= BikeRental()
