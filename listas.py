#colecciones
#listas
#[item1,item2,item_n]

my_list =[1,"dos", 3.14, True]

my_list.append("new item")
my_list.remove(1)
print(my_list.pop())
print(my_list.reverse())

#indexing
print(my_list[3])
my_list[0]="cambia valor"
print(my_list)

other_list =[3,1,4,8,2,6,4]
print(other_list)
other_list.sort()
print(other_list)

#slicing
print(other_list[:3])
print(other_list[3:])