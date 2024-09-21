#!/bin/bash

# Definir diretórios de origem e destino
DIR_ORIGEM="./meus_arquivos"
DIR_BACKUP="./meu_backup"

# Verificar se o diretório de backup existe, se não, criá-lo
if [ ! -d "$DIR_BACKUP" ]; then
  mkdir -p "$DIR_BACKUP"
fi

# Data atual para adicionar ao nome dos arquivos de backup
DATA=$(date +%Y%m%d)

# Loop para copiar e renomear arquivos com a data atual
for arquivo in "$DIR_ORIGEM"/*; do
  nome_arquivo=$(basename "$arquivo")
  cp "$arquivo" "$DIR_BACKUP/${nome_arquivo}_backup_$DATA"
  echo "Arquivo $nome_arquivo copiado para $DIR_BACKUP como ${nome_arquivo}_backup_$DATA"
done

echo "Backup completo."
