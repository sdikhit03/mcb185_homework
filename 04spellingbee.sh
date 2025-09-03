cd ~/Code/mcb185_homework/
gunzip -c ~/Code/MCB185/data/dictionary.gz \
| grep -E "^[acinorz]{4,}$" \
| grep r \
| wc -l
