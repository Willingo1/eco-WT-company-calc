import altair as alt
import pandas as pd
import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Eco Game WT")
st.title("🎬 Movies datasetttt")
st.write("This app does things")


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

# Editable DataFrame (this is where user interacts)
df = st.data_editor(df, num_rows="dynamic")

# **Recalculate "Unique Skills" before redisplaying**
df["Unique Skills"] = df[skill_names].sum(axis=1)

# **Now, display only the updated editable DataFrame**
st.data_editor(df, num_rows="dynamic")
