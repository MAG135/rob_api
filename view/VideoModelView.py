class VideoModelView:
    def __init__(self, id: str, publication_url: str, category: int, created_at: int):
        self.id = id
        self.publication_url = publication_url
        self.category = category
        self.created_at = created_at
