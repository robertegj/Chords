import csv
from os import walk


# Read all chords from Chords dir
filenames = next(walk('Chords'), (None, None, []))[2]  # [] if no file
print(filenames)

# Write them to a list 
with open("Chords/chords-list.csv", 'w', encoding='UTF8') as file:
    csvwriter = csv.writer(file)
    for row in filenames:
        print([row])
        csvwriter.writerow([row])
