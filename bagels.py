#coding:utf-8
import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # 返回一个由 NUM_DIGITS 个不重复随机数组成的字符串
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # 返回一个由 Pico, Fermi 和 Bagels 组成的，用来提示用户的字符串
    if guess == secretNum:
        return '你猜对了！'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    # 如果字符串只包含数字，返回真。否则返回假
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print('我想了一个 %s 位数字，猜猜它是几' % (NUM_DIGITS))
print('The clues I give are...')
print('当我说:    意思:')
print('  Bagels       你猜测的3个数都不在神秘数字中')
print('  Pico         你猜测的是神秘数字中的一个数，但是位置不对；')
print('  Fermi        你猜测的是正确位置上的一个正确的数。')

while True:
    secretNum = getSecretNum()
    print('我已经想好了数字， 你可以猜 %s 次' % (MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. 答案是 %s.' % (secretNum))

    print('你还想再玩一次吗？ (yes or no)')
    if not input().lower().startswith('y'):
        break
