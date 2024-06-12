from datetime import datetime, timedelta
from pytz import timezone

str_data = '2024-08-20 07:00:05'
str_fmt = '%Y-%m-%d %H:%M:%S'

date = datetime.strptime(str_data, str_fmt)
print(date.timestamp())

date = datetime.now(timezone('America/Sao_Paulo'))
print(date)

data_inicio = datetime(1979,8,20,6,20,13)
data_termino = datetime(2024,6,5,15,15,52)
delta = data_termino - data_inicio
print(delta)

delta = timedelta(days=16361, hours=8, minutes=55, seconds=39)
data_inicio = datetime(1979,8,20,6,20,13)
data_termino = data_inicio + delta
print(data_termino)


str_fmt = '%d/%m/%Y %H:%M:%S'

date2 = datetime.now()
print(date2)
print(date2.strftime(str_fmt))