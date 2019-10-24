import pandas as pd
import re

file = open(r'data.txt', 'r')
string1 = file.read()

ip_list = re.findall(r'\[(.*)\]', string1)
os_list = re.findall(r'"success": "(.*)"', string1)

os_list2 = [x.strip(' ').replace('Linux release ', '').replace('.1804 (Core)', '').replace('.1810 (Core)', '')
         .replace('.1908 (Core)', '').replace('.1511 (Core)', '').replace(' (Final)', '')
         .replace('release ', '').replace('.1611 (Core)', '') for x in os_list]

if len(ip_list) == len(os_list2):
    dict1 = {ip_list[n]:os_list2[n] for n in range(len(ip_list))}
else:
    print("something wrong. please check")

data_output = pd.DataFrame(list(dict1.items()), columns=['ip', 'os'])

data_output.to_csv(r'output.csv')
