import pickle 
import streamlit as st
import pandas as pd

def recommend(meal):
    similar_meal= similarity[new_meal[new_meal['name']== meal].index[0]]
    sorted_meal= sorted(list(enumerate(similar_meal)), reverse= True, key= lambda x: x[1])[1:6]
    
    recommend_meals=[]
    recommend_meal_poster_path=[]
    for i in sorted_meal:
        recommend_meals.append(new_meal['name'].iloc[i[0]])
        recommend_meal_poster_path.append(new_meal['image_url'].iloc[i[0]]) 
    return recommend_meals, recommend_meal_poster_path 


similarity= pickle.load(open("Similarity.pkl",'rb'))
meals_list= pickle.load(open('Meal_dict.pkl','rb'))
new_meal= pd.DataFrame(meals_list)



st.title("Meal Recommendation System")
option= st.selectbox(
    "What would you like to Taste next",
    new_meal['name'].values
)

# if st.button("Recommend"):
#     Recommended_meal, Recommended_poster = recommend(option)
    
#     col1, col2, col3, col4, col5= st.columns(5)
#     with col1:
#         st.header(Recommended_meal[0])
#         st.image(Recommended_poster[0])
#     with col2:
#         st.header(Recommended_meal[1])
#         st.image(Recommended_poster[1])
#     with col3:
#         st.header(Recommended_meal[2])
#         st.image(Recommended_poster[2])
#     with col4:
#         st.header(Recommended_meal[3])
#         st.image(Recommended_poster[3])
#     with col5:
#         st.header(Recommended_meal[4])
#         st.image(Recommended_poster[4])


if st.button("Recommend"):
    Recommended_meal, Recommended_poster = recommend(option)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    def display_recommendation(col, meal, poster):
        with col:
            st.markdown(f"<h3 style='text-align: center; font-size: 18px;'>{meal}</h3>", unsafe_allow_html=True)
            st.image(poster, use_column_width=True)
    
    display_recommendation(col1, Recommended_meal[0], Recommended_poster[0])
    display_recommendation(col2, Recommended_meal[1], Recommended_poster[1])
    display_recommendation(col3, Recommended_meal[2], Recommended_poster[2])
    display_recommendation(col4, Recommended_meal[3], Recommended_poster[3])
    display_recommendation(col5, Recommended_meal[4], Recommended_poster[4])




