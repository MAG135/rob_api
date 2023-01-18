from typing import List

from pydantic import BaseModel


class AddAuthorsRequest(BaseModel):
    author: str
    category: int


class AddAuthorsRequestList(BaseModel):
    authors: List[AddAuthorsRequest]
