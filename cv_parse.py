from cv_extract import pdf_to_string
from decouple import config

HOME = config('HOME')
# $HOME/Downloads/cv.pdf
file_default = '%s/Downloads/cv.pdf' % HOME
file_pdf = input('Digite o caminho do arquivo: ') or file_default

# Transforma o texto numa lista
_words = pdf_to_string(file_pdf).split('\n')

# Remove espaços vazios nas extremidades do texto
words = [word.strip() for word in _words]
output = {}

names = ['Regis da Silva Santos']


def is_first_name(word):
    if word in names:
        output['first_name'] = word
        return word


def is_date(word):
    if datetime.strptime(word, '%m/%Y') == '%m/%Y':
        output['date'] = word
        return word


for word in words:
    if is_first_name(word):
        words.remove(is_first_name(word))
    if is_date(word):
        words.remove(is_date(word))

print(output)
