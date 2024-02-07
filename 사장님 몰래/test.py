import  openpyxl  as  op  # openpyxl 모듈 import

# wb = op.Workbook() #새로운 Workbook 객체 생성
# print(wb) #객체를 출력해보기

# 1 새로 생성
# wb.save("test.xlsx")
#wb.save(r"C:\Users\woojin\Desktop\myproject\python_project\사장님 몰래\test.xlsx")
#경로 안에 있는 r 표시는 unicode 에러 발생시 사용합니다.


# 2 기존 파일을 객체로 생성할 때
# path = r"C:\Users\woojin\Desktop\myproject\python_project\사장님 몰래"
# wb = op.load_workbook(path + "/test.xlsx")

# print(wb)

# 2번까진 workbook 객체를 새로 생성하거나 이미 만들어진 엑셀 파일에 접근할 것인지에 대한 내용
