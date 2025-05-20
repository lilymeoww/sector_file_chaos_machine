import random
import re

with open("sct_pre.txt", "r") as sct_pre:
    sct_pre_rainbow = sct_pre.read().splitlines()

with open("sct_post.txt", "w+") as sct_post:
    for line in sct_pre_rainbow:
        if "16040642" in line:
            print(line)
            elephants = random.randint(0, 255) * 65536 + random.randint(0, 255) * 256 + random.randint(0, 255)
            line = line.replace("16040642", str(elephants))
            print(line)
        sct_post.write(line + "\n")

with open("sct_post.txt", "r") as sct_post_pre:
    sct_post_pre_randomness = sct_post_pre.read().splitlines()

list_of_labels_so_good = []
with open("sct_post.txt", "w+") as sct_post_pre_randomness_pre:
    for line in sct_post_pre_randomness:
        if re.compile(r'"([^"]+)" .+').search(line):
            list_of_labels_so_good.append(re.search(r'"([^"]+)" .+', line).group(0).split('"')[1])
    random.shuffle(list_of_labels_so_good)
    i = -1
    for line in sct_post_pre_randomness:
        if re.compile(r'"([^"]+)" .+').search(line):
            i += 1
            line = line.replace((re.search(r'"([^"]+)" .+', line).group(0).split('"')[1]), list_of_labels_so_good[i])
        sct_post_pre_randomness_pre.write(line + "\n")
