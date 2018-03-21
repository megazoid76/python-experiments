

def foo(*args, **kwargs):
	for arg in args:
		print("args : %s" % arg)

	for kwarg in kwargs:
		print("kwargs : %s" % kwarg)

args = (1,2,3, "testing", [123, 234])

kwargs = {"a":1, "b":2, "c":3}
foo(*args, **kwargs)
