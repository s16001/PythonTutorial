# キーボードから数字を入力して
# その高さの三角形を*で出力してください
"""
例) 5 と入力すると
*       *
**      **
***     *+*
****    *++*
*****   *****
と出力する
"""
h = int(input('高さを入力してください'))
"""
for horizontal in range(h + 1):
    for vertical in range(horizontal):
        print('*', end='')
    print()
"""

'''
*
**
*+*
*++*
*****
'''
for vertical in range(h + 1):
    for horizontal in range(vertical):
        if horizontal == 0 or horizontal == vertical - 1\
                or vertical == h:
            print('*', end='')
        else:
            print('+', end='')

    print()