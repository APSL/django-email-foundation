import os


def get_relative_from_manage_path(path: str) -> str:
    """
    In some cases we could have the manage.py inside the distinct folder where are gulpfile. It's could
    cause problems. This method return the relative path from the manage.py script.
    :return:
    """
    current_split = os.getcwd().split('/')
    path_split = path.split('/')
    response = [part for part in path_split if part not in current_split]
    response = '/'.join(response)
    return response
