import argparse
import sys
import requests

def main():
    newparser = argparse.ArgumentParser(description='Soubor.')
    newparser.add_argument("website", help="název webstranky")
    newparser.add_argument("znaky", help="Spočítat znaky", action="store_true")
    newparser.add_argument("slova", help="Spočítat slova", action="store_true")
    newparser.add_argument("radky", help="Spočítat řádky", action="store_true")
    arguments = newparser.parse_args()
    try:
        r = requests.get(arguments.website)
        f = r.text
        flag = False
        if arguments.slova:
            pocet_slov = f.count(' ') + len(f.split('\n'))
            print(f"Počet slov: {pocet_slov}")
            flag = True
        if arguments.znaky:
            pocet_znaku = len(f)
            print(f"Počet znaků: {pocet_znaku}")
            flag = True
        if arguments.radky:
            pocet_radku = len(f.split('\n'))
            print(f"Počet řádků: {pocet_radku}")
            flag = True
        if not flag:
            pocet_slov = f.count(' ') + len(f.split('\n'))
            pocet_znaku = len(f)
            pocet_radku = len(f.split('\n'))
            print(f"Počet slov: {pocet_slov}\nPočet znaků: {pocet_znaku}\nPočet řádků: {pocet_radku}")
    except:
        print("Something went wrong")
        sys.exit(1)


main()