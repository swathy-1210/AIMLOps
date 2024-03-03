#Dictionaries


print("how dictionaries are working")

carsposition = {"1":"Ford", "2":"Mercedes", "3": "Toyota"}
print(carsposition.keys())
print(carsposition.values())
print(carsposition["1"])



#filter , map and zip


def isEven(n):
    return n % 2 == 0


def square(n):
    return n * 2

#filter checks for boolean 

x= [10,20,30,40,50,60,70,80,90]
print(list(filter(isEven,x)))


#map
print(list(map(square,x)))

#zip

f = ["St1","St2","St3","St4","St5","St6","St7","St8","St9"]
h = [10.5,20.6,30.9,40,50,60,70,80,90]

print("how zip is working=")
print ( list(zip(f,h))) #if lists are of different length it will combine until the least length array
#produces tuples -- immutable value




#Mod is 0

x=53
flag = False
for i in range (0,x//53):
    if 53%2 == 0:
        flag = True
if(flag):
    print("Mod is zero")
else:
    print("what crap")



#slicing and reversing == image reversing

x= [10,20,30,40,50,60,70,80,90]
print (x[::-1]) # reverse with counter 1
print (x[::-2]) # reverse with counter 2

print("\r")   

print (x[-9:][::-2]) #starting reverse, counter 2

print("\r")   
print (x[-9:])



print("\r")   
print("\r")   
print("\r")   
print("\r")

#try except


#append and extend

f = [12,34,78,90]
print(f)
print(f.append(13))
print(f.append([21,31,45,67]))
print(f.extend([21,31,45,67]))
print(f)
print(f[2:6])
print(f[2:6:9])


#lists [] , tuples () , dictionaries {} -- collection data types in python

homoList =["Why", "The", "World", "Is", "Running","Behind", "AI"]
print(homoList[3])
heteroList = ["I", "dont", "have", 1, "worry", [0.09, "Going here"]]
print(heteroList[3][5]) #this fails why?



#concat

h = "Hello"
w = "World!"

print(h+w)
print(h+" "+w)
jumble = h*3+" "+w*2
print(jumble)

# in a string
print(h in w)



#while    
x = 0
while x < 2:
    x+=1
    print(x,x+2, sep = "::")
    print(x,x+2, end = "::")


confidenceScore = 94
if confidenceScore < 94 :
    print("\r")
    print("model not ready for production")
        #print("testing intendation") -- wil fail
    
else:
    print("\r")
    print("model is ready for production")

story = """ this is my story """ #multiple lines
#range 
print(list(range(0,11,3))) #3rd cannot be zero 

for x in range(10):
    if (x==3):
        continue

    if (x==5):
        break
    print (x)



