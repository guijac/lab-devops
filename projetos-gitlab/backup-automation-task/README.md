# Backup Automation Task

Simples coleção de scripts Python e Bash para criação de arquivos, demonstração de uma rotina de backup e comparação de desempenho.

# Requisitos

Ambiente Unix-like (como MacOS ou Linux) ou Windows com Git Bash.

## Criando os arquivos (Bash)

```
$ bash/create-files.sh
$ bash/backup-files.sh
```

## Criando os arquivos (Python)

```
$ python python/create-files.py
$ python python/backup-files.py
```

## Comparando performance

O comando time é utilizado para medir quanto tempo um processo leva para ser executado. Ele reporta três tipos de tempo:

- real: Tempo total de execução (tempo do relógio);
- user: Tempo gasto pela CPU no modo de usuário;
- sys: Tempo gasto pela CPU no modo do kernel (por exemplo, operações de I/O).

```
$ time bash/create-files.sh

real    0m0.164s
user    0m0.015s
sys     0m0.015s

$ time bash/backup-files.sh

real    0m7.101s
user    0m0.091s
sys     0m0.393s
```

```
$ ./cleanup_directories.sh
```

```
$ time python python/create-files.py

real    0m0.170s
user    0m0.000s
sys     0m0.000s

$ time python python/backup-files.py

real    0m0.250s
user    0m0.000s
sys     0m0.000s
```

## Finalizando

Este procedimento irá remover todos os diretórios e arquivos criados:

```
$ ./cleanup_directories.sh
```

## Conclusão

Scripts em Bash tendem a ser mais rápidos para operações simples como a criação de arquivos, já que são diretamente integrados ao shell do sistema operacional, ao passo que Python possui um melhor desempenho na cópia de arquivos, através do uso de bibliotecas otimizadas, como shutil.
