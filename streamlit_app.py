import pandas as pd
import streamlit as st


# Define skill names
skill_names = ["mining", "logging", "carpentry", "pottery", "masonry"]


@st.cache_data
def load_data():
    """Loads the initial DataFrame."""
    df = pd.DataFrame([{"Name": "Willingo", "Unique Skills": 0}])  # Default Unique Skills to 0
    for col in skill_names:
        df[col] = False  # Initialize skill columns as unchecked
    return df


# Load data initially
if "df" not in st.session_state:
    st.session_state.df = load_data()


# Display editable DataFrame
edited_df = st.data_editor(st.session_state.df, key="df_editor", num_rows="dynamic")


# Recalculate "Unique Skills" after user edits
edited_df["Unique Skills"] = edited_df[skill_names].sum(axis=1)


# Save the updated DataFrame back to session state
st.session_state.df = edited_df


# Debugging output
st.write("Here's the value in Session State:")
st.write(st.session_state.df)
