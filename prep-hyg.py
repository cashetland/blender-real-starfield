import csv

in_filename = "/home/shetland91/Documents/Blender Projects/HYG-Database/hyg/v3/hyg_v35.csv" # Change path or filename if needed
out_filename = "/home/shetland91/Documents/Blender Projects/starlist.csv"
out_filename_named = "/home/shetland91/Documents/Blender Projects/starlist-named.csv"

proper_name_column = 6
dist_column = 9

# We'll filter the stars by distance. If you want to limit the number of star markers due to render resource constraints, try setting
# the distance_filter to a lower value
distance_filter = 50 # 8750 stars as of v3.5

starlist = []
namedstarlist = []
skip_count = 0

def getDistance(row):
    try:
        distance = float(row[dist_column])
    except Exception:
        return 10000000 # Discard any entries without valid distance values (a large value will exclude them)
    return distance

with open(in_filename) as csvfile:
    csvReader = csv.reader(csvfile)
    for i, row in enumerate(csvReader):
        if i == 0: # Copy column titles
            starlist.append(row)
            namedstarlist.append(row)
        if getDistance(row) > distance_filter:
            skip_count += 1
        else:
            starlist.append(row)
            if row[proper_name_column] != '':
                namedstarlist.append(row)

    print("Found ", len(starlist), " entries")
    print("Found ", len(namedstarlist), " with names")
    print("Skipped ", skip_count, " entries further than ", distance_filter, " parsecs from Earth")

    with open(out_filename, 'w') as outfile:
        csvWriter = csv.writer(outfile)
        for i, row in enumerate(starlist):
            csvWriter.writerow(row)
            #print(row[0], "\t\t", row[dist_column], "\t\t", row[proper_name_column])

    with open(out_filename_named, 'w') as outfile:
        csvWriter = csv.writer(outfile)
        for i, row in enumerate(namedstarlist):
            csvWriter.writerow(row)
            #print(row[0], "\t\t", row[dist_column], "\t\t", row[proper_name_column])
