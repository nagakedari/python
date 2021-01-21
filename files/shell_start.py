import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("testtextfile.txt"):
        src=path.realpath("testtextfile.txt")
        dst = src+".bak"
        # shutil.copy(src, dst)
        # shutil.copystat(src, dst)
        # os.rename("testtextfile.txt", "newname.txt")
        
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("testtextfile.txt")
            newzip.write("testtextfile.txt.bak")
main()