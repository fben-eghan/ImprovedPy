# -*- coding: utf-8 -*-
import pandas as pd
from fileinput import FileInput
import re
import os

def replace_text(search_text, replace_text, filename):
    with FileInput(filename, inplace=True) as f:
        for line in f:
            print(line.replace(search_text, replace_text), end='')
    return "Text replaced"

def create_blank_file(filename):
    with open(filename, 'a'):
        pass

def main():
    # Replace text in HLD.JOH.PROD.YYYYMMDD-YYYYMMDD.txt
    filename = os.path.join('F:', 'Portia', 'HLD.JOH.PROD.YYYYMMDD-YYYYMMDD.txt')
    lb2 = pd.datetime.today().date() - pd.tseries.offsets.BDay(1)
    for curr in ['USD', 'GBP', 'RUR']:
        search_text = f'"{lb2}","","{curr}","Equity"'
        replace_text = f'"{lb2}","0.000000000001","{curr}","Equity"'
        print(replace_text(search_text, replace_text, filename))

    # Create blank INSIGNIS file
    titledate = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    title = f'{titledate}-{titledate}'
    filename = os.path.join('F:', 'Portia', f'JOH_INSIGNIS.{title}.cntl')
    create_blank_file(filename)

    # Run -RiskMetricsTNC for one previous business day
    bd_T1 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%d-%m-%y')
    filename = os.path.join('F:', 'Portia', 'TNC.JOH.PROD.YYYYMMDD-YYYYMMDD.txt')
    with open(filename) as f:
        newtext = [line.replace('"', '').replace(',', '|') for line in f.readlines()]
    title = f'{titledate}-{titledate}'
    filename = os.path.join('F:', 'Portia', f'TNC.JOH.{title}.txt')
    with open(filename, 'w') as f:
        f.writelines(newtext)
    os.remove(os.path.join('F:', 'Portia', 'TNC.JOH.PROD.YYYYMMDD-YYYYMMDD.txt'))

    # Replace text in HLD.JOH.PROD.YYYYMMDD-YYYYMMDD.txt again
    filename = os.path.join('F:', 'Portia', 'HLD.JOH.PROD.YYYYMMDD
