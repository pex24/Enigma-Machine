"""Takes in file and Write out Encryptic text to a file"""

work_file = input('enter a file name')


read_file = open (work_file, 'r')

#using read gives str and readlines give list of str
file_to_encrypt = read_file.read()

#run encrpyction

if ('Encrypted') in str(work_file):
	new_file_name = 'Decrypted' + str(work_file)
	decrypted_file = open(new_file_name, 'w+')
	decrypted_file.write(file_to_encrypt)
else:
	new_file_name = 'Encrypted' + str(work_file)
	encrypted_file = open(new_file_name, 'w+')
	encrypted_file.write(file_to_encrypt)
