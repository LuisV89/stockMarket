from stock import Stock
from yahoo_fin import stock_info
import yfinance as yf
import warnings
import os
warnings.filterwarnings("ignore")

portfolio = []

def addStock(name,ticker,sector,numOfShares):
    price = round(float(stock_info.get_live_price(ticker)),2)
    newStock = Stock(name,ticker,sector,price,numOfShares)
    portfolio.append(newStock)

def updatePrices():
    for stock in portfolio:
        price = stock_info.get_live_price(stock.ticker)
        stock.currentPrice = round(float(price),2)

def viewPortfolio():
    print("{0:20s}{1:10s}{2:25s}{3:13s}{4:6s}{5:10s}".format("Name of Stock","Ticker","Industry","Price","QTY","Gain"))
    count = 1
    for stock in portfolio:
        updatePrices()
        gain = round((stock.originalPrice - stock.currentPrice)*numOfShares,2)
        print(f"{count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{25}}${stock.currentPrice:{8}}{stock.numOfShares:{5}}     ${gain:{1}}")
        count += 1
    print(" ")

def mainMenu():
    print("Main Menu")
    print("1. Add a new stock to the portfolio")
    print("2. Update Stock Prices")
    print("3. Search by Sector")
    print("4. view portfolio")
    print("5. Exit program")

def searchBySector():
    sectorPortfolio = []
    userIndustry = input("What sector are you looking for: ").lower()
    for stock in portfolio:
        if stock.sector.lower() == userIndustry:
            sectorPortfolio.append(stock)
    print("{0:20s}{1:10s}{2:35s}{3:15s}{4:14s}{5:10s}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", ))
    sectorCount = 1
    for stock in sectorPortfolio:
        print(f"\n{sectorCount}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{35}}${stock.currentPrice:{8}}{stock.numOfShares:{8}}")
        sectorCount += 1
    sectorPortfolio = []
    input("\nPRESS ENTER TO CONTINUE ")

print("Welcome to My Stock Portfolio")
print(" ")

status = True

while(status):
    mainMenu()
    choice = input("Select from the following options: ")
    os.system('clear')
    if choice == "1":
        name = input("Enter the name of the Stock: ")
        ticker = input("Enter the stock ticker name: ")
        tick = yf.Ticker(ticker).info
        sector = tick['industry']
        numOfShares = int(input("Enter the number of stock shares to buy: "))
        addStock(name, ticker, sector, numOfShares)
        print(f"Succesfully added {name} to your Portfolio")
        print(" ")
    
    elif choice == "2":
        updatePrices()
        viewPortfolio()
    
    elif choice == "3":
        searchBySector()

    elif choice == "4":
        viewPortfolio()

    elif choice == "5":
        status = False

    else:
        print("please enter a valid number.")

print("Thanks for using my stock portfolio program. Have a nice day!")
print("Hi")



