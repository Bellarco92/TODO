from argparse import ArgumentParser

parser = ArgumentParser(description='Mała aplikacja TODO')
parser.add_argument('--add', help='Dodaj nowe zadanie')
parser.add_argument('--list', help='Wypisz tematy do zrobienia', action='store_true')
parser.add_argument('--toggle', help='Zmień status zadania')
args = parser.parse_args()


