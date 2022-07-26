from unittest import TestCase
from ordering.burbuja import burbuja
from ordering.seleccion import seleccion
from ordering.insercion_binaria import quick_sort


class Test(TestCase):
	def test_burbuja(self):
		self.assertEqual(burbuja([1, -15, 48, 2, 15]), [-15, 1, 2, 15, 48])
		self.assertEqual(burbuja([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

	def test_seleccion(self):
		self.assertEqual(seleccion([1, -15, 48, 2, 15]), [-15, 1, 2, 15, 48])
		self.assertEqual(seleccion([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

	def test_seleccion(self):
		self.assertEqual(quick_sort([1, -15, 48, 2, 15]), [-15, 1, 2, 15, 48])
		self.assertEqual(quick_sort([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
