from hanspell import spell_checker

from preprocess.regex import del_special_char


def naver_spell_check(texts):
    result = list()
    for text in texts:
        tmp = spell_checker.check(text)
        tmp_result = tmp.only_checked()
        regexed = del_special_char(tmp_result)
        result.append(regexed)
    return result


if __name__ == "__main__":
    result = naver_spell_check(['음이게지굼', '잘되는거맏지요?'])
    print(result)
