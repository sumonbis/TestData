try:
	class MyClass:
		"This is my second class"
		a = 10
		def func(self):
			print('Hello')
		
		class Inner:
		    """Inner Class"""

		    def inner_display(self, msg):
		        print(msg)
except NameError:
	print("Found error")