#!/bin/bash

# Identificar hosts abertos na rede

if [ "$1" == "" && "$2" == ""]
then
    echo "Digite um IP e em seguida a porta"
    echo "Exemplo: ./scannet.sh 192.168.1.105 80"
else
    for ip in {1..254};
    do
        hping3 -S -p $2 -c 1 $1.$ip 2> /dev/null | grep "flags=SA" | cut -d " " -f2;
    done
fi
