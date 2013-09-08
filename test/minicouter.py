# -*- coding: utf-8 -*-

def minicount():
	print ("미니계산기\n")
	print ("몇번 계산하고 싶으신가요? : \n")
	cal = float(input())
	for i in list(range(1,int(cal)+1)):
		a = float(input("첫번째 숫자를 입력하세요"))
		b = float(input("두번째 숫자를 입력하세요"))
		print ("각각 입력된수는",a,b,"입니다")
		c = float(input("더하기는 1을 빼기는 2를 눌러주세요"))
		if c == 1 :
			print ("값은",a+b)
		elif c == 2:
			print ("값은",a-b)
		else:
			print ("숫자 1,2가 아닙니다.")


