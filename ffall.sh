#!/bin/bash

rm -f times.txt zz.mkv 
timestamps.py *.mkv > times.txt
ffjoin.py *.mkv zz.mkv