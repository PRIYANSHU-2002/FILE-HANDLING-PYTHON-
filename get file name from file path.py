# Defining the file path
path = input('Enter the complete file path to extract file name from it:\n')

# Splitting the file path with '\' as separator

path_split=path.split('\\')

# Accessing the last element of the list which will be the file name

last=path_split[-1]

print('The file name extracted from given path is :\n',last)
