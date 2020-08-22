import json
import random
import time


def india_current_affairs(n):
	print(f'\nWelcome {n}')
	print("\n==========QUIZ START==========")
	score = 0
	with open("Questions\India Current Affairs [Nation & States].json", 'r+') as f:
		j = json.load(f)
		for i in range(20):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ").strip()
			if j[ch]["answer"][0] == answer[0].upper():
				print("\n{},you are correct Great".format(n))
				score+=1
			else:
				print("\n{},you are incorrect Oops".format(n))
				score-=0.25
			del j[ch]
		print(f'\n{n},yours final score: {score}\nThank you,{n}')
		time.sleep(30)


def science_and_technology(n):
	print(f'\nWelcome {n}')
	print("\n==========QUIZ START==========")
	score = 0
	with open("Questions\Science and Technology.json", 'r+') as f:
		j = json.load(f)
		for i in range(20):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ").strip()
			if j[ch]["answer"][0] == answer[0].upper():
				print("\n{},you are correct Great".format(n))
				score+=1
			else:
				print("\n{},you are incorrect Oops".format(n))
				score-=0.25
			del j[ch]
		print(f'\n{n},yours final score: {score}\nThank you,{n}')
		time.sleep(30)


def general_knowledge(n):
	print(f'\nWelcome {n}')
	print("\n==========QUIZ START==========")
	score = 0
	with open("Questions\GK Questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(20):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ").strip()
			if j[ch]["answer"][0] == answer[0].upper():
				print("\n{},you are correct Great".format(n))
				score+=1
			else:
				print("\n{},you are incorrect Oops".format(n))
				score-=0.25
			del j[ch]
		print(f'\n{n},yours final score: {score}\nThank you,{n}')
		time.sleep(30)

def sports_general_knowledge(n):
	print(f'\nWelcome {n}')
	print("\n==========QUIZ START==========")
	score = 0
	with open("Questions\Sports GK Questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(20):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ").strip()
			if j[ch]["answer"][0] == answer[0].upper():
				print("\n{},you are correct Great".format(n))
				score+=1
			else:
				print("\n{},you are incorrect Oops".format(n))
				score-=0.25
			del j[ch]
		print(f'\n{n},yours final score: {score}\nThank you,{n}')
		time.sleep(30)

def business_economy_banking_current(n):
	print(f'\nWelcome {n}')
	print("\n==========QUIZ START==========")
	score = 0
	with open("Questions\Business, Economy & Banking Current.json", 'r+') as f:
		j = json.load(f)
		for i in range(20):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ").strip()
			if j[ch]["answer"][0] == answer[0].upper():
				print("\n{},you are correct Great".format(n))
				score+=1
			else:
				print("\n{},you are incorrect Oops".format(n))
				score-=0.25
			del j[ch]
		print(f'\n{n},yours final score: {score}\nThank you,{n}')
		time.sleep(30)


if __name__ == "__main__":
	print('\n=========WELCOME TO QUIZ MASTER==========')
	print('-----------------------------------------')
	n=input('Enter yours name: ').strip()
	print('\n  ***************Rules*****************\na> Correct answer plus 1.00 point. \n   Wrong answer minus 0.25 points.  \nb> {},5 sections will be given you have to Choose 1 section to attend the Test.'.format(n))
	print('  \n\nSections \n a>India Current Affairs[Nation & States] \n b>Science and Technology \n c>General Knowledge  \n d>Sports General Knowledge \n e>Business, Economy & Banking Current')
	choice = input('\nEnter Your Choice: ').strip().lower()
	if choice == 'a':
		india_current_affairs(n)
	elif choice == 'b':
		science_and_technology(n)
	elif choice == 'c':
		general_knowledge(n)
	elif choice == 'd':
		sports_general_knowledge(n)
	elif choice == 'e':
		business_economy_banking_current(n)
	else:
		print('\nWRONG INPUT.Sorry')
