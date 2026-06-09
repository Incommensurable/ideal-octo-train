import re

word_pattern = re.compile(r"\[(\w+)\]")  # matches [word] and captures word

word_pattern.findall(
    "This is a [test] string with [multiple] [words]."
)  # returns ['test', 'multiple', 'words']


word_pattern = re.compile(
    r"\[([\w\s]+)\]"
)  # matches [a bunch of words] and captures 'a bunch of words'

word_pattern.findall(
    "This is a [test string with] [fsa dsfas a shbfs fhs  ]."
)  # returns ['test string with', 'fsa dsfas a shbfs fhs  ']
