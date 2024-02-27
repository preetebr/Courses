#!/bin/bash

VAR="a"
VAR2="a"

#Primeira Forma
if [[ "$VAR"="$VAR2" ]]; then
  echo "São iguais"
fi

#Segunda forma
if [[ "$VAR"="$VAR2" ]]
then
  echo "São iguais"
fi


if test "$VAR"="$VAR2";
then
  echo "São iguais"
fi

[ "$VAR"="$VAR2" ] && echo "São iguais"
[ "$VAR"="$VAR2" ] || echo "Não são iguais"
