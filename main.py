import os
import json
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import random

creds = open('data.json', encoding="utf-8")
 
filename = "data.json"

data = json.load(creds)

randgen = random.randrange(000000, 999999)
randgen = str(randgen)

def start():
	print("|---|BANK|---|\r\n")
	print("If you want to make new account, enter following: " + randgen)
	pin = input("\r\nPlease insert your PIN to account: ")

	if pin == randgen:
		os.system("cls")
		Createacc()

	if len(pin) != 4:
		os.system("cls")
		print("Pin must be 4 character!")
		start()

	else:
		result = [x for x in data if x["pin"] == pin]
		if result==[]:
			os.system("cls")
			print("Wrong Pin!")
			start()
		else:
			for i in result:
				if i["pin"]==pin:
					os.system("cls")
					print("Welcome! " + i['name'])
					print("Cash: $" + i['cash'])
					actions(i)
				else:
					os.system("cls")
					print("Wrong Pin!")
					start()

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
		print("Welcome! " + idata['name'])
		print("Cash: $" + idata['cash'])
		actions(idata)

def Deposit(i):
	print("Cash: $" + i['cash'])
	amount = input("\r\nHow much do you want to deposit on your account?")
	Saving("1", amount, i)

def Withdraw(i):
	print("Cash: $" + i['cash'])
	amount = input("\r\nHow much do you want to withdraw from your account?")
	Saving("2", amount, i)

def Createacc():
	name = input("Enter your full name: ")
	pin = random.randrange(0000, 9999)
	pin = str(pin)
	name = str(name)
	cash = "20"

	print("Your pin to login: " + pin)

	with open(filename, encoding="utf-8") as fp:
		listObj = json.load(fp)

	listObj.append({
		"pin": pin,
		"name": name,
		"cash": cash
	})

	with open(filename, 'w') as json_file:
		json.dump(listObj, json_file, indent=4,  separators=(',',': '))

	input()
	quit()

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