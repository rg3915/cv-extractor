from splitty import (clear_list_strings, find_elements,
                     make_intervals, apply_intervals)


def cv_parse(cv: list) -> dict:
    topics = ['WORK EXPERIENCE', 'EDUCATION']

    find_topics = find_elements(cv, topics)

    intervals = make_intervals(find_topics, start=True)

    res = apply_intervals(cv, intervals)

    # Insere uma chave 'meta' no começo da lista
    res[0].insert(0, 'meta')

    dic = {x[0]: x[1:] for x in res}

    return dic


cvs = ['cv.txt', 'cv2.txt', 'cv3.txt']

for cv in cvs:
    with open(cv) as text:
        print(cv_parse(clear_list_strings(text.read().split('\n'))))
