import matplotlib.pyplot as plt
import os.path

# Sets the home directory of this file.
directory = os.path.dirname(os.path.abspath(__file__))

# Names two lists to be used to store data of average salaries for certain school districts.
district=[]
average_salary=[]

# Runs a for loop to look through the files of the 16 districts.
for dn in range(1,16):

    # Declares variables to store the total salary of HS district employees and a counter to
    # keep track of how many employee's salaries were added.
    total_salary=0
    counter=0
    
    # Opens the files in succession.
    filename = os.path.join(directory, 'district'+str(dn)+'.csv')
    datafile = open(filename,'r')
    
    # Skips over the header row in each file.
    next(datafile)
    
    # Looks through each row; separates each piece of data in each row; and stores
    # two of those pieces of data into variables to reference later.
    for line in datafile:
        line_data = line.split(',')
        title = line_data[1]
        salary = line_data[2]
        
        # Checks to see if the row of data represents a HS teacher's salary or not.
        if title == 'TCHR 9-12' or title == 'TEACHER SECONDARY' or title == 'TEACHER HIGH SCHOOL' or title == 'TEACHER' or title == 'HIGH SCHOOL TEACHER' or title == 'Teacher 9-12' or title == 'TEACHER REGULAR' or title == 'TEACHER 9-12':
            
            # If teacher meets criteria, their salary gets added to a list and 
            # the counter increases by one.
            counter = counter+1
            total_salary = total_salary + float(salary)
    
    if counter != 0:
        average_salary.append(float(total_salary)/float(counter))
    else:
        average_salary.append(0)
    district.append(dn)
    
    datafile.close()

fig, ax = plt.subplots(1,1)
for dn in range(len(district)):
    if dn !=2:
        ax.bar(district[dn], average_salary[dn], 0.8, color='blue')
    else:
        ax.bar(district[dn], average_salary[dn], 0.8, color='red')
ax.hlines(y=average_salary[2], xmin=0, xmax=len(district)+1, label='Average Capistrano Salary', color='black', linestyle='dashed')
ax.set_title('Average Salaries of Orange County School Districts (mostly high schools).')
fig.show()