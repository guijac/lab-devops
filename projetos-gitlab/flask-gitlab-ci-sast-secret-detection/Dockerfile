# Especificação da imagem Docker a ser utilizada, neste caso a imagem Python 
# oficial da Docker do tipo "Alpine", mais "enxuta"
FROM python:3-alpine

# Para fins de organização, devemos definir o diretório de trabalho do contêiner, 
# aqui todos os comandos serão executados, além da sua própria aplicação.
WORKDIR /my-flask-app

# Realiza a cópia do diretório da nossa aplicação (/app) para o diretório (workdir) 
# do contêiner.
COPY /app /my-flask-app
COPY requirements.txt /my-flask-app

# Mantém o gerenciador de pacotes (pip) atualizado, independente da imagem base. 
RUN pip3 install --upgrade pip

# Executa a instalação da dependência do projeto, uma boa prática é justamente
# especificar estas dependências em um arquivo texto. 
RUN pip3 install -r /my-flask-app/requirements.txt

# Instrução para a execução da aplicação do contêiner, a mesma coisa que
# python -m flask run --host=0.0.0.0
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]