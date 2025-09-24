from bank import Bank


bank = Bank()

acc1 = bank.account_creation("Alice", 500, "1995-05-12", 1234)
acc2 = bank.account_creation("Bob", 1000, "1988-09-23")   # pin will be auto-generated


print(bank.display_transaction_history(acc1["account_number"], acc1["pin"]))


