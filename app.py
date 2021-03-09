# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:59:29 2021

@author: prana
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle



loaded_model=pickle.load(open('gram_model_dt.sav', 'rb'))


def predict_note_authentication(district, market, variety,day, month, year):
    
    prediction=loaded_model.predict([[district, market, variety,day, month, year]])
    print(prediction)
    return prediction





def main():
    st.title("Price Predictor for Tomato")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">ML App </h2>
    </div>
    """
    st.sidebar.selectbox('Disticts',('Hassan-9', 'Chikmagalur-4', 'Kolar-11', 'Belgaum-1', 'Bellary-2',
       'Bangalore-0', 'Chamrajnagar-3', 'Davangere-6', 'Dharwad-7', 'Gadag-8',
       'Madikeri(Kodagu)-12', 'Haveri-10', 'Chitradurga-5', 'Mysore-15', 'Mandya-13',
       'Mangalore(Dakshin Kannad)-14', 'Shimoga-17', 'Raichur-16', 'Tumkur-18',
       'Udupi-19' ))
    st.sidebar.selectbox('Markets',( 'Arasikere-0', 'Bagepalli-1', 'Bangarpet-2', 'Belgaum-3', 'Bellary-4',
       'Belur-5', 'Binny Mill (F&V)-6, Bangalore-7', 'Chamaraj Nagar-8',
       'Channapatana-9', 'Channarayapatna-10', 'Chickkaballapura-11',
       'Chikkamagalore-12', 'Chintamani-13', 'Davangere-14', 'Dharwar-15',
       'Doddaballa Pur-16', 'Gadag-17', 'Gonikappal-18', 'Gowribidanoor-19',
       'Gundlupet-20', 'Hassan-21', 'Haveri-22', 'Hiriyur-23', 'Holalkere-24',
       'Holenarsipura-25', 'Honnali-26', 'Hoskote-27', 'Hospet-28',
       'Hubli (Amaragol)-29', 'Hunsur-30', 'K.R. Pet-31', 'K.R.Nagar-32', 'Kadur-33',
       'Kanakapura-34', 'Kolar-35', 'Kollegal-36', 'Koppa-37', 'Kudchi-38', 'Maddur-39',
       'Malur-40', 'Mangalore-41', 'Mulabagilu-42', 'Mysore (Bandipalya)-43',
       'Nagamangala-44', 'Nanjangud-45', 'Ramanagara-46', 'Ranebennur-47',
       'Sakaleshpura-48', 'Santhesargur-49', 'Shimoga-50', 'Sindhanur-51',
       'Somvarpet-52', 'Srinivasapur-53', 'T. Narasipura-54', 'Tarikere-55',
       'Thirthahalli-56', 'Tiptur-57', 'Tumkur-58', 'Udupi-59'))
    
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    district = st.text_input("district","select number from district sidebar")
    market= st.text_input("market","select number from market sidebar")
    variety = st.text_input("variety","Normal-0 Hybrid-1")
    day = st.text_input("day","0-30")
    month = st.text_input("month","0-11")
    year = st.text_input("year","")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(district, market, variety,day, month, year)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()