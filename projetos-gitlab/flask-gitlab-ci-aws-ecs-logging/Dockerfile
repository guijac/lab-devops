# Especificação da imagem Docker a ser utilizada, neste caso a imagem Python 
# oficial da Docker do tipo "Alpine", mais "enxuta"
FROM python:3-alpine

# Dependências Linux para a instalação do uWSGI dentro do contêiner.
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
RUN apk add --no-cache pcre

# Para fins de organização, devemos definir o diretório de trabalho do contêiner, 
# aqui todos os comandos serão executados, além da sua própria aplicação.
WORKDIR /my-flask-app-ecs

# Opcional para contêineres com uma única aplicação ou sem "multi-stage build":
# Empacota todas as dependências do projeto precisa e armazena em um diretório(VIRTUAL_ENV), 
# desta forma, nenhum pacote é instalado diretamente no sistema operacional/contêiner.
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Realiza a cópia do diretório da nossa aplicação (/app) para o diretório (workdir) 
# do contêiner.
COPY /app /my-flask-app-ecs
COPY requirements.txt /my-flask-app-ecs

# Mantém o gerenciador de pacotes (pip) atualizado, independente da imagem base. 
RUN pip install --upgrade pip

# Executa a instalação da dependência do projeto, uma boa prática é justamente
# especificar estas dependências em um arquivo texto. 
RUN pip3 install -r /my-flask-app-ecs/requirements.txt

# Dependências que podem ser removidas após a instalação do uWSGI
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

# Instrução para a execução da aplicação do contêiner, a mesma coisa que
# python -m flask run --host=0.0.0.0
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# Para ambientes de produção, deve-se utilizar um servidor próprio (uWSGI)
# também exposto na porta 5000, mas que trata mais requisições simultâneas.
EXPOSE 5000
CMD ["uwsgi", "--ini", "/my-flask-app-ecs/uwsgi.ini"]