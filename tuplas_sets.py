 #mas colecciones en python 

#tuplas
#(item1,item2,item3)
#
#listas son mutables 
#tuplas inmutables

my_typle =(1,"dos",3.1,True)  
print(type(my_tuple))
print(my_tuple)
print(typemy_tuple[0])
print(my_tuple[-1])
#error
# my_tuple [0] ="algo mas"

# conjunto sets  
# desordenado
# mutable
# no permite duplicados
my_set = {"uno","dos","tres","uno"}
print(type(my_set))
print(my_set)
my_set.add(4)
print(my_set)

a = {1,2,3,4}
b = {3,4,5,6}
print(a.union(b))
print(a.intersection(b))
