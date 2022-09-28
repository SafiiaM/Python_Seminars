# Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ 
# студентами вуза \ учениками школы 


def sort_data(number,read,write,sor,da,data):
    while True: 
        с=number()
        if с=='1':
            print(*da(0,read()),sep='\n')    
        elif с=='2':
            print(*da(1,read()),sep='\n')        
        elif с=='3':
            print(*da(2,read()),sep='\n')    
        elif с=='4':
            print(*sor(input('Введите № класса: '),read()),sep='')   
        elif с=='5':
            print(*read(),sep='')
        elif с=='6':
            print(*sor(input('Введите фамилию ученика:'),read()),sep='')    
        elif с=='7':
            write(data())
        elif с=='8':
            print('До свидания!')        
            break
