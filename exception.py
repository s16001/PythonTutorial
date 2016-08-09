while True:
    try:
        x = int(input('数字を入れてください: '))
        break
    except (TypeError, NameError, ValueError):
        print("数字じゃないじゃん")