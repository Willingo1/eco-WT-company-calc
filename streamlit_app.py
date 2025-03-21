import altair as alt
import pandas as pd
import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Eco Game WT")
st.title("🎬 Movies datasetttt")
st.write("This app does things")

# Define skill names
skill_names = ["mining", "logging", "carpentry", "pottery", "masonry"]

# Initialize the dataframe in session state (only once)
if "df" not in st.session_state:
    df = pd.DataFrame([{"Name": "Willingo", "Unique Skills": 1}])
    for col in skill_names:
        df[col] = False
    st.session_state.df = df #in session state it persists

# Display editable DataFrame
#edited_df is this instance of the dataframe and loads the persist3ent session state dude
edited_df = st.data_editor(st.session_state.df, num_rows="dynamic")

# Recalculate "Unique Skills" based on edited booleans
edited_df["Unique Skills"] = edited_df.select_dtypes(include=bool).sum(axis=1)

# Save changes back to session state
st.session_state.df = edited_df

# Display the updated DataFrame to verify changes
# this is what is truly shown
st.dataframe(st.session_state.df)

# To help debug
st.data_editor(df, key="my_key", num_rows="dynamic")
st.write("Here's the value in Session State:")
st.write(st.session_state["my_key"])