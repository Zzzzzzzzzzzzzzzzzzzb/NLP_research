import jieba
import jieba.posseg as pseg
import jieba.analyse

'''
jieba: 分词、词性标注、关键词提取
'''

'''
定义用户词典
jieba.load_userdict('user.txt') 
示例:
小红烧肉 nr
事儿逼 a

'''


# 分词
s = '那些智力超常的人啊，认为已经熟悉了云和闪电的脾气，就不再迷惑，就不必了解自己，世界和他人，每天只管被微风吹拂，与猛虎谈情'
print('精确模式: ', jieba.lcut(s))  # 精确模式，默认有HMM
print('精确模式: ', jieba.lcut(s, HMM=False))  # 精确模式，关掉HMM
print('全模式: ', jieba.lcut(s, cut_all=True))  # 全模式
print('搜索引擎模型:', jieba.lcut_for_search(s))  # 搜索引擎模型

# 词性标注
print('词性标注:', pseg.lcut(s))

# 关键词提取
print('Tf-idf:', jieba.analyse.extract_tags(s, topK=5, withWeight=True, allowPOS=(('n',))))  # 只要名词
print('textrank:', jieba.analyse.textrank(s, topK=5, withWeight=True, allowPOS=(('v',))))  # 只要动词


