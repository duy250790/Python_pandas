#!/bin/bash


echo -n "Enter name file to extract> "
read file

echo -n "Enter number to extracted> "
read number

cd ../data

sed -n '1,'${number}'p' ${file}.json > ${file}${number}.json
echo done

