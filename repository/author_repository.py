from db.db import AuthorEntity, tiktok_db


# Удаление автора
def delete_author(author: str):
    with tiktok_db:
        tiktok_db.connect(reuse_if_open=True)
        author = AuthorEntity.get(AuthorEntity.author_id == author)
        author.delete_instance()


# Удаление авторов
def delete_authors(authors: list[str]):
    with tiktok_db:
        tiktok_db.connect(reuse_if_open=True)
        AuthorEntity.delete().where(AuthorEntity.author_id.in_(authors)).execute()


# Добавление автора
def add_author(author: str, category: int):
    with tiktok_db:
        tiktok_db.connect(reuse_if_open=True)
        author = AuthorEntity(
            author_id=author,
            last_publication_id="",
            category=category,
            is_working=False)
        author.save()


# Добавление авторов
def add_authors(authors: list[AuthorEntity]):
    with tiktok_db:
        tiktok_db.connect(reuse_if_open=True)
        AuthorEntity.bulk_create(authors)
