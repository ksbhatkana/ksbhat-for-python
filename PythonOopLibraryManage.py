class Library:
	i=0
	def __init__(self,name,libraryName):
		self.name=name
		self.libraryName=libraryName
	
	listt=[]
	dictt={}
	listt2=[]
	@classmethod
	def addBook(cls):
		#listt=[]
		#ictt={}
		#i=0
		print("Enter the name of the Book")
		book_name=input()
		#i+=1
		cls.listt.append(book_name)
		cls.i+=1
		print("Book added successfully!!")
		cls.listt2=cls.listt[:]
	@classmethod
	def lendBook(cls):
		#listt=[]
		#dictt={}
		print("Enter the name of the Book")
		book=input()
		print("Enter your name:")
		namee=input()
		if book in cls.listt:
			cls.dictt[book]=namee
			cls.listt.remove(book)
		elif book in listt:
			print(f"It is occupied by {dictt[book]} ")
		else:
			print(f"Book doesn't exist")
	@classmethod
	def display(cls):
		#listt=[]
		#dictt={}
		print("Books in library are:")
		for i in range(len(cls.listt2)):
			print(cls.listt2[i])
		print("Available books are:\n")
		for i in range(len(cls.listt)):
			print(cls.listt[i])
	@classmethod
	def returnBook(cls):
		#listt=[]
		#dictt={}
		print("Enter your name")
		namee=input()
		try:
			for name in dictt.iterval():
				l=dictt.key()
			#listtt=lambda x:dictt{key}=x[1]
			dictt.pop(l,None)
		except Exception as e:
			pass
Obj=[]
while True:
	print("Select the option")
	print("1.Register for library")
	print("2.Add book to library")
	print("3.Lend book")
	print("4.Display books")
	print("5.Return book")
	option=int(input())
	if option==1:
		print("Enter name:")
		name1=input()
		print("Enter library name:")
		lName=input()
		Obj.append(Library(name1,lName))
	elif option==2:
		Library.addBook()
	elif option==3:
		Library.lendBook()
	elif option==4:
		Library.display()
	elif option==5:
		Library.returnBook()
	else:
		print("Wrong input")
	print("Do you want to continue")
	ch=input()
	if ch=='n' or ch=='N':
		break
		
