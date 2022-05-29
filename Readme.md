# Script para juntar vídeos e fazer timestamps

## Dependencias

Instalar o bash, o ffmpeg e o python. Colocar os scripts dentro do path da sua máquina.

## ffjoin.py

Concatena todos os arquivos num único arquivo de saída.

Ex:
```sh
# de acordo com a sequencia de nomes, junta todos 
# os arquivos .mkv da pasta no arquivo zz.mkv
ffjoin.py *.mkv zz.mkv
```

## timestamps.py

Usa o tempo de cada arquivo de entrada para gerar os timestamps.

Utiliza o nome dos arquivos como título da marcação.

Exclui os _ que possam existir.

```sh
# pega todos os arquivos .mkv da pasta ordenados por nome
# para gerar os timestamps no arquivo times.txt
timestamps *.mkv > times.txt
```

## ffall.sh

```sh
# junta os arquivos e gera os timestamps 
# utilizando todos os arquivos da pasta
ffall.sh
```