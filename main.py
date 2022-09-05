#!/usr/bin/env python3

import sys
import json
from framework import FrameWorker
import argparse
from distutils.util import strtobool


parser = argparse.ArgumentParser()

parser.add_argument("--sw", help="Scale of width", default=1.0, type=float)
parser.add_argument("--sh", help="Scale of heigth", default=1.0, type=float)
parser.add_argument('--sb', help="Scale both", default=True, type=lambda x:bool(strtobool(x)))

args = parser.parse_args()
scale_w, scale_h, scale_both = args.sw, args.sh, args.sb


worker = FrameWorker()

for line in sys.stdin:
    if len(line) < 3:
        continue

    frame = json.loads(line)

    
    frame = worker.frame_processing(frame, scale_w, scale_h, scale_both)

    sys.stdout.write(json.dumps(frame))
    sys.stdout.write("\n")
    sys.stdout.flush()

