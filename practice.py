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
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1 http:// 부분 제외
#print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2 처음 만나는 점 이후 부분은 제외
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는{1}입니다".format(url,password))
