import csv
import operator

sample = open ('data_task3.csv', 'rb')
#reader = csv.reader((line.replace('/t', ',') for line in sample), delimiter=',')
csv1 = csv.reader ( sample, delimiter=',' )
key = 0

sort = sorted( csv1, key=operator.itemgetter(0))
for eachline in sort:
    key = key + 1
    print (eachline)
print(key)

# step 1: collect all the unique names of assessors ( uid ) in the array
# step 2: add to each assessor +1 score for every correctly solved task ( i.e. jud == cjud )
# step 3: sort the array of assessors asc order by their points
# step 4: show the result
