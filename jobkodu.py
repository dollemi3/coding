a = input("수식을 입력해 주십시오. = ")
print(a)
b = len(a)
print(b)
list_a = list(a)
print(list_a)
if ( "+" in list_a ):
    location = list_a.index("+")
    
    list_a.remove("+")
    wjdtn = list(map(int,list_a))
    left = (list_a[:location])
    right = (list_a[location:])
    print(left,right)
    
    wjdtn = list(map(int,left))
    wjdtn1 = list(map(int,right))
    
    result = wjdtn+wjdtn1
    print(result)