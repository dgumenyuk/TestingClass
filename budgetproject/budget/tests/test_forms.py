from django.test import SimpleTestCase
from budget.forms import ExpenseForm


class TestForms(SimpleTestCase):

	def test_expense_form_valid_data(self):
		form = ExpenseForm(data= {
			'title': 'expense1',
			'amount': 1000,
			#'amount': 'thousand',
			'category': 'development'
			#'category': 123

		})
        
		self.assertTrue(form.is_valid())


	def test_expense_form_no_data(self):
		form = ExpenseForm(data={})


		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 3)
