###################### Lab1 ###############
###### Ex1_Draw diamond with python language #########

n = 9
space = (n-1) // 2
for  i in range(1,n+1,2):
  print((space * " ")+(i * "*")+(space * " "))
  space = space - 1 
space = 1
for x in range(n-2,0,-2):
  print((space * " ")+(x * "*")+(space * " "))
  space = space +1
  
######Ex2_Draw diamond with python language with function ######### 
  
def dia(n):
  space = (n-1) // 2
  for  i in range(1,n+1,2):
    print((space * " ")+(i * "*")+(space * " "))
    space = space - 1 
  space = 1
  for y in range(n-2,0,-2):
    print((space * " ")+(y * "*")+(space * " "))
    space = space +1
 
dia(9)

#####Ex4_Summation of harmonic series #########

def sum(n):
     
    if n < 2:
        return 1
 
    else:
        return 1 / n + (sum(n - 1))
             
print("Limit = 1, value = ", (sum(1)))
print("Limit = 2, value = ", (sum(2)))
print("Limit = 3, value = ", (sum(3)))
print("Limit = 4, value = ", (sum(4)))
print("Limit = 5, value = ", (sum(5)))
print("Limit = 6, value = ", (sum(6)))
print("Limit = 7, value = ", (sum(7)))
print("Limit = 8, value = ", (sum(8)))
print("Limit = 9, value = ", (sum(9)))
print("Limit = 10, value = ", (sum(10)))

###### Ex3_Find prime number and odd or even number by recursive function #########
