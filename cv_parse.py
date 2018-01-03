from cv_extract import pdf_to_string
from datetime import datetime
from decouple import config
from splitty import (
    clear_list_strings,
    list_by_list,
    list_by_re_pattern,
    find_elements,
    make_intervals,
    apply_intervals)


def cv_parse(cv: list) -> dict:
    pattern = r'(\w+|WORK EXPERIENCE|EDUCATION)'

    list_pattern = list_by_re_pattern(cv, pattern)

    topics = ['WORK EXPERIENCE', 'EDUCATION']

    find_topics = find_elements(cv, topics)

    # Inserindo o elemento no começo da lista
    find_topics.insert(0, list_pattern[0])

    intervals = make_intervals(find_topics)

    res = apply_intervals(cv, intervals)

    # Insere uma chave 'meta' no começo da lista
    res[0].insert(0, 'meta')

    dic = {x[0]: x[1:] for x in res}

    return dic


cvs = ['cv.txt', 'cv2.txt', 'cv3.txt']


for cv in cvs:
    with open(cv) as text:
        print(cv_parse(clear_list_strings(text.read().split('\n'))))
