import json
import requests

Transactions = []
start = 1

#Requests all pages of the Bench API aka p.1-4 and prints them

while start < 5:

	i = str(start)
	url = "http://resttest.bench.co/transactions/" + i + ".json"
	r = requests.get(url)

	data = json.loads(r.text)
	goods_only = data.get('transactions') #this makes sure it only pulls the 'transactions' key from the dict, and not the date or page #
	Transactions.append(goods_only)
	start += 1

print Transactions


#Time to calculate the running balance

runningbal = []
j = 0

while j < 4: #index starts at 0

	allthenums = [float(inner_dict['Amount']) for inner_dict in Transactions[j]] #grabs values of the key 'Amount' within the list nested in Transactions as a float
	pageBalance = sum(allthenums)

	
	runningbal.append(pageBalance) #Adds the tally of each page into the list runningbal

	j += 1


print "\n" + "Your current running balance is: $" + str(sum(runningbal))















