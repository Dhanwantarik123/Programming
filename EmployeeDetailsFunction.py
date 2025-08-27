def read():
	name=input("Enter  name of developer:")
	dept=input("Enetr department:")
	degn=input("Enter Designation:")
	emp_Id=input("Enter Employee ID:")
	BS=input("Enter Basic Salary:")
	print("Name of Developer \t:",name)
	print("Department of Developer \t:",dept)
	print("Designation of Developer \t:",degn)
	print("Emp_ID of Developer \t:",emp_Id)

	cal_sal(BS,total_bal)
	
def cal_sal(BS,total_bal):
	HRA=0.4*BS
	TA=0.3*BS
	DA=0.9*BS
	inc=5000
	Lic=2000
	PF=2400
	TDS=800
	total_bal=BS+HRA+TA+DA+inc-Lic-PF-TDS
	display(BS,total_bal)
	
def display(BS,total_bal):
	print("Basic Salary Of Developer\t:"+BS)
	print("Total Balance Of Developer\t:"+total_bal)
read()

