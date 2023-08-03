# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!


def switch_it_up(number):
   #  stroka = ""
    match number:
        case 1:
             stroka = 'One'
        case 2:
             stroka = 'Two'
        case 3:
             stroka = 'Three'
        case 4:
             stroka = 'Four'
        case 5:
             stroka = 'Five'
        case 6:
             stroka = 'Six'     
        case 7:
             stroka = 'Seven'
        case 8:
             stroka = 'Eight'
        case 9:
             stroka = 'Nine'
        case _:
             stroka = 'None'
    return stroka

chislo = int(input('Введите число - ')) 
print(f'{switch_it_up (chislo)}') 