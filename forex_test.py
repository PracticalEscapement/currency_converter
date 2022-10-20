from forex_python.converter import CurrencyRates

def currency_converter(from_code='USD', to_code='USD', amt=1):
  get_from_currency = input("Desired currency to be converted: ")
  get_to_currency = input("What Would You like this to be converted to?: ")
  get_amount = input("How much would you like to convert?: ")
  
  c = CurrencyRates()
  rate = c.get_rate(get_from_currency.upper(), get_to_currency.upper())
  return rate * float(get_amount)


print(currency_converter())