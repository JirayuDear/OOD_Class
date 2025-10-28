def manage_book(shelf, order):
    price = 0
    not_found_cache = set()

    for item in order:
        if item in shelf:
            index_on_shelf = shelf.index(item)
            print(f"Search {item} -> found at {shelf.index(item) + 1} move to front ->  ", end="")
            price += shelf.index(item) + 1
            book = shelf.pop(index_on_shelf)
            shelf.insert(0, book)
            print(*shelf)
        elif item in not_found_cache:
            print(f"Search {item} -> add new book ->  ", end="")
            price += 1
            shelf.insert(0, item)
            print(*shelf)
        else:
            print(f"Search {item} -> not found -> ", end="")
            price += len(shelf) + 1
            not_found_cache.add(item)
            print(*shelf)

    return shelf, price

print("This is your BOOK!!!")
inp = input("Enter input: ").split("/")
shelf = inp[0].split(" ")
order = inp[1].split(" ")

shelf, price = manage_book(shelf, order)
print()
print(f"Final books: ", end="")
print(*shelf)
print(f"Total cost: {price}")