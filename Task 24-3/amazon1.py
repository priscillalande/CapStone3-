from statistics import mean#Importing the mean function

#defing functions
def min_func(numb_list):
    min_numb = min(numb_list)
    return f'The min of {numb_list} is {min_numb}'

#defing functions
def max_func(numb1_list):
    max_numb = max(numb1_list)
    return f'The max of {numb1_list} is {max_numb}'

#defing functions
def avg_func(numb2_list):
    avg_numb = mean(numb2_list)
    return f'The avg of {numb2_list} is {avg_numb}'

in_file = open("input.txt","r") # open our input file
out_file = open("output.txt","w")

#reading the first line
min_line = in_file.readline()
max_line = in_file.readline()
avg_line = in_file.readline()

min_values = [int(num) for num in min_line.strip("\n").split(":")[1].split(',')]
max_values = [int(num) for num in max_line.strip("\n").split(":")[1].split(',')]
avg_values = [int(num) for num in avg_line.strip("\n").split(":")[1].split(',')]

min_mesage = min_func(min_values)
max_mesage = max_func(max_values)
avg_mesage = avg_func(avg_values)

values = min_mesage , max_mesage , avg_mesage

out_file.write('\n'.join(values))

#print(min,max,avg_line)

in_file.close()
out_file.close()