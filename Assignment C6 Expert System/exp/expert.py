import pandas as pd
data = pd.read_csv('stocks.csv')
stocks = data['Symbol'].unique()[:10]
quitList = ['bye', 'exit', 'quit', 'end', 'bye bye', 'bye-bye']
while(True):
    print("\nA. View Stock Details")
    print("B. Book a flight")
    choice = (input("Enter your choice: "))
    if(choice in quitList):
        exit(0)
        
    if choice == 'A':
        for i in range(10):
            print(i+1, data['Symbol'].unique()[i])
        print()
        stocksymbol = (input("Enter your stock symbol: "))
        data = data.loc[data['Symbol'] == stocksymbol]
        print("What information do you want?")
        print("1. Open")
        print("2. High")
        print("3. Low")
        print("4. Change Percentage")
        print("5. Volume (in lakhs)")
        print("6. Turnover (in crores)")
        print("7. 52w High")
        print("8. 52w Low")
        print("9. Year Change Percentage")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            print(data[['Symbol', 'Open']])
            print()
        elif ch == 2:
            print(data[['Symbol', 'High']])
            print()
        elif ch == 3:
            print(data[['Symbol', 'Low']])
            print()
        elif ch == 4:
            print(data[['Symbol', '% Chng']])
            print()
        elif ch == 5:
            print(data[['Symbol', 'Volume (lacs)']])
            print()
        elif ch == 6:
            print(data[['Symbol', 'Turnover (crs.)']])
            print()
        elif ch == 7:
            print(data[['Symbol', '52w H']])
            print()
        elif ch == 8:
            print(data[['Symbol', '52w L']])
            print()
        elif ch == 9:
            print(data[['Symbol', '30 d % chng']])
            print()
    elif choice == 'B':
        qn = input("Do you want to buy by stock symbol? [Y|N]")
        if qn == 'Y':
            fno = (input("Enter stock symbol: "))
            data = data.loc[data['Symbol'] == fno]
            print("All details available for stocks are:")
            print(data[['Symbol',	'Open',	'High'	,'Low',	'LTP','Chng','% Chng'	,'Volume (lacs)',	'Turnover (crs.)'	,'52w H'	,'52w L'	,'365 d % chng'	,'30 d % chng']])
            
            stockprice = int(input("Enter the stock quantity: "))
            org = input("Enter  ")
            data1 = data.loc[(data['Origin'] == org) & (data['DayOfWeek'] == stockprice)]
            if(data1.empty):
                print("No flights matching your requirements")
            else:
                print(data1[['DayOfWeek', 'FlightNum', 'TailNum',
                      'Distance', 'DepTime', 'ArrTime']])
                confirm = input("Do you want to book this flight? [Y|N}")
                if(confirm == 'Y'):
                    print("Booked!")
        else:
            org = input("Enter origin airport code:")
            dest = input("Enter destination airport code:")
            data1 = data.loc[(data['Origin'] == org) & (data['Dest'] == dest)]
            print("Origin is    : ", org)
            print("Destination is: ", dest)
            print("Available flights are")
            print(data1[['DayOfWeek', 'FlightNum', 'TailNum',
                  'Distance', 'DepTime', 'ArrTime']])
            stockprice = int(input("Enter day of week: "))
            fno = int(input("Enter flight number: "))
            if(data1.empty):
                print("No flights matching your requirements")
            else:
                data1 = data1.loc[(data['FlightNum'] == fno) &
                              (data['DayOfWeek'] == stockprice)]
                print(data1[['DayOfWeek', 'FlightNum', 'TailNum',
                      'Distance', 'DepTime', 'ArrTime']])
                confirm = input("Do you want to book this flight? [Y|N}")
                if(confirm == 'Y'):
                    print("Booked!")
