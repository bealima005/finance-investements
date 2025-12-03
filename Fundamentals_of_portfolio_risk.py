#Python code to compute the daily returns in percentage, of Apple Inc. Common Stock (AAPL)
#calls function Stock_Returns_Computing to compute asset returns

#dependencies
import numpy as np
import pandas as pd

#input stock prices dataset
stockfile = 'C:/Users/Utilizador/Desktop/Patinha Parreca/Projeto/HistoricalData_apple.csv'

#reads the CSV file and turns it into a table - dataframe(df)
df = pd.read_csv(stockfile)

#Print all the dataframe
print(df)

#chooses a specific column, in this case, the one referring to the close/last stock price
cl = df['Close/Last']

#deletes $, by replacing it with a blank space, and turns the stock prices, originally strings, into floats
close_price = cl.replace(r'\$','', regex = True).astype(float)
print(close_price)


#the return of a stock buy on day x and sell on day y>x, can be achieved
# calculating the rate of return Rt (%) = ((Py-Px)/Px)*100
# in other words, the daily return of a stock is Rt% for the day concerned

def Stocks_Return_Computing (close_price, rows):
    """computes the daily returns of stocks, 
       ((today-yesterday)/yesterday)*100,
       given the daily stock prices"""

    stock_return = np.zeros([rows-1]) #vai até rows-1 = 19 pq nao temos informação do dia 20 para fazer a taxa de retorno do dia 19
    
    for i in range(0,rows-1,1):
        stock_return[i] = ((close_price[i] - close_price[i+1])/close_price[i+1])*100

    return stock_return

print(Stocks_Return_Computing(close_price= close_price, rows=20))




