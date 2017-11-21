from cv_extract import pdf_to_string

texto = (pdf_to_string('cv.pdf'))

nome = []
data = []
sexo = []
endereco = []
local = []
estadoc = []
cep = []
telefone = []
email = []

for line in texto.split('\n'):
    if "Nome:" in line:
        nome.append(line.strip())

for line in texto.split('\n'):
    if "Data de" in line:
        data.append(line.strip())

for line in texto.split('\n'):
    if "Sexo:" in line:
        sexo.append(line.strip())

for line in texto.split('\n'):
    if "Endere" in line:
        endereco.append(line.strip())

for line in texto.split('\n'):
    if "Local" in line:
        local.append(line.strip())

for line in texto.split('\n'):
    if "Estado " in line:
        estadoc.append(line.strip())

for line in texto.split('\n'):
    if "CEP" in line:
        cep.append(line.strip())

for line in texto.split('\n'):
    if "Telefone:" in line:
        telefone.append(line.strip())

for line in texto.split('\n'):
    if "E-mail" in line:
        email.append(line.strip())

print(nome, data, sexo, endereco, local, estadoc, cep, telefone, email)
