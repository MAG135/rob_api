import traceback

from db.db import AuthorEntity
from repository import author_repository
from requests.add_author_request import AddAuthorsRequestList
from requests.delete_author_request import DeleteAuthorsRequestList


# Удаление автора
def delete_author(author: str):
    try:
        author_repository.delete_author(author)
        return True
    except Exception:
        print(traceback.format_exc())
        return False


# Удаление авторов
def delete_authors(request: DeleteAuthorsRequestList):
    authors = list()
    for r in request.authors:
        authors.append(r.author)
    print(authors)
    author_repository.set_is_deleted(authors)
    return True


# Добавление автора
def add_author(author: str, category: int):
    try:
        authors = list()
        author_repository.add_author(author, category)
        return True
    except Exception:
        print(traceback.format_exc())
        return False


# Добавление авторов
def add_authors(request: AddAuthorsRequestList):
    try:
        authors = list()
        for r in request.authors:
            authors.append(AuthorEntity(author_id=r.author,
                                        last_publication_id="",
                                        category=r.category,
                                        is_working=False))
        author_repository.add_authors(authors)
        return True
    except Exception:
        print(traceback.format_exc())
        return False
