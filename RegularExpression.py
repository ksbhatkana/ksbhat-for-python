import re
strr="Hi, This is Kumara subrahmanya bhat alias ksbhat"
f1=open("File1.txt")
strre=str(f1.read())
st=re.compile(r'[+91]{3}-[0-9]{10}')
mates=st.finditer(strre)
ls=[i for i in mates]
print(ls[:])
