from hanspell import spell_checker


def naver_spell_check(texts):
    result = list()
    for texts in texts:
        tmp = spell_checker.check(texts)
        result.append(tmp.only_checked())
    return result


if __name__ == "__main__":
    result = naver_spell_check(['음이게지굼', '잘되는거맏지요?'])
    print(result)
