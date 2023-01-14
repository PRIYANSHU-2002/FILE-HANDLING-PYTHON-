first = open('first.txt')  # default mode is read
print('Contents of first file:')
first_read = first.read()
print(first_read)
print()

print('Initial content of second file:')
second = open('second.txt','rt')  # r represents read mode
                               # t represents text file
print(second.read())
print()

# Making list of words in first file

l = first_read.split()

# Reversing the contents of first file

reverse = l[::-1]


second = open('second.txt','a') # a for append mode

second.write('\n')
for i in reverse:
    second.write('\t')
    second.write(i)



print('The second file after copying from first file:\n')
second = open('second.txt','r')
print(second.read())

first.close()
second.close()

