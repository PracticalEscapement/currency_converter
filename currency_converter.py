from forex_python.converter import CurrencyRates # Get current rates
from forex_python.converter import CurrencyCodes # Get Currency symbols

class CurrencyConversion:
	def __init__(self, initail_code=None, converted_code=None, amount=1):
		self.initial_code = initail_code
		self.converted_code = converted_code
		self.amount = amount
		self.rate = 1
		self.valid_codes = ('AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR')
		self.errors = []

	# def list_country_codes(self):
	# 	pass
	
	def get_user_input(self):
		data = {
			"from_code": input("\nDesired currency to be converted: ").upper(),
			"to_code": input("\nWhat Would You like this to be converted to?: ").upper(),
			"amt": input("\nHow much would you like to convert?: ")
		}
		return data
	
	def validate_user_input(self, data):
		# todo Check if instance variables of currency codes are None 
		if data["from_code"] and data["to_code"] in self.valid_codes:
			self.initial_code = data["from_code"]
			self.converted_code = data["to_code"]
			if data["amt"].isnumeric():
				self.amount = float(data["amt"])
				return True
			else:
				self.errors.append("Amount must be a valid numeric value!")
				return False
		else:
			self.errors.append("Must be a valid country code!")
			return False
	
	def get_current_rate(self):
		currency_rate = CurrencyRates()
		self.rate = currency_rate.get_rate(self.initial_code, self.converted_code)
		self.convert_total_amount()
	
	def convert_total_amount(self):
		print(self.rate * self.amount)
		count = 0
		different_amount = input('\nWould you like to convert another amount (Y/N)?: ')
		while different_amount != 'N' and count < 5:
			get_different_amount = float(input('\nGive the amount to convert or "N" to quit: '))
			if get_different_amount == 'N':
				break
			total = self.rate * get_different_amount
			print(total)
			count += 1
		if count >= 5:
			print('Max number of conversions reached!')

	def call(self):
		user_input = self.get_user_input()
		validated_data = self.validate_user_input(user_input)
		if validated_data:
			self.get_current_rate()
		else:
			print(self.errors)
			self.call()



cc = CurrencyConversion()
cc.call()
