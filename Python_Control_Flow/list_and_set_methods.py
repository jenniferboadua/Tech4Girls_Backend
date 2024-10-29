#!/usr/bin/python3

list6 = ['Dami', 'Toyosi', 'Chinwe', 'Zion']

#to append
list6.append('Ruthie')
print(list6)

#to remove
list6.remove('Zion')
print(list6)

#to pop
list6.pop()
print(list6)

#to sort
print(list6.sort())
print(list6)

#to reverse
list6.reverse()
print(list6)

#to extend
list7=(1, 2, 3, 4)
print(list6.extend(list7))
print(list6)

my_favs={'Wanni', 'Handi', 'Kassia', 'Victoria', 'Nelly'}
#to add in sets
my_favs.add ('Anita')
print(my_favs)

#to remove
my_favs.remove ('Wanni')
print(my_favs)

#to demonstrate union
my_other_fav={'Kelly','Ocee', 'Ozee', 'Sooj'}
print(my_favs.union(my_other_fav))

#to demonstrate intersection
print(my_favs.intersection(my_other_fav))

#to demonstrate difference
print(my_favs.difference(my_other_fav))


