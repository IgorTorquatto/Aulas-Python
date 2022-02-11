from datetime import date, datetime , time

def trabalhando_com_date():
    data_atual=date.today()
    print(data_atual.strftime("%d/%m/%y"))
    data_atual2=data_atual.strftime("%A %B %Y")
    print(data_atual2)

def trabahando_com_time():
    horario= time(hour=18,minute=15,second=15)
    print(horario)

def trabalhando_com_datatime():
    data_atual=datetime.now()
    print(data_atual)
    print(data_atual.strftime("%d %m %Y"))
    print(data_atual.weekday())
    tupla=("Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo")
    print(tupla[data_atual.weekday()])


if __name__ =="__main__":
    trabalhando_com_date()
    trabahando_com_time()
    trabalhando_com_datatime()