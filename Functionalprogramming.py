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
print(is_perfect_square(16))

#lambdas

def is_perfect_cube(n:int) ->int:
    return inv(lambda x:x * x * x, n)           

print(is_perfect_cube(27)) 


sqr = lambda k: k*k

#print(sqr)

g = lambda a,b : a if a > b else b-1

g(6,7)
#print(g)
g (12,7)
#print(g) 



def is_perf_cube(n: int) -> int:
    return inv(lambda x: x*x*x, n)

g = lambda a, b: a-b
g(6,7)

m = [0,1,1,2,3,5, 8, 13 , 21, 34, 55, 89]

#find all fibanocci numbers which are even

is_even = lambda x: x%2 == 1
print(filter(is_even, m))

print(list(filter(is_even, m)))



y = filter(lambda x: x % 5 == 0, m)
print(sum(y))
print(sum(y))




#Make an iterator that computes the fucntion using arguments from each iterable. STop when shortest iterable is exahauted

m = [0,1,1,2,3,8,13,21,34,55,89]

list(map(lambda a: a+2 , m))
list(map(lambda x: x% 2 == 0, m))

list (map(lambda x: x+1, filter(lambda z: z% 2 ==0,m)))

#list comprehension - filter after a map

f = lambda x : x+1
g = lambda x : x % 2 == 0
print([f(p) for p in m if g(p)])