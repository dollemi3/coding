
# print("hello coding python")
# print("string")
# print("these are sentences")
# print("start code programming..")

# print(".\n"*10)
# print("success!")
# print("예제 문장")
# print("\"나는 롤을 잘한다\"라고 하라고 했다.")
# print("""그냥 줄바꿈을 보기위해 쓰는 아무런 의미없는 문장이다
# 진짜 잘 되는거 같다
# 개쩐다""")
# print("""\
# \로 줄바꿈을 선언하지 않는다고 한다
# 솔직히 의미가 있는지는 잘 모르곘다.\
#     이렇게 하면 줄이 안 바뀌는건가?
#     \
# 역시 개쩐다
# """)
# print("인덱싱에 대해 araboza")
# print("인덱싱"[0],"인덱싱"[1],"인덱싱"[2])

# print("인덱싱"[-1],"인덱싱"[-2],"인덱싱"[-3])

#print("글자수부족으로대충때운문장"[3:9])
#print("글자수부족으로대충때운문장"[:9])
# print("글자수부족으로대충때운문장"[3:])

# print("이건 몇글자인가 알려주십쇼 =",len("이건 몇글자인가 알려주십쇼"))

# string_a = input("숫자를 입력하십시오 = ")
# int_a = int(string_a)
# string_b = input("숫자를 입력하십시오 = ")
# int_b = int(string_b)

# print("합산값 = ",int_a+int_b)


# a = 25000
# b = 136
# format_a = "현재 잔고 = {}".format(a)
# format_b = "파이썬 진행상황 {}P 'format 함수'".format(b)
# print(format_a,"\n",format_b)
# print("경로변환체크")
# a = input("경로가 변경되었습니까?=")
# if (a == "yes"):
#     print("success!")
# elif(a == 'no'):
#     print("fail..")
# else:
#     print("명령어를 확인하십시오.")
#######################################################################################################################

#a = "hello python programming"
#a.upper()
#print(a.upper())
#print(a.lower())
#print("Train10".isalnum())
#print("10".isdecimal())

#a = "split_point1 split_point2 split_point3 split_point4".split(" ")
#print(a)

#b = " 3 + 4 = " +str(3+4)
#print(b)

#c = "3 + 4 = {}".format(3+4)


#list_a = [1,2,3]
#list_a.append(4)
#list_a.append(5)
#list_a.insert(5,6)
#list_a.extend([7,8,9])
#print(list_a)


#list_a = [0,1,2,3,4,5]
#del list_a[1]
#print("del list_a[1]: ", list_a)

#list_b = [0,1,2,3,2,5]
#list_b.pop(2)
#print("pop(2):",list_b)

#list_c = [0,1,2,3,4,5]
#del list_c[2:5]
#print("del list_c[2:5]:",list_c)

#list_d = [2,1,2,3,4,2]

#for i in range(3):
#    list_d.remove(2)    
#print("list_d.remove(2):",list_d)

#list_d.clear()
#print(list_d)

#list_e = [12,52,64,69,85,19]
#list_e.sort(reverse=False)
#print(list_e)

#list_e.sort(reverse=True)
#print(list_e)

#list_of_list = [
#    [1,2,3],
#    [4,5,6,7],
#    [8,9]
#]

#for items in list_of_list:
#    for item in items:
#        print(items)

#a = [1,2,3,4]
#b = [*a,*a]
#print(b)

#numbers = [273,103,5,32,65,9,72,800,99]
#for number in numbers:
#    if(number >= 100 ):
#        print("100 이상 :",number)
#for number in numbers:
#    if(number%2 == 0):
#        print(number,"짝수입니다")
#    if(number%2 != 0):
#        print(number,"홀수입니다")
#for number in numbers:
#    print(number,"는",len(str(number)),"자릿수입니다")

# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]
# for number in numbers:
#     output[(number+2)%3].append(number)
# print(output)
#####################################################################################
# for i in range(0,len(numbers) // 2):
#     j = (i*2+1)
#     print(f"i = {i},j = {j}")
#     numbers[j] = numbers[j]**2
# print(numbers)

# dict_a = {
#     "name":"avengers",
#     "type":"hero_movie"
# }

# print(dict_a["type"])

# dict_b = {
#     "director":["anthony_luso","joe_luso"],
#     "cast":["iron_man","thanos","thor","Dr_strange","hulk"]
# }

# print(dict_b["cast"])

# dictionary = {
#     "name":"7D 건조 망고",
#     "type":"당절임",
#     "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
#     "origin":"필리핀"

