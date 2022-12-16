from fastapi import FastAPI

from service.publication_service import *

app = FastAPI()


@app.get("/{publication_id_bookmark}")
async def get_publication_by_bookmark(publication_id_bookmark: int):
    return get_publications_after_publication_id(publication_id_bookmark)


@app.get("/{publication_id_bookmark}/category/{category}")
async def get_publication_by_bookmark_and_category(publication_id_bookmark: int, category: int):
    return get_publications_by_category_after_publication_id(publication_id_bookmark, category)
