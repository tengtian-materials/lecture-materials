"""初期・中期・終期を表示する"""
from .yao_rank import Yao_Rank as YR
from .yao_lushu import Yao_Lushu as YL
from .guishu_method import guishu_method as gm
from .three_lifespan import three_lifespan as tl


def lifespan(a, b):
    """
    args:
        a(str):誕生年の卦
        b(str):誕生月の爻
    returns:
        int:初期・中期・終軌の数   
    
    """

    # 乾
    qian_r = YR('乾', '乾')
    qian_l = YL('乾', '乾')
    qian_rank = qian_r.total_rank()
    qian_lushu = qian_l.total_lushu()
    qian_gui = gm('乾')
    if a == '乾' and b == '初爻':
        rank = qian_rank.get(b)
        lushu = qian_lushu.get(b)
        guixian = int(qian_gui * rank / lushu)
        """軌数を得位の失位で掛け、七均の数で割ったのを軌限とする"""

        return tl(guixian, rank)

    elif a == '乾' and b == '二爻':

        rank = qian_rank.get(b)
        lushu = qian_lushu.get(b)
        guixian = int(qian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '乾' and b == '三爻':

        rank = qian_rank.get(b)
        lushu = qian_lushu.get(b)
        guixian = int(qian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '乾' and b == '四爻':

        rank = qian_rank.get(b)
        lushu = qian_lushu.get(b)
        guixian = int(qian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '乾' and b == '四爻':

        rank = qian_rank.get(b)
        lushu = qian_lushu.get(b)
        guixian = int(qian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '乾' and b == '五爻':

        rank = qian_rank.get(b)
        lushu = qian_lushu.get(b)
        guixian = int(qian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '乾' and b == '上爻':

        rank = qian_rank.get(b)
        lushu = qian_lushu.get(b)
        guixian = int(qian_gui * rank / lushu)

        return tl(guixian, rank)

# 坤
    chun_r = YR('坤', '坤')
    chun_l = YL('坤', '坤')
    chun_rank = chun_r.total_rank()
    chun_lushu = chun_l.total_lushu()
    chun_gui = gm('坤')

    if a == '坤' and b == '初爻':
        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '坤' and b == '二爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '坤' and b == '三爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '坤' and b == '四爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '坤' and b == '五爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '乾' and b == '上爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

# 屯
    chun_r = YR('震', '坎')
    chun_l = YL('震', '坎')
    chun_rank = chun_r.total_rank()
    chun_lushu = chun_l.total_lushu()
    chun_gui = gm('屯')

    if a == '屯' and b == '初爻':
        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '屯' and b == '二爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '屯' and b == '三爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '屯' and b == '四爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '屯' and b == '五爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '屯' and b == '上爻':

        rank = chun_rank.get(b)
        lushu = chun_lushu.get(b)
        guixian = int(chun_gui * rank / lushu)

        return tl(guixian, rank)

# 蒙
    meng_r = YR('坎', '艮')
    meng_l = YL('坎', '艮')
    meng_rank = meng_r.total_rank()
    meng_lushu = meng_l.total_lushu()
    meng_gui = gm('屯')

    if a == '蒙' and b == '初爻':
        rank = meng_rank.get(b)
        lushu = meng_lushu.get(b)
        guixian = int(meng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蒙' and b == '二爻':

        rank = meng_rank.get(b)
        lushu = meng_lushu.get(b)
        guixian = int(meng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蒙' and b == '三爻':

        rank = meng_rank.get(b)
        lushu = meng_lushu.get(b)
        guixian = int(meng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蒙' and b == '四爻':

        rank = meng_rank.get(b)
        lushu = meng_lushu.get(b)
        guixian = int(meng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蒙' and b == '五爻':

        rank = meng_rank.get(b)
        lushu = meng_lushu.get(b)
        guixian = int(meng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蒙' and b == '上爻':

        rank = meng_rank.get(b)
        lushu = meng_lushu.get(b)
        guixian = int(meng_gui * rank / lushu)

        return tl(guixian, rank)

# 需
    xu_r = YR('乾', '坎')
    xu_l = YL('乾', '坎')
    xu_rank = xu_r.total_rank()
    xu_lushu = xu_l.total_lushu()
    xu_gui = gm('需')

    if a == '需' and b == '初爻':
        rank = xu_rank.get(b)
        lushu = xu_lushu.get(b)
        guixian = int(xu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '需' and b == '二爻':

        rank = xu_rank.get(b)
        lushu = xu_lushu.get(b)
        guixian = int(xu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '需' and b == '三爻':

        rank = xu_rank.get(b)
        lushu = xu_lushu.get(b)
        guixian = int(xu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '需' and b == '四爻':

        rank = xu_rank.get(b)
        lushu = xu_lushu.get(b)
        guixian = int(xu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '需' and b == '五爻':

        rank = xu_rank.get(b)
        lushu = xu_lushu.get(b)
        guixian = int(xu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '需' and b == '上爻':

        rank = xu_rank.get(b)
        lushu = xu_lushu.get(b)
        guixian = int(xu_gui * rank / lushu)

        return tl(guixian, rank)

# 訟
    song_r = YR('坎', '乾')
    song_l = YL('坎', '乾')
    song_rank = song_r.total_rank()
    song_lushu = song_l.total_lushu()
    song_gui = gm('訟')

    if a == '訟' and b == '初爻':
        rank = song_rank.get(b)
        lushu = song_lushu.get(b)
        guixian = int(song_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '訟' and b == '二爻':

        rank = song_rank.get(b)
        lushu = song_lushu.get(b)
        guixian = int(song_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '訟' and b == '三爻':

        rank = song_rank.get(b)
        lushu = song_lushu.get(b)
        guixian = int(song_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '訟' and b == '四爻':

        rank = song_rank.get(b)
        lushu = song_lushu.get(b)
        guixian = int(song_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '訟' and b == '五爻':

        rank = song_rank.get(b)
        lushu = song_lushu.get(b)
        guixian = int(song_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '訟' and b == '上爻':

        rank = song_rank.get(b)
        lushu = song_lushu.get(b)
        guixian = int(song_gui * rank / lushu)

        return tl(guixian, rank)

# 師
    shi_r = YR('坎', '坤')
    shi_l = YL('坎', '坤')
    shi_rank = shi_r.total_rank()
    shi_lushu = shi_l.total_lushu()
    shi_gui = gm('師')

    if a == '師' and b == '初爻':
        rank = shi_rank.get(b)
        lushu = shi_lushu.get(b)
        guixian = int(shi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '師' and b == '二爻':

        rank = shi_rank.get(b)
        lushu = shi_lushu.get(b)
        guixian = int(shi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '師' and b == '三爻':

        rank = shi_rank.get(b)
        lushu = shi_lushu.get(b)
        guixian = int(shi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '師' and b == '四爻':

        rank = shi_rank.get(b)
        lushu = shi_lushu.get(b)
        guixian = int(shi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '師' and b == '五爻':

        rank = shi_rank.get(b)
        lushu = shi_lushu.get(b)
        guixian = int(shi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '師' and b == '上爻':

        rank = shi_rank.get(b)
        lushu = shi_lushu.get(b)
        guixian = int(shi_gui * rank / lushu)

        return tl(guixian, rank)

# 比
    bi_r = YR('坤', '坎')
    bi_l = YL('坤', '坎')
    bi_rank = bi_r.total_rank()
    bi_lushu = bi_l.total_lushu()
    bi_gui = gm('比')

    if a == '比' and b == '初爻':
        rank = bi_rank.get(b)
        lushu = bi_lushu.get(b)
        guixian = int(bi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '比' and b == '二爻':

        rank = bi_rank.get(b)
        lushu = bi_lushu.get(b)
        guixian = int(bi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '比' and b == '三爻':

        rank = bi_rank.get(b)
        lushu = bi_lushu.get(b)
        guixian = int(bi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '比' and b == '四爻':

        rank = bi_rank.get(b)
        lushu = bi_lushu.get(b)
        guixian = int(bi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '比' and b == '五爻':

        rank = bi_rank.get(b)
        lushu = bi_lushu.get(b)
        guixian = int(bi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '比' and b == '上爻':

        rank = bi_rank.get(b)
        lushu = bi_lushu.get(b)
        guixian = int(bi_gui * rank / lushu)

        return tl(guixian, rank)

# 小畜
    xiaoxu_r = YR('乾', '巽')
    xiaoxu_l = YL('乾', '巽')
    xiaoxu_rank = xiaoxu_r.total_rank()
    xiaoxu_lushu = xiaoxu_l.total_lushu()
    xiaoxu_gui = gm('小畜')

    if a == '小畜' and b == '初爻':
        rank = xiaoxu_rank.get(b)
        lushu = xiaoxu_lushu.get(b)
        guixian = int(xiaoxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小畜' and b == '二爻':

        rank = xiaoxu_rank.get(b)
        lushu = xiaoxu_lushu.get(b)
        guixian = int(xiaoxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小畜' and b == '三爻':

        rank = xiaoxu_rank.get(b)
        lushu = xiaoxu_lushu.get(b)
        guixian = int(xiaoxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小畜' and b == '四爻':

        rank = xiaoxu_rank.get(b)
        lushu = xiaoxu_lushu.get(b)
        guixian = int(xiaoxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小畜' and b == '五爻':

        rank = xiaoxu_rank.get(b)
        lushu = xiaoxu_lushu.get(b)
        guixian = int(xiaoxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小畜' and b == '上爻':

        rank = xiaoxu_rank.get(b)
        lushu = xiaoxu_lushu.get(b)
        guixian = int(xiaoxu_gui * rank / lushu)

        return tl(guixian, rank)

# 履
    lu_r = YR('兌', '乾')
    lu_l = YL('兌', '乾')
    lu_rank = lu_r.total_rank()
    lu_lushu = lu_l.total_lushu()
    lu_gui = gm('履')

    if a == '履' and b == '初爻':
        rank = lu_rank.get(b)
        lushu = lu_lushu.get(b)
        guixian = int(lu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '履' and b == '二爻':

        rank = lu_rank.get(b)
        lushu = lu_lushu.get(b)
        guixian = int(lu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '履' and b == '三爻':

        rank = lu_rank.get(b)
        lushu = lu_lushu.get(b)
        guixian = int(lu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '履' and b == '四爻':

        rank = lu_rank.get(b)
        lushu = lu_lushu.get(b)
        guixian = int(lu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '履' and b == '五爻':

        rank = lu_rank.get(b)
        lushu = lu_lushu.get(b)
        guixian = int(lu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '履' and b == '上爻':

        rank = lu_rank.get(b)
        lushu = lu_lushu.get(b)
        guixian = int(lu_gui * rank / lushu)

        return tl(guixian, rank)

# 泰
    tai_r = YR('乾', '坤')
    tai_l = YL('乾', '坤')
    tai_rank = tai_r.total_rank()
    tai_lushu = tai_l.total_lushu()
    tai_gui = gm('泰')

    if a == '泰' and b == '初爻':
        rank = tai_rank.get(b)
        lushu = tai_lushu.get(b)
        guixian = int(tai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '泰' and b == '二爻':

        rank = tai_rank.get(b)
        lushu = tai_lushu.get(b)
        guixian = int(tai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '泰' and b == '三爻':

        rank = tai_rank.get(b)
        lushu = tai_lushu.get(b)
        guixian = int(tai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '泰' and b == '四爻':

        rank = tai_rank.get(b)
        lushu = tai_lushu.get(b)
        guixian = int(tai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '泰' and b == '五爻':

        rank = tai_rank.get(b)
        lushu = tai_lushu.get(b)
        guixian = int(tai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '泰' and b == '上爻':

        rank = tai_rank.get(b)
        lushu = tai_lushu.get(b)
        guixian = int(tai_gui * rank / lushu)

        return tl(guixian, rank)

# 否
    fou_r = YR('坤', '乾')
    fou_l = YL('坤', '乾')
    fou_rank = fou_r.total_rank()
    fou_lushu = fou_l.total_lushu()
    fou_gui = gm('否')

    if a == '否' and b == '初爻':
        rank = fou_rank.get(b)
        lushu = fou_lushu.get(b)
        guixian = int(fou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '否' and b == '二爻':

        rank = fou_rank.get(b)
        lushu = fou_lushu.get(b)
        guixian = int(fou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '否' and b == '三爻':

        rank = fou_rank.get(b)
        lushu = fou_lushu.get(b)
        guixian = int(fou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '否' and b == '四爻':

        rank = fou_rank.get(b)
        lushu = fou_lushu.get(b)
        guixian = int(fou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '否' and b == '五爻':

        rank = fou_rank.get(b)
        lushu = fou_lushu.get(b)
        guixian = int(fou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '否' and b == '上爻':

        rank = fou_rank.get(b)
        lushu = fou_lushu.get(b)
        guixian = int(fou_gui * rank / lushu)

        return tl(guixian, rank)

# 同人
    tongren_r = YR('離', '乾')
    tongren_l = YL('離', '乾')
    tongren_rank = tongren_r.total_rank()
    tongren_lushu = tongren_l.total_lushu()
    tongren_gui = gm('同人')

    if a == '同人' and b == '初爻':
        rank = tongren_rank.get(b)
        lushu = tongren_lushu.get(b)
        guixian = int(tongren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '同人' and b == '二爻':

        rank = tongren_rank.get(b)
        lushu = tongren_lushu.get(b)
        guixian = int(tongren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '同人' and b == '三爻':

        rank = tongren_rank.get(b)
        lushu = tongren_lushu.get(b)
        guixian = int(tongren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '同人' and b == '四爻':

        rank = tongren_rank.get(b)
        lushu = tongren_lushu.get(b)
        guixian = int(tongren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '同人' and b == '五爻':

        rank = tongren_rank.get(b)
        lushu = tongren_lushu.get(b)
        guixian = int(tongren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '同人' and b == '上爻':

        rank = tongren_rank.get(b)
        lushu = tongren_lushu.get(b)
        guixian = int(tongren_gui * rank / lushu)

        return tl(guixian, rank)

# 大有
    dayou_r = YR('乾', '離')
    dayou_l = YL('乾', '離')
    dayou_rank = dayou_r.total_rank()
    dayou_lushu = dayou_l.total_lushu()
    dayou_gui = gm('大有')

    if a == '大有' and b == '初爻':
        rank = dayou_rank.get(b)
        lushu = dayou_lushu.get(b)
        guixian = int(dayou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大有' and b == '二爻':

        rank = dayou_rank.get(b)
        lushu = dayou_lushu.get(b)
        guixian = int(dayou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大有' and b == '三爻':

        rank = dayou_rank.get(b)
        lushu = dayou_lushu.get(b)
        guixian = int(dayou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大有' and b == '四爻':

        rank = dayou_rank.get(b)
        lushu = dayou_lushu.get(b)
        guixian = int(dayou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大有' and b == '五爻':

        rank = dayou_rank.get(b)
        lushu = dayou_lushu.get(b)
        guixian = int(dayou_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大有' and b == '上爻':

        rank = dayou_rank.get(b)
        lushu = dayou_lushu.get(b)
        guixian = int(dayou_gui * rank / lushu)

        return tl(guixian, rank)

# 謙
    qianken_r = YR('艮', '坤')
    qianken_l = YL('艮', '坤')
    qianken_rank = qianken_r.total_rank()
    qianken_lushu = qianken_l.total_lushu()
    qianken_gui = gm('謙')

    if a == '謙' and b == '初爻':
        rank = qianken_rank.get(b)
        lushu = qianken_lushu.get(b)
        guixian = int(qianken_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '謙' and b == '二爻':

        rank = qianken_rank.get(b)
        lushu = qianken_lushu.get(b)
        guixian = int(qianken_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '謙' and b == '三爻':

        rank = qianken_rank.get(b)
        lushu = qianken_lushu.get(b)
        guixian = int(qianken_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '謙' and b == '四爻':

        rank = qianken_rank.get(b)
        lushu = qianken_lushu.get(b)
        guixian = int(qianken_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '謙' and b == '五爻':

        rank = qianken_rank.get(b)
        lushu = qianken_lushu.get(b)
        guixian = int(qianken_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '謙' and b == '上爻':

        rank = qianken_rank.get(b)
        lushu = qianken_lushu.get(b)
        guixian = int(qianken_gui * rank / lushu)

        return tl(guixian, rank)

# 豫
    yu_r = YR('坤', '震')
    yu_l = YL('坤', '震')
    yu_rank = yu_r.total_rank()
    yu_lushu = yu_l.total_lushu()
    yu_gui = gm('豫')

    if a == '豫' and b == '初爻':
        rank = yu_rank.get(b)
        lushu = yu_lushu.get(b)
        guixian = int(yu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豫' and b == '二爻':

        rank = yu_rank.get(b)
        lushu = yu_lushu.get(b)
        guixian = int(yu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豫' and b == '三爻':

        rank = yu_rank.get(b)
        lushu = yu_lushu.get(b)
        guixian = int(yu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豫' and b == '四爻':

        rank = yu_rank.get(b)
        lushu = yu_lushu.get(b)
        guixian = int(yu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豫' and b == '五爻':

        rank = yu_rank.get(b)
        lushu = yu_lushu.get(b)
        guixian = int(yu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豫' and b == '上爻':

        rank = yu_rank.get(b)
        lushu = yu_lushu.get(b)
        guixian = int(yu_gui * rank / lushu)

        return tl(guixian, rank)

# 随
    sui_r = YR('震', '兌')
    sui_l = YL('震', '兌')
    sui_rank = sui_r.total_rank()
    sui_lushu = sui_l.total_lushu()
    sui_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = sui_rank.get(b)
        lushu = sui_lushu.get(b)
        guixian = int(sui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = sui_rank.get(b)
        lushu = sui_lushu.get(b)
        guixian = int(sui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = sui_rank.get(b)
        lushu = sui_lushu.get(b)
        guixian = int(sui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = sui_rank.get(b)
        lushu = sui_lushu.get(b)
        guixian = int(sui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = sui_rank.get(b)
        lushu = sui_lushu.get(b)
        guixian = int(sui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = sui_rank.get(b)
        lushu = sui_lushu.get(b)
        guixian = int(sui_gui * rank / lushu)

        return tl(guixian, rank)

# 蠱
    gu_r = YR('巽', '艮')
    gu_l = YL('巽', '艮')
    gu_rank = gu_r.total_rank()
    gu_lushu = gu_l.total_lushu()
    gu_gui = gm('蠱')

    if a == '蠱' and b == '初爻':
        rank = gu_rank.get(b)
        lushu = gu_lushu.get(b)
        guixian = int(gu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蠱' and b == '二爻':

        rank = gu_rank.get(b)
        lushu = gu_lushu.get(b)
        guixian = int(gu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蠱' and b == '三爻':

        rank = gu_rank.get(b)
        lushu = gu_lushu.get(b)
        guixian = int(gu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蠱' and b == '四爻':

        rank = gu_rank.get(b)
        lushu = gu_lushu.get(b)
        guixian = int(gu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蠱' and b == '五爻':

        rank = gu_rank.get(b)
        lushu = gu_lushu.get(b)
        guixian = int(gu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蠱' and b == '上爻':

        rank = gu_rank.get(b)
        lushu = gu_lushu.get(b)
        guixian = int(gu_gui * rank / lushu)

        return tl(guixian, rank)

# 臨
    lin_r = YR('兌', '坤')
    lin_l = YL('兌', '坤')
    lin_rank = lin_r.total_rank()
    lin_lushu = lin_l.total_lushu()
    lin_lini = gm('蠱')

    if a == '蠱' and b == '初爻':
        rank = lin_rank.get(b)
        lushu = lin_lushu.get(b)
        linixian = int(lin_lini * rank / lushu)

        return print(tl(linixian, rank))

    elif a == '蠱' and b == '二爻':

        rank = lin_rank.get(b)
        lushu = lin_lushu.get(b)
        linixian = int(lin_lini * rank / lushu)

        return print(tl(linixian, rank))

    elif a == '蠱' and b == '三爻':

        rank = lin_rank.get(b)
        lushu = lin_lushu.get(b)
        linixian = int(lin_lini * rank / lushu)

        return print(tl(linixian, rank))

    elif a == '蠱' and b == '四爻':

        rank = lin_rank.get(b)
        lushu = lin_lushu.get(b)
        linixian = int(lin_lini * rank / lushu)

        return print(tl(linixian, rank))

    elif a == '蠱' and b == '五爻':

        rank = lin_rank.get(b)
        lushu = lin_lushu.get(b)
        linixian = int(lin_lini * rank / lushu)

        return print(tl(linixian, rank))

    elif a == '蠱' and b == '上爻':

        rank = lin_rank.get(b)
        lushu = lin_lushu.get(b)
        linixian = int(lin_lini * rank / lushu)

        return print(tl(linixian, rank))

# 観
    guan_r = YR('坤', '巽')
    guan_l = YL('坤', '巽')
    guan_rank = guan_r.total_rank()
    guan_lushu = guan_l.total_lushu()
    guan_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = guan_rank.get(b)
        lushu = guan_lushu.get(b)
        guixian = int(guan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = guan_rank.get(b)
        lushu = guan_lushu.get(b)
        guixian = int(guan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = guan_rank.get(b)
        lushu = guan_lushu.get(b)
        guixian = int(guan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = guan_rank.get(b)
        lushu = guan_lushu.get(b)
        guixian = int(guan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = guan_rank.get(b)
        lushu = guan_lushu.get(b)
        guixian = int(guan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = guan_rank.get(b)
        lushu = guan_lushu.get(b)
        guixian = int(guan_gui * rank / lushu)

        return tl(guixian, rank)

# 噬嗑
    shike_r = YR('震', '離')
    shike_l = YL('震', '離')
    shike_rank = shike_r.total_rank()
    shike_lushu = shike_l.total_lushu()
    shike_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = shike_rank.get(b)
        lushu = shike_lushu.get(b)
        guixian = int(shike_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = shike_rank.get(b)
        lushu = shike_lushu.get(b)
        guixian = int(shike_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = shike_rank.get(b)
        lushu = shike_lushu.get(b)
        guixian = int(shike_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = shike_rank.get(b)
        lushu = shike_lushu.get(b)
        guixian = int(shike_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = shike_rank.get(b)
        lushu = shike_lushu.get(b)
        guixian = int(shike_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = shike_rank.get(b)
        lushu = shike_lushu.get(b)
        guixian = int(shike_gui * rank / lushu)

        return tl(guixian, rank)

# 賁
    fun_r = YR('離', '艮')
    fun_l = YL('離', '艮')
    fun_rank = fun_r.total_rank()
    fun_lushu = fun_l.total_lushu()
    fun_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = fun_rank.get(b)
        lushu = fun_lushu.get(b)
        guixian = int(fun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = fun_rank.get(b)
        lushu = fun_lushu.get(b)
        guixian = int(fun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = fun_rank.get(b)
        lushu = fun_lushu.get(b)
        guixian = int(fun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = fun_rank.get(b)
        lushu = fun_lushu.get(b)
        guixian = int(fun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = fun_rank.get(b)
        lushu = fun_lushu.get(b)
        guixian = int(fun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = fun_rank.get(b)
        lushu = fun_lushu.get(b)
        guixian = int(fun_gui * rank / lushu)

        return tl(guixian, rank)


# 剥
    bo_r = YR('坤', '艮')
    bo_l = YL('坤', '艮')
    bo_rank = bo_r.total_rank()
    bo_lushu = bo_l.total_lushu()
    bo_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = bo_rank.get(b)
        lushu = bo_lushu.get(b)
        guixian = int(bo_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = bo_rank.get(b)
        lushu = bo_lushu.get(b)
        guixian = int(bo_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = bo_rank.get(b)
        lushu = bo_lushu.get(b)
        guixian = int(bo_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = bo_rank.get(b)
        lushu = bo_lushu.get(b)
        guixian = int(bo_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = bo_rank.get(b)
        lushu = bo_lushu.get(b)
        guixian = int(bo_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = bo_rank.get(b)
        lushu = bo_lushu.get(b)
        guixian = int(bo_gui * rank / lushu)

        return tl(guixian, rank)

# 復
    fu_r = YR('震', '坤')
    fu_l = YL('震', '坤')
    fu_rank = fu_r.total_rank()
    fu_lushu = fu_l.total_lushu()
    fu_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = fu_rank.get(b)
        lushu = fu_lushu.get(b)
        guixian = int(fu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = fu_rank.get(b)
        lushu = fu_lushu.get(b)
        guixian = int(fu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = fu_rank.get(b)
        lushu = fu_lushu.get(b)
        guixian = int(fu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = fu_rank.get(b)
        lushu = fu_lushu.get(b)
        guixian = int(fu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = fu_rank.get(b)
        lushu = fu_lushu.get(b)
        guixian = int(fu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = fu_rank.get(b)
        lushu = fu_lushu.get(b)
        guixian = int(fu_gui * rank / lushu)

        return tl(guixian, rank)

# 无妄
    wuwang_r = YR('震', '乾')
    wuwang_l = YL('震', '乾')
    wuwang_rank = wuwang_r.total_rank()
    wuwang_lushu = wuwang_l.total_lushu()
    wuwang_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = wuwang_rank.get(b)
        lushu = wuwang_lushu.get(b)
        guixian = int(wuwang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = wuwang_rank.get(b)
        lushu = wuwang_lushu.get(b)
        guixian = int(wuwang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = wuwang_rank.get(b)
        lushu = wuwang_lushu.get(b)
        guixian = int(wuwang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = wuwang_rank.get(b)
        lushu = wuwang_lushu.get(b)
        guixian = int(wuwang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = wuwang_rank.get(b)
        lushu = wuwang_lushu.get(b)
        guixian = int(wuwang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = wuwang_rank.get(b)
        lushu = wuwang_lushu.get(b)
        guixian = int(wuwang_gui * rank / lushu)

        return tl(guixian, rank)

# 大畜
    daxu_r = YR('乾', '艮')
    daxu_l = YL('乾', '艮')
    daxu_rank = daxu_r.total_rank()
    daxu_lushu = daxu_l.total_lushu()
    daxu_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = daxu_rank.get(b)
        lushu = daxu_lushu.get(b)
        guixian = int(daxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = daxu_rank.get(b)
        lushu = daxu_lushu.get(b)
        guixian = int(daxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = daxu_rank.get(b)
        lushu = daxu_lushu.get(b)
        guixian = int(daxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = daxu_rank.get(b)
        lushu = daxu_lushu.get(b)
        guixian = int(daxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = daxu_rank.get(b)
        lushu = daxu_lushu.get(b)
        guixian = int(daxu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = daxu_rank.get(b)
        lushu = daxu_lushu.get(b)
        guixian = int(daxu_gui * rank / lushu)

        return tl(guixian, rank)

# 頤
    yi_r = YR('震', '艮')
    yi_l = YL('震', '艮')
    yi_rank = yi_r.total_rank()
    yi_lushu = yi_l.total_lushu()
    yi_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

# 大過
    dagua_r = YR('巽', '兌')
    dagua_l = YL('巽', '兌')
    dagua_rank = dagua_r.total_rank()
    dagua_lushu = dagua_l.total_lushu()
    dagua_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = dagua_rank.get(b)
        lushu = dagua_lushu.get(b)
        guixian = int(dagua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = dagua_rank.get(b)
        lushu = dagua_lushu.get(b)
        guixian = int(dagua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = dagua_rank.get(b)
        lushu = dagua_lushu.get(b)
        guixian = int(dagua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = dagua_rank.get(b)
        lushu = dagua_lushu.get(b)
        guixian = int(dagua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = dagua_rank.get(b)
        lushu = dagua_lushu.get(b)
        guixian = int(dagua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = dagua_rank.get(b)
        lushu = dagua_lushu.get(b)
        guixian = int(dagua_gui * rank / lushu)

        return tl(guixian, rank)

# 坎
    kan_r = YR('坎', '坎')
    kan_l = YL('坎', '坎')
    kan_rank = kan_r.total_rank()
    kan_lushu = kan_l.total_lushu()
    kan_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = kan_rank.get(b)
        lushu = kan_lushu.get(b)
        guixian = int(kan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = kan_rank.get(b)
        lushu = kan_lushu.get(b)
        guixian = int(kan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = kan_rank.get(b)
        lushu = kan_lushu.get(b)
        guixian = int(kan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = kan_rank.get(b)
        lushu = kan_lushu.get(b)
        guixian = int(kan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = kan_rank.get(b)
        lushu = kan_lushu.get(b)
        guixian = int(kan_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = kan_rank.get(b)
        lushu = kan_lushu.get(b)
        guixian = int(kan_gui * rank / lushu)

        return tl(guixian, rank)

# 離
    li_r = YR('離', '離')
    li_l = YL('離', '離')
    li_rank = li_r.total_rank()
    li_lushu = li_l.total_lushu()
    li_gui = gm('随')

    if a == '随' and b == '初爻':
        rank = li_rank.get(b)
        lushu = li_lushu.get(b)
        guixian = int(li_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '二爻':

        rank = li_rank.get(b)
        lushu = li_lushu.get(b)
        guixian = int(li_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '三爻':

        rank = li_rank.get(b)
        lushu = li_lushu.get(b)
        guixian = int(li_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '四爻':

        rank = li_rank.get(b)
        lushu = li_lushu.get(b)
        guixian = int(li_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '五爻':

        rank = li_rank.get(b)
        lushu = li_lushu.get(b)
        guixian = int(li_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '随' and b == '上爻':

        rank = li_rank.get(b)
        lushu = li_lushu.get(b)
        guixian = int(li_gui * rank / lushu)

        return tl(guixian, rank)

    """ 以上、上経三十卦"""
# 咸
    xian_r = YR('艮', '兌')
    xian_l = YL('艮', '兌')
    xian_rank = xian_r.total_rank()
    xian_lushu = xian_l.total_lushu()
    xian_gui = gm('咸')

    if a == '咸' and b == '初爻':
        rank = xian_rank.get(b)
        lushu = xian_lushu.get(b)
        guixian = int(xian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '咸' and b == '二爻':

        rank = xian_rank.get(b)
        lushu = xian_lushu.get(b)
        guixian = int(xian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '咸' and b == '三爻':

        rank = xian_rank.get(b)
        lushu = xian_lushu.get(b)
        guixian = int(xian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '咸' and b == '四爻':

        rank = xian_rank.get(b)
        lushu = xian_lushu.get(b)
        guixian = int(xian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '咸' and b == '五爻':

        rank = xian_rank.get(b)
        lushu = xian_lushu.get(b)
        guixian = int(xian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '咸' and b == '上爻':

        rank = xian_rank.get(b)
        lushu = xian_lushu.get(b)
        guixian = int(xian_gui * rank / lushu)

        return tl(guixian, rank)

# 恒
    heng_r = YR('巽', '震')
    heng_l = YL('巽', '震')
    heng_rank = heng_r.total_rank()
    heng_lushu = heng_l.total_lushu()
    heng_gui = gm('恒')

    if a == '恒' and b == '初爻':
        rank = heng_rank.get(b)
        lushu = heng_lushu.get(b)
        guixian = int(heng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '恒' and b == '二爻':

        rank = heng_rank.get(b)
        lushu = heng_lushu.get(b)
        guixian = int(heng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '恒' and b == '三爻':

        rank = heng_rank.get(b)
        lushu = heng_lushu.get(b)
        guixian = int(heng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '恒' and b == '四爻':

        rank = heng_rank.get(b)
        lushu = heng_lushu.get(b)
        guixian = int(heng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '恒' and b == '五爻':

        rank = heng_rank.get(b)
        lushu = heng_lushu.get(b)
        guixian = int(heng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '恒' and b == '上爻':

        rank = heng_rank.get(b)
        lushu = heng_lushu.get(b)
        guixian = int(heng_gui * rank / lushu)

        return tl(guixian, rank)

# 遯
    dun_r = YR('艮', '乾')
    dun_l = YL('艮', '乾')
    dun_rank = dun_r.total_rank()
    dun_lushu = dun_l.total_lushu()
    dun_gui = gm('遯')

    if a == '遯' and b == '初爻':
        rank = dun_rank.get(b)
        lushu = dun_lushu.get(b)
        guixian = int(dun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '遯' and b == '二爻':

        rank = dun_rank.get(b)
        lushu = dun_lushu.get(b)
        guixian = int(dun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '遯' and b == '三爻':

        rank = dun_rank.get(b)
        lushu = dun_lushu.get(b)
        guixian = int(dun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '遯' and b == '四爻':

        rank = dun_rank.get(b)
        lushu = dun_lushu.get(b)
        guixian = int(dun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '遯' and b == '五爻':

        rank = dun_rank.get(b)
        lushu = dun_lushu.get(b)
        guixian = int(dun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '遯' and b == '上爻':

        rank = dun_rank.get(b)
        lushu = dun_lushu.get(b)
        guixian = int(dun_gui * rank / lushu)

        return tl(guixian, rank)

# 大壮
    dazhuang_r = YR('乾', '震')
    dazhuang_l = YL('乾', '震')
    dazhuang_rank = dazhuang_r.total_rank()
    dazhuang_lushu = dazhuang_l.total_lushu()
    dazhuang_gui = gm('大壮')

    if a == '大壮' and b == '初爻':
        rank = dazhuang_rank.get(b)
        lushu = dazhuang_lushu.get(b)
        guixian = int(dazhuang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大壮' and b == '二爻':

        rank = dazhuang_rank.get(b)
        lushu = dazhuang_lushu.get(b)
        guixian = int(dazhuang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大壮' and b == '三爻':

        rank = dazhuang_rank.get(b)
        lushu = dazhuang_lushu.get(b)
        guixian = int(dazhuang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大壮' and b == '四爻':

        rank = dazhuang_rank.get(b)
        lushu = dazhuang_lushu.get(b)
        guixian = int(dazhuang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大壮' and b == '五爻':

        rank = dazhuang_rank.get(b)
        lushu = dazhuang_lushu.get(b)
        guixian = int(dazhuang_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '大壮' and b == '上爻':

        rank = dazhuang_rank.get(b)
        lushu = dazhuang_lushu.get(b)
        guixian = int(dazhuang_gui * rank / lushu)

        return tl(guixian, rank)

# 晋
    jin_r = YR('坤', '離')
    jin_l = YL('坤', '離')
    jin_rank = jin_r.total_rank()
    jin_lushu = jin_l.total_lushu()
    jin_gui = gm('晋')

    if a == '晋' and b == '初爻':
        rank = jin_rank.get(b)
        lushu = jin_lushu.get(b)
        guixian = int(jin_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '晋' and b == '二爻':

        rank = jin_rank.get(b)
        lushu = jin_lushu.get(b)
        guixian = int(jin_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '晋' and b == '三爻':

        rank = jin_rank.get(b)
        lushu = jin_lushu.get(b)
        guixian = int(jin_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '晋' and b == '四爻':

        rank = jin_rank.get(b)
        lushu = jin_lushu.get(b)
        guixian = int(jin_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '晋' and b == '五爻':

        rank = jin_rank.get(b)
        lushu = jin_lushu.get(b)
        guixian = int(jin_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '晋' and b == '上爻':

        rank = jin_rank.get(b)
        lushu = jin_lushu.get(b)
        guixian = int(jin_gui * rank / lushu)

        return tl(guixian, rank)

# 明夷
    mingyi_r = YR('離', '坤')
    mingyi_l = YL('離', '坤')
    mingyi_rank = mingyi_r.total_rank()
    mingyi_lushu = mingyi_l.total_lushu()
    mingyi_gui = gm('明夷')

    if a == '明夷' and b == '初爻':
        rank = mingyi_rank.get(b)
        lushu = mingyi_lushu.get(b)
        guixian = int(mingyi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '明夷' and b == '二爻':

        rank = mingyi_rank.get(b)
        lushu = mingyi_lushu.get(b)
        guixian = int(mingyi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '明夷' and b == '三爻':

        rank = mingyi_rank.get(b)
        lushu = mingyi_lushu.get(b)
        guixian = int(mingyi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '明夷' and b == '四爻':

        rank = mingyi_rank.get(b)
        lushu = mingyi_lushu.get(b)
        guixian = int(mingyi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '明夷' and b == '五爻':

        rank = mingyi_rank.get(b)
        lushu = mingyi_lushu.get(b)
        guixian = int(mingyi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '明夷' and b == '上爻':

        rank = mingyi_rank.get(b)
        lushu = mingyi_lushu.get(b)
        guixian = int(mingyi_gui * rank / lushu)

        return tl(guixian, rank)

# 家人
    jiaren_r = YR('離', '巽')
    jiaren_l = YL('離', '巽')
    jiaren_rank = jiaren_r.total_rank()
    jiaren_lushu = jiaren_l.total_lushu()
    jiaren_gui = gm('家人')

    if a == '家人' and b == '初爻':
        rank = jiaren_rank.get(b)
        lushu = jiaren_lushu.get(b)
        guixian = int(jiaren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '家人' and b == '二爻':

        rank = jiaren_rank.get(b)
        lushu = jiaren_lushu.get(b)
        guixian = int(jiaren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '家人' and b == '三爻':

        rank = jiaren_rank.get(b)
        lushu = jiaren_lushu.get(b)
        guixian = int(jiaren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '家人' and b == '四爻':

        rank = jiaren_rank.get(b)
        lushu = jiaren_lushu.get(b)
        guixian = int(jiaren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '家人' and b == '五爻':

        rank = jiaren_rank.get(b)
        lushu = jiaren_lushu.get(b)
        guixian = int(jiaren_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '家人' and b == '上爻':

        rank = jiaren_rank.get(b)
        lushu = jiaren_lushu.get(b)
        guixian = int(jiaren_gui * rank / lushu)

        return tl(guixian, rank)

# 睽
    kui_r = YR('兌', '離')
    kui_l = YL('兌', '離')
    kui_rank = kui_r.total_rank()
    kui_lushu = kui_l.total_lushu()
    kui_gui = gm('睽')

    if a == '睽' and b == '初爻':
        rank = kui_rank.get(b)
        lushu = kui_lushu.get(b)
        guixian = int(kui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '睽' and b == '二爻':

        rank = kui_rank.get(b)
        lushu = kui_lushu.get(b)
        guixian = int(kui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '睽' and b == '三爻':

        rank = kui_rank.get(b)
        lushu = kui_lushu.get(b)
        guixian = int(kui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '睽' and b == '四爻':

        rank = kui_rank.get(b)
        lushu = kui_lushu.get(b)
        guixian = int(kui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '睽' and b == '五爻':

        rank = kui_rank.get(b)
        lushu = kui_lushu.get(b)
        guixian = int(kui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '睽' and b == '上爻':

        rank = kui_rank.get(b)
        lushu = kui_lushu.get(b)
        guixian = int(kui_gui * rank / lushu)

        return tl(guixian, rank)

# 蹇
    jian_r = YR('艮', '坎')
    jian_l = YL('艮', '坎')
    jian_rank = jian_r.total_rank()
    jian_lushu = jian_l.total_lushu()
    jian_gui = gm('蹇')

    if a == '蹇' and b == '初爻':
        rank = jian_rank.get(b)
        lushu = jian_lushu.get(b)
        guixian = int(jian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蹇' and b == '二爻':

        rank = jian_rank.get(b)
        lushu = jian_lushu.get(b)
        guixian = int(jian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蹇' and b == '三爻':

        rank = jian_rank.get(b)
        lushu = jian_lushu.get(b)
        guixian = int(jian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蹇' and b == '四爻':

        rank = jian_rank.get(b)
        lushu = jian_lushu.get(b)
        guixian = int(jian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蹇' and b == '五爻':

        rank = jian_rank.get(b)
        lushu = jian_lushu.get(b)
        guixian = int(jian_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '蹇' and b == '上爻':

        rank = jian_rank.get(b)
        lushu = jian_lushu.get(b)
        guixian = int(jian_gui * rank / lushu)

        return tl(guixian, rank)

# 解
    xie_r = YR('坎', '震')
    xie_l = YL('坎', '震')
    xie_rank = xie_r.total_rank()
    xie_lushu = xie_l.total_lushu()
    xie_gui = gm('解')

    if a == '解' and b == '初爻':
        rank = xie_rank.get(b)
        lushu = xie_lushu.get(b)
        guixian = int(xie_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '解' and b == '二爻':

        rank = xie_rank.get(b)
        lushu = xie_lushu.get(b)
        guixian = int(xie_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '解' and b == '三爻':

        rank = xie_rank.get(b)
        lushu = xie_lushu.get(b)
        guixian = int(xie_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '解' and b == '四爻':

        rank = xie_rank.get(b)
        lushu = xie_lushu.get(b)
        guixian = int(xie_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '解' and b == '五爻':

        rank = xie_rank.get(b)
        lushu = xie_lushu.get(b)
        guixian = int(xie_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '解' and b == '上爻':

        rank = xie_rank.get(b)
        lushu = xie_lushu.get(b)
        guixian = int(xie_gui * rank / lushu)

        return tl(guixian, rank)

# 損
    sun_r = YR('兌', '艮')
    sun_l = YL('兌', '艮')
    sun_rank = sun_r.total_rank()
    sun_lushu = sun_l.total_lushu()
    sun_gui = gm('損')

    if a == '損' and b == '初爻':
        rank = sun_rank.get(b)
        lushu = sun_lushu.get(b)
        guixian = int(sun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '損' and b == '二爻':

        rank = sun_rank.get(b)
        lushu = sun_lushu.get(b)
        guixian = int(sun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '損' and b == '三爻':

        rank = sun_rank.get(b)
        lushu = sun_lushu.get(b)
        guixian = int(sun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '損' and b == '四爻':

        rank = sun_rank.get(b)
        lushu = sun_lushu.get(b)
        guixian = int(sun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '損' and b == '五爻':

        rank = sun_rank.get(b)
        lushu = sun_lushu.get(b)
        guixian = int(sun_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '損' and b == '上爻':

        rank = sun_rank.get(b)
        lushu = sun_lushu.get(b)
        guixian = int(sun_gui * rank / lushu)

        return tl(guixian, rank)

# 益
    yi_r = YR('震', '巽')
    yi_l = YL('震', '巽')
    yi_rank = yi_r.total_rank()
    yi_lushu = yi_l.total_lushu()
    yi_gui = gm('益')

    if a == '益' and b == '初爻':
        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '益' and b == '二爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '益' and b == '三爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '益' and b == '四爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '益' and b == '五爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '益' and b == '上爻':

        rank = yi_rank.get(b)
        lushu = yi_lushu.get(b)
        guixian = int(yi_gui * rank / lushu)

        return tl(guixian, rank)

# 夬
    guai_r = YR('乾', '兌')
    guai_l = YL('乾', '兌')
    guai_rank = guai_r.total_rank()
    guai_lushu = guai_l.total_lushu()
    guai_gui = gm('夬')

    if a == '夬' and b == '初爻':
        rank = guai_rank.get(b)
        lushu = guai_lushu.get(b)
        guixian = int(guai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '夬' and b == '二爻':

        rank = guai_rank.get(b)
        lushu = guai_lushu.get(b)
        guixian = int(guai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '夬' and b == '三爻':

        rank = guai_rank.get(b)
        lushu = guai_lushu.get(b)
        guixian = int(guai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '夬' and b == '四爻':

        rank = guai_rank.get(b)
        lushu = guai_lushu.get(b)
        guixian = int(guai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '夬' and b == '五爻':

        rank = guai_rank.get(b)
        lushu = guai_lushu.get(b)
        guixian = int(guai_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '夬' and b == '上爻':

        rank = guai_rank.get(b)
        lushu = guai_lushu.get(b)
        guixian = int(guai_gui * rank / lushu)

        return tl(guixian, rank)

# 姤
    cui_r = YR('巽', '乾')
    cui_l = YL('巽', '乾')
    cui_rank = cui_r.total_rank()
    cui_lushu = cui_l.total_lushu()
    cui_gui = gm('姤')

    if a == '姤' and b == '初爻':
        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '姤' and b == '二爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '姤' and b == '三爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '姤' and b == '四爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '姤' and b == '五爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '姤' and b == '上爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

# 萃
    cui_r = YR('坤', '兌')
    cui_l = YL('坤', '兌')
    cui_rank = cui_r.total_rank()
    cui_lushu = cui_l.total_lushu()
    cui_gui = gm('萃')

    if a == '萃' and b == '初爻':
        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '萃' and b == '二爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '萃' and b == '三爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '萃' and b == '四爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '萃' and b == '五爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '萃' and b == '上爻':

        rank = cui_rank.get(b)
        lushu = cui_lushu.get(b)
        guixian = int(cui_gui * rank / lushu)

        return tl(guixian, rank)

# 升
    sheng_r = YR('巽', '坤')
    sheng_l = YL('巽', '坤')
    sheng_rank = sheng_r.total_rank()
    sheng_lushu = sheng_l.total_lushu()
    sheng_gui = gm('升')

    if a == '升' and b == '初爻':
        rank = sheng_rank.get(b)
        lushu = sheng_lushu.get(b)
        guixian = int(sheng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '升' and b == '二爻':

        rank = sheng_rank.get(b)
        lushu = sheng_lushu.get(b)
        guixian = int(sheng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '升' and b == '三爻':

        rank = sheng_rank.get(b)
        lushu = sheng_lushu.get(b)
        guixian = int(sheng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '升' and b == '四爻':

        rank = sheng_rank.get(b)
        lushu = sheng_lushu.get(b)
        guixian = int(sheng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '升' and b == '五爻':

        rank = sheng_rank.get(b)
        lushu = sheng_lushu.get(b)
        guixian = int(sheng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '升' and b == '上爻':

        rank = sheng_rank.get(b)
        lushu = sheng_lushu.get(b)
        guixian = int(sheng_gui * rank / lushu)

        return tl(guixian, rank)

# 困
    kun4_r = YR('坎', '兌')
    kun4_l = YL('坎', '兌')
    kun4_rank = kun4_r.total_rank()
    kun4_lushu = kun4_l.total_lushu()
    kun4_gui = gm('困')

    if a == '困' and b == '初爻':
        rank = kun4_rank.get(b)
        lushu = kun4_lushu.get(b)
        guixian = int(kun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '困' and b == '二爻':

        rank = kun4_rank.get(b)
        lushu = kun4_lushu.get(b)
        guixian = int(kun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '困' and b == '三爻':

        rank = kun4_rank.get(b)
        lushu = kun4_lushu.get(b)
        guixian = int(kun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '困' and b == '四爻':

        rank = kun4_rank.get(b)
        lushu = kun4_lushu.get(b)
        guixian = int(kun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '困' and b == '五爻':

        rank = kun4_rank.get(b)
        lushu = kun4_lushu.get(b)
        guixian = int(kun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '困' and b == '上爻':

        rank = kun4_rank.get(b)
        lushu = kun4_lushu.get(b)
        guixian = int(kun4_gui * rank / lushu)

        return tl(guixian, rank)

# 井
    jing_r = YR('巽', '坎')
    jing_l = YL('巽', '坎')
    jing_rank = jing_r.total_rank()
    jing_lushu = jing_l.total_lushu()
    jing_gui = gm('井')

    if a == '井' and b == '初爻':
        rank = jing_rank.get(b)
        lushu = jing_lushu.get(b)
        guixian = int(jing_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '井' and b == '二爻':

        rank = jing_rank.get(b)
        lushu = jing_lushu.get(b)
        guixian = int(jing_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '井' and b == '三爻':

        rank = jing_rank.get(b)
        lushu = jing_lushu.get(b)
        guixian = int(jing_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '井' and b == '四爻':

        rank = jing_rank.get(b)
        lushu = jing_lushu.get(b)
        guixian = int(jing_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '井' and b == '五爻':

        rank = jing_rank.get(b)
        lushu = jing_lushu.get(b)
        guixian = int(jing_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '井' and b == '上爻':

        rank = jing_rank.get(b)
        lushu = jing_lushu.get(b)
        guixian = int(jing_gui * rank / lushu)

        return tl(guixian, rank)

# 革
    ge_r = YR('離', '兌')
    ge_l = YL('離', '兌')
    ge_rank = ge_r.total_rank()
    ge_lushu = ge_l.total_lushu()
    ge_gui = gm('革')

    if a == '革' and b == '初爻':
        rank = ge_rank.get(b)
        lushu = ge_lushu.get(b)
        guixian = int(ge_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '革' and b == '二爻':

        rank = ge_rank.get(b)
        lushu = ge_lushu.get(b)
        guixian = int(ge_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '革' and b == '三爻':

        rank = ge_rank.get(b)
        lushu = ge_lushu.get(b)
        guixian = int(ge_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '革' and b == '四爻':

        rank = ge_rank.get(b)
        lushu = ge_lushu.get(b)
        guixian = int(ge_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '革' and b == '五爻':

        rank = ge_rank.get(b)
        lushu = ge_lushu.get(b)
        guixian = int(ge_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '革' and b == '上爻':

        rank = ge_rank.get(b)
        lushu = ge_lushu.get(b)
        guixian = int(ge_gui * rank / lushu)

        return tl(guixian, rank)

# 鼎
    ding_r = YR('巽', '離')
    ding_l = YL('巽', '離')
    ding_rank = ding_r.total_rank()
    ding_lushu = ding_l.total_lushu()
    ding_gui = gm('鼎')

    if a == '鼎' and b == '初爻':
        rank = ding_rank.get(b)
        lushu = ding_lushu.get(b)
        guixian = int(ding_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '鼎' and b == '二爻':

        rank = ding_rank.get(b)
        lushu = ding_lushu.get(b)
        guixian = int(ding_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '鼎' and b == '三爻':

        rank = ding_rank.get(b)
        lushu = ding_lushu.get(b)
        guixian = int(ding_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '鼎' and b == '四爻':

        rank = ding_rank.get(b)
        lushu = ding_lushu.get(b)
        guixian = int(ding_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '鼎' and b == '五爻':

        rank = ding_rank.get(b)
        lushu = ding_lushu.get(b)
        guixian = int(ding_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '鼎' and b == '上爻':

        rank = ding_rank.get(b)
        lushu = ding_lushu.get(b)
        guixian = int(ding_gui * rank / lushu)

        return tl(guixian, rank)

# 震
    zhen_r = YR('震', '震')
    zhen_l = YL('震', '震')
    zhen_rank = zhen_r.total_rank()
    zhen_lushu = zhen_l.total_lushu()
    zhen_gui = gm('震')

    if a == '震' and b == '初爻':
        rank = zhen_rank.get(b)
        lushu = zhen_lushu.get(b)
        guixian = int(zhen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '震' and b == '二爻':

        rank = zhen_rank.get(b)
        lushu = zhen_lushu.get(b)
        guixian = int(zhen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '震' and b == '三爻':

        rank = zhen_rank.get(b)
        lushu = zhen_lushu.get(b)
        guixian = int(zhen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '震' and b == '四爻':

        rank = zhen_rank.get(b)
        lushu = zhen_lushu.get(b)
        guixian = int(zhen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '震' and b == '五爻':

        rank = zhen_rank.get(b)
        lushu = zhen_lushu.get(b)
        guixian = int(zhen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '震' and b == '上爻':

        rank = zhen_rank.get(b)
        lushu = zhen_lushu.get(b)
        guixian = int(zhen_gui * rank / lushu)

        return tl(guixian, rank)

# 艮
    gen_r = YR('艮', '艮')
    gen_l = YL('艮', '艮')
    gen_rank = gen_r.total_rank()
    gen_lushu = gen_l.total_lushu()
    gen_gui = gm('艮')

    if a == '艮' and b == '初爻':
        rank = gen_rank.get(b)
        lushu = gen_lushu.get(b)
        guixian = int(gen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '艮' and b == '二爻':

        rank = gen_rank.get(b)
        lushu = gen_lushu.get(b)
        guixian = int(gen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '艮' and b == '三爻':

        rank = gen_rank.get(b)
        lushu = gen_lushu.get(b)
        guixian = int(gen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '艮' and b == '四爻':

        rank = gen_rank.get(b)
        lushu = gen_lushu.get(b)
        guixian = int(gen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '艮' and b == '五爻':

        rank = gen_rank.get(b)
        lushu = gen_lushu.get(b)
        guixian = int(gen_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '艮' and b == '上爻':

        rank = gen_rank.get(b)
        lushu = gen_lushu.get(b)
        guixian = int(gen_gui * rank / lushu)

        return tl(guixian, rank)

# 漸
    jian4_r = YR('艮', '巽')
    jian4_l = YL('艮', '巽')
    jian4_rank = jian4_r.total_rank()
    jian4_lushu = jian4_l.total_lushu()
    jian4_gui = gm('漸')

    if a == '漸' and b == '初爻':
        rank = jian4_rank.get(b)
        lushu = jian4_lushu.get(b)
        guixian = int(jian4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '漸' and b == '二爻':

        rank = jian4_rank.get(b)
        lushu = jian4_lushu.get(b)
        guixian = int(jian4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '漸' and b == '三爻':

        rank = jian4_rank.get(b)
        lushu = jian4_lushu.get(b)
        guixian = int(jian4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '漸' and b == '四爻':

        rank = jian4_rank.get(b)
        lushu = jian4_lushu.get(b)
        guixian = int(jian4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '漸' and b == '五爻':

        rank = jian4_rank.get(b)
        lushu = jian4_lushu.get(b)
        guixian = int(jian4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '漸' and b == '上爻':

        rank = jian4_rank.get(b)
        lushu = jian4_lushu.get(b)
        guixian = int(jian4_gui * rank / lushu)

        return tl(guixian, rank)

# 帰妹
    guimei_r = YR('兌', '震')
    guimei_l = YL('兌', '震')
    guimei_rank = guimei_r.total_rank()
    guimei_lushu = guimei_l.total_lushu()
    guimei_gui = gm('帰妹')

    if a == '帰妹' and b == '初爻':
        rank = guimei_rank.get(b)
        lushu = guimei_lushu.get(b)
        guixian = int(guimei_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '帰妹' and b == '二爻':

        rank = guimei_rank.get(b)
        lushu = guimei_lushu.get(b)
        guixian = int(guimei_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '帰妹' and b == '三爻':

        rank = guimei_rank.get(b)
        lushu = guimei_lushu.get(b)
        guixian = int(guimei_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '帰妹' and b == '四爻':

        rank = guimei_rank.get(b)
        lushu = guimei_lushu.get(b)
        guixian = int(guimei_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '帰妹' and b == '五爻':

        rank = guimei_rank.get(b)
        lushu = guimei_lushu.get(b)
        guixian = int(guimei_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '帰妹' and b == '上爻':

        rank = guimei_rank.get(b)
        lushu = guimei_lushu.get(b)
        guixian = int(guimei_gui * rank / lushu)

        return tl(guixian, rank)

# 豊
    feng_r = YR('離', '震')
    feng_l = YL('離', '震')
    feng_rank = feng_r.total_rank()
    feng_lushu = feng_l.total_lushu()
    feng_gui = gm('豊')

    if a == '豊' and b == '初爻':
        rank = feng_rank.get(b)
        lushu = feng_lushu.get(b)
        guixian = int(feng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豊' and b == '二爻':

        rank = feng_rank.get(b)
        lushu = feng_lushu.get(b)
        guixian = int(feng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豊' and b == '三爻':

        rank = feng_rank.get(b)
        lushu = feng_lushu.get(b)
        guixian = int(feng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豊' and b == '四爻':

        rank = feng_rank.get(b)
        lushu = feng_lushu.get(b)
        guixian = int(feng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豊' and b == '五爻':

        rank = feng_rank.get(b)
        lushu = feng_lushu.get(b)
        guixian = int(feng_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '豊' and b == '上爻':

        rank = feng_rank.get(b)
        lushu = feng_lushu.get(b)
        guixian = int(feng_gui * rank / lushu)

        return tl(guixian, rank)

# 旅
    lv_r = YR('艮', '離')
    lv_l = YL('艮', '離')
    lv_rank = lv_r.total_rank()
    lv_lushu = lv_l.total_lushu()
    lv_gui = gm('旅')

    if a == '旅' and b == '初爻':
        rank = lv_rank.get(b)
        lushu = lv_lushu.get(b)
        guixian = int(lv_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '旅' and b == '二爻':

        rank = lv_rank.get(b)
        lushu = lv_lushu.get(b)
        guixian = int(lv_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '旅' and b == '三爻':

        rank = lv_rank.get(b)
        lushu = lv_lushu.get(b)
        guixian = int(lv_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '旅' and b == '四爻':

        rank = lv_rank.get(b)
        lushu = lv_lushu.get(b)
        guixian = int(lv_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '旅' and b == '五爻':

        rank = lv_rank.get(b)
        lushu = lv_lushu.get(b)
        guixian = int(lv_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '旅' and b == '上爻':

        rank = lv_rank.get(b)
        lushu = lv_lushu.get(b)
        guixian = int(lv_gui * rank / lushu)

        return tl(guixian, rank)

# 巽
    xun4_r = YR('巽', '巽')
    xun4_l = YL('巽', '巽')
    xun4_rank = xun4_r.total_rank()
    xun4_lushu = xun4_l.total_lushu()
    xun4_gui = gm('巽')

    if a == '巽' and b == '初爻':
        rank = xun4_rank.get(b)
        lushu = xun4_lushu.get(b)
        guixian = int(xun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '巽' and b == '二爻':

        rank = xun4_rank.get(b)
        lushu = xun4_lushu.get(b)
        guixian = int(xun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '巽' and b == '三爻':

        rank = xun4_rank.get(b)
        lushu = xun4_lushu.get(b)
        guixian = int(xun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '巽' and b == '四爻':

        rank = xun4_rank.get(b)
        lushu = xun4_lushu.get(b)
        guixian = int(xun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '巽' and b == '五爻':

        rank = xun4_rank.get(b)
        lushu = xun4_lushu.get(b)
        guixian = int(xun4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '巽' and b == '上爻':

        rank = xun4_rank.get(b)
        lushu = xun4_lushu.get(b)
        guixian = int(xun4_gui * rank / lushu)

        return tl(guixian, rank)

# 兌
    dui_r = YR('兌', '兌')
    dui_l = YL('兌', '兌')
    dui_rank = dui_r.total_rank()
    dui_lushu = dui_l.total_lushu()
    dui_gui = gm('兌')

    if a == '兌' and b == '初爻':
        rank = dui_rank.get(b)
        lushu = dui_lushu.get(b)
        guixian = int(dui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '兌' and b == '二爻':

        rank = dui_rank.get(b)
        lushu = dui_lushu.get(b)
        guixian = int(dui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '兌' and b == '三爻':

        rank = dui_rank.get(b)
        lushu = dui_lushu.get(b)
        guixian = int(dui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '兌' and b == '四爻':

        rank = dui_rank.get(b)
        lushu = dui_lushu.get(b)
        guixian = int(dui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '兌' and b == '五爻':

        rank = dui_rank.get(b)
        lushu = dui_lushu.get(b)
        guixian = int(dui_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '兌' and b == '上爻':

        rank = dui_rank.get(b)
        lushu = dui_lushu.get(b)
        guixian = int(dui_gui * rank / lushu)

        return tl(guixian, rank)

# 渙
    huan4_r = YR('坎', '巽')
    huan4_l = YL('坎', '巽')
    huan4_rank = huan4_r.total_rank()
    huan4_lushu = huan4_l.total_lushu()
    huan4_gui = gm('渙')

    if a == '渙' and b == '初爻':
        rank = huan4_rank.get(b)
        lushu = huan4_lushu.get(b)
        guixian = int(huan4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '渙' and b == '二爻':

        rank = huan4_rank.get(b)
        lushu = huan4_lushu.get(b)
        guixian = int(huan4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '渙' and b == '三爻':

        rank = huan4_rank.get(b)
        lushu = huan4_lushu.get(b)
        guixian = int(huan4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '渙' and b == '四爻':

        rank = huan4_rank.get(b)
        lushu = huan4_lushu.get(b)
        guixian = int(huan4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '渙' and b == '五爻':

        rank = huan4_rank.get(b)
        lushu = huan4_lushu.get(b)
        guixian = int(huan4_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '渙' and b == '上爻':

        rank = huan4_rank.get(b)
        lushu = huan4_lushu.get(b)
        guixian = int(huan4_gui * rank / lushu)

        return tl(guixian, rank)

# 節
    jie2_r = YR('兌', '坎')
    jie2_l = YL('兌', '坎')
    jie2_rank = jie2_r.total_rank()
    jie2_lushu = jie2_l.total_lushu()
    jie2_gui = gm('節')

    if a == '節' and b == '初爻':
        rank = jie2_rank.get(b)
        lushu = jie2_lushu.get(b)
        guixian = int(jie2_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '節' and b == '二爻':

        rank = jie2_rank.get(b)
        lushu = jie2_lushu.get(b)
        guixian = int(jie2_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '節' and b == '三爻':

        rank = jie2_rank.get(b)
        lushu = jie2_lushu.get(b)
        guixian = int(jie2_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '節' and b == '四爻':

        rank = jie2_rank.get(b)
        lushu = jie2_lushu.get(b)
        guixian = int(jie2_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '節' and b == '五爻':

        rank = jie2_rank.get(b)
        lushu = jie2_lushu.get(b)
        guixian = int(jie2_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '節' and b == '上爻':

        rank = jie2_rank.get(b)
        lushu = jie2_lushu.get(b)
        guixian = int(jie2_gui * rank / lushu)

        return tl(guixian, rank)

# 中孚
    zhongfu_r = YR('兌', '巽')
    zhongfu_l = YL('兌', '巽')
    zhongfu_rank = zhongfu_r.total_rank()
    zhongfu_lushu = zhongfu_l.total_lushu()
    zhongfu_gui = gm('中孚')

    if a == '中孚' and b == '初爻':
        rank = zhongfu_rank.get(b)
        lushu = zhongfu_lushu.get(b)
        guixian = int(zhongfu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '中孚' and b == '二爻':

        rank = zhongfu_rank.get(b)
        lushu = zhongfu_lushu.get(b)
        guixian = int(zhongfu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '中孚' and b == '三爻':

        rank = zhongfu_rank.get(b)
        lushu = zhongfu_lushu.get(b)
        guixian = int(zhongfu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '中孚' and b == '四爻':

        rank = zhongfu_rank.get(b)
        lushu = zhongfu_lushu.get(b)
        guixian = int(zhongfu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '中孚' and b == '五爻':

        rank = zhongfu_rank.get(b)
        lushu = zhongfu_lushu.get(b)
        guixian = int(zhongfu_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '中孚' and b == '上爻':

        rank = zhongfu_rank.get(b)
        lushu = zhongfu_lushu.get(b)
        guixian = int(zhongfu_gui * rank / lushu)

        return tl(guixian, rank)

# 小過
    xiaogua_r = YR('艮', '震')
    xiaogua_l = YL('艮', '震')
    xiaogua_rank = xiaogua_r.total_rank()
    xiaogua_lushu = xiaogua_l.total_lushu()
    xiaogua_gui = gm('小過')

    if a == '小過' and b == '初爻':
        rank = xiaogua_rank.get(b)
        lushu = xiaogua_lushu.get(b)
        guixian = int(xiaogua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小過' and b == '二爻':

        rank = xiaogua_rank.get(b)
        lushu = xiaogua_lushu.get(b)
        guixian = int(xiaogua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小過' and b == '三爻':

        rank = xiaogua_rank.get(b)
        lushu = xiaogua_lushu.get(b)
        guixian = int(xiaogua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小過' and b == '四爻':

        rank = xiaogua_rank.get(b)
        lushu = xiaogua_lushu.get(b)
        guixian = int(xiaogua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小過' and b == '五爻':

        rank = xiaogua_rank.get(b)
        lushu = xiaogua_lushu.get(b)
        guixian = int(xiaogua_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '小過' and b == '上爻':

        rank = xiaogua_rank.get(b)
        lushu = xiaogua_lushu.get(b)
        guixian = int(xiaogua_gui * rank / lushu)

        return tl(guixian, rank)

# 既済
    jiji_r = YR('離', '坎')
    jiji_l = YL('離', '坎')
    jiji_rank = jiji_r.total_rank()
    jiji_lushu = jiji_l.total_lushu()
    jiji_gui = gm('随')

    if a == '既済' and b == '初爻':
        rank = jiji_rank.get(b)
        lushu = jiji_lushu.get(b)
        guixian = int(jiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '既済' and b == '二爻':

        rank = jiji_rank.get(b)
        lushu = jiji_lushu.get(b)
        guixian = int(jiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '既済' and b == '三爻':

        rank = jiji_rank.get(b)
        lushu = jiji_lushu.get(b)
        guixian = int(jiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '既済' and b == '四爻':

        rank = jiji_rank.get(b)
        lushu = jiji_lushu.get(b)
        guixian = int(jiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '既済' and b == '五爻':

        rank = jiji_rank.get(b)
        lushu = jiji_lushu.get(b)
        guixian = int(jiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '既済' and b == '上爻':

        rank = jiji_rank.get(b)
        lushu = jiji_lushu.get(b)
        guixian = int(jiji_gui * rank / lushu)

        return tl(guixian, rank)

# 未済
    weiji_r = YR('坎', '離')
    weiji_l = YL('坎', '離')
    weiji_rank = weiji_r.total_rank()
    weiji_lushu = weiji_l.total_lushu()
    weiji_gui = gm('未済')

    if a == '未済' and b == '初爻':
        rank = weiji_rank.get(b)
        lushu = weiji_lushu.get(b)
        guixian = int(weiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '未済' and b == '二爻':

        rank = weiji_rank.get(b)
        lushu = weiji_lushu.get(b)
        guixian = int(weiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '未済' and b == '三爻':

        rank = weiji_rank.get(b)
        lushu = weiji_lushu.get(b)
        guixian = int(weiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '未済' and b == '四爻':

        rank = weiji_rank.get(b)
        lushu = weiji_lushu.get(b)
        guixian = int(weiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '未済' and b == '五爻':

        rank = weiji_rank.get(b)
        lushu = weiji_lushu.get(b)
        guixian = int(weiji_gui * rank / lushu)

        return tl(guixian, rank)

    elif a == '未済' and b == '上爻':

        rank = weiji_rank.get(b)
        lushu = weiji_lushu.get(b)
        guixian = int(weiji_gui * rank / lushu)

        return tl(guixian, rank)


