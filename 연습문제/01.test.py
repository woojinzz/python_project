
# year = int(input())
# age_type = input()

# if age_type == "Korea":
#     answer = 2030 - year + 1

# elif age_type == "Year":
#     answer = 2030 - year

# print(answer)

# numbers = [1,2,3]
# our_score = [40,50,60]
# score_list = [40,50,70]

# def solution(numbers, our_score, score_list):
#     answer = []
#     for i in range(len(numbers)):
#         if numbers[our_score[i]] == score_list[i]:
#             answer.append("Same")
#         else:
#             answer.append("Different")
    
#     return answer

storage = ["pencil", "pencil", "pencil", "book"]
num = [2, 4, 3, 1]

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
            print(storage[i])
        else:
            clean_storage.append(num[i])
            clean_num.append(num[i])
            
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer
            
solution(storage, num)

    