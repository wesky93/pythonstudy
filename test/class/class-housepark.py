# -*- coding: utf-8 -*-

class housepark:
	lastname = "박"
	def setname(slef):
		name = input("이름을 입력하세요")
		self.fullname = self.lastname + name

	def travel(self):
		where = input("여행하고 싶은곳은 어디인가요")
		print("%s, %s 여행을 가고싶다." %(self.fullname, where))
		