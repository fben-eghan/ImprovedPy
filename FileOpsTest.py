import os
import shutil
import subprocess
import time
from datetime import date, datetime
from pathlib import Path
from shutil import copy2, move
from typing import List

import pandas as pd


class FileOperations:
    def __init__(self, dir_path: str) -> None:
        self.dir_path = dir_path

    def remove_files(self, files: List[str]) -> None:
        for file in files:
            file_path = os.path.join(self.dir_path, file)
            if os.path.exists(file_path):
                os.remove(file_path)

    def copy_file(self, file_name: str, dest_path: str) -> None:
        src_path = os.path.join(self.dir_path, file_name)
        copy2(src_path, dest_path)


class E2ETesting:
    def __init__(self, dir_path: str) -> None:
        self.dir_path = dir_path
        self.file_ops = FileOperations(dir_path)

    def backup_files(self) -> None:
        # Back up the files for E2E testing
        today = datetime.today().strftime("%Y%m%d")
        files = [
            f"BloombergAskPrices_{today}.txt",
            f"BloombergMidPrices_{today}.txt",
            f"BloombergFWDs_{today}.txt",
            f"BloombergVotingShares_{today}.txt",
            f"BloombergSharesOS_{today}.txt",
            f"BloombergCorpPrices_{today}.txt",
            f"BloombergBidPrices_{today}.txt",
            f"BloombergFXs_{today}.txt",
            f"BloombergPrices_{today}.txt",
            "mpx.prn",
            "mpx2.prn",
            "Currencies.prn",
        ]
        backup_dir = os.path.join(self.dir_path, "backup")
        if not os.path.exists(backup_dir):
            os.mkdir(backup_dir)
        for file in files:
            self.file_ops.copy_file(file, backup_dir)


class PxRemover:
    def __init__(self, dir_path: str) -> None:
        self.dir_path = dir_path
        self.file_ops = FileOperations(dir_path)

    def remove_files(self) -> None:
        # Remove the price sourcing files
        files = [
            "mpx.txt",
            "mpx2.txt",
            "dailypricesreturn2.txt",
            "fwdsdailyreturn.txt",
            "corpcoupons.txt",
            "fxdailyreturn.txt",
        ]
        self.file_ops.remove_files(files)


class Backup:
    def __init__(self, dir_path: str, felix_notes_path: str) -> None:
        self.dir_path = dir_path
        self.felix_notes_path = felix_notes_path
        self.file_ops = FileOperations(dir_path)

    def backup_files(self) -> None:
        # Back up the files
        today = datetime.today().strftime("%Y%m%d")
        self.file_ops.copy_file("ManualPrices.xlsx", "H:")
        self.file_ops.copy_file("ManualPrices.xlsx", self.felix_notes_path)
        print("ManualPrices.xlsx backed up")

        self.file_ops.copy_file(f"Q:/Rec/Cash Rec {today}.xlsx", "H:")
        self.file_ops.copy_file(f"Q:/Rec/Cash Rec {today}.xlsx", self.felix_notes_path)
        print(f"Cash Rec {today}.xlsx backed up")


def main():
    dir_path = r"F:\Portia\FTP"
    felix_notes_path = r"F:\IT\!! NEW IT\Data Admin\Data Administrators
