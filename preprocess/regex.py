import re


def del_special_char(text):
    pattern = "[^\w\s]"
    repl = ""
    regexed_text = re.sub(pattern=pattern, repl=repl, string=str(text))
    return regexed_text
