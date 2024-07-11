import streamlit as st
import pandas as pd
import pickle
lawyer_data = pd.read_csv("dataset.csv")
similarity = pickle.load(open("similarity.pkl", 'rb'))
lawyer_names = lawyer_data['Name'].tolist()

st.header("Lawyer Recommender")

selected_lawyer = st.selectbox("Select a lawyer", lawyer_names)

def recommend(lawyer_data, target_name):
    index = lawyer_data[lawyer_data['Name'] == target_name].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_lawyers = []
    
    for i in distance[1:6]:
        recommend_lawyers.append(lawyer_data.iloc[i[0]]['Name'])
    
    return recommend_lawyers

if st.button("Show Recommendations"):
    recommended_lawyers = recommend(lawyer_data, selected_lawyer)
    st.write("Selected lawyer:", selected_lawyer)
    st.write("Top 5 Recommended Lawyers:")
    for i, lawyer in enumerate(recommended_lawyers):
        st.write(f"{i + 1}. {lawyer}")




