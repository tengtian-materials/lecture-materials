import datetime
import streamlit as st

def solarTerm_and_date(pre_b_year):
    dongzhi_date = {'name':'冬至', 'month':12, 'd':22.6587, 'a':0.242752, 'deltaYear':0}
    month = dongzhi_date['month']
    d = dongzhi_date['d']
    a = dongzhi_date['a']
    deltaYear = dongzhi_date['deltaYear']
    day = int(d + (a * (pre_b_year + deltaYear - 1900 )) - int((pre_b_year + deltaYear - 1900) / 4))
    return datetime.datetime(pre_b_year, month , day)

def cal_days(b_year,b_month,b_day):
    birth_days = datetime.datetime(b_year, b_month, b_day)
    dongzhi_date_days=solarTerm_and_date(b_year-1)
    add_days = birth_days - dongzhi_date_days 
    if add_days.days + 1 <365:
       return add_days.days + 1
    else:
        dongzhi_date_days=solarTerm_and_date(b_year)
        add_days = birth_days - dongzhi_date_days
        return  add_days.days + 1  

st.title('冬至から誕生日までの日数')

with st.form('form', clear_on_submit=False):
    b_year = st.number_input('誕生年を入力してください', min_value=1950,
                           max_value=2050, value=2000, step=1)
    b_month = st.number_input('誕生月を入力してください', min_value=1, max_value=12, value=1)
    b_day = st.number_input('誕生日を入力してください', min_value=1, max_value=31, value=1)
    submit_btn = st.form_submit_button('送信')

if submit_btn:
    try:
        st.write(f'#### 冬至から誕生日までの日数は:{cal_days(b_year,b_month,b_day)}')
    
    except ValueError:
        st.write('#### エラー！ 正確な値を入力してください')

    
if __name__ == '__main__':
  print(solarTerm_and_date(1989))
  print(cal_days(1989,2,24))
 
  
