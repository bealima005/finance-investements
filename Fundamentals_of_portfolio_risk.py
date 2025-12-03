#Python code to compute the daily returns in percentage, of Dow Stocks listed in Sec.1.1
#calls function StockReturnsComputing to compute asset returns

#dependencies
import numpy as np
import pandas as pd

#input stock prices dataset
#'/kaggle/input/fundamentals-of-risk-and-return-of-a-portfolio/DJIA_Apr112014_Apr112019.csv'
stockfile = 'C:/Users/Utilizador/Desktop/Patinha Parreca/Projeto/HistoricalData_apple.csv'

#lê o ficheiro csv e coloca o por colunas 
df = pd.read_csv(stockfile)

#imprime todo o dataframe em formato de tabela: linha e coluna
print(df)

#imprime uma coluna especifica 
print(df['Close/Last'])

#substitui o $ por nada e torna o um float
close_price = df['Close/Last'].replace(r'\$','', regex = True).astype(float)
print(close_price)

"""for i in close_price:
    print(i)"""


#the return of a stock buy on day x and sell on day y>x, can be achieved
# calculating the rate of return Rt (%) = ((Py-Px)/Px)*100
# in other words, the dayly return of a stock is Rt% for the day concerned

#function to compute asset returns
def Stocks_Return_Computing (close_price, rows):
    """computes the daily returns of stocks, 
       ((today-yesterday)/yesterday)*100,
       given the daily stock prices"""

    stock_return = np.zeros([rows-1]) #vai até rows-1 = 19 pq nao temos informação do dia 20 para fazer a taxa de retorno do dia 19
    
    for i in range(0,rows-1,1):
        stock_return[i] = ((close_price[i] - close_price[i+1])/close_price[i+1])*100

    return stock_return

print(Stocks_Return_Computing(close_price= close_price, rows=20))



