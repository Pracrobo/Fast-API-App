from fastapi import FastAPI, Body

app = FastAPI()
BOOKS = [
    {'bookId' : 1, 'title' : 'Title-one', 'author' : 'Author-one', 'year' : 'Year-one', 'category' : 'Science'},
    {'bookId' : 2, 'title': 'Title-two', 'author': 'Author-two', 'year': 'Year-one', 'category': 'Science'},
    {'bookId' : 3, 'title': 'Title-three', 'author': 'Author-three', 'year': 'Year-one', 'category': 'Science'},
    {'bookId' : 4, 'title': 'Title-four', 'author': 'Author-four', 'year': 'Year-one', 'category': 'history'},
    {'bookId' : 5, 'title': 'Title-five', 'author': 'Author-five', 'year': 'Year-one', 'category': 'math'},
    {'bookId' : 6, 'title': 'Title-six', 'author': 'Author-one', 'year': 'Year-one', 'category': 'math'},

]
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author : str, category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
            book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

