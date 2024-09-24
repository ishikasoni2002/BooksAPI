from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'book one', 'author': 'author one', 'category': 'science'},
    {'title': 'book two', 'author': 'author two', 'category': 'science'},
    {'title': 'book three', 'author': 'author three', 'category': 'math'},
    {'title': 'book four', 'author': 'author four', 'category': 'physics'},
    {'title': 'book five', 'author': 'author five', 'category': 'physics'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/")
async def get_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            return book


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)



@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == updated_book['title'].casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == book_title.casefold():
            BOOKS.pop(i)

@app.get("/books/find_book/{author_name}")
async def find_book_by_author(author_name: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'].casefold() == author_name.casefold():
            books_to_return.append(book)
    return books_to_return

