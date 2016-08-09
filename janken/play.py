
HANDS = ('グー', 'チョキ', 'パー')


def select_hand():
    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか。
    """
    import random
    pass


def judgement(player, computer):
    """
    じゃんけんの勝敗を判定する。
    :param player: HANDSの中のどれか
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は1,あいこは0,負けは-1を返す
    """
    pass


def save_score(result):
    """
    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: None
    """
    pass


if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示
    save_score(result)