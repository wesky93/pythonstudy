# -*- coding:utf-8 -*-

#전역변수 선언

runcheck = 0	#이전 계산값을 다음계산에 사용여부 판단함수 
				#0이면 새로운 계산을 1이면 재사용을 의미

num_a = int()	#계산기에 넣을 첫번째 숫자
num_b = int()	#계산기에 넣을 두번째 숫자

while 1:
    if runcheck==0:
        num_a = fnum()
        num_b = snum()
        askcount(num_a,num_b)
    elif runcheck==1:
        resetcheck()
        if runcheck == 0:
            pass
        elif runcheck == 1:
            askcount(num_a,num_b)