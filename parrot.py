import sys

prompt = ("\nTell me something, and I will repeat it back to you:")
prompt += ("\nEnter 'quit' to end the program. ")

message = input()

while message != "quit":
     print(message)
if message == "quit":
    sys.exit
