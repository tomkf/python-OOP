#public: 
# Access owner's full name and balance
# Access only partial IBAN, e.g. IBAN: FR14**************606
# Print partial account info in an user-friendly way
# Withdraw or deposit money
# Print transaction history if a password is provided
#account = BankAccount.new("John Lennon", "FR14-2004-1010-0505-0001-3M02-606", 200, "yoko")
# the puts will call the `to_s` method on the object
# =>  Owner: John Lennon - IBAN: FR14**************606 - Balance: 200 euros


class BankAccount:
 def __init__(self, fullname, accountnum, balance, password):
  self.name = fullname
  self._accountnum = accountnum
  self.balance = balance
  self._password = password
 
 def get_account_info(self, paswrd):
  if paswrd == self._password:
   account_hashed = self._accountnum[0:4] + "**************" + self._accountnum[-3:]
   print("Owner: " + self.name +  " - IBAN: " + account_hashed + " - Balance: " + str(self.balance) + " dollars" ) 
  else: 
   print("wrong password")

 def withdraw(self, amount):
  self.balance -= amount
  print('You have withdrawn %s dollars'%(amount))

 def deposit(self, amount):
  self.balance += amount
  print('You have deposited %s dollars'%(amount))

my_account = BankAccount("Tom Ferris", "FR14-2004-1010-0505-0001-3M02-606", 500, "yoko")
my_account.deposit(100)
my_account.get_account_info("yoko")