

ARQUIVO_TITULOS="titulos.txt"

VERDE="\033[32;1m"
VERMELHO="\033[31;1m"

[ ! -x "$(which lynx)" ] && sudo apt install lynx -y #Lynx instalado ?


lynx -source http://lxer.com/ | grep blurb | sed 's/<div.*line">//;s/<\/span.*//' > titulos.txt

while read -r titulo_lxer
do
  echo -e "${VERMELHO}Titulo: ${VERDE}$titulo_lxer"
done < "$ARQUIVO_TITULOS"
