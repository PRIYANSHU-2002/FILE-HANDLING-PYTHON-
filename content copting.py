first = open('first.txt')  # default mode is read
print('Contents of first file:\n')
first_read = first.read()
print(first_read)

print('Initial content of second file:\n')
second = open('second.txt','rt')  # r represents read mode
                               # t represents text file
print(second.read())


second = open('second.txt','a') # a for append mode

second.write('\n')
second.write(first_read)



print('The second file after copying from first file:\n')
second = open('second.txt','r')
print(second.read())

first.close()
second.close()
