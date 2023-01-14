# OPening the first file

first=open('first.txt','r')
first_content = first.read()
print('Contents of first file are:\n',first_content)

# Opening third file for copying

third=open('third.txt','r')
third_content=third.read()

print('The contents of third file before copying are:\n',third_content)

# Writing in third.txt

third=open('third.txt','a') # 'a' for opening in append mode
third.write('\n')

for i in first_content:
    third.write(i.upper())

# Reading the contents after copying

third=open('third.txt','r')
third_content=third.read()
print('The contents of third file after copying are:\n',third_content)

first.close()
third.close()
