import os

# Diretório onde os arquivos serão criados
dir_name = "./meus_arquivos"

# Cria o diretório, se não existir
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

# Loop para criar 100 arquivos com o conteúdo da variável "i"
for i in range(1, 101):
    # Nome do arquivo
    file_name = os.path.join(dir_name, f"arquivo_{i}.txt")
    
    # Abre o arquivo em modo de escrita e escreve o número
    with open(file_name, 'w') as file:
        file.write(f"{i}\n")
    
    # Exibe uma mensagem indicando o arquivo criado
    print(f"Arquivo {file_name} criado com o conteúdo {i}")

print("Todos os 100 arquivos foram criados!")