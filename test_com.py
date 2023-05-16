from email import header
import time
import datetime 
import math
import numpy as np
import matplotlib.pyplot as plt
from newspaper import Article
from konlpy.tag import Kkma
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np
         
timee = 0.1
def delay(a):
    time.sleep(a)
now = datetime.datetime.now()

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
        

from ast import Continue, main
i = 5
a = int(input("Enter the password = "))
for i in range (5):
    if (a == 7675):
        print("unlocked")
        for i in range (3):
            delay(0.5)
            print(".")
        break
    elif(a != 7675):
        print("failed")
        
        delay(1)
        print(".")
        print("password incorrect")
        
        delay(2)
        print(".")
        a = int(input("Enter the password = "))


for i in range (3):
    delay(1)
    print(".")

print("----------------------------------------------------------------------------------------")
delay(timee)
print("-                                                                                      -")
delay(timee)
print("-       hh            eeeeeeeee    ll           ll               oo                    -")
delay(timee)
print("-       hh            ee           ll           ll             oo  oo                  -")
delay(timee)
print("-       hh            ee           ll           ll            oo    oo                 -")
delay(timee)
print("-       hhhhhhhhhhh   eeeeeeeee    ll           ll           oo      oo                -")
delay(timee)
print("-       hh       hh   ee           ll           ll            00    00                 -")
delay(timee)
print("-       hh       hh   ee           ll           ll             00  00                  -")
delay(timee)
print("-       hh       hh   eeeeeeeee    lllllllllll  llllllllll       00                    -")
delay(timee)
print("-                                                                                      -")
delay(timee)
print("----------------------------------------------------------------------------------------")

print("language list")
delay(1)
print("korean (kr)")
delay(1)
print("english (en)")
  
