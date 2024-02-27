#!/bin/bash
#My code

NOME="Kelvyn"
echo $NOME


NUMERO_1=25
NUMERO_2=45
TOTAL=$((NUMERO_1+NUMERO_2))

echo  $TOTAL

SAIDA_CAT=$(cat /etc/passwd | grep kelvyn)
echo $SAIDA_CAT


echo *----------------------------*

echo "Paramentro 1: $1"
echo "Paramentro 1: $2"

echo "Todos Paramentros 1: $* "
echo "Qntd Parametros? $#"
echo "Saida do ultimo comando: $?"
echo "PID: $$"
echo $0
