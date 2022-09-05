#!/usr/bin/env python3

import sys
import json
from framework import FrameWorker
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--sw", help="Scale width", default=3.5, type=float)
parser.add_argument("--sh", help="Scale height", default=3.5, type=float)
parser.add_argument('--sb', help="Scale both", default=True, type=bool)

args = parser.parse_args()

worker = FrameWorker()

for line in sys.stdin:
    if len(line) < 3:
        continue

    frame = json.loads(line)

    frame = worker.frame_processing(frame, args.sw, args.sh, args.sb)

    sys.stdout.write(json.dumps(frame))
    sys.stdout.write("\n")
    sys.stdout.flush()

