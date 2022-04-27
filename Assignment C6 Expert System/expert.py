import re
import pandas as pd
data = pd.read_csv('stocks.csv')
dataB = data
stocks = data['Symbol'].unique()[:10]
quitList = ['bye', 'exit', 'quit', 'end', 'bye bye', 'bye-bye']
while(True):
    print("\nA. View Stock Details")
    print("B. Suggest Stock to Buy")
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
        avg_user_price = float((input("Enter your purchase budget: ")))
  
        dataB['Low'] = dataB['Low'].astype(str).astype(float)
        dataB['High'] = dataB['High'].astype(str).astype(float)
        dataB['Open'] = dataB['Open'].astype(str).astype(float)
        
        previous_avg = ((dataB['Low'] + dataB['High'] )/2)
        stocks =[]
        dataB = dataB[(dataB['Open'] <= avg_user_price)]
        dataB = dataB[((dataB['365 d % chng'] > 0))]
        dataB = dataB[((dataB['30 d % chng'] > 0))]
       
        print("\nBased on your budget you can BUY : ")
        dataB['Quantity'] = (avg_user_price/dataB['Open'])
        print(dataB[['Symbol','Quantity']])
        
    
        
        qn = input("Do you want to buy by stock symbol? [Y|N]")
        if qn == 'Y':
            fno = (input("Enter stock symbol: "))
            data = data.loc[data['Symbol'] == fno]
            print("All details available for stocks are:")
            print(data[['Symbol',	'Open',	'High', 'Low',	'LTP', 'Chng', '% Chng', 'Volume (lacs)',
                  'Turnover (crs.)', '52w H', '52w L', '365 d % chng', '30 d % chng']])

            stockqty = int(input("Enter the stock quantity: "))

            if(stockqty < 0):
                print("Stock in negative quanitity can be purchased.")
            else:

                confirm = input("Please confirm your purchase? [Y|N}")
                if(confirm == 'Y'):
                    print("Stockk Purchased!")
    elif choice == 'C':
        qn = input("Do you want to buy by stock symbol? [Y|N]")
            
