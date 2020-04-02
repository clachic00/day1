from webcatch import getData

answer = input("크롤링을 시작할까요? 좀 기다리셔야 해요")

result = getData()
print(result)







#if answer == 'N':
#    exit()

#result = getData()
#print(result)




# from random import randrange
#
# #프로그램 짤때 문제점이 있어도 짜놓고 수정하는 형식
#
# nums=[]
#
# #루프를 nums가 6개가 되는 동안
#
# def checkDuplicate(num_list, target):
#
#     result=False
#
#     for x in num_list:
#         if x == target:
#             result = True
#             break
#
#     return result
#
#
# while len(nums)<6:
#     # 1부터 45 사이의 숫자를 뽑고 nums에 저장
#     num = randrange(1,46)
#
#
#     if checkDuplicate(nums,num)==True:
#
#         continue
#     nums.append(num)
#     #뽑은 값이 있다면 다시 뽑는다.
#
# print(nums)






