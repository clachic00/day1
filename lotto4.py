import random
def makeNums():
    balls=[i for i in range(1,46)]
    random.shuffle(balls)

    return balls[0:6]

def input_display():
    money = int(input("금액을 넣어주세요"))
    if money % 1000 != 0:
        print("천원단위로 넣어주세요")
        return input_display()
    else:

        return money / 1000


def main():
    count = input_display()
    for x in range(int(count)):
        nums = makeNums()
        print(sorted(nums))
    print("--------------------")

if __name__== "__main__":

    main()

