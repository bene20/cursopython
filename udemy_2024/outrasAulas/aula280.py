import locale
import calendar

print(locale.getlocale())

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8') # ao deixar o locale vazio (2o parâmetro), será usado o do sistema
print(calendar.month(2024,12))