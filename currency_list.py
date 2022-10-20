raw_text = "|EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |GBP - United Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint |RON - Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar |HKD - Hong Kong Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi |TRY - Turkey Lira |HRK - Croatia Kuna |NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States Dollar |NOK - Norway Krone |RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic Koruna |BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand"

countries = raw_text.split('|')

country_codes = []
for code in countries:
  country_codes.append(code[:3])

country_codes.sort()
print(country_codes[1:])


