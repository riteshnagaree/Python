
month=[
("Monday",[25,21,19,29]),
("Tuesday",[23,22,20,25]),
("Wednesday",[23,22,26,27]),
("Thursday",[23,22,28,25]),
("Friday",[21,24,23,26])
]



for Day,Temp in month:
	total=max(Temp)
	a=min(Temp)
	print(f"{Day}:  Maximum temp {total}")
	print(f"{Day}:  minimum temp  {a}\n ")