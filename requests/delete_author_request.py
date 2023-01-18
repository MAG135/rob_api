from typing import List

from pydantic import BaseModel


class DeleteAuthorsRequest(BaseModel):
    author: str


class DeleteAuthorsRequestList(BaseModel):
    authors: List[DeleteAuthorsRequest]
