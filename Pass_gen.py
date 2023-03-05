import sys
import os
from random import choice

charset = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN123456789!$%()+*-.=[]^"
password = ''
file_name = 'Password_manager.txt'

def main():
    print('\nPython Pass_gen.py [website name] [username] [number of characters]\n\nDescription :\n\n    Generate a random password for a website\n')

if len(sys.argv) == 4:
	print("\nSecure password :\n")
	#print(i,end="")for i in range(int(sys.argv[1]))
	for i in range(int(sys.argv[3])):
		password += str(choice(charset))
	print(password)
	os.system('type null > Password_manager.txt')
	os.system('echo Website : ' + str(sys.argv[1]) + ' Username : ' + str(sys.argv[2]) + ' Password : ' + password + ' > ' + file_name)
	os.system(file_name)
else:
	main()

