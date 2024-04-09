from the_Bank_class import Bank, Account
import unittest


class TestBank1(unittest.TestCase):
    def test_open_account(self):
        bank = Bank([])
        initial_balance = 5000
        account_number = 'GB29 NWBK 6016 1331 9268 19'
        new_account = Account(initial_balance, account_number)

        bank.open_account(new_account)

        self.assertIn(new_account, bank._accounts)
        self.assertEqual(new_account.get_balance(), initial_balance)


unittest.main()
