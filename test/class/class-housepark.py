# -*- coding: utf-8 -*-

class housepark:
	lastname = "박"
	def __init__(self,name):
		self.fullname = self.lastname + name

	def travel(self):
		where = input("여행하고 싶은곳은 어디인가요")
		print("%s, %s 여행을 가고싶다." %(self.fullname, where))

	def __del__(self):
		print ("%s 죽네" % self.fullname)