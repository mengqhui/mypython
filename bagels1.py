import random


# 生成神秘数字
def generate_secret_num(size):
    list_0_9 = [str(i) for i in range(10)]
    random.shuffle(list_0_9)
    secret_num = list_0_9[:size]
    return secret_num


# 判断猜测结果
def check_answer(question, answer):
    result = []
    for i in range(len(question)):
        if answer[i] == question[i]:
            result.append('yes')
        elif answer[i] in question:
            result.append('lose')
        else:
            result.append('no')
    return result


# 结果状态
# ['no', 'lose', 'lose']
def get_check_status(result, size):
    status = 0
    if result.count('yes') == size:
        status = 1
    elif result.count('no') == size:
        status = 2
    return status


# 获取玩家答案
def get_answer():
    answer = list(input('输入答案》'))
    return answer


def format_answer(answer, size):
    if len(answer) != size:
        print('必须输入长度为%s的答案！' % size)
        return False
    for i in answer:
        if i not in '1234567890':
            print('%s为非数字' % i)
            return False
    return True


if __name__ == '__main__':
    r = check_answer('123','045')
    print(r)
    print(get_check_status(r))