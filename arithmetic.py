# 0x = HEX (16진법)
# 0o = octal(8진법)
# bin() = 2진법     oct() = 8진법       hex() = 16진법
# format 내장함수 사용법    EX: b = format(value,'#b') ==> 0b~~~~    ---\
#                              o = format(value,'#o') ==> 0o~~~     ----------- 3개 모두 #을 빼고 쓰면 0b,0o,0x가 사라진다
#                              h = format(value,'#x') ==> 0x~~~~    ---/
# format 을 사용한 진수 변환 (EX)  s = "2진수: {0:#b}, 8진수: {0:#o}, 10진수: {0:#d}, 16진수: {0:#x}".format(60)  
####################################################################################################################
import time
timee = 0.1
def delay(a):
    time.sleep(a)


def ari_cal():
    print("the maximun range is 3")
    num = input("type your counting = ")
    if (num=='1'):
        print(" please choose for translation")
        print("hex = (1)\n","oct = (2)\n","bin = (3)\n")
        a = input(" please choose your arithmetic : ")
        delay(1)
        b = int(input(" please type you want to for translating : "))
        if (a == '1'):
            print("the result is : ",hex(b))
        if (a == '2'):
            print("the result is : ",oct(b))
        if (a == '3'):
            print("the result is : ",bin(b))
    if ( num == '2'):
        print("anding  = &")
        print("oring = | ")
        a = input("please choose your work = ")
        if (a == '&'):
            b = int(input("please type the first number = "))
            c = int(input("please type the second number = "))
            print("writing..\n",".\n",".\n",".\n",".\n")
            print("hex = (1)\n","oct = (2)\n","bin = (3)\n")
            ari = input(" please choose your arithmetic : ")
            if (ari == '1'):
                result = b & c
                resulting = format(result,'#x')
                print("the result is = ",resulting)

            if (ari == '2'):
                result = b & c
                resulting = format(result,'#o')
                print("the result is = ",resulting)
                
            if (ari == '3'):
                result = b & c
                resulting = format(result,'#b')
                print("the result is = ",resulting)
        if (a == '|'):
            b = int(input("please type the first number = "))
            c = int(input("please type the second number = "))
            print("writing..\n",".\n",".\n",".\n",".\n")
            print("hex = (1)\n","oct = (2)\n","bin = (3)\n")
            ari = input(" please choose your arithmetic : ")
            if (ari == '1'):
                result = b | c
                resulting = format(result,'#x')
                print("the result is = ",resulting)

            if (ari == '2'):
                result = b | c
                resulting = format(result,'#o')
                print("the result is = ",resulting)
                
            if (ari == '3'):
                result = b | c
                resulting = format(result,'#b')
                print("the result is = ",resulting)


                
    else:
        print("you type the wrong range")
        
ari_cal()
            
        
    


# result = 0xB3 & 0xC2
# #B3 == 1011 0011 /// C2 == 11000010
# #      1000 0010
# resulted = format(result, 'x')
# print("result = ",resulted)

# results = "16진서: {0:x}".format(result)
# print("results = ",results)



# #1000 0011