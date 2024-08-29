import requests
n=1
while n!=0:
     
    base_currency= input("Enter Base currency: ")
    amount=float(input("Enter the amount: "))
    quote_currency=input('Enter the quote currency:  ')
    api_keys= '85b233df6e50d1e4b18487c6'

    url= f'https://v6.exchangerate-api.com/v6/{api_keys}/latest/{base_currency}'
    response= requests.get(url)
    if response.status_code == 200:
        data = response.json()
        conversion_rates = data['conversion_rates']

        if quote_currency in conversion_rates:
            exchange_rate = conversion_rates[quote_currency]
            converted_amount = amount * exchange_rate
            print("converted amount is {} {}".format(converted_amount,quote_currency))
        else:
            print("currency is not found")

    else:
        print("Invalid url")