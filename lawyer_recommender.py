import streamlit as st
import pickle
lawyer_data = pickle.load(open("lawyers_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
lawyer_names = lawyer_data['Name'].tolist()

st.header("Lawyer recommender")

selected_lawyer = st.selectbox("Select a lawyer", lawyer_names)

def recommend(target_name):
    index = lawyer_data[lawyer_data['Name'] == target_name].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    store = []
    for i in distance[1:6]:
        store.append(lawyer_data.iloc[i[0]]['Name'])
    return store

if st.button("Show recommendation"):
    recommended_lawyers = recommend(selected_lawyer)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_lawyers[0])
    with col2:
        st.text(recommended_lawyers[1])
    with col3:
        st.text(recommended_lawyers[2])
    with col4:
        st.text(recommended_lawyers[3])
    with col5:
        st.text(recommended_lawyers[4])
    st.write("Selected lawyer:", selected_lawyer)

