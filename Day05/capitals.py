capital = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Dominican Republic": "Santo Domingo",
    "Japan": "Tokyo",
    "USA": "Washington D.C."
}

for country, city in sorted(capital.items()):
    print(f"The capital of {country} is {city}.")

print(f"\nTotal countries: {len(capital)}")

search = input("\nLook up a country: ")
print(capital.get(search, "Country not found!"))
