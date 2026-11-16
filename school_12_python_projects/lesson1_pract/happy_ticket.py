# Счастливым считается билет, у которого суммы первых и последних трёх цифр равны.
ticket = 0

left_part = 0
right_part = 0

number1 = 0
number2 = 0
number3 = 0

sum_left = 0
sum_right = 0

# Ожидается шестизначный номер; проверка длины ввода здесь не выполняется.
ticket = int(input("Введите номер билета (6 цифр): "))

# Деление нацело отбрасывает последние три цифры, а остаток выделяет их.
left_part = ticket // 1000
right_part = ticket % 1000

# Выделяем сотни, десятки и единицы левой части номера.
# Для десятков сначала убираем единицы, затем берём последнюю цифру.
number1 = left_part // 100
number2 = (left_part // 10) % 10
number3 = left_part % 10

sum_left = number1 + number2 + number3

# Повторно используем переменные для цифр правой части:
# сумма левой части уже сохранена в sum_left.
number1 = right_part // 100
number2 = (right_part // 10) % 10
number3 = right_part % 10

sum_right = number1 + number2 + number3

# Сравниваем суммы цифр, а не сами трёхзначные части номера.
if sum_left == sum_right:
    print("билет счастливый")
else:
    print("билет НЕ счастливый")
