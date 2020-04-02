from random import randrange


result_a=[]

def rcp():
    user=int(input("가위0 바위1 보2"))
    com=randrange(0,3)

    print(com)

    if com < user:
        com=com+3

    result = com - user
    str=""

    if result ==2:
        str="win"
    elif result ==1:
        str="lose"
    else :
        str="draw"

    print(str)
    return str


for x in range(9):
    result = rcp()
    result_a.append(result)


print(result_a)