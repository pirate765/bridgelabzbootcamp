class MyClass:
	"This is my custom class"
	a = 10
	def func(self):
		print('Hello', self.a)

obj1 = MyClass()
print(obj1)
print(obj1.func())
print(obj1.func2())
# print(MyClass.a)
# print(obj1.func())
