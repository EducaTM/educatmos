#!/usr/bin/env python3

import subprocess, re, requests

# define global variable
payload = {}

# helper function to extract number from strings
def find_numbers(string, ints=True):            
    numexp = re.compile(r'[-]?\d[\d,]*[\.]?[\d{2}]*') #optional - in front
    numbers = numexp.findall(string)    
    numbers = [x.replace(',','') for x in numbers]
    if ints is True:
        return [int(x.replace(',','').split('.')[0]) for x in numbers]            
    else:
        return numbers[0]

def getUsageData():
    # execute the ac command to get the daily usage data
    acHandle = subprocess.run(['/usr/bin/ac', '-d', '--print-year'], stdout=subprocess.PIPE)
    # cast the stdout to string and split by new line
    acData = acHandle.stdout.decode("utf-8").split("\n");

    # slice last two elements from the data
    acData = acData[:-2]

    data = []

    # iterate over the data
    for row in acData:
        cell = row.split("\t")
        date = cell[0]
        time = float(find_numbers(cell[1], False))
        data.append([date, time])
    
    return data



payload["usage"] = getUsageData()


x = requests.post("https://educatm.free.beeceptor.com", json = payload)

print(x.text)