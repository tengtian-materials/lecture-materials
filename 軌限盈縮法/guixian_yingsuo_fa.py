from sub_module.zhusui_guayao import zhusui_guayao as ZG
from sub_module.total_lifespan import lifespan

import streamlit as st

st.title('軌限盈縮法')

with st.form('form', clear_on_submit=False):
    year = st.number_input('誕生年を入力してください', min_value=1950,
                           max_value=2050, value=2000, step=1)
    month = st.number_input('誕生月を入力してください', min_value=1, max_value=12, value=1)
    submit_btn = st.form_submit_button('送信')

if submit_btn:
    try:
        gua_yao = ZG(year, month)
        birth_gua = str(gua_yao.zhusui_gua_method())
        birth_yao = str(gua_yao.zhusui_yao_method())
        st.write(f'あなたの誕生年の卦:{birth_gua}')
        st.write(f'あなたの誕生月の爻:{birth_yao}')
        

        st.write(f'あなたの寿命:{lifespan(birth_gua, birth_yao)}')
    
    except ValueError:
            st.write('数字を入力してください')

if __name__ == '__main__':
    
