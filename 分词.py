import jieba

import jieba.posseg as pos
s = "数字人文概念的出现，大约在21世纪初期。但人文计算的历史相当悠久。"
jieba.load_userdict("/users/tao/temp/dateset_forClass/dic.txt")
words = pos.cut(s)
for word, flag in words:
    print('%s %s' % (word, flag))
