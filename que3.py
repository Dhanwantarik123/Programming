class person():
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
class info(person):
	def __init__(self,name,roll,dept,year,sec):
		super().__init__(name,roll)
		self.dept=dept
		self.year=year
		self.sec=sec
class student(info):
	def __init__(self,name,roll,dept,year,sec,sp,emf,m4,pp,oe):
		super().__init__(name,roll,dept,year,sec)
		self.sp=sp
		self.emf=emf
		self.m4=m4
		self.pp=pp
		self.oe=oe
	def display(self):
		print(f"Name:{self.name}\nRoll No:{self.roll}\nDepartment:{self.dept}\nYear:{self.year}\nSection:{self.sec}")
		print(f"Sp:{self.sp}\nEmf:{self.emf}\nM4:{self.m4}\nPP:{self.pp}\nOE:{self.oe}")

		total=self.sp+self.emf+self.m4+self.pp+self.oe
		print("Total:",total)
students=[
	student("Dk",33,"Etc",3,"A",55,77,88,99,88)
]
for s in students:
	s.display()
	

