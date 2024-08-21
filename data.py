from datetime import date
data = date.today()
print("data de hoje = " + str(data))
dia = date.today().day
mes = date.today().month
ano = date.today().year


print("dia = {}, mês = {}, ano = {}".format(dia,mes,ano))