l = input("language setting = ")
if (l == "kr"):
    print("setting..korean")
    delay(3)
    print("설정이 완료돠었습니다.")
    delay(1)
    while True:
        command = input("명령을 내려주십시오. 명령어를 확인 하려면 '도움'을 입력하세요 = ")
        if (command == "도움"):
            print("시계 [현재 시간을 표시합니다.]")
            print("뉴스 [링크를 이용하여 뉴스의 요약본을 표시합니다.] ")
            print("환율 [현재 선택 나라의 환율을 표시합니다.]")
            print("주식 [현재 선택 주식의 상황을 표시합니다.]")
            print("계산기 [ 입력받은 숫자를 명령에 맞추어 계산합니다.]")
            print("진법 변환기 [ 입력받은 명령과 숫자를 이용해 진법을 변환합니다 ]")
        if (command == "진법 변환기"):
            ari_cal()

        if (command == "계산기"):
            
            print("――――무엇을 하시겠습니까?―――――――")
            print("｜        사칙연산             ｜")
            print("｜        삼각함수             ｜")
            print("｜        제곱▣               ｜")
            print("｜        제곱근               ｜")
            print("｜        함수▣▣ 업데이트중   ｜")
            print("｜        수열▣▣ 업데이트중   ｜")
            print("―――――――――――――――――――――――――――――――")
            #####################################################
            b = input("무슨 작업을 하시겠습니까? = ")
            if ( b == "사칙연산" ):
                print("――――――작업목록―――――――――――――")
                print("｜         더하기         ｜")
                print("｜         빼기▣         ｜")
                print("｜         곱하기         ｜")
                print("｜         나누기         ｜")
                print("―――――――――――――――――――――――――――")
                c = input ( " 어떤 연산을 하시겠습니까? = ")
                if( c and "더하기" == "더"):
                    e = float(input('첫번째 숫자를 입력하세요 = '))
                    f = float(input("두번째 숫자를 입력하세요 = "))
                    print("결과값 = ",(e+f))

                if( c and "빼기" == "빼"):
                    e = float(input('첫번째 숫자를 입력하세요 = '))
                    f = float(input('두번째 숫자를 입력하세요 = '))
                    print("결과값 = ",(e-f))

                if( c and "곱하기" == "곱"):
                    e = float(input('첫번째 숫자를 입력하세요 = '))
                    f = float(input('두번째 숫자를 입력하세요 = '))
                    print("결과값 = ",(e*f))

                if (c and "나누기" == "나"):
                    e = float(input('첫번째 숫자를 입력하세요 = '))
                    f = float(input('두번째 숫자를 입력하세요 = '))
                    print("결과값 = ",(e/f))
                
            #############################################################
            if(b == "삼각함수"):
                a = int(input("밑변을 입력 해주십시오 = "))
                b = int(input("높이를 입력 해주십시오 = "))
                PI = 3.1415926535
                qus_c = (a * a) + (b * b)
                c = math.sqrt(qus_c)
                angle = (math.atan2(a, b) * (180 / PI))
                if (a >= b):
                    print("빗변 길이 = ", c)
                    print("빗변과 밑변사이의 각도 = ", angle)

                print("빗변 길이 = ", c)
                print("빗변과 밑변사이의 각도 = ", 90-angle)

            ##############################################################

            if(b=="제곱"):
                a = int(input("제곱할 숫자 = "))
                b = int(input("지수 = "))
                print(a ** b)
            ##############################################################
            if(b=="제곱근"):
                a = int(input("밑 = "))
                b = int(input("진수 = "))
                print(a ** (1/b))
            ##############################################################
            if( b == "수열"):
                print("업데이트중")
            if(b == "함수"):
                a = input("몇차 함수식 입니까? = ")
                print("일차/이차")
                if(a == '일차'):
                    x = int(input("X 좌표의 시작점을 입력하세요 = "))
                    x1 = int(input("X 좌표의 끝을 입력하세요 = "))
                    y = int(input("Y 좌표의 시작점을 입력하세요 = "))
                    y1 = int(input("Y 좌표의 끝을 입력하세요 = "))
                    X = np.arange(x, x1, 0.01)
                    Y = np.arange(y, y1, 0.01)

                    plt.title('graph of a function')
                    plt.xlabel('X-coordinate')
                    plt.ylabel('Y-coordinate')
                    plt.grid(True)
                    plt.axis([x, x1, y, y1])
                    plt.plot([x, x1], [y, y1], 'r')
                    plt.annotate('origin', xy=(-1, -1), xytext=(0, 0), size=10)

                    plt.show()

        if (command == "뉴스"):
            
            class SentenceTokenizer(object):
                def __init__(self):
                    self.kkma = Kkma()
                    self.twitter = Okt()
                    self.stopwords = ['중인' ,'만큼', '마찬가지', '꼬집었', "연합뉴스", "데일리", "동아일보", "중앙일보", "조선일보", "기자"
                        ,"아", "휴", "아이구", "아이쿠", "아이고", "어", "나", "우리", "저희", "따라", "의해", "을", "를", "에", "의", "가",]
                def url2sentences(self, url):
                    article = Article(url, language='ko')
                    article.download()
                    article.parse()
                    sentences = self.kkma.sentences(article.text)
                    
                    for idx in range(0, len(sentences)):
                        if len(sentences[idx]) <= 10:
                            sentences[idx-1] += (' ' + sentences[idx])
                            sentences[idx] = ''
                    
                    return sentences
            
                def text2sentences(self, text):
                    sentences = self.kkma.sentences(text)      
                    for idx in range(0, len(sentences)):
                        if len(sentences[idx]) <= 10:
                            sentences[idx-1] += (' ' + sentences[idx])
                            sentences[idx] = ''
                    
                    return sentences

                def get_nouns(self, sentences):
                    nouns = []
                    for sentence in sentences:
                        if sentence != '':
                            nouns.append(' '.join([noun for noun in self.twitter.nouns(str(sentence)) 
                                                if noun not in self.stopwords and len(noun) > 1]))
                    return nouns

            class GraphMatrix(object):
                def __init__(self):
                    self.tfidf = TfidfVectorizer()
                    self.cnt_vec = CountVectorizer()
                    self.graph_sentence = []
                    
                def build_sent_graph(self, sentence):
                    tfidf_mat = self.tfidf.fit_transform(sentence).toarray()
                    self.graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)
                    return  self.graph_sentence
                    
                def build_words_graph(self, sentence):
                    cnt_vec_mat = normalize(self.cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
                    vocab = self.cnt_vec.vocabulary_
                    return np.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word] : word for word in vocab}

            class Rank(object):
                def get_ranks(self, graph, d=0.85): # d = damping factor
                    A = graph
                    matrix_size = A.shape[0]
                    for id in range(matrix_size):
                        A[id, id] = 0 # diagonal 부분을 0으로 
                        link_sum = np.sum(A[:,id]) # A[:, id] = A[:][id]
                        if link_sum != 0:
                            A[:, id] /= link_sum
                        A[:, id] *= -d
                        A[id, id] = 1
                        
                    B = (1-d) * np.ones((matrix_size, 1))
                    ranks = np.linalg.solve(A, B) # 연립방정식 Ax = b
                    return {idx: r[0] for idx, r in enumerate(ranks)}

            class TextRank(object):
                def __init__(self, text):
                    self.sent_tokenize = SentenceTokenizer()
                    
                    if text[:5] in ('http:', 'https'):
                        self.sentences = self.sent_tokenize.url2sentences(text)
                    else:
                        self.sentences = self.sent_tokenize.text2sentences(text)
                    
                    self.nouns = self.sent_tokenize.get_nouns(self.sentences)
                                
                    self.graph_matrix = GraphMatrix()
                    self.sent_graph = self.graph_matrix.build_sent_graph(self.nouns)
                    self.words_graph, self.idx2word = self.graph_matrix.build_words_graph(self.nouns)
                    
                    self.rank = Rank()
                    self.sent_rank_idx = self.rank.get_ranks(self.sent_graph)
                    self.sorted_sent_rank_idx = sorted(self.sent_rank_idx, key=lambda k: self.sent_rank_idx[k], reverse=True)
                    
                    self.word_rank_idx =  self.rank.get_ranks(self.words_graph)
                    self.sorted_word_rank_idx = sorted(self.word_rank_idx, key=lambda k: self.word_rank_idx[k], reverse=True)
                    
                    
                def summarize(self, sent_num=3):
                    summary = []
                    index=[]
                    for idx in self.sorted_sent_rank_idx[:sent_num]:
                        index.append(idx)
                    
                    index.sort()
                    for idx in index:
                        summary.append(self.sentences[idx])
                    
                    return summary
                    
                def keywords(self, word_num=10):
                    rank = Rank()
                    rank_idx = rank.get_ranks(self.words_graph)
                    sorted_rank_idx = sorted(rank_idx, key=lambda k: rank_idx[k], reverse=True)
                    
                    keywords = []
                    index=[]
                    for idx in sorted_rank_idx[:word_num]:
                        index.append(idx)
                        
                    #index.sort()
                    for idx in index:
                        keywords.append(self.idx2word[idx])
                    
                    return keywords
            a = input("뉴스 링크를 입력 하세요= ")
            url = a
            print("")
            textrank = TextRank(url)
            for row in textrank.summarize(3):
                print(row)
                print()
            print('keywords :',textrank.keywords())
            print("뉴스 링크 = ",a)

        if (command == "환율"):
            print("업데이트중")

        if (command == "주식"):
            print("업데이트중")

        if (command == "시계"):
            now = datetime.datetime.now()
                
            # while True:
            print("현재 시간은 {}년 {}월 {}일 {} 시 {} 분 {}초 입니다.".format(now.year,now.month,now.day,now.hour,now.minute,now.second))
            delay(1)

        continue    
        


if (l == "en"):
    print("setting preserve.. ")
    delay(1)
    while True:
        command = input("please order commander.")
        if (command == "clock"):
            now = datetime.datetime.now()
                
            # while True:
            print("now is {}year {}month {}day {} hour {} minute {}second.".format(now.year,now.month,now.day,now.hour,now.minute,now.second))
            delay(1)
        

        continue

if (l != "kr"  or "en"):
    print("bug!")

