import streamlit as st

st.title('KE Zubereitet')

with st.form(key='columns_in_form'):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        carbs = st.text_input('Carbs/100g')
    with c2:
        trockenmasse = st.text_input('Trockenmasse')
    with c3:
        zubereitete_masse = st.text_input('Masse zubereiten')
    with c4:
        teller = st.text_input('Teller')
    calculateButton = st.form_submit_button(label = 'Calculate')

if calculateButton:
    ke = round((float(teller)/float(zubereitete_masse))*(float(carbs)*float(trockenmasse)/1000), 4)
    st.write(f'Die Anzahl KE beträgt {ke}.')
