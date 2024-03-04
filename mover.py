#!/usr/bin/env python3

import os, sys, time
import argparse as ap
import pathlib as pl
from rich import print
from exif import Image


def mover(source_list, target_directory):
    print(source_list)
    for file in source_list:
        with open(file, "rb") as target:
            img = Image(target)
            print(f"[bold green]Moving[/bold green]: {file.name}\n")
            print(F"[bold green]Comment[/bold green]: {img.user_comment}\n")
            file_name=input("New file name: ")
            os.rename(file, target_directory / file_name)



if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument("-s", "--source", type=str, required=True)
    parser.add_argument("-t", "--target", type=str, required=True)
    parser.add_argument("-e", "--extension", type=str, required=True)
    args = parser.parse_args()
    source = pl.Path(args.source)
    if not source.exists():
        print(f"[bold red]ERROR[/bold red]: source directory {source} does not exist")
        sys.exit(1)
    target = pl.Path(args.target)
    if not target.exists():
        print("[bold red]ERROR[/bold red]ß: target directory {targeT} does not exist")
        sys.exit(1)
    extension = args.extension
    extension = extension if extension.startswith(".") else f".{extension}"
    files = list(source.glob(f"*{extension}"))
    mover(files, target)
