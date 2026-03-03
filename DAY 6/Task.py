#tuple
elements = ( 10,20,30,40,50 )

print( elements )


for elmnt in elements:
    print(' for ', elmnt )

count = 0
while count<len(elements):
    print( ' while ', elements[count] )
    count+=1


tuple

elements = ( 10,20,30,40,50 )

#elements.append(60) #error
#elements.insert(1,15) #error
#elements.add(60) #error

print( elements )
elements[0]=100 #error
print( elements )
