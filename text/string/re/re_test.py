import re

# pattern = 'this'
# text = 'does this text match the pattern?'
# match = re.search(pattern, text)

# s = match.start()
# e = match.end()
# print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
#     match.re.pattern, match.string, s, e, text[s:e]))

"""
Found "this"
in "does this text match the pattern?"
from 5 to 9 ("this")
"""

# 虽然re包含用于将正则表达式作为文本字符串处理的模块级函数，但编译程序经常使用的表达式更有效。
# 该compile()函数将表达式字符串转换为RegexObject
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:  
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')

"""
Text: 'Does this text match the pattern?'

Seeking "this" -> match!
Seeking "that" -> no match
"""
