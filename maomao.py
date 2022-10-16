#coding=utf8
import jieba
import wordcloud
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('file:/home/user/.config/icalingua/databases/eqq[QQNumber].db?mode=ro', uri= True)

cur = conn.cursor()

cur.execute('SELECT content FROM messages WHERE roomId = [-(groupid)] AND senderId = [QQ Number]')

s_pre = cur.fetchall()
s = ' '.join(' '.join(tup) for tup in s_pre)

# replaces words that disturbs the generation of wordcloud.
s = s.replace('replace1', 'replace2')

# s = "words you want to have"

# jieba use dictionary
jieba.load_userdict('dictionary.txt')

words = jieba.lcut(s)
word_list = [word for word in words if len(word.strip())>1]#清洗一个字的词
word_clean=" ".join(word_list)
# counts = {}
# for word in words:
#   if len(word) == 1:
#       continue
#   else:
#       counts[word] = counts.get(word, 0) + 1
#   items = list(counts.items())

wc = wordcloud.WordCloud(font_path = "simhei.ttf",#指定字体类型
                        background_color = "white",#指定背景颜色
                        max_words = 800,  # 词云显示的最大词数
                        max_font_size = 256,#指定最大字号
                        width = 1920,
                        height = 1080
                        ) #指定模板
wc = wc.generate(word_clean)
plt.imshow(wc)
plt.axis("off")
plt.show()