import pyperclip

# Defining a file name
input_file = input('enter file name: ')
file_name = input_file + ".txt"

# Create an input for users to enter in text
with open(file_name, "w") as file:
	print("enter the details in and hit enter to create a new line. Type 'done' to finish")

	while True:
		user_input =input()
		if user_input.lower() == 'done':
			break
		else:
			file.write(user_input + "\n")
print(f"Input saved to {file_name}")

# copy to clipboard
with open(file_name, 'r') as file:
	file_content = file.read()
	pyperclip.copy(file_content)
print("Content copied to clipboard")