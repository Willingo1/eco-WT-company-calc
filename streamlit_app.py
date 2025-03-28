import streamlit as st
from streamlit import session_state as ss
import pandas as pd
import streamlit as st
import pandas as pd
import string
st.set_page_config(page_title="WT Eco Company Tax Calc", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)


st.title("Eco Game WHite Tiger Company Tax Calculator")
st.info("Made by Willingo#3404. DM on Discord for feedback,advice, or bugs")
# Inspiration from https://discuss.streamlit.io/t/trigger-function-from-an-st-data-editor/57610/4
# Not sure if there is a more pythonic way to accomplish this, but it works so whatever

#st.subheader("Override Manual Tax (Likely not needed)")
#compound_tax = st.number_input("Compounding Tax Per Skill 20% is accurate as of March 21st 2025. Likely won't change",value=0.20)
compound_tax = 0.20


# Handle Skill names
skill_names = ["Smelting","Blacksmith","Advanced Smelting",
                "Tailoring",
                  "Baking","Cutting Edge\n Cooking", "Advanced Baking", "Cooking", "Campfire Cooking", "Advanced Cooking",
                  "Hunting", "Butcher",
                  "Oil Drilling","Painting",
                  "Carpentry","Paper Milling", "Shipwright", "Logging (OP)", "Composites",
                  "Pottery","Glassworking","Mining","Masonry","Advanced Masonry",
                  "Industry","Basic Engineering", "Electronics", "Mechanics", 
                  "Gathering","Fertilziers","Farming","Milling"]


# Initialize session state
if 'df' not in st.session_state:
    # Define initial data
    data = {
        'Names': ['A', 'B'],
        'Unique Skills': [0, 0],
    }
    for skill in skill_names:
        data[skill]= [False]*len(data['Names'])
    st.session_state.df = pd.DataFrame(data)

st.subheader("Add sorting skill capabilities (Purely for convenience)")
## Give sorting skill capabilities
# Store sorting option in session state
if "sort_option" not in st.session_state:
    st.session_state.sort_option = "Group"

# Present option
option = st.selectbox(
    "How should skill names be ordered?",
    ("Group", "Alphabetical"),
    index=0
)

# Apply sorting only when the option changes
#probably could simplify this with data_editor parameter column_order but w/e
if option != st.session_state.sort_option:
    st.session_state.sort_option = option  # Update stored option

    skill_names_sorted = sorted(skill_names)
    remaining_cols = [col for col in st.session_state.df.columns if col not in skill_names]
    if option == "Alphabetical":
        st.session_state.df = st.session_state.df[remaining_cols + skill_names_sorted]

    elif option == "Group":
        st.session_state.df = st.session_state.df[remaining_cols + skill_names]
##
# Callback function to update values
def update_dataframe():
    """Handles row edits, additions, deletions, and assigns the next letter."""
    new_data = st.session_state.skill_table

    # **Handle edited rows**
    if "edited_rows" in new_data:
        for idx, changes in new_data["edited_rows"].items():
            for col, new_value in changes.items():
                st.session_state.df.at[idx, col] = new_value

    # **Handle newly added rows**
    if "added_rows" in new_data and new_data["added_rows"]:
        new_rows = pd.DataFrame(new_data["added_rows"])

        # Add False to all skills for new dude
        # Fill missing columns in case new rows are incomplete
        for col in st.session_state.df.columns:
            if col not in new_rows:
                new_rows[col] = False if col in skill_names else ""

        ## Cleverly add the next letter in the alphabet that exists as a blank name

        # Find existing letters in "Names" that are in the alphabet
        ascii_letters = list(string.ascii_uppercase)
        existing_letters = set(st.session_state.df["Names"]) & set(ascii_letters)

        # Get the next available letter
        if existing_letters:
            highest_letter = max(existing_letters, key=ord)
            next_letter = chr(ord(highest_letter) + 1) if highest_letter < "Z" else None
        else:
            next_letter = "A"  # Default to "A" if no alphabetic names exist

        # Assign this letter to all new rows
        new_rows["Names"] = next_letter

        # Append new rows to session state
        st.session_state.df = pd.concat([st.session_state.df, new_rows], ignore_index=True)

    # **Handle deleted rows** (Names are not reassigned)
    if "deleted_rows" in new_data and new_data["deleted_rows"]:
        st.session_state.df.drop(new_data["deleted_rows"], inplace=True)
        st.session_state.df.reset_index(drop=True, inplace=True)  # Reset index to avoid gaps

    # **Recalculate "Unique Skills"**
    st.session_state.df["Unique Skills"] = st.session_state.df[skill_names].astype(int).sum(axis=1)

    
def tax_calc(val):
    return {round(100*(1-(1-compound_tax)**val),0)}

# Streamlit UI
def main():
    #st.session_state.df[skill_names]= st.session_state.df[skill_names].apply(sorted)
    st.subheader("Add Employees & Select Skills")
    st.info("You can add new players by hovering below the last name and clicking '+' or delete a player by selecting the checkmark to the left of a name and then in top right of dataframe, press the trashcan",icon="ℹ️")
    st.info("Make sure you add all employees. Having 2 or having more than 2 matters for the 2 star exemption",icon="ℹ️")
    st.info("Note: It doesn't really matter which skills are chosen, just the number of unique skills and whether players choose the same ones. There is no bias toward any certain skills",icon="ℹ️")
    st.data_editor(st.session_state.df, num_rows="dynamic",hide_index=True, on_change=update_dataframe, key='skill_table')
    #st.write(st.session_state)

    st.subheader("Tax Conclusion")
    # Find the highest "Unique Skills" value
    max_unique_skills = st.session_state.df["Unique Skills"].max() if not st.session_state.df.empty else 0
    # Find the number of unique skills across all rows
    total_unique_skills = st.session_state.df[skill_names].any(axis=0).sum() if not st.session_state.df.empty else 0
    num_employees = st.session_state.df["Names"].nunique()
    if total_unique_skills ==2 and num_employees == 2:
        st.info(f"Only 2 unique skills in entire company, so due to 2-star exemption, you have no extra tax")
        st.warning(f"""Be careful. You should 'meet up' in skills on the next level, since this is an exemption\nFor example, if player B chooses the skill of player A
        but player A chooses another new skill, you will have a {tax_calc(1)}% tax. And if you both choose two new skills, there will be 4 unique skills and you will have a {tax_calc(2)})% tax) """,icon="⚠️")
        st.success("You will have 0%, NO tax applied",icon="💡")

    # could refactor this later if I care
    elif total_unique_skills==2 and num_employees > 2:
        st.warning(f"While you only have 2 unique skills in the entire company, you do not have the 2-star exemption, because you have {num_employees} employees, and it only applies to 2-player companies",icon="⚠️")
        st.info(f"Your most skilled player has:{max_unique_skills} total skills",icon="ℹ️")
        st.info(f"Your total number of unique skills is: {total_unique_skills}",icon="ℹ️")
        st.success(f"You will have a {round(100*(1-(1-compound_tax)**(total_unique_skills-max_unique_skills)),0)}% tax applied before other taxes",icon="💡")
    else:
        st.info(f"Your most skilled player has:{max_unique_skills} total skills",icon="ℹ️")
        st.info(f"Your total number of unique skills is: {total_unique_skills}",icon="ℹ️")
        st.success(f"You will have a {round(100*(1-(1-compound_tax)**(total_unique_skills-max_unique_skills)),0)}% tax applied before other taxes",icon="💡")
    #st.write(type(st.session_state.df))
if __name__ == '__main__':
    main()
