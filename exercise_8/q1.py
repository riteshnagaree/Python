#factorial
def factorial(n):
	if n == 0:
		return 1
	else:
		return n* factorial(n-1)

res = factorial(5)
print(res)




#using lambda

fact = (lambda n: 1 if n == 0 else n * fact(n-1))

result = fact(6)
print(result)