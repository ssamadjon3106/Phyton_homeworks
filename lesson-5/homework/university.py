
def enrollment_stats(universities):
    Total1=0
    Total2=0
    enrollment=[row[1] for row in universities]
    Total1=sum(enrollment)
    tuition=[row[2] for row in universities]
    Total2=sum(tuition)
    print(f'Total students: {Total1}')
    print(f'Total tuition: ${Total2}')

def mean(universities):
    Total1=0
    Total2=0
    mean_s=0
    mean_t=0
    enrollment=[row[1] for row in universities]
    Total1=sum(enrollment)
    tuition=[row[2] for row in universities]
    Total2=sum(tuition)
    mean_s=Total1/len(universities)
    mean_t=Total2/len(universities)

    print(f'Student mean: {mean_s}')
    print(f'Tuition mean: {mean_t}')
    
def median(universities):
    median_1 = sorted([row[1] for row in universities])  
    median_2 = sorted([row[2] for row in universities])  
    n = len(universities)
    mid = n // 2  


    if n % 2 != 0: 
        median_11 = median_1[mid]
    else: 
        median_11 = (median_1[mid - 1] + median_1[mid]) / 2

   
    if n % 2 != 0:
        median_12 = median_2[mid]
    else:
        median_12 = (median_2[mid - 1] + median_2[mid]) / 2

    print(f'Student Median: {median_11}')
    print(f'Tuition Median: {median_12}')









universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
print('******************************')
enrollment_stats(universities)
mean(universities)
median(universities)

print("******************************")