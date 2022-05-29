#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
from subprocess import PIPE

def time_to_sec(time):
    return float(time[0]) * 60 * 60 + float(time[1]) * 60 + float(time[2])

def fix(value):
    parts = str(value).split(".")
    if len(parts[0]) == 1:
        parts[0] = "0" + parts[0]
    return ".".join(parts)

def sec_to_time(sec):
    h, m = divmod(sec, 3600)
    m, s = divmod(m, 60)
    return [fix(int(h)), fix(int(m)), fix(int(s))]


files = os.listdir(".")
files = sorted(files)
files = [f for f in files if f.endswith(".mkv")]

acc = 0

for f in files:
    cmd = ["ffmpeg", "-i", f]
    p = subprocess.Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE, universal_newlines=True)
    _stdout, stderr = p.communicate()

    lines = stderr.split("\n")
    lines = [l.strip() for l in lines if "DURATION" in l]
    time_parts = lines[0].split(":")[-3:]
    time_parts[-1] = time_parts[-1][:5]

    titulo = f.replace("_", " ")
    titulo = " ".join(titulo.split(".")[:-1]) # removendo extensao
    parts = titulo.split(" ") # removendo indice
    if parts[0].isdigit():
        del parts[0]
    titulo = " ".join(parts)
    if(len(titulo) > 0 and titulo[-1] != "~"):
        print(":".join(sec_to_time(acc)), titulo)
    acc += time_to_sec(time_parts)
