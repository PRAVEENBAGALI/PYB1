a = [1,2,3,4,5]
for i in a:
    print(i,end="\t")  #print the list with tab seperated list with tab seperation

print("\n")
a1 = [1,2,3,4,5,6]
for i in a:
    print(i)  #print the list
print("\n")

a2 = [1,2,3,4,5]
print(*a2, sep="/")
print("\n")

a3 = [5,6,7,8]
for i in range(len(a3)):
    print(a3[i])
print("\n")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append("pineapple")
print(fruits)

vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
vegetables.insert(2,"Lfinger")
print(vegetables)

animal_products = ['milk', 'meat', 'butter', 'yoghurt']
animal_products.sort(reverse=True)
print(animal_products)

numbers = [1,2,3,6,7,2,3,4]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print(fruits)
fruits.count("Potato")

