import codecs
from sklearn.model_selection import train_test_split
import pickle

input_data = './RenMinData.txt_utf8'
save_path = './datasave.pkl'
id2tag = ['B', 'M', 'E', 'S']  # B：分词头部 M：分词词中 E：分词词尾 S：独立成词 id与状态值
tag2id = {'B': 0, 'M': 1, 'E': 2, 'S': 3}  # 状态值对应的id
word2id = {}  # 每个汉字对应的id
id2word = []  # 每个id对应的汉字


def getList(input_str):
    '''
    单个分词转换为tag序列
    :param input_str:
    :return:
    '''
    output_str = []
    if len(input_str) == 1:
        output_str.append(tag2id['S'])
    elif len(input_str) == 2:
        output_str = [tag2id['B'], tag2id['E']]
    else:
        M_num = len(input_str) - 2
        M_list = [tag2id['M']] * M_num
        output_str.append((tag2id['B']))
        output_str.extend(M_list)
        output_str.append(tag2id['E'])
    return output_str


def handle_data():
    '''
    处理数据，并保存至 save path
    :return:
    '''
    x_data = []  # 观测值序列集合
    y_data = []  # 状态值序列集合
    word_num = 0
    line_num = 0
    with open(input_data, 'r', encoding='utf-8') as ifp:
        for line in ifp:
            line_num += 1
            line = line.strip()
            if not line: continue
            line_x = []
            for i in range(len(line)):
                if line[i] == ' ': continue
                if line[i] in id2word:
                    line_x.append(word2id[line[i]])
                else:
                    id2word.append(line[i])
                    word2id[line[i]] = word_num
                    line_x.append(word_num)
                    word_num += 1
            x_data.append(line_x)

            lineArr = line.split(' ')
            line_y = []
            for item in lineArr:
                line_y.extend(getList(item))
            y_data.append(line_y)

    print(x_data[0])
    print([id2word[i] for i in x_data[0]])
    print(y_data[0])
    print([id2tag[i] for i in y_data[0]])
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=43)
    with open(save_path, 'wb') as outp:  # 保存
        pickle.dump(word2id, outp)
        pickle.dump(id2word, outp)
        pickle.dump(tag2id, outp)
        pickle.dump(id2tag, outp)
        pickle.dump(x_train, outp)
        pickle.dump(y_train, outp)
        pickle.dump(x_test, outp)
        pickle.dump(y_test, outp)


if __name__ == '__main__':
    handle_data()

































