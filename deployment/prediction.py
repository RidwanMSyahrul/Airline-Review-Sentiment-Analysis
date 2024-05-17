import pandas as pd
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

def run():
    # Load Model
    model_imp_SimpleRNN = load_model('model_imp_SimpleRNN')

    st.title('Airline Review Sentiment Analysis')
    
    with st.form ('Review Form'):
        st.title('Airline Review Form')
        review= st.text_area('Input your review on our Airline here!')

        sub= st.form_submit_button('Submit Data')

        # st.write(data_predict)
        if sub:
            data_predict= {
            'customer_review': review
            }
            df_pred= pd.DataFrame([data_predict])

            y_pred_inf = model_imp_SimpleRNN.predict(df_pred)
            y_pred_inf_class = np.argmax(y_pred_inf, axis=1)

            if y_pred_inf_class[0] == 2:
                result = 'This review is a Promoter.'
            elif y_pred_inf_class[0] == 1:
                result = 'This review is a Passive.'
            else:
                result = 'This review is a Detractor.'


            st.write("Analysis Result : ", result)