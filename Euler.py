
# find sum of multiples of 3 and 5 till 100

limit = 1000;
sumMulti35 = 0;

for x in range(1,1000):
    if (x%3 ==0 or x%5 == 0):
        sumMulti35 +=x
print("first method")
print(sumMulti35)



def select(n:int) -> bool:
    return n%3 == 0 or n%5 ==0

def sumMulti35(limit:int) ->int:
    total = 0
    for n in range(1,limit):
        if select(n):
            total += n
    return total
print("second method")   
print(sumMulti35(1000))


#third method for multiples of 3 & 5 sum

def euler001_3(limit: int) -> int:
    return sum(range(3, limit, 3)) +\
           sum(range(5,limit, 5)) -\
           sum(range(15, limit, 15))
print("third method")   
print(euler001_3 (1000))


#fourth method for multiples of 3 & 5 sum

def multiples (of:int, upto:int) -> range:
    return range(of,upto,of)

def sumMulti35(limit:int) -> int:
    return sum(set(multiples(3,limit)) | set(multiples(5,limit)))
print("fourth method")  
print(sumMulti35(1000))


#fifth method for multiples of 3 & 5 sum

def sumMulti35(limit:int) -> int:
    return sum(filter(select, range(1,limit)))
print("fifth method")  
print (sumMulti35(1000))


#sixth method for multiples of 3 & 5 sum

def sumMulti35(limit:int) -> int:
    print("sixth method") 
    return sum([n for n in range(1,limit) if select(n)]) 
print (sumMulti35(1000))



 #functional programming way 

def alpha(n):
    r = 0
    while r*r*r < n:
        r+=1
    return r*r*r == n


 #function of function

def inv(f, n: int) -> bool:
    r = 0
    while f(r) < n:
        r += 1
    return f(r) == n

def power3(n: int) -> int:
    return inv(power3, n)

def square(n: int) -> int:
    return n* n

def is_perfect_square(n: int) -> bool:
    return inv(square, n)
is_perfect_square(16)
