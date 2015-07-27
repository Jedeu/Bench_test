import json
import requests

Transactions = []
runningbal = []
start = 1
z = 0
j = 0


#Requests all pages of the Bench API aka p.1-4 and prints them

while start < 5:

	i = str(start)
	url = "http://resttest.bench.co/transactions/" + i + ".json"
	r = requests.get(url)

	data = json.loads(r.text)
	goods_only = data.get('transactions') #this makes sure it only pulls the 'transactions' key from the dict, and not the date or page #
	Transactions.append(goods_only)
	start += 1

#Cleans up the transaction data into legible format



print "\n" + "Your monthly statement for December 2013:" + "\n"

while z < 4:

	for d in Transactions[z]:

		clean_format = "Date: " + d['Date'] + " | " "Amount: " + d['Amount'] + " | " "Company: " + d['Company'] + " | " "Ledger: " +  d['Ledger']

		print clean_format

	z += 1



#Time to calculate the running balance



while j < 4: #index starts at 0 and there are only 4 pages

	allthenums = [float(inner_dict['Amount']) for inner_dict in Transactions[j]] #grabs values of the key 'Amount' within the list nested in Transactions as a float
	pageBalance = sum(allthenums)

	runningbal.append(pageBalance)

	j += 1


print "\n" + "Your current balance on this credit card is: $" + str(sum(runningbal))















