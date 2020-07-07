#! python
# -*- coding: latin1 -*-
import csv


with open('desafio-ibge.csv') as arquivo :
    with open('ibge.txt', 'w') as saida :
        for lines in csv.reader(arquivo) :
            print(f"Nono = {lines[8]}, Quarto = {lines[3]}", file = saida)
