
class houseshin:
	lastname = "신"
	def __init__(self, name):
		self.fullname = self.lastname + name

	def travel(self, where):
		print ("%s, %s 여행을 가다." %(self.fullname, where))

	def love(self, other):
		print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))

	def __add__(self, other):
		print("%s, %s 결혼했네" %(self.fullname, other.fullname))

	def __del__(self):
		print("%s 죽네" % self.fullname)


class houselee(houseshin):
	lastname = "이"
	def travel(self, where, day):
		print("%s, %s 여행 %d일 가네" %(self.fullname, where, day))
	
pey = houseshin("재현")
her = houselee("여혜")
pey.love(her)
pey + her