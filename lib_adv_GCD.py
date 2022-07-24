



# Simple and Advanced mods of GCD here
#  -for more than 2 parametrs - big_GCD() and big_adv_GCD()
#************************************************************************





#-----------Big GCD-----------------------------------
def GCD(num_1, num_2):  # Euclidian Algoritm

    num, q = max(num_1, num_2), min(num_1, num_2)
    if q == 0 and num ==0:
        return 0
    if q == 0:
        return num

    r = 1               # just initializing r                  
    while r!= 0:
     r = num % q
 #    print(f"{num} = {num//q}*{q} +{r}") #just reflecting sugar
     num = q
     q = r 

    gcd = num   #normaly it`s q, but due extra loop of while it`s num
    return num

def big_GCD(nums):     # Euclidian algoritm for many as u want numbers
    gcd = nums[0]                       #initialization(gcd is used in GCD() )           
    for num in nums[1:]:                #nums[0]`s already in gcd
        gcd = GCD(gcd, num) 
    return gcd



#---------Advanced GCD----------------------------------------------------------------------------------------------


'''
 k  q           u                        v
 0  -           0                        1                                                     # Initialize separate way
 1  q_1         1                        -q_1                                                  # Initialize separate way
 2  q_2   u_2 = u_0 - u_1*q_2    v_2 = v_0 - v_1*q_2          # Template way - by t() function
 .....
 n  q_n   u_n = u_n-2 - u_n-1*q_n    v_n = v_n-2 - v_n-1*q_n  # Template way - by t() function

 AND THE LAST STEP OF ALGO, WHEN r=0 - DOESN`T COUNT (it might be n+1 st)! (**@**)

 Result: a * u_n + b * v_n = GCD(a, b), where a >= b!

 => we will use t_n = t_n-2 - t_n-1*q_n, where t in {u, v}
 so there must be function like t(q_n, t_n-1, t_n-2)
'''


#Same GCD() function as above, but with collecting all the "q_" = q//num - called "q" in table above. (****) - changes from GCD()
def data_GCD(num_1, num_2):  # Euclidian Algoritm
    num, q = max(num_1, num_2), min(num_1, num_2)
    _q_ = [None]          # Due to table "q_0 = - "
    r = 1                 # just initializing r                  
    while r!= 0:
     #print(f"")
     _q_.append(num//q)    #(****)DATA COLLECTION
     r = num % q
     print(f"{num} = {num//q}*{q} +{r}") #just reflecting sugar
     num = q
     q = r 
     

    gcd = num   #normaly it`s q, but due extra loop of while it`s num
    return num, _q_



#*** t_n2 - t_n1*q_n  is  t_n-2 - t_n-1*q_n ***
# q is q[2:] - list of all q - collected while working of GCD() !!!!
def t(q, t_n2,  t_n1):  #searching of u_n and v_n are very simmular so let`s merge `em  
    for q_n in q: 
        t_n = t_n2 - t_n1*q_n
        print(f"{t_n2} - {t_n1}*{q_n} = {t_n}") #just reflecting
        t_n1, t_n2 = t_n, t_n1
        
    return t_n



#!!!!!! Аккуратнее при использовании(с > 2 числами)  adv_GCD() возвращает отсортированный по ВОЗРАСТАНИЮ массив, из-за data_GCD()   !!!!!!!!!!!!!
def adv_GCD(num_1, num_2): #advanced Euclidian Algoritm which finds u,v: au + bv = GCD(a, b)
    print("Euclidian Algorithm:")
    gcd, q = data_GCD(num_1, num_2)           #counting gcd and collect all the "q"

    print("q[]: ", q, end = '\n'*2)

#---Starting initialization(first two lines of table abowe): (u_k2 - u_k1*q_k  is  u_k-2 - u_k-1*q_k, where k = 2 and 3)
    u_k2,  u_k1 = 0, 1                           #u_0 and u_1
    v_k2,  v_k1 = 1, -1*q[1]                     #v_0 and v_1

#---Checking uniqual situations
    N = len(q)
    if N == 1 + 1:                               #Only 1 step was made in Euclidian Algorim  ( +1 because 0th element = None - see "data_GCD()" )
      return u_k2, v_k2, gcd                     #u_0 and v_0
    if N == 2 + 1:
      return u_k1, v_k1, gcd                     #u_1 and v_1
#---Usual sequance:
    print("---Counting u: notise, that we ignore q, when r = 0 in Euc.Alg.")
    u_n = t(q[2:N-1], u_k2,  u_k1)               # 0th and 1st  were already initialized, so send u[2:N-1], but not u[2:N] due (**@** - see table) 
    print("\n---Counting v: notise, that we ignore q, when r = 0 in Euc.Alg.")
    v_n = t(q[2:N-1], v_k2,  v_k1)                

    return u_n, v_n, gcd




#-----big_adv_GCD()---------------------------------------------------
'''
*********Let`s extend adv_GCD() to make it work with >2 numbers:*********

big_adv_GCD()
-example:
(a, b, c) = ((a, b), c) = (a,b)*u + c*v
 but (a, b) = a*u_ + b*v_
  so (a, b, c) = ((a, b), c) = (a,b)*u + c*v = (a*u_ + b*v_)*u + c*v = a*(u_*u) + b*(v_*u) + c*v = 
   = a*t_1 + b*t_2 + c*v

Result: a*t_1 + b*t_2 + c*v = (a, b, c) 

when 4 numbers:
(a, b, c, d) = ( ((a, b), c), d) = ((a, b), c)*u + d*v = (a*t_1 + b*t_2 + c*v_)*u + d*v

-Итак, алгоритм: 
 1)Сверху - вниз: (a, b),    (a, b), c),    ( ((a, b), c), d), ...... 
 2)Снежный ком: 1-ый луп узнаём u,v для (a, b) и кладём их в left, на 2-ом лупе (уже ((a, b), c) ) домножаем то, что в left на полученный на этом шаге u, а  v кладём в left,
    на 3-ем шаге домножаем всё, что в left на полученный на этом шаге u, и добавляем v в left  
 3)Все коэфф-ты лежат по порядку в left


'''


def big_adv_GCD(nums):   
    left = []
    u, v, gcd = adv_GCD(nums[0], nums[1])       #first "loop"
    if nums[1] > nums[0]:                       #adv_GCD returns u which must be koeff by largest of two given numbs 
         u, v = v, u                            #so we make "u" koeff by "nums[0]" and "v" koeff by "nums[1]" at any possible situation
    left.append(u)
    left.append(v)

    for k in range(2, len(nums)):               #k - current rightest number`s(like "c" in example) index( 0th and 1th are watched)            
        u, v, gcd = adv_GCD(gcd, nums[k])
                    
        
        if nums[k] > gcd:                       #adv_GCD returns u which must be koeff by largest of two given numbs 
         u, v = v, u                            #so we make "u" koeff by "gcd" and "v" koeff by "nums[k]" at any possible situation
        for j in range(len(left)):
            left[j] *= u                        #"u" is multiplying koeff for next(going left) brakets pair
        left.append(v)                          #adding new element that`ll be multiplyed as the rest part of "left" in the next loop
        
    return left, gcd                       
         




#--------MAIN









if __name__ == "__main__":    #Благодаря этой пров-ке, написанное ниже будет выполнено только при запуске этой программы и не будет выполнено при импортивовании в другую программу(как библиотека)

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


'''
 82 42
82 = 42*1 + 40
42 = 40*1 + 2   => deviders: [None, 1, 1, 20]
40 = 2*20 + 0
'''


