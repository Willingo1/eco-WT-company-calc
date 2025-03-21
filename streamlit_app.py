import altair as alt
import pandas as pd
import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Eco Game WT")
st.title("🎬 Movies datasetttt")
st.write("This app does things")

# Define skill names
skill_names = ["mining", "logging", "carpentry", "pottery", "masonry"]

# Initialize DataFrame
df = pd.DataFrame([{"Name": "Willingo", "Unique Skills": 1}])
for col in skill_names:
    df[col] = False

# Editable DataFrame (returns an updated copy)
edited_df = st.data_editor(df, num_rows="dynamic")

# **Recalculate "Unique Skills" after user edits**
edited_df["Unique Skills"] = edited_df[skill_names].sum(axis=1)

# **Show only the updated DataFrame (no duplicates)**
st.data_editor(edited_df, num_rows="dynamic")
