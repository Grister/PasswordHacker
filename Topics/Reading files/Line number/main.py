# read sample.txt and print the number of lines
with open('sample.txt', 'r') as file:
    my_list = file.readlines()
    print(len(my_list))