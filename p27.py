string=input("Enter the string:").split()
i=0
for word in string:
    if len(word)>i:
    	i=len(word)
print('The longest word is: '+ word)