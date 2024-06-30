#using lambda as expression 

def upperLowerCase2(mystr : str) -> str:
    return "".join([(lambda i: mystr[i].upper() if (i % 2 == 0) else mystr[i].lower())(i) for i in range(len(mystr))])

upperLowerCase2("test")


#prime check

#a > sq rt N = b <sq rt N


#smallest positive number that can be divided by 1-20. - LCM - least common factor

def gcd (a : int, b : int) -> int:
    if a % b == 0:
        return b
    return gcd (b, a%b)

print (gcd(10,15))

def lcm2(a:int, b:int) -> int:
    return (a * b) // gcd(a,b)

def lcm(nums : list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return lcm2(nums[0], nums[1])
    else:
        return lcm([lcm2(nums[0], nums[1])] + nums[2:]) # nums[2:] remainign list



def alpha (ns: list[int]) -> int:
    if len(ns) == 0:
        return 0
    elif len(ns) == 1:
        return ns[0]
    else:
        return ns[0] +alpha (ns[1:])
    


    #reduce will take a collection and a function (2 args of same type) and produced a new collection



from functools import reduce as fold

def lcm(nums : list[int]) -> int:
    return fold(lcm2, nums)

import functools as ft

def gcd (a : int, b : int) -> int:
    if a % b == 0:
        return b
    return gcd (b, a%b)

def lcm2(a:int, b:int) -> int:
    return (a * b) // gcd(a,b)




    
