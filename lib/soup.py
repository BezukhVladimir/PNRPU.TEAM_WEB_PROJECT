from bs4 import BeautifulSoup


def get_soup(file_path):
    file = open(file_path)
    soup = BeautifulSoup(file, "lxml")
    file.close()
    return soup