# }


# dictionary["price"] = 5000

# print("name:",dictionary["name"])

# print("type:",dictionary["type"])

# print("ingredient:",dictionary["ingredient"])

# print("origin:",dictionary["origin"])

# print("price:",dictionary["price"])

# print(dictionary)   

# print()

# dictionary["name"] = "8D 건조 망고"
# print(dictionary["ingredient"][2])

# print("name:",dictionary["name"])

# del dictionary["ingredient"]

# tuple_universary_freshman = ("김기태",1,2)

# print(tuple_universary_freshman[0])

# def call_10_times(func):
#     for i in range(10):
#         func()

# def print_hello():
#     print("hello")

# call_10_times(print_hello)

# def power(item):
#     return item*item

# def under_3(item1):
#     return item1 < 3

# list_input_a = [1,2,3,4,5]
# output_a = map(power,list_input_a)
# print("map(power, list_input_a):",output_a)
# print("map(power, list_input_a):",list(output_a))

# output_b = filter(under_3,list_input_a)

# print("under_3,list_input_b:",output_b)
# print("under_3,list_input_b:",list(output_b))

# power = lambda x: x*x
# under_3 = lambda x: x<3

# list_input_a = [1,2,3,4,5]

# output_a = map(power,list_input_a)
# print("map(power,list_input_a):",output_a)
# print("map(power,list_input_a):",list(output_a))

# output_b = filter(under_3,list_input_a)
# print("filter(under_3,list_input_a):",output_b)
# print("filter(under_3,list_input_a):",list(output_b))

# file = open("basic.txt","w")

# file.write("test")

# file.close()

#import random

# hanguls = list("가나다라마바사아자차카타파하")

# with open("info.txt","w") as file:
#     for i in range(1000):
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40,100)
#         height = random.randrange(140,200)
#         file.write("{},{},{}\n".format(name,weight,height))


# with open("info.txt","r") as file:
#     for line in file:
#         (name,weight,height) = line.strip().split(",")

#         if ( not name ) or (not weight) or (not height):
#             continue

#         bmi = int(weight) / ( (int (height) / 100 ) **2 )
#         result = ""
        
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상체중"
#         else:
#             result = "저체중"

#         print('\n'.join([
#             "이름: {}",
#             "몸무게: {}",
#             "키: {}",
#             "bmi: {}",
#             "결과: {}",
#         ]).format(name,weight,height,bmi,result))
#         print()

# for i in range(10):
# 	list = {random.randrange(3,9)}
    
# if (3 in list):
# 	print("3이 출력 되었습니다")
# elif(4 in list):
# 	print("4가 출력 되었습니다")
# elif(5 in list):
# 	print("5가 출력 되었습니다")
# elif(6 in list):
# 	print("6이 출력 되었습니다")
# elif(7 in list):
# 	print("7이 출력 되었습니다")
# elif(8 in list):
# 	print("8이 출력 되었습니다")

# def test():
#     print("A지점 통과")
#     yield 1
#     print("B지점 통과")
#     yield 2
#     print("C지점 통과")
#     yield 3
# output = test()
# print("D지점 통과")
# a = next(output)
# print(a)
# print("E지점 통과")
# b = next(output)
# print(b)
# print("F지점 통과")
# c = next(output)
# print(c)

# books = [{
#     "제목": "혼자 공부하는 파이썬",
#     "가격": "18000"
# },{
#     "제목": "혼자 공부하는 머신러닝 + 딥러닝",
#     "가격": "26000"
# },{
#     "제목": "혼자 공부하는 자바스크립트",
#     "가격": "24000"
# }]

# def 가격추출함수(book):
#     return book["가격"]

# print("#가장 저렴한 책")
# print(min(books, key = lambda book: book["가격"])) 가격추출함수 없어도 됨 ㄷㄷ
# print()
# print("#가장 비싼 책")
# print(max(books, key = lambda book: book["가격"]))
# #############################################################################
# print("가격 오름차순 정렬")
# books.sort(key = lambda book : book["가격"])
# for book in books:
#     print(book)

# numbers = [1,2,3,4,5,6]

# print("::".join(map(str,numbers)))

numbers = list(range(1,10+1))
print("#홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1,numbers)))
print()

print("#3이상 7미만 추출하기")
print(list(filter(lambda x: 3 <= x < 7,numbers)))
print()

print("#제곱해서 50 미만이 되는수 추출하기")
print(list(filter(lambda x: x**2 <50,numbers)))