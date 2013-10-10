# -*- coding: utf-8 -*-

class housepark:
	lastname = "박"
	#__init__은 클래스 선언할시에 작동하는 함수로 sky = housepark("이름")처럼
	#초기 선언할때 변수값도 같이 입력해줘야 한다.
	def __init__(self,name):
		self.fullname = self.lastname + name

	def travel(self):
		where = input("여행하고 싶은곳은 어디인가요")
		print("%s, %s 여행을 가고싶다." %(self.fullname, where))

	#__del__은 del함수로 class를 삭제하면 작동하는 함수이다.
	def __del__(self):
		print ("%s 죽네" % self.fullname)


#상속하기 housekim(housepark)를 하게되면 lastname은 박대신 김이되며 나머지는 
#똑같이 작동한다.
class housekim (housepark):
	lastname = "김"

#상속하였을때 만약 원래 클래스의 함수와 다르게 작동을 원하면 다시
#함수를 선언하면 된다.
	def travel(self):
		where = input("여행하고싶은 곳은 어디인가요?")
		day = input("몇일동안 여행을 가나요?")
		print ("%s, %s 여행을 %s동안 가고싶다" % (self.fullname, where, day))