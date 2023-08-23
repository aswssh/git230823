

import random
number = random.randint(1, 50)
tries = 0
n = 10

print ('========================================')
print ('-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
print ('')
print ('              환영합니다!')
print ('       UP & DOWN 게임을 시작합니다')
print ('     1~100 사이의 숫자를 입력하세요')
print (' # 10번의 시도 안에 정답을 맞춰주세요! # ')
print ('')
print ('-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
print ('========================================')
print ('')
# print(number)
print("")

while tries <= n:
    print("")
    guess = int(input('정답은? :'))
    print("")


    tries += 1
    if number == guess:
        print("__________________________________")
        print("")
        print("  WOW!! 축하합니다!! 정답입니다!!")
        print("  * %d회 * 만에 성공하셨습니다!! :)  " % tries)
        print("  ***:. 게임을 종료합니다 .:***")
        print("")
        break
    elif number < guess:
        print("")
        print("__________________________________")
        print("")
        print("       %d번째 시도입니다" % tries)
        print('  더 작은수를 입력해주세요. Down!')
        print("")
        print("__________________________________")
        print("")
    elif number > guess:
        print("")
        print("__________________________________")
        print("")
        print("       %d번째 시도입니다" % tries)
        print('   더 큰수를 입력해주세요. Up!')
        print("")
        print("__________________________________")
        print("")
        
        
if tries > n:
    print("__________________________________")
    print("")
    print("       ;ㅅ; 아쉽네요.")
    print("주어진 기회를 모두 사용하셨습니다.")
    print("     정답은 * %d * 입니다." % number)
    print("")
    print("#####   게임을 종료합니다   #####")
    print("")
