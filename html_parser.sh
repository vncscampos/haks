#!/bin/bash

echo "=============================================="
echo ""
echo "[+] Resolvendo URLs em:" $1
echo ""
echo "=============================================="
echo ""
wget  -q $1
grep href index.html | cut -d "/" -f 3 | grep "\." | cut -d '"' -f1 | grep -v "{" > lista

echo "[+] Salvando os resultados em: "$1".txt"

for url in $(cat lista); do host $url | grep "has address"; done > $1.txt

echo ""
echo "=========================================================="
echo " ADDRESS                                        IP"
echo "=========================================================="

cut -d " " -f1,4 $1.txt --output-delimiter="                    "
