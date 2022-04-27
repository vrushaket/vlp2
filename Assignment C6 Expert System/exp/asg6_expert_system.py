from curses.ascii import isdigit
import numpy as np
import pandas as pd
import datetime as dt


print("Hello! I am Yatri the flight manager")
df = pd.read_csv("flights_new.csv")
flights = df['FlightNum'].unique()[:10]
quitList = ['bye', 'exit', 'quit', 'end', 'bye bye', 'bye-bye']
while(True):
    print("A, View Flight Details")
    print("B. Book a flight")
    choice = (input("Enter your choice: "))
    if(choice in quitList):
        exit(0)
    if choice == 'A':
        for i in range(10):
            print(i+1, df['FlightNum'].unique()[i])
        print()
        flightno = int(input("Enter your flight number: "))
        df = df.loc[df['FlightNum'] == flightno]
        print("What information do you want?")
        print("1. All schedules")
        print("2. Arrival time")
        print("3. Departure time")
        print("4. Average Departure Delay")
        print("5. Average cancellation rate")
        print("6. Air Time")
        print("7. Airline Operator")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            print(df[['DayOfWeek', 'FlightNum', 'TailNum', 'Origin',
                  'Dest', 'Distance', 'DepTime', 'ArrTime']])
        elif ch == 2:
            print("Destination airport codes are")
            print(df[df['FlightNum'] == flightno]['Dest'].unique())
            dst = input("Enter your destination airport code: ")
            df1 = df.loc[df['Dest'] == dst]
            print(df1[['DayOfWeek', 'FlightNum', 'TailNum', 'Origin',
                  'Dest', 'Distance', 'ArrTime', 'ArrDelay']])
        elif ch == 3:
            print("Origin airport codes are")
            print(df[df['FlightNum'] == flightno]['Origin'].unique())
            org = input("Enter your origin airport code: ")
            df1 = df1.loc[df['Origin'] == org]
            print(df1[['DayOfWeek', 'FlightNum', 'TailNum', 'Origin',
                  'Dest', 'Distance', 'DepTime', 'DepDelay']])
        elif ch == 4:
            print("Average Departure Delay of the flight is ",
                  df[df['FlightNum'] == flightno]['DepDelay'].mean(), " minutes")
            print()
        elif ch == 5:
            print("Number of flights cancelled: ",
                  df[df['FlightNum'] == flightno]['Cancelled'].sum())
        elif ch == 6:
            org = input("Enter your origin airport code: ")
            df1 = df.loc[df['Origin'] == org]
            if df1[df['FlightNum'] == flightno]['AirTime'].mean() is np.nan:
                print("Incorrect information")
            else:
                print("Average air time of your flight is ",
                      df1[df['FlightNum'] == flightno]['AirTime'].mean())
            print()
        elif ch == 7:
            print("Carrier for your airline is ", df['UniqueCarrier'][0])
            print()
    elif choice == 'B':
        qn = input("Do you want to book by flight number? [Y|N]")
        if qn == 'Y':
            fno = int(input("Enter flight number: "))
            df = df.loc[df['FlightNum'] == fno]
            print("All flights available are:")
            print(df[['DayOfWeek', 'FlightNum', 'TailNum', 'Origin',
                  'Dest', 'Distance', 'DepTime', 'ArrTime']])
            dow = int(input("Enter day of week: "))
            org = input("Enter origin airport code: ")
            df1 = df.loc[(df['Origin'] == org) & (df['DayOfWeek'] == dow)]
            if(df1.empty):
                print("No flights matching your requirements")
            else:
                print(df1[['DayOfWeek', 'FlightNum', 'TailNum',
                      'Distance', 'DepTime', 'ArrTime']])
                confirm = input("Do you want to book this flight? [Y|N}")
                if(confirm == 'Y'):
                    print("Booked!")
        else:
            org = input("Enter origin airport code:")
            dest = input("Enter destination airport code:")
            df1 = df.loc[(df['Origin'] == org) & (df['Dest'] == dest)]
            print("Origin is    : ", org)
            print("Destination is: ", dest)
            print("Available flights are")
            print(df1[['DayOfWeek', 'FlightNum', 'TailNum',
                  'Distance', 'DepTime', 'ArrTime']])
            dow = int(input("Enter day of week: "))
            fno = int(input("Enter flight number: "))
            if(df1.empty):
                print("No flights matching your requirements")
            else:
                df1 = df1.loc[(df['FlightNum'] == fno) &
                              (df['DayOfWeek'] == dow)]
                print(df1[['DayOfWeek', 'FlightNum', 'TailNum',
                      'Distance', 'DepTime', 'ArrTime']])
                confirm = input("Do you want to book this flight? [Y|N}")
                if(confirm == 'Y'):
                    print("Booked!")
