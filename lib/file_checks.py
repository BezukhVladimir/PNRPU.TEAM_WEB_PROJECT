import os.path


def does_file_not_exist_or_is_empty(file_path):

    return (not os.path.isfile(file_path)) or (os.path.getsize(file_path) == int(0))
