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

# collect all the unique names of assessors ( uid ) in the array
# add to each name +1 score for every correctly solved task ( jud == cjud )
# sort and print array of assessors by their points and show their scores
