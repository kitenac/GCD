from lib_adv_GCD import *



# TEST OF SIMPLE big_GCD()
print("Все функции взяты из модуля lib_adv_GCD")
n = input(f"{chr(9775)}Выбери функцию(номер её), которую хочешь запустить: \n0.GCD() \n1.big_GCD, \n2.adv_GCD(), \n3.big_adv_GCD()\n{chr(9899)}  ")
n = int(n)

#TEST GCD() 
if n == 0: 
 print("[Просто НОД 2-ух чисел \\_(0-0)_/]")
 nums = input(f"Введите 2-a числа(через один пробел), чтоб получить их НОД\n{chr(9889)}").split(' ')
 nums = [int(a) for a in nums]           #changing type from str to int
 print(big_GCD(nums))

elif n == 1:
 print("[НОД произвольного количества чисел]")
 nums = input(f"Введите числа(через один пробел), чтоб получить их НОД\n{chr(9889)}").split(' ')
 nums = [int(a) for a in nums]           #changing type from str to int
 print(big_GCD(nums))



elif n == 2: 
 print("[Коэф-ты u,v для выражения НОД 2-ух чисел - именно эта функция больше всего пригождается обычно]")
 print(f'''\n
 {chr(9994)}{chr(9994)} Эту функцию тоже можно сделать для более чем 2-ух параметров 
        - см. пример расш.Алг.Евк. в НД(зелён тетр.)   \n  ''')

 nums = input(f"Введите 2-а числа a и b, чтобы узнать u,v: au + bv = НОД(a,b)\n{chr(9935)}  ").split(' ')
 nums = [int(a) for a in nums]           #changing type from str to int
 a, b = max(nums), min(nums)             #a must be greater then b

 u, v, gcd = adv_GCD(a, b)

 print(f"\nu = {u}, v = {v}, gcd(a, b) = {gcd} | Проверка: u*{a} + v*{b} = {u*a + v*b}" )
 print(f"simple GCD says gcd(a, b) = {GCD(a,b)}")



elif n == 3: 
 print("[Коэф-ты u,v,u_1,v_1, .....  для выражения НОД произвольного кол-ва чисел - жемчужина библиотеки)]")
 print("[Расширенный Алг. Евклида]\n Введите сколь угодно чисел(через один пробел), чтоб получить их НОД \nи его представление в виде линейной комбинации на элементах НОД \n")
 nums = input(f"{chr(9889)}").split(' ')
 nums = [int(a) for a in nums]           #changing type from str to int

 koefts, gcd = big_adv_GCD(nums)

 s = 0
 print(f"\n\n[Ответ]Коэффиценты по порядку ввода: {koefts}, gcd = {gcd}\n \nПровер0чка: ")
 for i in range(len(nums)):
    s += nums[i]*koefts[i]
    print(f" + a[{i}]*{koefts[i]}")

 print(f"            = {s} - it`s gcd of all inputed numbers (a[0]-a[n])")
 print(f"Simple big_GCD says gcd = {big_GCD(nums)}")


else:
 print("Incorrect number of function")