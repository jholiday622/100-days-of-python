# Create a dictionary
person = {
    "name": "Holiday",
    "age": 49,
    "city": "California"
}

# Access a value
print(person["name"])        # Holiday

# Add or update
person["job"] = "Cloud Architect"

# Delete
del person["age"]

# Loop through
for key, value in person.items():
    print(key, ":", value)

# Check if key exists
if "city" in person:
    print("Found it!")

# Get with default (safe - won't crash)
print(person.get("salary", "Not found"))