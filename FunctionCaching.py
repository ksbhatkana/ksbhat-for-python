from functools import lru_cache
class Example:
	
	@lru_cache(maxsize=int(input("Enter the number to cache")))
	def function(self,n):
		#print("Enter the number")
		#n=int(input())
		summ=1
		j=-11
		for i in range(1,n+1):
			summ=summ*i
		while j<100000000:
			j+=1000
		print(summ)
if __name__=='__main__':
	e=Example()
	print("Calling function")
	print("Enter the number")
	n=int(input())
	e.function(n)
	print("Enter the number")
	n=int(input())
	e.function(n)	
	print("kjvcjhshjchvklcjahbcklasdmjasjdasv,k.asnb ")
