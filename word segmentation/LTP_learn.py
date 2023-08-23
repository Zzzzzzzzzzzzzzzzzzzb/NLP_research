from ltp import LTP
from ltp import StnSplit

ltp = LTP()  # 默认加载 LTP/small 模型


# 分句
sents = StnSplit().split('当初为了这个我也没少用去口臭的东西，像什么抑菌的口喷，漱口水，啥的都没少买，但是都只是起到暂时的作用！'
                         '顶多顶个30分钟，口臭就又卷土重来了！而且像这种，依靠香味的还不能长期用，时间一长还会破坏咱们口腔内的菌群环境，导致一些并发症！')
print(sents)

sents = StnSplit().batch_split(['他叫汤姆去拿外衣。', '汤姆生病了。他去了医院。'])  # 分批分句，防止单条文本过长，后面输出没了
print(sents)

# 分词
words = ltp.pipeline(['他叫武汉市长江大桥去拿外衣。'], tasks=['cws'], return_dict=False)
print(words)
ltp.add_words(words=['江大桥', '武汉市长'], freq=2)  # 添加用户词典
words = ltp.pipeline(['他叫武汉市长江大桥去拿外衣。', '汤姆生病了。他去了医院。'], tasks=['cws'], return_dict=False)
print(words)

# 词性标注
pipline = ltp.pipeline(['他叫武汉市长江大桥去拿外衣。', '汤姆生病了。他去了医院。'], tasks=['cws', 'pos'], return_dict=False)
for i in range(2):  # 2 为句子数量
    l = len(pipline[0][i])
    for j in range(l):
        print(pipline[0][i][j], ' ', pipline[1][i][j])
    # print('分词结果：', pipline[0][i], end='  ||  ')  # 分词结果
    # print('词性标注：', pipline[1][i])  # 词性标注

# 命名实体识别
result = ltp.pipeline(['汤姆和杰瑞在北京上学。'], tasks=['cws', 'ner'])  # 识别出了人名、地名、机构名
print(result)
for item in result.ner[0]:
    if item[0] == 'Nh':
        print(item[1])

# 语义角色类型
result = ltp.pipeline(['政府鼓励个人投资服务业'], tasks=['cws', 'srl'])
print(result.srl)

# 依存句法分析
result = ltp.pipeline(['他叫汤姆去拿外衣。'], tasks=['cws', 'dep'])
print(result.dep)
'''
0节点指的是root节点，第一个词的节点index为1
[2, 0, 2, 5, 2, 5, 2]
['SBV', 'HED', 'DBL', 'ADV', 'VOB', 'VOB', 'WP']
从上面两个列表的第一个元素来看，它表示：2节点（叫）指向了 1节点（他），并且他们的关系是 SBV-主谓关系
从上面两个列表的第二个元素来看，它表示：0节点（root）指向了 2节点（叫），并且他们的关系是 HED-核心关系
其他依次类推
'''

# 语义依存分析（树）- 不交叉
result = ltp.pipeline(['他叫汤姆去拿外衣。'], tasks=['cws', 'sdp'])
print(result.sdp)

# 语义依存分析（图）
result = ltp.pipeline(['他叫汤姆去拿外衣。'], tasks=['cws', 'sdpg'])
print(result.sdpg)







