class VideoModelView:
    def __init__(self, id: str, publication_url: str, category: int, author_unique_id: str, created_at: int):
        self.id = id
        self.publication_url = publication_url
        self.category = category
        self.author_unique_id = author_unique_id
        self.created_at = created_at
