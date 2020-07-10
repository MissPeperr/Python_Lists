# Lists (ordered, mutable & allows duplicates)

animals = ["Jack", "Noonan", "Blue", "Gypsy"]

junk = ["Fred", True, [1, 2, 3], 234]
print(f'testing OG List: {junk}')
print(f'testing OG List: {junk[0]}')

# Adding items to the list
junk.append(234)
junk.insert(0, "oh, I get it")
print(f'inserted: {junk}')
junk.extend(["Mary", "Joseph", "Bob"])
print(f'extended: {junk}')

# Negative indexing
junk[-1] = "The last item"
print(f'the last item --> {junk}')
print(f'negative indexing: {junk[-4]}')

# Loop through the items in a list
for taco in junk:
    print(f'in the LOOOOP {taco}')

# Javascript equivalent: junk.forEach(taco => console.log(taco));

# You can declare an empty list:
stuff = []

# Create a NEW list from a subset of values in another list with slice
my_list = [1, 2, 4, "hello", "monkey"]
my_subset = my_list[0:3]
my_subset = my_list[1:3]
my_subset = my_list[:3]
my_subset = my_list[2:]
print(my_subset)
print(my_list)