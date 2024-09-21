import os
import shutil
from datetime import datetime

# Definir diretórios de origem e destino
dir_origem = './meus_arquivos'
dir_backup = './meu_backup'

# Verificar se o diretório de backup existe, se não, criá-lo
if not os.path.exists(dir_backup):
    os.makedirs(dir_backup)

# Data atual para adicionar ao nome dos arquivos de backup
data_atual = datetime.now().strftime('%Y%m%d')

# Loop para copiar e renomear arquivos com a data atual
for nome_arquivo in os.listdir(dir_origem):
    caminho_arquivo = os.path.join(dir_origem, nome_arquivo)
    
    # Verifica se é um arquivo antes de copiar
    if os.path.isfile(caminho_arquivo):
        nome_backup = f"{nome_arquivo}_backup_{data_atual}"
        caminho_backup = os.path.join(dir_backup, nome_backup)
        
        # Copiar o arquivo para o diretório de backup
        shutil.copy2(caminho_arquivo, caminho_backup)
        print(f"Arquivo {nome_arquivo} copiado para {caminho_backup}")

print("Backup completo.")
