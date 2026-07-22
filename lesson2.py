# Create a dictionary representing a "book"
book = {
    "title": "Harry potter",
    "author": "Harrry",
    "pages": 5000
}

# Write a function called describe_book that takes a book dictionary
# and returns a sentence like: "Dune by Frank Herbert has 412 pages"

def describe_book(book):
    return f"{book['title']} by {book['author']} has {book['pages']} pages"
    pass

print(describe_book(book))