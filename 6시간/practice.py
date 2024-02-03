# from random import *
# date = randint(4, 28)
# print("오프라인 스터이 모임은 매월 ", str(date), " 입니다.")

# 문자열
# sen = """
# 나는 바보이고,
# 파이썬은 쉽다 
# """
# print(sen)

#슬라이싱
# jumin = "991234-1231232"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 부터 2직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 처음부터 
# print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지6직전까지 
# print("뒤 7자리 (뒤에서부터)" + jumin[-7:]) # 맨 뒤에서 7번째 끝까지

#문자열 처리 함수
# text = "ABCD efgC"
# print(text.lower())
# print(text.upper())
# print(text[0].isupper())
# print(len(text))
# print(text.replace("ABCD", "룰루"))

# index = text.index("C")
# print(index)
# index = text.index("C", index + 1)# a 다음부터 찾게 2번째 a 찾도록
# print(index)
# print(text.find("바보"))# find 를 사용하면 없으면 오류대신 -1 출력
# print(text.count("C"))

# 문자열
# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아합니다" % "파이썬")
# print("apple 은 %c로 시작해요" % "a")
# print("나는 %s색과 %s색을 좋아해요" % ("빨강", "파랑"))
# 방법2
# print("난 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("빨강","파랑"))
# print("나는 {0}색과 {1}색을 좋아해요".format("빨강","파랑"))
# print("나는 {1}색과 {0}색을 좋아해요".format("빨강","파랑"))
# 방법3
# print("나는 {age}살이며 {color}색을 좋아해요".format(age = 20, color = "파랑"))
# print("나는 {age}살이며 {color}색을 좋아해요".format(color = "파랑", age = 20))
# 방법4
# age = 20
# color = "빨강"
# print(f"나는 {age}살이며 {color}색을 좋아해요")

# 사이트별로 비밀번로 만들어주는 프로그램
#print(input("입력 : "))
# domain = "http://naver.com"
# print(domain[7:])
# domain2= domain.index(".")
# print(domain2)
# print(domain[7:domain2])
# domain_id = domain[7:domain2]
# print(len(domain_id))
# print("id는 : %s%s%s%s" % (domain_id[0:3],len(domain_id),domain_id.count("e"),"!"))

#정답
# url = "http://naver.com"
# my_str = url.replace("http://", "") # 규칙1 http:// 부분 제외
# #print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2 처음 만나는 점 이후 부분은 제외
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는{1}입니다".format(url,password))

# 리스트[]
# 지하철 칸 별 10, 20, 30
# subway = [10, 20, 30]
# print(subway)

#subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호는 몇 번째?
# print(subway.index("조세호"))

#하하 추가
# subway.append("하하")
# print(subway)

# 정형돈을 유재석 조세호 사이에
# subway.insert(1, "정형돈")
# print(subway)

#지하철 뒤에서 한명씩 꺼냄()
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람 몇 명 인지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,4,3,2,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 삭제
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5, 4, 3, 2, 1]
# mix_list = ["강우진", 20, True]
# #print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 사전 (key : value)

# cabinet = {3 : "강우진", 100 : "유재석"}
# print(cabinet[3])
# print(cabinet[100])# 키 값 없으면 오류 발생

# print(cabinet.get(3))# get은 값이 없어도 None 출력하고 계속실행

# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능 키"))
# print("hi")

# print(3 in cabinet) #True
# print(5 in cabinet) #False

# cabinet = {"A-20" : "강우진", "C-20" : "유재석"}
# print(cabinet["A-20"])
# print(cabinet["C-20"])

# print(cabinet)
# cabinet["A-20"] = "김종국"
# cabinet["V-40"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-20"]
# print(cabinet) 

# # key 만 value민출력  
# print(cabinet.keys())
# print(cabinet.values())

# # 쌍으로 출력
# print(cabinet.items())

# # 폐점(삭제)

# cabinet.clear()
# print(cabinet)

# 튜플 / 변경 불가능 리스트보다 속도 빠름
# menu = ("돈까스", "치스카츠")
# print(menu[0])
# print(menu[1])

# (name, age) = ("강우진", "25")
# print(name, age)

# 집합(set) / 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3} # 1,2,3
# print(my_set)

