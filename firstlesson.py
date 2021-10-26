# Задание № 1
#name = input('Введите Ваше имя ')
#surname = input('Введите Вашу фамилию ')
#age = int(input('Сколько Вам лет (введите цифрами) ? '))
#next_age = age + 1
#year = 2021 - age

#print(surname, name, ', Вам уже', age, 'лет !' )
#print(surname, name, ', в следующем году Вам исполнится', next_age, 'лет !')
#print(name,',Вы родились в',year,' году!' )

# Задание № 2
#time = int(input('Введите время в секундах '))
#hours = time // 3600
#minutes = (time - hours * 3600) // 60
#seconds = time - (hours * 3600 + minutes * 60)
#print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

# Задание № 3
#n = int(input("Введите число: "))

#number = str(n)
#t1 = number + number
#t2 = number + number + number
#result = n + int(t1) + int(t2)
#print("Результат равен:", result)

#Задание №4
#n = abs(int(input("Введите целое положительное число ")))
#max = n % 10
#while n >= 1:
#    n = n // 10
#    if n % 10 > max:
#        max = n % 10
#   if n > 9:
#       continue
#    else:
#        print("Максимальное цифра в числе ", max)
#        break

#Задание №5
#profit = float(input("Введите выручку фирмы "))
#costs = float(input("Введите издержки фирмы "))
#if profit > costs:
#    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
#    workers = int(input("Введите количество сотрудников фирмы "))
#    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
#elif profit == costs:
#    print("Фирма работает в ноль")
#else:
#    print("Фирма работает в убыток")

#Задание №6
#a = int(input('Введите результаты пробежки первого дня в км '))
#b = int(input('Введите общий желаемый результат в км '))
#result_days = 1
#result_km = a
#while result_km < b:
#        a = a + 0.1 * a
#        result_days += 1
#        result_km = result_km + a
#print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
