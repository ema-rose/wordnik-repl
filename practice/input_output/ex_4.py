my_file = open("text.txt", "r")

print my_file.readline()
print my_file.readline()
print my_file.readline()

# If you open a file and call .readline() on the file object, \ 
you'll get the first line of the file; \ 
subsequent calls to .readline() will return successive lines.

my_file.close()

# don't forget to close!
