# Especificação da imagem Docker a ser utilizada, neste caso a imagem Python 
# oficial da Docker
FROM python:3.8-slim-buster

# Para fins de organização, devemos definir o diretório de trabalho do contêiner, 
# aqui todos os comandos serão executados, além da sua própria aplicação.
WORKDIR /my-flask-app-docker

# Realiza a cópia do arquivo existente em nosso diretório para o diretório 
# (workdir) do contêiner
COPY requirements.txt requirements.txt

# Executa a instalação da dependência do projeto, uma boa prática é justamente
# especificar estas dependências em um arquivo texto. 
RUN pip3 install -r requirements.txt

# Realiza a cópia dos demais arquivos em nosso diretório, para o diretório do
# contêiner (em nosso exemplo, arquivo app.py e Dockerfile)
COPY . .

# Instrução para a execução da aplicação do contêiner, a mesma coisa que
# python -m flask run --host=0.0.0.0
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]