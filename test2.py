print ('')
print ('........................................')
print ('***.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.***')
print ('')
print ('              환영합니다!')
print ('     가위! 바위! 보! 게임을 시작합니다.')
print ('         어떤것을 내시겠습니까?')
print ('')
print ('***.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.***')
print ('........................................')
print ('')

import random
com = random.choice(['가위', '바위', '보'])
# print(com)

player = input('가위,바위,보 중 하나를 입력하세요:')

if com == '가위':
      print('')
      print('* COMPUTER: 가위')

      if player == '가위':
            print ('* YOU     : 가위')
            print ('')
            print ('* 결과는 / !무승부! / 입니다')
            print ('* ...한판 더 도전하시겠습니까?')
            print ('')
        
      elif player == '바위':
            print ('* YOU     : 바위')
            print ('')
            print ('********************************')
            print ('')
            print ('* 결과는 / 당신의 승리!! / 입니다')
            print ('* .! WOW ! 축하드립니다 ! WOW !.')
            print ('')
            print ('********************************')
            print ('')
              
      elif player == '보':
            print ('* YOU     : 보')
            print ('')
            print ('* 결과는 / 당신의 패배;; / 입니다')
            print ('* ...한판 더 도전하시겠습니까?')
            print ('')

if com == '바위':
      print('')
      print('* COMPUTER: 바위')

      if player == '가위':
            print ('* YOU     : 가위')
            print ('')
            print ('* 결과는 / 당신의 패배;; / 입니다')
            print ('* ...한판 더 도전하시겠습니까?')
            print ('')
        
      elif player == '바위':
            print ('* YOU     : 바위')
            print ('')
            print ('* 결과는 / !무승부! / 입니다')
            print ('* ...한판 더 도전하시겠습니까?')
            print ('')
              
      elif player == '보':
            print ('* YOU     : 보')
            print ('')
            print ('********************************')
            print ('')
            print ('* 결과는 / 당신의 승리! / 입니다')
            print ('* .! WOW ! 축하드립니다 ! WOW !.')
            print ('')
            print ('********************************')
            print ('')      

if com == '보':
      print('')
      print('* COMPUTER: 보')

      if player == '가위':
            print ('* YOU     : 가위')
            print ('')
            print ('********************************')
            print ('')
            print ('* 결과는 / 당신의 승리!! / 입니다')
            print ('* .! WOW ! 축하드립니다 ! WOW !.')
            print ('')
            print ('********************************')
            print ('')
        
      elif player == '바위':
            print ('* YOU     : 바위')
            print ('')
            print ('* 결과는 / 당신의패배;; / 입니다')
            print ('* ...한판 더 도전하시겠습니까?')
            print ('')
              
      elif player == '보':
            print ('* YOU     : 보')
            print ('')
            print ('* 결과는 / !무승부! / 입니다')
            print ('* ...한판 더 도전하시겠습니까?')
            print ('')      
