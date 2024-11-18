messi_dict = {
    'name': "Lionel",
    'surname': "Messi",
    'age': 40,
    'team': "Barcelona",
    'sport': "football"
}

print(messi_dict)
print(messi_dict.items())



book_dict = {
    'Harry Potter': 1999,
    'Warlock of the magus world': 2015
}

print("\n", book_dict)

book_dict.update({'Reverend Insanty': 2012})

print(book_dict)


capital_country = "USA"
# capital_country = "Ukraine"
# capital_country = "France"

country_dict = {
    'Ukraine': 'Kiev',
    'Poland': 'Warszawa',
    'USA': 'Washington',
    'German': 'Berlin'
}

if capital_country in country_dict:
    print(f"\nCapital of {capital_country} is {country_dict[capital_country]}")
else:
    print(f"\nThere are no {capital_country} in dictenory")

