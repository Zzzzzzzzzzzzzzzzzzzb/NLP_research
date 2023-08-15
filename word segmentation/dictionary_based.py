import torch


def MM_func(user_dict, sentence):
    """
    正向最大匹配（FMM）
    :param user_dict:词典
    :param sentence: 句子
    :return: 分词结果
    """
    max_len = max([len(item) for item in user_dict])
    start = 0
    res = []
    while start != len(sentence):
        index = start + max_len
        if index > len(sentence):
            index = len(sentence)
        for i in range(max_len):
            if (sentence[start: index] in user_dict) or (len(sentence[start: index]) == 1):
                # print(sentence[start: index], end='/')
                res.append(sentence[start: index])
                start = index
                break
            index -= 1
    return res


def RMM_func(user_dict, sentence):
    max_len = max([len(item) for item in user_dict])
    res = []
    start = len(sentence)
    while start != 0:
        index = start - max_len
        if index < 0:
            index = 0
        for i in range(max_len):
            if (sentence[index: start] in user_dict) or (len(sentence[start: index]) == 1):
                res.append(sentence[index: start])
                start = index
                break
            index += 1
    return res[::-1]


def Bi_MM_func(user_dict, sentence):
    res_MM = MM_func(user_dict, sentence)
    res_RMM = RMM_func(user_dict, sentence)
    if len(res_MM) < len(res_RMM):
        return res_MM
    elif len(res_MM) > len(res_RMM):
        return res_RMM
    else:
        MM_count, RMM_count = 0, 0
        for w in res_MM:
            if len(w) == 1:
                MM_count += 1
        for w in res_RMM:
            if len(w) == 1:
                RMM_count += 1
        if MM_count <= RMM_count:
            return res_MM
        else:
            return res_RMM


if __name__ == '__main__':
    user_dict = ['我们', '在', '在野', '生动', '野生', '动物园', '野生动物园', '物', '园', '玩']
    sentence = '我们在野生动物园玩'
    res = Bi_MM_func(user_dict, sentence)
    print('/'.join(res))