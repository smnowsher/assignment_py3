mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 107.25
}

i = 0
data_field = len(mobile_data['data'])

while i < data_field:
    text = '{name} is made in {made}. Its price is {price} or approximately '.format_map(mobile_data['data'][i]) + str(
        int(float(mobile_data['data'][i]['price'].split()[0]) * float(mobile_data['exchange_rate']))) + ' BDT.'
    print(text)
    i = i + 1
