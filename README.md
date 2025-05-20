# sector_file_chaos_machine
add a .txt copy of your sector file into the directory and call it `sct_pre.txt` but you're gonna have to change all the colours manually to hot pink (16040642), don't ask why just go with it. it should look something like

```
#define motorway 16040642
```
etc.

you need to to do this to lines 8 - 151 if you're on 2505 sct file which you totally are because you update it monthly, right?

make an empty .txt called `sct_post.txt`

if you wanna make colours random comment out lines 16 onwards, run main and copy sct_post.txt to a new sct file
if you wanna make labels random, firstly, i hate you, secondly, good luck lol.

how to make random labels + random colours:
run main.py
copy sct_post.txt to a new sct file

how to make random labels + normal colours
run main.py
copy sct_post.txt to a new sct file
copy lines 1 - 151 of the normal, holy sector file into your new unholy one

gg

