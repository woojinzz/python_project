# s = "hello"
# t = "python"

# print(s + "!", t)

# num_str = "720"
# num_int = int(num_str)
# print(type(num_int))

# year = "2020"
# print(int(year)-3)  # 2017
# print(int(year)-2)  # 2018
# print(int(year)-1)  # 2019

# air = 48584
# sum = air * 36
# print(sum)

# 문자열 
# 인덱싱

# letters = 'python'
# print(letters[0],letters[2])

# car = "24가 2101"
# print(car[4:8])
# print(car[4:])
# print(car[-4:])
# 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미합니다.

# string = "홀짝홀짝홀짝"
# print(string[::2])
#슬라이싱할 때 `시작인덱스:끝인덱스:오프셋`을 지정할 수 있습니다. 오프셋 = 2칸씩 건너띄워라

#문자열 거꾸로
# string = "python"
# print(string[::-1])

#하이폰 제거
# phone = "010-1234-1234"
# phone1  = phone.replace("-", " ")
# print(phone1)

# phone = "010-1234-1234"
# phone1  = phone.replace("-", "")
# print(phone1)
# 문자열은 변경할 수 없음

# url = "http://sharebook.kr"
# url_split = url.split('.')# . 기준으로 2개로 나눠줌
# print(url_split[-1]) # 뒤에 기준
# print(url[-2:])

# 대문자 변경
# str = 'asdsdasa'
# print(str.replace("a","A"))

# #B 로 변경한 값을 할당을 안해줘서 사라지고 b로 그대로 출력됨
# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# 31 ~ 40=============================================================

# 31 문자열 합치기
# a = "3"
# b = "4" 
# print(a + b)
# 문자열에서 + 기호는 문자열 연결을 의미 따라서 34 출력

# 32 문자열 곱하기
# print("Hi" * 3)
# 문자열에 대한 곱셈은 문자열의 반복을 의미 따라서 HiHiHi 출력

# 33 문자열 곱하기
# print("-" * 80)

# 34
# t1 = "python"
# t2 = "java"
# t3 = t1 + ' ' + t2 + ' '

# print(t3 * 4)

# 35 문자열 출력 
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름 : %s 나이 : %d" % (name1, age1))
# print("이름 : %s 나이 : %d" % (name2, age2))
# %s 문자열 %d 정수형 데이터 출력

# 36 format() 메서드는 타입 상관없이 값 출력 위치에 {}
# print("이름 : {0} 나이 : {1}".format(name1,age1))
# print("이름 : {0} 나이 : {1}".format(name2,age2))

# 37 f-string 3.6 부터 지원
# print(f"이름 : {name1} 나이 : {age1}")
# print(f"이름 : {name2} 나이 : {age2}")

# 38 컴마 제거
# 상장주식수 = "5,123,123,123"
# 컴마제거 = 상장주식수.replace(",","")
# print(상장주식수.replace(",",""))

# 타입변환 = int(컴마제거)# 컴마를 제거하고 int 형으로 변환 해야함
# print(타입변환, type(타입변환))

# 39 슬라이싱
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# 40 strip() 메서드 /공백제거
# data = "  삼성  "
# print(data.strip())

# 41 ~ 50
# 41 upper() 메서드 / 대문자 변경
# ticker = "btc_krw"
# ticker2 = ticker.upper()
# print(ticker2)

# 42 lower 메서드 / 소문자 변경
# ticker = "BTC_KRW"
# ticker2 = ticker.lower()
# print(ticker2)

# 43 capitalize 메서드 / 첫글자 대문자로 변경
# a = "hello"
# a = a.capitalize()
# print(a)

# 44 endswith 메서드 ("조건") 로 끝나는지 확인
# file_name = "보고서.xlsx"
# file_name = file_name.endswith("xlsx")
# print(file_name)

# 45 endswith 메서드 xlsx, xls로 끝나는지 확인 ()로 묶어서 확인 
# file_name = "보고서.xlsx"
# file_name = file_name.endswith(("xlsx", "xls"))
# print(file_name)

# 46 startswith 메서드 / 시작문자열 확인
# file_name = "2020_보고서.xlsx"
# file_name = file_name.startswith("2020")
# print(file_name)

# 47 split 메서드 
# a = "hello world"
# a = a.split()
# print(a) 

# 48 split 메서드
# ticker = "btc_krw"
# ticker = ticker.split("_")
# print(ticker)

# 49 split 메서드
# date = "2020-05-01"
# print(date.split("-"))

# 50 rstrip 메서드 / 오른쪽 공백제거
# data = "14121414        "
# print(data.rstrip())

#========================================================
# 리스트 / 순서가 있고 수정 가능
# 51 ~ 60

# 51 리스트 생성
# movie = ["닥터", "스플릿", "럭키"]
# print(movie)

# 52 리스트에 원소 추가
# movie = ["닥터", "스플릿", "럭키"]
# movie.append("배트맨")
# print(movie)

# 53 리스트 ~사이에 값 넣기
# movie = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
# movie.insert(1, "슈퍼맨")
# print(movie)
# 리스트의 insert(인덱스, 원소) 메서드를 사용하면 특정 위치에 값을 끼워넣기 가능

# 54 삭제
# movie = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
# movie.remove("럭키")
# print(movie)

# movie = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
# del movie[2]
# print(movie)

# 55 2개 원소 삭제
# movie = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
# del movie[2]
# del movie[2]
# print(movie) 
# 리스트의 어떤 값을 삭제하면 남은 값들은 새로 인덱싱 됩니다.

# 56 합치기
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)

# 57 최대, 최소값
# nums = [1,2,3,4,5]
# print(max(nums), min(nums))

# 58 합
# nums = [1,2,3,4,5]
# print(sum(nums))

# 59 길이
# cook = ["김치", "김밥", "만두", "라면", "피자"]
# print(len(cook))

# 60 평균
# nums = [1,2,3,4,5]
# age = sum(nums) / len(nums) 
# print(age)

# 61 리스트 출력
# price = ["20202022", 100, -200, 300 ]
# print(price[1:])

# 62 홀수 출력
# nums = [1,2,3,4,5,6 ]
# print(nums[::2])

# 63 짝수
# nums = [1,2,3,4,5,6 ]
# print(nums[1::2]) # 2개당 하나씩 2~6

# 64 역방향
# nums = [1,2,3,4,5,6 ]
# print(nums[::-1]) # -1씩 가져옴 뒤에서부터 1을 주면 앞에서부터 하나씩

# 65 
# interest = ['삼전', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# 66 join 메서드 / 리스트에 원소들을 하나의 문자열로 붙여줌
interest = ['삼성', 'LG', 'Naver', 'SK', '미래에셋대우']
result = " ".join(interest) # 중간에 공백을 두고 합쳐라 result는 문자열로 변경 
print(result)