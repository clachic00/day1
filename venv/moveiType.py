import math

moviedata=[

    (10,50,"a"),
    (20,40,"a"),
    (30,40,"a"),
    (50,40,"a"),
    (20,15,"m"),
    (30,15,"m"),
    (40,10,"m"),
    (50,0,"m")
]


action=int(input("키스신 횟수를 입력"))
melo=int(input("액션신 횟수를 입력"))
target=(action,melo)


def calculator_d(X,Y):

    distance=math.sqrt(math.pow(X[0]-Y[0],2)+ math.pow(X[1]-Y[1],2))
    return distance




moviedata.sort(key=lambda x: calculator_d(x, target))

print("target과 가까운 3개 영화 정보:", moviedata[0:3])
stack_a=0
stack_m=0

for x in range(3):
    if moviedata[x][2]=="a":
        stack_a= stack_a+1
    else :
        stack_m= stack_m+1

if stack_m>stack_a:
    print("멜로영화입니다")
else :
    print("액션영화입니다.")






