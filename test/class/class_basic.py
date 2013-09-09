# -*- coding: utf-8 -*-

#점프투파이썬을 보고 만드는 클래스 익히기위한 파일
class Service():
	secret = "클래스의 시크릿."
	def sum(self, a, b):
		result = a+b
		print("%s님 %s + %s = %s 입니다" %(self.name, a,b,result))
	
	def setname(self, name):
		self.name = name
		