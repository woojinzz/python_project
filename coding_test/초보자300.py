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
# letters = 'python'
# print(letters[0],letters[2])

# car = "24 가 2101"
# print(car[-4:])
# 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미합니다.

# string = "홀짝홀짝홀짝"
# print(string[::2])
#슬라이싱할 때 `시작인덱스:끝인덱스:오프셋`을 지정할 수 있습니다.

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

# url = "http://sharebook.kr"
# url_split = url.split('.')# . 기준으로 2개로 나눠줌
# print(url_split[-1]) # 뒤에 기준

# 대문자 변경
# str = 'asdsdasa'
# print(str.replace("a","A"))

string = 'abcd'
string.replace('b', 'B')
print(string)