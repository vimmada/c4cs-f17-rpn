import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	# def test_subtract(self):
	# 	result = rpn.calculate('5 3 -')
	# 	self.assertEqual(2, result)
	# def test_multiply(self):
	# 	result = rpn.calculate('2 3 *')
	# 	self.assertEqual(6, result)
	# 	result = rpn.calculate('3 5 *')
	# 	self.assertEqual(15, result)
	# def test_divide(self):
	# 	result = rpn.calculate('2 10 /')
	# 	self.assertEqual(0.2, result)
	# 	result = rpn.calculate('10 2 /')
	# 	self.assertEqual(5, result)
	# def test_exponentiation(self):
	# 	result = rpn.calculate('2 3 ^')
	# 	self.assertEqual(8, result)
	# 	result = rpn.calculate('2 0 ^')
	# 	self.assertEqual(1, result)
	# 	result = rpn.calculate('0 10 ^')
	# 	self.assertEqual(0, result)
	# 	result = rpn.calculate('5 10 + 3 ^')
	# 	self.assertEqual(3375, result)
