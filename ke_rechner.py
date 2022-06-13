import streamlit as st
import pandas as pd

st.title('🥰 KE Rechner')

with st.form(key='columns_in_form'):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        food = st.text_input("Food")
    with c2:
        carbs = st.text_input("Carbs/100g")
    with c3:
        grams = st.text_input('Grams')
    with c4:
        factor = st.text_input('Factor')
    addButton = st.form_submit_button(label = 'Add')

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.write('Food')
with c2:
    st.write('Grams')
with c3:
    st.write('KE')
with c4:
    st.write('IE')

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Food', 'Grams', 'KE', 'IE'])

if addButton:
    ke = round((int(carbs)*(int(grams)/100)),4)
    ie = round(ke * float(factor), 4)
    df2 = pd.DataFrame({'Food': [food], 'Grams': [grams], 'KE': [ke], 'IE': [ie]})
    st.session_state.df = pd.concat([st.session_state.df, df2])
    for row in range(len(st.session_state.df)):
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.write(st.session_state.df.Food.iloc[row])
        with c2:
            st.write(st.session_state.df.Grams.iloc[row])
        with c3:
            st.write(str(st.session_state.df.KE.iloc[row]))
        with c4:
            st.write(str(st.session_state.df.IE.iloc[row]))

st.write('')
sum_ke = st.session_state.df.KE.apply(lambda x: float(x))
sum_ie = st.session_state.df.IE.apply(lambda x: float(x))
c1, c2 = st.columns(2)
with c1:
    st.write(f'Total KE: {sum_ke.sum()}')
with c2:
    st.write(f'Total IE: {sum_ie.sum()}')





with st.form(key='test'):
    refreshButton = st.form_submit_button(label = 'Refresh')
if refreshButton:
    st.session_state.df = pd.DataFrame(columns=['Food', 'Grams', 'KE', 'IE'])
    sum_ke = 0
    sum_ie = 0


