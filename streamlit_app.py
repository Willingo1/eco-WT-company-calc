import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Eco Game WT")
st.title("🎬 Movies datasetttt")
st.write(
    """
    This app does things
    """
)

import streamlit as st
import pandas as pd
# Define skill names
skill_names = ["mining","logging","carpentry","pottery","masonry"]

# Initialize dataframe
df = pd.DataFrame(
    [
       {"Name": "Willingo", "Unique Skills":1},
   ]
)
for col in skill_names:
    df[col]=False

# Make rows addable and skills editable
edited_df = st.data_editor(df, num_rows="dynamic")

# Recalculate "Unique Skills"
edited_df["Unique Skills"] = edited_df.select_dtypes(include=bool).sum(axis=1)

# Display edited and recalculated dataframe
st.dataframe(edited_df)
print()
