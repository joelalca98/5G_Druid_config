import argparse
import sys
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default=1.0, help='Elige el primer numero para operar')
args = parser.parse_args()
sys.stdout.write(str(args))
inputfile = args.file
with open (inputfile) as f:
    Druid_json = json.load(f)


