#!/bin/bash
for ((i=1; i<=31; i++))
do
  python tfidf.py -a=$i > results/results_arc_$i.txt
done
