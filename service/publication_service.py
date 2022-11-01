from repository.publication_repository import select_after_id
from view.VideoModelView import VideoModelView


def get_publications_after_publication_id(publication_id_bookmark: int):
    publications = select_after_id(publication_id_bookmark)

    video_model_view_list = list()
    for p in publications:
        video_model_view_list.append(VideoModelView(p.id, p.publication_url))

    return video_model_view_list
