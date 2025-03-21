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

# Editable DataFrame without column C
edited_data = st.data_editor(
    st.session_state.df.drop(columns=["C"]),  # Users edit only A & B
    num_rows="dynamic",
    key="editor"
)

# Update session state DataFrame with recalculated column C
st.session_state.df.update(edited_data)  # Update A & B
st.session_state.df["C"] = st.session_state.df["A"] * st.session_state.df["B"]  # Recalculate C

# Re-display the same updated DataFrame (overwriting the previous one)
st.data_editor(
    st.session_state.df,  # Now includes updated C
    num_rows="dynamic",
    key="updated_editor",
    disabled=["C"]  # Prevent manual editing of C
)


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