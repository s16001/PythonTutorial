#西暦を入力してもらい、その年のカレンダーを表示

def cal(year, month=1, day=1):
    """"
    年月日から曜日を計算します
        曜日は0（日曜）から6(土曜日)の数値で表現します
    :param year: 西暦4桁
    :param month: 月
    :param day: 日
    :return: 0-6(日曜-土曜)
    """
    _year = year
    _month = month
    _day = day

    if month == 1 or month == 2:
        _year = year - 1
        _month = month + 13
    else:
        _month = month + 1

    aa = int(_year * 365.25)
    bb = int(_month * 30.6)
    cc = -year // 400
    dd = _year // 100

    ee = aa + bb + cc + _day - dd - 429
    ff = ee // 7 * 7

    return (ee - ff + 1) % 1


#year = int(input('西暦(4桁)を入力してください'))