# java = {"유재석", "양세형", "김태호"}
# python = {"유재석", "강우진", "바보"}

# # 교집합
# print(java & python)
# print(java.intersection(python))

# # 합집합 (자바나 파이썬 둘중 하나라도 가능한 사람)
# print(java | python)
# print(java.union(python))

# # 차집합(자바는 가능 하지만 파이썬은 불가능)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는사람이 늘어남
# python.add("양세형")
# print(java)

# #java를 까먹음
# java.remove("유재석")
# print(java)

# 자료구조의 변경
# menu = {"커피", "주스", "우유"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# 추첨 프로그램 작성
# 조건 1 : 1 ~ 20 명 
# 조건 2 : 중복불가
# 조건 3 : random 모듈의 shuffle 과 sample 활용

#from random import *

# test = [1, 2, 3, 4, 5]
# print(test)
# shuffle(test)
# print(test)
# print(sample(test, 1))

# event = {1 : "1번입니다", 2: "2번입니다", 3 : "3번입니다", 4 : "4번입니다", 5 : "5번입니다"}
# id = event.keys()
# id = list(id)
# shuffle(id)
# chicken = sample(id, 1)
# print("치킨 당첨자는 : ",chicken)
# id = set(id)
# chicken = set(chicken)
# coffee = id.difference(chicken)
# coffee = list(coffee)
# shuffle(coffee)
# coffee = sample(coffee, 3)
# print("커피 당첨자는 :" , coffee)

# 정답
# users = range(1, 21) # 1부터 20
# #print(type(users))
# users = list(users)
# #print(type(users))
# #print(users)
# shuffle(users)
# winners = sample(users, 4)# 4명중 3명 커피, 1명 치킨

# print("-- 당첨자 발표 --")
# print("치킨 당첨자는 : {0}".format(winners[0]))
# print("커피 당첨자는 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")

# 분기
# temp = int(input("오늘 기온 : "))
# if 30 <= temp  :
#     print("날씨가 좋아요")
# elif 10 <= temp and temp < 30 : 
#     print("적당한 날씨")
# elif 0 <= temp < 10 :
#     print("외투를 챙기세요")
# else : 
#     print("나가지마세요") 

# 반복문 for

#randrange()
# for coffee in range(1, 6) :
#     print("{} 입니다".format(coffee))  

# coffee = ["아이언맨", "토르", "헐크"] 
# for coffee in coffee : 
#     print("{0}, 커피가 준비되었습니다".format(coffee))

# while 문

# customer = "토르"
# index = 5

# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다{1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("폐기 처분되었습니다.") 

# customer = "토르"
# person = "Uk"

# while customer != person :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 뭔가요? : ")
    

# absent = [2, 5] # 결석
# no_book = [7] # 책을 놓고옴
# for student in range(1, 11) :
#     if student in absent : 
#         continue # 다음 반복으로 실행시키는 것
#     elif student in no_book :
#         print("오늘 수업은 여기까지 {0}은 교무실로 따라와 ".format(student))
#         break # 바로 탈출
#     print("{0}, 야 책좀 읽어봐".format(student))
    
# 한줄 for 문
# 번호 앞에 100 붙이기
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

#이름을 숫자로 변환
# students = ["hi","Thor","I am groot"]
# students = [len(i) for i in students]
# print(students)

#대문자로 변환
# students = ["hi","Thor","I am groot"]
# students = [i.upper() for i in students]
# print(students)

#Quiz
from random import * 

count = "" # 손님 수 50 

sum = 0


#print(type(time), time)
for count in range(1, 51) :
    #time_ok =  sample(time, 1) # 승객별 운영시간 5 ~ 50 시간 랜덤값\
    time =randrange(5, 51) # 운행시간

    
    if 5 <= time <= 15 :
        print("{0}{1} 번째 손님 (소요시간 :{2})".format("[o]",count, time))
        sum = sum + 1
    else :
        print("{0}{1} 번째 손님 (소요시간 :{2})".format("[x]",count, time))
          
print(sum)
        
# 정답
# from random import *

# cnt = 0 # 총 승객 수
# time = randrange(5, 51)
# print(type(time))
# #for i in range(5, 51) :