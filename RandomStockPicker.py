from tkinter import * 
import csv
import random

def extractData(search_files, sector_search):
    '''
    Extracts data from the csv files and return that data
    Parameters:
        search_files: list: list of files to search (nasdaq.csv, nyse.csv etc.)
        sector_search: list: list of sectors to search (Finance, Technology etc.)
    Return: extracted_data: list: list of companies [Symbol, Name, Sector, Industry] that matched the search criteria
    '''    
    extracted_data = []
    for i in search_files:
        with open(i , 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[9] in sector_search:         # if sector is in sector to search
                    # add the symbol, name and sector 
                    extracted_data.append([row[0], row[1], row[9], row[10]])

    return extracted_data

def getData(exchangevalue, sectorsValue):
    '''
    Makes a list of files and sectors to search
    Parameters:
        exchangevalue: string: selected exchange value
        sectorsValue: string: selected sector value
    Return: extracted_data: list: list of companies [Symbol, Name, Sector, Industry] that matched the search criteria
    '''    

    files = ["nasdaq.csv", "nyse.csv", "amex.csv"]

    # get the files to serach based on exchange slection
    search_files = []
    if exchangevalue != "ALL":
        file = f"{exchangevalue}.csv"
        search_files.append(file)
    else: search_files = files

    # get the sectors to serach based on slection
    sector_search = []
    if sectorsValue == "ALL": 
        sector_search = ['Energy', 'Technology', 'Finance', 'Capital Goods', 'Health Care', 'Consumer Non-Durables', 'Basic Industries', 'Public Utilities', 'Transportation', 'Consumer Durables', 'Consumer Services', 'Miscellaneous']
    else: sector_search.append(sectorsValue)

    extracted_data = extractData(search_files, sector_search)
    return extracted_data


gui = Tk(className='Random Stock Picker')
gui.geometry("800x500")
# set the texts
label = Label(gui, text="Welcome to Random Stock Picker!",  font=(None, 16), width=30).pack()
label = Label(gui, text="Choose an Exchange followed by Sector",  font=(None, 10), width=38).pack()



# set the exchanges and sectors
exchanges = ["ALL", "NYSE", "NASDAQ", "AMEX"] 
exchangeValue = StringVar(gui)
exchangeValue.set(exchanges[0]) # default value
exchangeswid = OptionMenu(gui, exchangeValue, *exchanges)
exchangeswid.pack()

# sectors data
sectors = ['ALL', 'Energy', 'Technology', 'Finance', 'Capital Goods', 'Health Care', 'Consumer Non-Durables', 'Basic Industries', 'Public Utilities', 'Transportation', 'Consumer Durables', 'Consumer Services', 'Miscellaneous']
sectorsValue = StringVar(gui)
sectorsValue.set(sectors[0]) # default value
sectorsWid = OptionMenu(gui, sectorsValue, *sectors)
sectorsWid.pack()


def ok():
    '''
    On press submit, call the functions and display the data
    '''    
    extracted_data = getData(exchangeValue.get(), sectorsValue.get())
    picker = random.randint(0, len(extracted_data))
    stock_picked = extracted_data[picker]
    label = Label(gui, text=f"Stock symbol: {stock_picked[0]}",  font=(None, 10)).pack()
    label = Label(gui, text=f"Company Name: {stock_picked[1]}",  font=(None, 10)).pack()
    label = Label(gui, text=f"Company Sector: {stock_picked[2]}",  font=(None, 10)).pack()
    label = Label(gui, text=f"Company Industry: {stock_picked[3]}",  font=(None, 10)).pack()


button = Button(gui, text="Select", command=ok)
print(ok)
button.pack()
gui.mainloop()



