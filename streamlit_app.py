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

skill_names = ["mining","logging","carpentry","pottery","masonry"]
df = pd.DataFrame(
    [
       {"Name": "Willingo", "Unique Skills":1},
   ]
)
for col in skill_names:
    df[col]=False
df["Unique Skills"] = df.select_dtypes(include=bool).sum(axis=1)

edited_df = st.data_editor(df, num_rows="dynamic")
print()
