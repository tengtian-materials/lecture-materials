"""各爻の正位と失位の数をまとめる"""
class Yao_Rank:
    
    def __init__(self,xiagua,shanggua):
        """

        Args:
            xiagua (str):誕生年の卦の下卦
            shanggua (str):誕生年の卦の上卦
        returns:
            total_lushu:誕生年の卦の各爻に
            配当された得位・失位の数をかえす。
        """
        self.xiagua = xiagua
        self.shanggua =shanggua
        
    def xia_rank(self):
        """下卦の正位と失位の数"""

        if self.xiagua == '乾':
            self.qian = {'初爻': 9, '二爻': 7, '三爻': 9}
            return self.qian
        elif self.xiagua == '兌':
            self.dui = {'初爻': 9, '二爻': 7, '三爻': 6}
            return self.dui
        elif self.xiagua == '離':
            self.li = {'初爻': 9, '二爻': 6, '三爻': 9}
            return self.li
        elif self.xiagua == '震':
            self.zhen = {'初爻': 9, '二爻': 6, '三爻': 8}
            return self.zhen
        elif self.xiagua == '巽':
            self.xun = {'初爻': 8, '二爻': 7, '三爻': 9}
            return self.xun
        elif self.xiagua == '坎':
            self.kan = {'初爻': 8, '二爻': 7, '三爻': 8}
            return self.kan
        elif self.xiagua == '艮':
            self.gen = {'初爻': 8, '二爻': 6, '三爻': 9}
            return self.gen
        elif self.xiagua == '坤':
            self.kun = {'初爻': 8, '二爻': 6, '三爻': 8}
            return self.kun

    def shang_rank(self):
        """上卦の正位と失位の数"""

        if self.shanggua == '乾':
            self.qian = {'四爻': 7, '五爻': 9, '上爻': 7}
            return self.qian
        elif self.shanggua == '兌':
            self.dui = {'四爻': 7, '五爻': 9, '上爻': 8}
            return self.dui
        elif self.shanggua == '離':
            self.li = {'四爻': 7, '五爻': 8, '上爻': 7}
            return self.li
        elif self.shanggua == '震':
            self.zhen = {'四爻': 7, '五爻': 6, '上爻': 8}
            return self.zhen
        elif self.shanggua == '巽':
            self.xun = {'四爻': 6, '五爻': 9, '上爻': 7}
            return self.xun
        elif self.shanggua == '坎':
            self.kan = {'四爻': 6, '五爻': 9, '上爻': 6}
            return self.kan
        elif self.shanggua == '艮':
            self.gen = {'四爻': 6, '五爻': 8, '上爻': 7}
            return self.gen
        elif self.shanggua == '坤':
            self.kun = {'四爻': 6, '五爻': 8, '上爻': 6}
            return self.kun

    def total_rank(self):
        """各卦の正失の数をまとめる"""
        total_rank = self.xia_rank() | self.shang_rank()
        return total_rank

