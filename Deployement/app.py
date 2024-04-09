import streamlit as st
import pickle 
import pandas as pd
teams=['Chennai Super Kings',
 'Delhi Daredevils',
 'Kings XI Punjab',
 'Kolkata Knight Riders',
 'Mumbai Indians',
 'Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Sunrisers Hyderabad']

cities=['Hyderabad', 'Pune', 'Rajkot', 'Indore', 'Bangalore', 'Mumbai',
       'Kolkata', 'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai',
       'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Kochi',
       'Visakhapatnam', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah',
       'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))

st.title('IPL WIN PREDICTOR')

col1 ,col2,col3 = st.columns(3)

with col1:
    batting_team=st.selectbox('Select the batting team ',sorted(teams))
with col2:
    bowling_team=st.selectbox('Select the bowling team ',sorted(teams))

with col3:
    city=st.selectbox('select venue',sorted(cities))

target=st.number_input('Target')

col4,col5,col6=st.columns(3)

with col4:
    score=st.number_input('Score')
with col5:
    overs=st.number_input('Overs completed')
with col6:
    wickets=st.number_input('Wickets out')

if st.button('Predict Probablity'):
    runs_left=target-score
    balls_left=120-(overs*6)
    wickets=10-wickets
    crr=score/overs
    rrr=(runs_left*6)/balls_left

    
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")