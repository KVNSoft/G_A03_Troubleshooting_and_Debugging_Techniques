#!/usr/bin/env python
import os
import subprocess
from multiprocessing import Pool

src = r"data/prod/"
dest = r"data/prod_backup/"


def my_func01(dir):
    try:
        subprocess.call(["rsync", "-arq", src + str(dir), dest])
    except Exception as e:
        print("ERROR!!!", e)

def main():
    try:
        os.chdir(os.getenv("HOME"))
        my_dir01 = list()

        for path01, dir01, file01 in os.walk(src):
            my_dir01.append(dir01)

        my_dir02 = my_dir01[0]

        my_pool01 = Pool(len(my_dir02))
        my_pool01.map(my_func01, my_dir02)
    except Exception as e:
        print("ERROR!!!", e)


if __name__ == "__main__":
    main()