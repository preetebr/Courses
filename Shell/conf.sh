#!/bin/bash



ARQUIVO_DE_CONFIGURACAO="configuracao.cf"
USAR_CORES=
USAR_MAIUSCULO=
MENSAGEM="Mensagem teste"

VERDE="\033[32;1m"
VERMELHO="\033[31;1m"


[ ! -r "$ARQUIVO_DE_CONFIGURACAO" ] && echo "Não tem acesso de leitura" && exit 1


DefinirParametros () {
  local parametro="$(echo $1 | cut -d = -f 1)"
  local valor="$(echo $1 | cut -d = -f 2)"

  case "$parametro" in
    USAR_CORES) USAR_CORES=$valor;;
    USAR_MAIUSCULO) USAR_MAIUSCULO=$valor;;
  esac

}

echo "VALOR USAR_CORES: $USAR_CORES"
echo "VALOR USAR_MAIUSCULO: $USAR_MAIUSCULO"


while read -r linha
do
  [ "$(echo $linha | cut -c1)" = "#" ] && continue
  [ ! "$linha" ] && continue
  DefinirParametros "$linha"
done < "$ARQUIVO_DE_CONFIGURACAO"


[ $USAR_MAIUSCULO -eq 1 ] && MENSAGEM="$(echo -e $MENSAGEM | tr [a-z [A-Z]])"
[ $USAR_CORES -eq 1 ] && MENSAGEM="$(echo -e ${VERDE}$MENSAGEM)"


echo "$MENSAGEM"
