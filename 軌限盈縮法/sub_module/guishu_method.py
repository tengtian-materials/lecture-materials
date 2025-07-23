"""軌数を求める"""
def guishu_method(gua):
    """
    args:
        gua(str): 誕生年の卦
    return:
        guishu(int):誕生年の卦の軌数
    """
    yang6 = (6 * 36 + 6 * 28)*2
    yang5_yin1 = (5 * 36 + 5 * 28+ 1 * 24 + 1 *32) * 2
    yang4_yin2 = (4 * 36 + 4 * 28+ 2 * 24 + 2 *32) * 2  
    yang3_yin3 = (3 * 36 + 3 * 28+ 3 * 24 + 3 *32) * 2
    yang2_yin4 = (2 * 36 + 2 * 28+ 4 * 24 + 4 *32) * 2
    yang1_yin5 = (1 * 36 + 1 * 28+ 5 * 24 + 5 *32) * 2
    yin6 = (6 * 24 + 6 *32) * 2
    """
    陽六の軌数は七百六十八、陽五陰一は七百五十二、陽四陰二は七百三十六、
    陽三陰三は七百二十、陽二陰四は七百四、陽一陰五は六百八十八、陰六は六百七十二となる
    """
    
    yang6_gua = '乾'
    yang5_yin1_gua = ['小畜' , '履' ,'同人' , '大有' , '夬', '姤'] 
    yang4_yin2_gua = ['需' , '訟' , '无妄' , '大畜' , '大過' , '離' , '遯' \
            , '大壮' , '家人' , '睽' , '革' ,  '鼎' , '巽' , '兌' , '中孚']
    yang3_yin3_gua = [ '泰' , '否'  , '随' , '蠱' , '噬嗑' , '賁' , '咸' , '恒'\
            ,'損' , '益' , '困' , '井' , '漸' ,  '帰妹' , '豊' ,  '旅' , '渙' , '節' , '既済' ,  '未済']
    yang2_yin4_gua =['屯', '蒙' , '臨' , '観' , '頤', '坎','晋' , '明夷', '蹇' , '解','萃', '升', '震', '艮','小過']
    yang1_yin5_gua = ['師' , '比' , '謙' , '豫' , '剥' , '復']
    yin6_gua = '坤'

    yang6_gua_guishu ={yang6_gua:yang6}
    yang5_yin1_gua_guishu = {k: yang5_yin1  for k  in yang5_yin1_gua}
    yang4_yin2_gua_guishu = {k: yang4_yin2  for k  in yang4_yin2_gua}
    yang3_yin3_gua_guishu = {k: yang3_yin3  for k  in yang3_yin3_gua}
    yang2_yin4_gua_guishu = {k: yang2_yin4  for k  in yang2_yin4_gua}
    yang1_yin5_gua_guishu = {k: yang1_yin5  for k  in yang1_yin5_gua}
    yin6_gua_guishu = {yin6_gua:yin6}
    """六十四卦と軌数を結びつける。"""
    
    total_gua_guishu = yang6_gua_guishu | yang5_yin1_gua_guishu | yang4_yin2_gua_guishu | yang3_yin3_gua_guishu\
        |  yang2_yin4_gua_guishu | yang1_yin5_gua_guishu | yin6_gua_guishu
    """六十四卦すべての軌数をまとめる。"""
    
    for i_key,i_value in total_gua_guishu.items():
        if i_key == gua:
           guishu = i_value
           break
    return guishu 


            
    
