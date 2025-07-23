"""誕生年月の卦爻を導き出す"""
class zhusui_guayao:

    def __init__(self, year, month):
        self.year = year
        self.month = month

        self.year_1 = ['乾', '坤']
        self.year_2 = ['屯', '蒙']
        self.year_3 = ['需', '訟']
        self.year_4 = ['師', '比']
        self.year_5 = ['小畜', '履']
        self.year_6 = ['泰', '否']
        self.year_7 = ['同人', '大有']
        self.year_8 = ['謙', '豫']
        self.year_9 = ['随', '蠱']
        self.year_10 = ['臨', '観']
        self.year_11 = ['噬嗑', '賁']
        self.year_12 = ['剥', '復']
        self.year_13 = ['无妄', '大畜']
        self.year_14 = ['頤', '大過']
        self.year_15 = ['坎', '離']
        self.year_16 = ['咸', '恒']
        self.year_17 = ['遯', '大壮']
        self.year_18 = ['晋', '明夷']
        self.year_19 = ['家人', '睽']
        self.year_20 = ['蹇', '解']
        self.year_21 = ['損', '益']
        self.year_22 = ['夬', '姤']
        self.year_23 = ['萃', '升']
        self.year_24 = ['困', '井']
        self.year_25 = ['革', '鼎']
        self.year_26 = ['震', '艮']
        self.year_27 = ['漸', '帰妹']
        self.year_28 = ['豊', '旅']
        self.year_29 = ['巽', '兌']
        self.year_30 = ['渙', '節']
        self.year_31 = ['中孚', '小過']
        self.year_32 = ['既済', '未済']

        self.list_s = [self.year_1, self.year_2, self.year_3, self.year_4, self.year_5, self.year_6, self.year_7, self.year_8,
                       self.year_9, self.year_10, self.year_11, self.year_12, self.year_13, self.year_14, self.year_15, self.year_16,
                       self.year_17, self.year_18, self.year_19, self.year_20, self.year_21, self.year_22, self.year_23, self.year_24,
                       self.year_25, self.year_26, self.year_27, self.year_28, self.year_29, self.year_30, self.year_31, self.year_32]

        self.month_1 = {1: '二爻', 2: '三爻', 3: '三爻', 4: '二爻', 5: '四爻', 6: '初爻',
                        7: '五爻', 8: '上爻', 9: '上爻', 10: '五爻', 11: '初爻', 12: '四爻'}
        self.month_2 = {1: '初爻', 2: '二爻', 3: '二爻', 4: '初爻', 5: '三爻', 6: '上爻',
                        7: '四爻', 8: '五爻', 9: '五爻', 10: '四爻', 11: '上爻', 12: '三爻'}
        self.month_3 = {1: '上爻', 2: '初爻', 3: '初爻', 4: '上爻', 5: '二爻', 6: '五爻',
                        7: '三爻', 8: '四爻', 9: '四爻', 10: '三爻', 11: '五爻', 12: '二爻'}
        self.month_4 = {1: '五爻', 2: '上爻', 3: '上爻', 4: '五爻', 5: '初爻', 6: '四爻',
                        7: '二爻', 8: '三爻', 9: '三爻', 10: '二爻', 11: '四爻', 12: '初爻'}
        self.month_5 = {1: '四爻', 2: '五爻', 3: '五爻', 4: '四爻', 5: '上爻', 6: '三爻',
                        7: '初爻', 8: '二爻', 9: '二爻', 10: '初爻', 11: '三爻', 12: '上爻'}
        self.month_6 = {1: '三爻', 2: '四爻', 3: '四爻', 4: '三爻', 5: '五爻', 6: '二爻',
                        7: '上爻', 8: '初爻', 9: '初爻', 10: '上爻', 11: '二爻', 12: '五爻'}

        self.month_1_n = [1, 7, 13, 19, 25, 31]
        self.month_2_n = [0, 2, 8, 14, 20, 26, 32]
        self.month_3_n = [3, 9, 15, 21, 27]
        self.month_4_n = [4, 10, 16, 22, 28]
        self.month_5_n = [5, 11, 17, 23, 29]
        self.month_6_n = [6, 12, 18, 24, 30]
        """month1-6に対応するyear1-32までの番号"""

    def zhusui_gua_method(self):
        """誕生年の主歳卦を導き出す"""
        years_since_gua = (2759946 + 481 + self.year) % 32

        zhusui_gua = self.list_s[years_since_gua-1]
        self.gua = zhusui_gua[1] if self.month % 2 == 0 else zhusui_gua[0]
        return self.gua

    def zhusui_yao_method(self):
        """誕生月の爻を導き出す"""
        years_since_gua = (2759946 + 481 + self.year) % 32

        if years_since_gua in self.month_1_n:
            self.yao = self.month_1[self.month]

        elif years_since_gua in self.month_2_n:
            self.yao = self.month_2[self.month]

        elif years_since_gua in self.month_3_n:
            self.yao = self.month_3[self.month]

        elif years_since_gua in self.month_4_n:
            self.yao = self.month_4[self.month]

        elif years_since_gua in self.month_5_n:
            self.yao = self.month_5[self.month]

        elif years_since_gua in self.month_6_n:
            self.yao = self.month_6[self.month]
        return self.yao
