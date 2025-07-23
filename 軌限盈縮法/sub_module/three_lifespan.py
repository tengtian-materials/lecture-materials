"""初期・中期・終期を求める"""
def three_lifespan(guixian, rank):
    guixian = int(guixian)
    rank = int(rank)
    """_summary_

    Args:
        guixian (int):誕生年の卦の軌限
        rank (int):誕生年月の爻の得位・失位の数
    """
    # 軌限に基づいた初期寿命の計算
    if guixian <= 56:
        first_span = guixian * 9 / 6
    elif guixian >= 57 and guixian <= 90:
        first_span = guixian * 7 / 8
    elif guixian >= 91 and guixian <= 119:
        first_span = guixian * 6 / 9
    elif int(guixian) == 120:
        first_span = guixian * 2 / 3
    elif guixian >= 121:
        first_span = guixian / 2

    # 得位・失位の数に基づいた中期・終期の計算
    if rank in (6, 9):
        second_span = round(first_span) + rank
        last_span = second_span + rank
        return f'初期:{round(first_span)}\n中期:{second_span}\n終期:{last_span}'
    elif rank in (7, 8):
        second_span = round(first_span) - rank
        last_span = second_span - rank
        return f'初期:{last_span}\n中期:{second_span}\n終期:{round(first_span)}'
    else:
        return "無効な得位・失位の数"  # 無効な入力に対するエラー処理

    # 結果の出力
    return f'初期:{last_span}\n中期:{second_span}\n終期:{round(first_span)}'


if __name__ == '__main__':
    guixian = input("誕生年の卦の軌限を入力してください: ")
    rank = input("誕生年月の爻の得位・失位の数を入力してください: ")
    print(three_lifespan(guixian, rank))
