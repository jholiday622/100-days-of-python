phonebook = {
    "Jason Davis": "323-777-7562",
    "Omar Williams": "323-762-9088",
    "Derrick Johnson": "323-777-7562",
    "Michael Brown": "323-762-9088"
}

search = input("Enter a name: ")
if search in phonebook:
    print(f"{search}'s number is {phonebook[search]}")
else:
    print("Contact not found")