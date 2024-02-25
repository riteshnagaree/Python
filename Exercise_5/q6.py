bank ={
	"SBI":500,
	"CNRB":100
}

for bank_name,Balance in bank.items():
	print(f"Bank:{bank_name},  Avlbl balance:{Balance}")





bank["SBI"] -= 100


bank["CNRB"] +=200


bank["SBI"] +=  300

print("updated statement")

for bank_name,Balance in bank.items():
	print(f"Bank:{bank_name},  Avlbl balance:{Balance}")