import csv

filepath = "A2/People.csv"

peoplefile = open(filepath,'r')

peopledata = []

readfile = csv.reader(peoplefile)

for person in readfile:
    if person[0].startswith("\ufeff"):
        person[0] = person[0][1:]
    peopledata.append(person)


for person in peopledata:
    print(person)