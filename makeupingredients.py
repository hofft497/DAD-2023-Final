import streamlit as st
import pandas as pd
import openai 

openai.api_key = "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"

makeup_data = pd.read_csv('cosmetics.csv')

def main():
    st.title('Makeup Ingredient Search')
    st.write('Enter an ingredient to find makeup products that contain it.')

    ingredient = st.text_input('Enter an ingredient')

    filtered_data = makeup_data[makeup_data['Ingredients'].str.contains(ingredient, case=False)]

    st.subheader('Makeup products containing the ingredient:')
    st.dataframe(filtered_data)

if __name__ == '__main__':
    main()
