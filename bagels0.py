#from common import *
# 数字长度
num_size = 3
# 猜测次数
guess_times = 3

while True:
    times = 0
    # 生成神秘数字
    secret_num = generate_secret_num(num_size)

    while times < guess_times:
        # 获取用户答题答案
        answer = get_answer()
        # 排除异常输入
        format_result = format_answer(answer, num_size)
        if format_result is False:
            continue
        # 检查答案
        check_result = check_answer(secret_num, answer)
        check_status = get_check_status(check_result, num_size)
        # 正确处理
        if check_status == 1:
            print('恭喜你，答对了!')
            break
        else:
            # 错误处理
            times += 1
            if times == guess_times:
                print('答错了,加油!')
                break
            else:
                print('提示你：%s' % check_result)
                continue

    is_again = input('再玩一局,输入y>> ')
    if is_again != 'y':
        break