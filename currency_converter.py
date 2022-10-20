from forex_python.converter import CurrencyRates # Get current rates
from forex_python.converter import CurrencyCodes


class CurrencyConversion:
	def __init__(self, initail_code=None, converted_code=None, amount=1):
		self.initial_code = initail_code
		self.converted_code = converted_code
		self.amount = amount
		self.requests = 1
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
		if self.requests >= 3:
			return print('Max number of requests reached!')
		
		currency_rate = CurrencyRates()
		self.rate = currency_rate.get_rate(self.initial_code, self.converted_code)
		self.requests += 1
		print(self.rate * self.amount)
		
		get_additional_amount = input('\nWould you like to convert another amount(Y/N)?: ')
		if get_additional_amount == 'Y':
			self.additonal_amount()

	def additonal_amount(self):
		data = {
			"from_code": self.initial_code,
			"to_code": self.converted_code,
			"amt": input('\nGive the amount to convert: ')
		}
		
		valid_input = self.validate_user_input(data)
		if valid_input:
			self.get_current_rate()

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
