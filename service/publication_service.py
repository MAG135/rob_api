from repository.publication_repository import *
from view.VideoModelView import VideoModelView


def get_publications_after_publication_id(publication_id_bookmark: int):
    publications = select_after_id(publication_id_bookmark)

    video_model_view_list = list()
    for p in publications:
        view = VideoModelView(p.id, p.publication_url, p.category, p.created_at)
        if p.publication_id != "-1":
            video_model_view_list.append(view)

    return video_model_view_list


def get_publications_by_category_after_publication_id(publication_id_bookmark: int, category: int):
    publications = select_by_category_after_id(publication_id_bookmark, category)

    video_model_view_list = list()
    for p in publications:
        view = VideoModelView(p.id, p.publication_url, p.category, p.created_at)
        if p.publication_id != "-1":
            video_model_view_list.append(view)

    return video_model_view_list
