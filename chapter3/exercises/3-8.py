locations = ['dubai', 'maldives', 'newyork', 'brisbane', 'greenland']
print(f"raw list: {locations}")
sorted_locations = sorted(locations)
print(f"sorted : {sorted_locations}")
print(f"original: {locations}")

#reverse alphametical order
reverse_sort = sorted(locations, reverse=True)
print(f"reverse sorted : {reverse_sort}")

#reverse list
locations.reverse()
print(f"reversed list: {locations}")
locations.reverse()
print(f"back to original: {locations}")

#using sort

locations.sort()
print(f"Sorted locations: {locations}")
locations.sort(reverse=True)
print(f"Reverse sorted locations: {locations}")