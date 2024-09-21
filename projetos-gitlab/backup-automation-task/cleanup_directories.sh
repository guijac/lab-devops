#!/bin/bash

# Loop para remover cada diretório e seu conteúdo
for dir in meus_arquivos meu_backup; do
  if [ -d "$dir" ]; then
    # Remove o diretório e seu conteúdo
    rm -rf "$dir"
    echo "Diretório $dir e todo o seu conteúdo foram removidos."
  else
    echo "Diretório $dir não existe."
  fi
done

echo "Todos os diretórios foram processados."