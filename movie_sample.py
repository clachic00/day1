import math


movie_sample = [
    (10, 50, 'M'),
    (20, 40, 'M'),
    (30, 40, 'M'),
    (50, 40, 'M'),
    (20, 15, 'A'),
    (30, 15, 'A'),
    (40, 10, 'A'),
    (50, 0, 'A')
]

count_kiss = int(input("키스씬의 횟수를 입력하세요"))
count_action = int(input("액션씬의 횟수를 입력하세요"))
target = (count_kiss, count_action)



def calcDistance(point1, point2):

    result = math.sqrt(math.pow(point1[0]-point2[0],2)+math.pow(point1[1]-point2[1],2))
    return result

movie_sample.sort(key=lambda x: calcDistance(x,target))

print("target과 가장 가까운 영화 3개 : ",movie_sample[0:3])