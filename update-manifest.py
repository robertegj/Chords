import csv

# Read all chords from Chords dir



# Write them to a list
with open("Chords/chords-list.csv") as file:
    csvreader = csv.reader(file)
    chords = []
    for row in csvreader:
        chords.append(row[0])


print(chords)
print("...Added")
