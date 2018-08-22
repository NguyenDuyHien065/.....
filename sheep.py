size = [5 ,7 ,300 , 90 ,24 ,50 ,75]
print("Hello , my name is Hien and these are my sheep size")
print(size)
print("Now my biggest ship has size", max(size), "let's shear it")
max_index = size.index (max(size))
size[max_index] = 8
print ("After shearing , here is my flock")
print(size)

for i in range (1,7):
    print("Month",i)
    size = [x + 50 for x in size]
    print("One month has pass, now here is my flock")
    print (size)
    print("Now my biggest ship has size", max(size), "let's shear it")
    max_index = size.index(max(size))
    size[max_index] = 8
    print("After shearing , here is my flock")
    print(size)
size_total = sum(size)
print("My flock has size in total:",size_total)
earn = size_total * 2
print("I would get:",earn , "$")
