#!/usr/bin/env bash
apt install toilet
clear
sleep 1
toilet -f digital MassDeface5
sleep 1
echo "[+]Installing Dependencies"
apt update && apt upgrade
apt install python2
pip2 install requests
apt install git
echo "[*]Succes To Install"
sleep 1
read -p "[+]Go To sdcard?"
cd /sdcard
read -p "[+]make Folder MD5_Hack ?"
mkdir MD5_Hack
cd MD5_Hack
echo "[~]Moving file "
mv -f ns.py /sdcard/MD5_Hack
mv -f target.txt /sdcard/MD5_Hack
mv -f index.html /sdcard/MD5_Hack
sleep 1
echo "[#]installation Succes"
sleep 1
echo "[*]Opening MD5"
python2 ns.py
