# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import preprocess.naver_spell_check as nsc


def get_current_path():
    path = os.getcwd()
    print("\n [[Check your path]] ", path, "\n")
    return path


def get_text_list(path):
    textList = os.listdir(path)
    return textList


def load_text(filePath):
    filename = os.path.splitext(filePath)[0]
    with open(filePath, 'r', encoding="utf-8") as f:
        text = f.readlines()
    return filename, text


def save_text(filePath, contents):
    file = open(filePath, 'w', encoding='utf-8')
    for content in contents:
        file.write(content)
        exit()


def preprocess():
    # load txt list
    path = get_current_path()
    textList = get_text_list(path + "/data")

    # pre-processing each text files
    for textFile in textList:
        filename, texts = load_text(path + "/data/" + textFile)
        result = nsc.naver_spell_check(texts)
        save_text(path + "/data/tgt" + filename + "_naver.txt", result)


if __name__ == "__main__":
    preprocess()
