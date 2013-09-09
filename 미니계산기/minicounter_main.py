# -*- coding:utf-8 -*-

#전역변수 선언

runcheck = 0	#이전 계산값을 다음계산에 사용여부 판단함수 
				#0이면 새로운 계산을 1이면 재사용을 의미

num_a = int()	#계산기에 넣을 첫번째 숫자는 정수형 선언
num_b = int()	#계산기에 넣을 두번째 숫자는 정수형 선언

#m_count모듈 및 내부함수 모조리 등록
from m_count import *



while 1:
    if runcheck==0:
        num_a = fnum()
        num_b = snum()
        num_a = askcount(num_a,num_b)
        runcheck = 1
    elif runcheck==1:
        runcheck, num_b = resetcheck()    
        if runcheck == 0:
            pass
        elif runcheck == 1:
            num_a = askcount(num_a,num_b)
