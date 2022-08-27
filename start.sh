#!/bin/bash
python3 pars.py
less result.txt
echo "Введите имя файла для сохранения результатов: "
read FN
if [ -n "$FN" ];
then
cp result.txt $FN.txt
fi
echo "Поиск по результатам: "
read SR
if [ -n "$SR" ];
then
echo found.txt>found.txt
cat result.txt | grep "$SR">>found.txt
less found.txt
fi
