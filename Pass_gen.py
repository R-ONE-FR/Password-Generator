import sys
import os
from random import choice

charset = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN123456789!$%()+*-.=[]^"
password = ''

def main():
    print('\nPython Pass_gen.py [website name] [username] [number of characters]\n\nDescription :\n\n    Generate a random password for a website\n')

if len(sys.argv) == 4:
	file_name = str(sys.argv[1])
	print("\nSecure password :\n")
	for i in range(int(sys.argv[3])):
		password += str(choice(charset))
	print(password)
	os.system(f'type null > {file_name}.txt')
	os.system(f'echo Website : {file_name} Username : {str(sys.argv[2])} Password : {password}> {file_name}.txt')
	os.system(f'{file_name}.txt')
else:
	main()
