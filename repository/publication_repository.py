from db.db import PublicationEntity


# Получение побликаций, у которых id больше заданного
def select_after_id(primary_key_id: int):
    return PublicationEntity.select().where(PublicationEntity.id > primary_key_id)
