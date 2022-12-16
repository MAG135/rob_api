from db.db import PublicationEntity, tiktok_db


# Получение публикаций, у которых id больше заданного
def select_after_id(primary_key_id: int):
    with tiktok_db:
        tiktok_db.connect(reuse_if_open=True)
        return PublicationEntity.select().where(PublicationEntity.id > primary_key_id)


# Получение публикаций из категории, у которых id больше заданного
def select_by_category_after_id(primary_key_id: int, category: int):
    with tiktok_db:
        tiktok_db.connect(reuse_if_open=True)
        return PublicationEntity.select().where(
            (PublicationEntity.id > primary_key_id) & (PublicationEntity.category == category))
