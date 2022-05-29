#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import subprocess

parse = argparse.ArgumentParser()
parse.add_argument("files", type=str, nargs="+")
parse.add_argument("output", type=str)
args = parse.parse_args()

file_paths = ".file_paths.txt"
with open(file_paths, "w") as f:
    for entry in args.files:
        f.write("file " + "'" + entry + "'" + "\n")
print(file_paths)
cmd= ["ffmpeg", "-f", "concat", "-safe", "0", "-i" , file_paths, "-c", "copy", args.output]
subprocess.run(cmd)


#ffmpeg -i zz.mkv -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192K -pix_fmt yuv420p outputtest.mkv