import altair as alt
import pandas as pd
import streamlit as st

import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    "A": [10, 20, 30],
    "B": [2, 3, 4],
    "C": [0, 0, 0]  # Will be recalculated
}
df = pd.DataFrame(data)

# Initialize session state
if "df" not in st.session_state:
    st.session_state.df = df

# Editable DataFrame
edited_df = st.data_editor(st.session_state.df.drop(columns=["C"]), num_rows="dynamic")

# Recalculate column C based on A * B
edited_df["C"] = edited_df["A"] * edited_df["B"]

# Save updated DataFrame
st.session_state.df = edited_df

# Display the updated DataFrame interactively
st.data_editor(st.session_state.df, num_rows="dynamic", key="updated_editor")


'''
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

# Store DataFrame in session state
if "df" not in st.session_state:
    st.session_state.df = df


# Editable DataFrame (returns an updated copy)
edited_df = st.data_editor(st.session_state.df, num_rows="dynamic")

# **Recalculate "Unique Skills" after user edits**
edited_df["Unique Skills"] = edited_df[skill_names].sum(axis=1)

# save updated df
st.session_state.df=edited_df

# **Show only the updated DataFrame (no duplicates)**
st.write("updated df")
st.data_editor(edited_df, num_rows="dynamic")
'''