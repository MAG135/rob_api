from fastapi import FastAPI
from starlette.responses import JSONResponse

from requests.add_author_request import AddAuthorsRequestList
from requests.delete_author_request import DeleteAuthorsRequestList
from service import author_service
from service.publication_service import *

app = FastAPI()


@app.get("/{publication_id_bookmark}")
async def get_publication_by_bookmark(publication_id_bookmark: int):
    return get_publications_after_publication_id(publication_id_bookmark)


@app.get("/{publication_id_bookmark}/category/{category}")
async def get_publication_by_bookmark_and_category(publication_id_bookmark: int, category: int):
    return get_publications_by_category_after_publication_id(publication_id_bookmark, category)


@app.post("/authors/{author}/delete")
async def delete_author(author: str):
    return JSONResponse({"status:": author_service.delete_author(author)})


@app.post("/authors/delete")
async def delete_author_list(request: DeleteAuthorsRequestList):
    return JSONResponse({"status": author_service.delete_authors(request)})


@app.post("/authors/{author}/category/{category}/add")
async def add_author(author: str, category: int):
    return JSONResponse({"status:": author_service.add_author(author, category)})


@app.post("/authors/add")
async def add_author_list(request: AddAuthorsRequestList):
    return JSONResponse({"status:": author_service.add_authors(request)})
