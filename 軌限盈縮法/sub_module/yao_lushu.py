"""各爻の七均の数をまとめる"""
class Yao_Lushu:   
    def __init__(self,xiagua,shanggua):
        """

        Args:
            xiagua (str):誕生年の卦の下卦
            shanggua (str):誕生年の卦の上卦
        returns:
            total_lushu:誕生年の卦の各爻に
            配当された七均の数をかえす。
        """
        self.xiagua = xiagua
        self.shanggua =shanggua
        
    def xia_lushu(self):
        """下卦の七均の数"""
        
        if self.xiagua == '乾':
            self.qian = {'初爻': 81, '二爻': 72, '三爻': 64}
            return self.qian
        elif self.xiagua == '兌':
            self.dui = {'初爻': 72, '二爻': 64, '三爻': 56}
            return self.dui
        elif self.xiagua == '離':
            self.li = {'初爻': 64, '二爻': 56, '三爻': 54}
            return self.li
        elif self.xiagua == '震':
            self.zhen = {'初爻': 42, '二爻': 81, '三爻': 72}
            return self.zhen
        elif self.xiagua == '巽':
            self.xun = {'初爻': 56, '二爻': 54, '三爻': 48}
            return self.xun
        elif self.xiagua == '坎':
            self.kan = {'初爻': 48, '二爻': 42, '三爻': 81}
            return self.kan
        elif self.xiagua == '艮':
            self.gen = {'初爻': 54, '二爻': 48, '三爻': 42}
            return self.gen
        elif self.xiagua == '坤':
            self.kun = {'初爻': 54, '二爻': 48, '三爻': 42}
            return self.kun

    def shang_lushu(self):
        """"上卦の七均の数"""

        if self.shanggua == '乾':
            self.qian = {'四爻': 56, '五爻': 54, '上爻': 48}
            return self.qian
        elif self.shanggua == '兌':
            self.dui = {'四爻': 54, '五爻': 48, '上爻': 42}
            return self.dui
        elif self.shanggua == '離':
            self.li = {'四爻': 48, '五爻': 42, '上爻': 81}
            return self.li
        elif self.shanggua == '震':
            self.zhen = {'四爻': 64, '五爻': 56, '上爻': 54}
            return self.zhen
        elif self.shanggua == '巽':
            self.xun = {'四爻': 73, '五爻': 64, '上爻': 56}
            return self.xun
        elif self.shanggua == '坎':
            self.kan = {'四爻': 72, '五爻': 64, '上爻': 56}
            return self.kan
        elif self.shanggua == '艮':
            self.gen = {'四爻': 81, '五爻': 72, '上爻': 64}
            return self.gen
        elif self.shanggua == '坤':
            self.kun = {'四爻': 81, '五爻': 72, '上爻': 64}
            return self.kun

    def total_lushu(self):
        """各卦の七均の数をまとめる"""
        total_lushu = self.xia_lushu() | self.shang_lushu()       
        return total_lushu


