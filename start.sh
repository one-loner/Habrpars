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
cat result.txt | grep "$SR"
fi
