import re

data = [
    'c15103', 'c15104', 'c15202'
    'n16001', 'n16002', 'n16003', 'n16004', 'n16005', 'n16006', 'n16007', 'n16008', 'n16009',
    'n16101', 'n16102', 'n16103', 'n16104', 'n16105', 'n16106', 'n16107',
    's16001', 's16002', 's16003', 's16004', 's16005', 's16006', 's16007', 's16008', 's16009',
]


str_data = str(data)
print(re.findall(r'c15[12]0[342]', str_data))
print(re.findall(r'c15\d{3}', str_data))
print(re.findall(r'n161\d{2}', str_data))
print(re.findall(r'[cns]\d{4}3', str_data))