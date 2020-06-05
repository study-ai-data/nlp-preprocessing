# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from preprocess import naver_spell_check


def check_tgt_folder(targetPath):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)


def get_current_path():
    path = os.getcwd()
    print("\n [[Check your path]] ", path, "\n")
    return path


def get_text_list(path):
    textList = os.listdir(path)
    return textList


def load_text(filePath):
    print("\n [[Load text file]]", filePath)
    filename = os.path.splitext(filePath)[0].replace(os.getcwd()+"/data/", "")
    with open(filePath, 'r', encoding="utf-8") as f:
        text = f.readlines()
    return filename, text


def save_text(filePath, contents):
    check_tgt_folder(os.getcwd() + "/data/tgt/")
    print(" [[Save text file]] ", filePath)
    file = open(filePath, 'w', encoding='utf-8')
    for content in contents:
        file.write(content + "\n")


def preprocess():
    # load txt list
    path = get_current_path()
    textList = get_text_list(path + "/data")

    # pre-processing each text files
    for textFile in textList:
        filename, texts = load_text(path + "/data/" + textFile)
        result = naver_spell_check(texts)
        print(result)
        filePath = os.getcwd() + "/data/tgt/" + filename + "_naver.txt"
        save_text(filePath, result)


if __name__ == "__main__":
    preprocess()
