# NLP Preprocessing

## File Structure
```
.
├─ preprocess
│  ├─ __init__.py
│  ├─ naver_spell_check.py
│  └─ regex.py
├─ .gitignore
├─ LICENSE
├─ main.py 
├─ README.md  
└─ setup.py
```

## Getting Started
```bash
git clone https://github.com/study-ai-data/nlp-preprocessing.git
cd nlp-preprocessing
python setup.py install
python main.py
```

## File Description
### ```./preprocess/```
pre-process codes:
* ```__init__.py```: setting setup.py default information
* ```naver_spell_check.py```: pre-process contents using package: ```py-hanspell```
  * current ```py-hanspell``` is not working because,
    1. Update pip version 
    2. Change Naver target code
    3. Change tags
    4. Etc...
  * so, you'd better use [study-ai-data/py-hanspell](https://github.com/study-ai-data/py-hanspell) rather than original ```py-hanspell``` file.
* ```regex.py```: regex function. Delete specific word what you want
### ```./main.py```
test code for this repo. (run pre-processing codes)<br>
running: ```python main.py```

## License: MIT
```
MIT License

Copyright (c) 2020 Kyeongnam Kim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```