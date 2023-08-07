message = input("Please enter a sentence:")
message = message.lower()

new_message = ''
for char in message:
    if ord(char) >= 97 and ord(char) <= 122:
        new_message +=  chr((ord(char) + 5-97) % 26 + 97)
    else:
        new_message +=  char
    
print("The encrypted sentence is: " + new_message)
