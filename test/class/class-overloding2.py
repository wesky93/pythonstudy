# -*- coding: utf-8 -*-

class houseshin:
	lastname = "신"
	def __init__(self, name):
		self.fullname = self.lastname + name

	def travel(self, where):
		print ("%s, %s 여행을 가다." %(self.fullname, where))

	def love(self, other):
		print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))

	def fight(self, other):
		print("%s, %s 싸웠네" %(self.fullname, other.fullname))

	def __add__(self, other):
		print("%s, %s 결혼했네" %(self.fullname, other.fullname))

	def __sub__(self, other):
		print("%s, %s 이혼했네" %(self.fullname, other.fullname))

	def __del__(self):
		print("%s 죽네" % self.fullname)


class houselee(houseshin):
	lastname = "이"
	def travel(self, where, day):
		print("%s, %s 여행 %d일 가네" %(self.fullname, where, day))
	
shin = houseshin("재현")
lee = houselee("여혜")
shin.travel("부산")
lee.travel("부산", 3)
shin.love(lee)
shin + lee
shin.fight(lee)
shin - lee
