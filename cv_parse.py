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


def is_first_name(word):
    if word == 'Regis da Silva Santos':
        output['first_name'] = word
        return word


for word in words:
    if is_first_name(word):
        words.remove(is_first_name(word))

print(output)
