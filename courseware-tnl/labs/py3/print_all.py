def print_all(*args,**kargs):
	for i in args:
		print(i)
	for key,value in kargs.items():
		print("{}={}".format(key,value))
print_all(1,2,3,'x',[1,2,3],name="Kasi",Age="32")
