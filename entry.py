#!/usr/bin python3

import argparse
from datetime import datetime


parser = argparse.ArgumentParser()


parser.add_argument('--amount', type=str, required=True)
parser.add_argument('--units', type=str, required=True)
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--roa', type=str, required=False)
parser.add_argument('--annotate', type=str, required=False)

args = parser.parse_args()
now = datetime.utcnow()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f'{date_time} : Consumed {args}')
