from pandas_datareader import data
import datetime 

start = datetime.datetime(2019, 10, 14)
end = datetime.datetime(2019, 10, 25)
df = data.DataReader(name = "AAPL", data_source= 'yahoo', start = start, end =end)

print(df)