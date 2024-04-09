from the_Bank_class import Bank, SavingsAccount, CurrentAccount
import unittest
from unittest.mock import patch


class TestBankUpdate(unittest.TestCase):
    def test_update(self):
        account_s_1 = SavingsAccount(1200, 'GB29 NWBK 6016 1331 9268 19', 2)
        account_s_2 = SavingsAccount(1500, 'FI21 1234 5600 0007 85', 2.5)
        account_c_1 = CurrentAccount(1050, 'DE89 3704 0044 0532 0130 00', -200)
        account_c_2 = CurrentAccount(1400, 'SE45 5000 0000 0583 9825 7466',
                                     -100)

        with patch('builtins.print') as mock_print:
            bank = Bank([account_s_1, account_s_2, account_c_1])
            account_c_1.withdraw(1100)
            bank.update()

            self.assertEqual(account_s_1.get_balance(), 1224.0)
            self.assertEqual(account_s_2.get_balance(), 1537.5)
            self.assertEqual(account_c_2.get_balance(), 1400)

            mock_print.assert_called_once_with('DE89 3704 0044 0532 0130 00\
 in overdraft')


unittest.main()
