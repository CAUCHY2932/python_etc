import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
 
# text_from_file_with_apath = open('/Users/hecom/23tips.txt').read()
text_from_file_with_apath = open(u'远走高飞3.txt',encoding='utf-8').read()

 
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
 
my_wordcloud = WordCloud().generate(wl_space_split)
 
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()