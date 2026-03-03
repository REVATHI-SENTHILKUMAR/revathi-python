#list datatype

elements = [ 10, 20,30,40,50 ]

#printing all elements together
print( ' elements ' , elements )


#printing elements one by one using for loop
for elmnt in elements:
    print( ' for ', elmnt )


#printing elements one by one using while loop
count = 0

while count<5:
    print( ' while ', elements[count] )
    count+=1

    


# different datatypes are allowed
elements = [ 10, 20,30, 'arjun', 10.5, True ]
print( ' elements ' , elements )




# duplicates  are allowed
elements = [ 10, 20,30, 'arjun', 10.5, 10,20,30 ]
print( ' elements ' , elements )


#index is supported
elements = [ 10, 20,30, 'arjun', 10.5, 10,20,30 ]
result = elements[0] + elements[5]
print( result )


# ordered collection
elements=[10,20,30,40,50]
print( elements )


#tuple
elements = ( 10,20,30,40,50 )

print( elements )


for elmnt in elements:
    print(' for ', elmnt )

count = 0
while count<len(elements):
    print( ' while ', elements[count] )
    count+=1


elements = ( 10,20,30,40,50 )

#elements.append(60) #error
#elements.insert(1,15) #error
#elements.add(60) #error

print( elements )
elements[0]=100 #error
print( elements )
