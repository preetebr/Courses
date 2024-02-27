#!/bin/bash

#Extrai usuários do /etc/passwd
USUARIOS="$(cat /etc/passwd | cut -d : -f 1)"
MENSAGEM_USO="
  $(basename $0) - [OPÇÕES]
  -h - Menu de ajuda
  -v - Versão
  -s - Ordenar a saída
  -m - Coloca em maiusculo
"

VERSAO="v1.0"
CHAVE_ORDENA=0
CHAVE_MAIUSCULO=0



#Execução
# if [ "$1" = "-h" ]; then
#   echo "$MENSAGEM_USO" && exit 0
# fi
#
# if [ "$1" = "-v" ]; then
#   echo "$VERSAO" && exit 0
# fi
#
# if [ "$1" = "-s" ]; then
#   echo "$USUARIOS" | sort && exit 0
# fi

while test -n "$1"
do
  case "$1" in
    -h) echo "$MENSAGEM_USO" && exit 0;;
    -v) echo "$VERSAO" && exit 0;;
    -s) CHAVE_ORDENA=1 ;;
    -m) CHAVE_MAIUSCULO=1 ;;
    *) echo "Invalida" && exit 1;
  esac
  shift
done

[ $CHAVE_ORDENA -eq 1 ] && USUARIOS=$(echo "$USUARIOS" | sort)
[ $CHAVE_MAIUSCULO -eq 1 ] && USUARIOS=$(echo "$USUARIOS" | tr [a-z] [A-Z])

echo "$USUARIOS"
