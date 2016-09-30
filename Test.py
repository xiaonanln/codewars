
class Fail(Exception):
	pass

def expect(expr, errmsg):
	if expr:
		return

	print 'ERROR: %s: %s is not True' % (errmsg, expr)

def assert_equals(e1, e2):
	if e1 == e2:
		return

	print 'ERROR: %s and %s should be equal' % (e1, e2)
