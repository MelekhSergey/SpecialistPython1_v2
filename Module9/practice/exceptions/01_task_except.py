# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
while True:
    try:
        s = input("Введите параметры прямоугольника")
        parse = s.split("x")
        print(int(parse[0])/int(parse[1]))
        break
    except ValueError:
        print("Неправильно введена строчка")
