# from random import *
# date = randint(4, 28)
# print("오프라인 스터이 모임은 매월 ", str(date), " 입니다.")

# 문자열
# sen = """
# 나는 바보이고,
# 파이썬은 쉽다 
# """
# print(sen)

#슬라이싱===============================================
# jumin = "991234-1231232"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 부터 2직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 처음부터 
# print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지6직전까지 
# print("뒤 7자리 (뒤에서부터)" + jumin[-7:]) # 맨 뒤에서 7번째 끝까지

#문자열 처리 함수==============================================
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

# 문자열===================================================================
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

# 사이트별로 비밀번로 만들어주는 프로그램===================================================================
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

# 리스트[]===================================================================
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

# 사전 (key : value)===================================================================

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

# 튜플 / 변경 불가능 리스트보다 속도 빠름===================================================================
# menu = ("돈까스", "치스카츠")
# print(menu[0])
# print(menu[1])

# (name, age) = ("강우진", "25")
# print(name, age)

# 집합(set) / 중복 안됨, 순서 없음===================================================================
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

# 자료구조의 변경===================================================================
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

# 분기===================================================================
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
# from random import * 

# count = "" # 손님 수 50 
# sum = 0


# #print(type(time), time)
# for count in range(1, 51) :
#     #time_ok =  sample(time, 1) # 승객별 운영시간 5 ~ 50 시간 랜덤값\
#     time =randrange(5, 51) # 운행시간

    
#     if 5 <= time <= 15 :
#         print("{0}{1} 번째 손님 (소요시간 :{2})".format("[o]",count, time))
#         sum = sum + 1
#     else :
#         print("{0}{1} 번째 손님 (소요시간 :{2})".format("[x]",count, time))
          
# print(sum)
        
# 정답
# from random import *

# cnt = 0 # 총 승객 수
# for i in range(1, 51) : # 1 ~ 50 승객 수
#     time = randrange(5, 51) # 1~ 51 분 소요시간
#     if 5 <= time <= 15 : 
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else :
#         print("[X] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("태운 총 승객 수는 : {0}".format(cnt))

# 함수==========================================================
# 실행키 shift + / 키 설정

# def open():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print("{0} 원 입금되었습니다. 잔액은 {1} 원 입니다.".format(balance + money, money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money: # 잔액이 출금액보다 많으면
#         print("{0} 원 출금이 완료되었습니다. 남은 잔액은 {1}".format(money, balance - money))
#         return balance - money
#     else :
#         print("잔액이 부족합니다. 남은 잔액은 {0} 원 입니다.".format(balance))
#         return balance
    
# def withdraw_night(balance, money):
#     commisssion = 100 # 수수료 100원
#     return commisssion, balance - money - commisssion

# balance = 0    
# balance = deposit(balance, 1000)
# #balance = withdraw(balance, 2000)
# #balance = withdraw(balance, 500)

# commisssion, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며 잔액은 {1} 원 입니다".format(commisssion, balance))

# 함수 기본값 설정

# def profile(name, age = 17, lang = "python"):
#     print("이름  : {0} 나이 : {1} 언어 : {2}".format(name, age, lang))
    
# profile("유재석")
# profile("유재석", "20", "java")

# 키워드 값을 이용한 함수호출
# 값 순서에 상관없이 키워드 사용해서 호출 가능

# def profile(name, age, lang):
#     print(name, age, lang)

# profile(age = 20, lang = "java", name = "유재석")
# profile(lang = "php", name = "바보", age = 39)

# 가변인자를 이용한 함수 호출
# 서로 다른 개수의 값을 넣어줄 때는 가변인자 * 로 시작하는 매개변수 활용

# def profile(name, age, *language):
#     print("이름 : {0} 나이 : {1} ".format(name, age), end=" ")# end=" " 은 print 문 한줄로 이어줌
#     for lang in language:
#         print(lang, end=" ")
#     print()
    
# profile("유재석", "22", "java", "php", "JS", "python")
# profile("김태호", "25", "java", "python")

# 지역변수 전역변수 
# 지역 함수 내에 / 전역 프로그램 내 모든 

# gun = 10

# def check(sold):# 경계근무
#     global gun # 전역 공간에 gun 사용
#     gun = gun - sold
#     print("함수 내 남은 총 {0}".format(gun))
    
# print("전체 남은 총 {0}".format(gun))
# check(2)# 2명이 경계근무 나감  
# print("남은 총 {0}".format(gun))

# 일반적으로 전역변수를 많이쓰면 코드 관리 어려움
# 가급적 함수의 전달값으로 파라미터로 던져서 계산을 하고 반환값을 받아서 사용

# gun = 10

# def check_ret(gun, sold):
#     gun = gun - sold
#     print("함수 내 남은 총 {0}".format(gun))
#     return gun

# print("전체 남은 총 {0}".format(gun))
# gun = check_ret(gun, 2)# 2명이 경계근무 나감  
# print("남은 총 {0}".format(gun))

#Quiz

# def std_weight(height, gender):
#     if gender == "남자":
#         weight_man = height * height * 22
#         print("키 {0} 남자의 표준 체중은{1:.2f} kg입니다 ".format(height, round(weight_man, 2)))
#     else:
#         weight_woman = height * height * 21
#         print("키 {0} 여자의 표준 체중은{1} kg입니다 ".format(height, weight_woman))
    
# std_weight(170, "남자")
# std_weight(180, "여자")

#정답

# def std(height, gender): # 키 m단위 (실수) / 성별 
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std(height / 100, gender), 2)
# print("키 {0} {1} 표준체중은 {2} kg 입니다.".format(height, gender, weight))



