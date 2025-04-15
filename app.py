import pandas as pd
import streamlit as st

df = pd.read_csv("C:/Users/ASUS/Desktop/music-recommender/clustered_df.csv")



if 'name' not in df.columns:
    st.error("The column 'name' is missing. Please check your dataset.")
else:
    df = df[df['name'].notna()]
    df['name_lower'] = df['name'].str.lower()

    st.title("🎵 Music Recommendation System")

    search_query = st.text_input("Enter a song name:")

    if search_query:
        search_query = search_query.strip().lower()
        results = df[df['name_lower'].str.contains(search_query)]

        if not results.empty:
            st.subheader("🔍 Matching Songs")
            st.dataframe(results[['name', 'artists']].head(10))

            cluster_col = [col for col in df.columns if 'cluster' in col.lower()]
            if cluster_col:
                selected_cluster = results[cluster_col[0]].iloc[0]
                st.subheader("🎧 Recommended Songs")
                recommended = df[df[cluster_col[0]] == selected_cluster]
                st.dataframe(recommended[['name', 'artists']].sample(10))
            else:
                st.info("Cluster column not found — can't show recommendations.")
        else:
            st.warning("No matching songs found.")
