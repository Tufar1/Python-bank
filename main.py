import os
import json
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

creds = open('data.json', encoding="utf-8")
 
data = json.load(creds)

def start():
	print("|---|BANK|---|\r\n")
	pin = input("Please insert your PIN to account: ")

	if len(pin) != 4:
		os.system("cls")
		print("Pin must be 4 character!")
		start()

	else:
		result = [x for x in data if x["pin"]==pin]
		print(result)
		for i in result:
			if i["pin"]==pin:
				os.system("cls")
				print("Welcome! " + i['name'])
				print("Cash: $" + i['cash'])
				actions(i)
				break
			else:
				os.system("cls")
				print("Wrong Pin!")
				start()
				break

def actions(idata):
	print("\r\nWhat do you want to do?\r\n1) Withdraw\r\n2) Deposit\r\n99) Exit\r\n")
	choice = input()

	if choice == "99":
		quit()
	elif choice == "1":
		os.system("cls")
		Withdraw(idata)
	elif choice == "2":
		os.system("cls")
		Deposit(idata)
	else:
		os.system("cls")
		print("Invalid choice!")
		actions(idata)

def Deposit(i):
	print("Cash: $" + i['cash'])
	amount = input("\r\nHow much do you want to deposit on your account?")
	Saving("1", amount, i)

def Withdraw(i):
	print("Cash: $" + i['cash'])
	amount = input("\r\nHow much do you want to withdraw from your account?")
	Saving("2", amount, i)

def Saving(switch, amount, i):
	try:
		inputamount = int(amount)
		cashamount = int(i['cash'])
		totalamount = 1

		if switch == "1":
			totalamount = inputamount + cashamount
		else:
			totalamount = cashamount - inputamount

		printamount = str(totalamount)
		cashamount = str(cashamount)

		os.system("cls")
		print("Your new cash amount: $" + printamount)
		replace('data.json', cashamount, printamount)
	except:
		os.system("cls")
		print("You need to write number!")
		Deposit(i)

def replace(file_path, pattern, subst):
	creds.close()
	fh, abs_path = mkstemp()
	with fdopen(fh,'w', encoding="utf-8") as new_file:
		with open(file_path, encoding="utf-8") as old_file:
			for line in old_file:
				new_file.write(line.replace(pattern, subst))
	remove(file_path)
	move(abs_path, file_path)

start()

input()
