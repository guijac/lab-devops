#!/bin/bash

# Diretório dos arquivos que serão criados
DIR="././meus_arquivos"

# Cria o diretório, se não existir
mkdir -p "$DIR"

# Loop para criar 100 arquivos com o conteúdo da variável "i"
for i in $(seq 1 100); do
    # Nome do arquivo
    ARQUIVO="$DIR/arquivo_$i.txt"
    echo "$i" > "$ARQUIVO"
    echo "Arquivo $ARQUIVO criado com o conteúdo $i"
done

echo "Todos os 100 arquivos foram criados!"