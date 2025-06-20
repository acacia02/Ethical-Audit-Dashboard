import pandas as pd
import numpy as np

# upload the demographics data
# df = pd.read_sas("DEMO_J.xpt")

# print(df.info())
# print(df.head())
# getting the initial and basic info

# print(df.columns)
# see all column names


# print(df.isnull().sum())
# checking for missing values


# Loading the demographic AND diabetes datasets
df_demographics = pd.read_sas("DEMO_J.xpt")
df_diabetes = pd.read_sas("DIQ_J.xpt")

# merge them using SEQN (which is participant ID)
df = pd.merge(df_demographics, df_diabetes, on="SEQN", how="left")
df = df.replace(".", np.nan)


# check/show the resutls
# print(merged_df.info())
# print(df_merged.head())

# finding demographic participants that HAVE NOT answered wether they have diabetes
demographics_valid = df[df["DIQ010"].notna()]


# count of the row with ACTUAL diabetes answers
# print(merged_df["DIQ010"].notna().sum())

# checking the shape of (the layout) of the demographics and diabetes data and then seeing the overlap between the two (I can probably get rid of this)
# print(df_demographics.shape)
# print(df_diabetes.shape)
# print(merged_df.shape)
# print(merged_df["SEQN"].nunique())

# print(df_diabetes.head())

# renaming variables

# print(merged_df.columns.tolist())


# IT WAS RIGHT HERE THAT I DID THE DROP COLUMNS


# slicing out the household variables 
hh_cols = [
    "DMDHHSIZ", "DMDFMSIZ", "DMDHHSZA", "DMDHHSZB", "DMDHHSZE", 
    "DMDHRGND", "DMDHRAGZ", "DMDHREDZ", "DMDHRMAZ", "DMDHSEDZ"
    ]

household_df = df[["SEQN"] + [col for col in hh_cols if col in df.columns]]
df = df.drop(columns=[col for col in hh_cols if col in df.columns])

# to merge the household variables back in later use:
# merged_df = merged_df[["SEQN"] + [col for col in hh_cols if col in merged_df.columns]]

# saving sliced data so that I can use it again
household_df.to_csv("household_variables_backup.csv", index=True)
# to bring it back use:
# household_df = pd.read_csv("household_variables_backup.csv")

df.to_csv("df_backup.csv", index=False)
# im stopping at 3:15pm because I gotta get ready to see bethany and then go to work.... started cleaning some data by getting rid irrelevant columns; saved to CSV?

drop_columns = [
    # asking about diabetes medication
    "DIQ050", "DID060", "DIQ060U", "DIQ070", 
    # asking about doctor and management and specialist care
    "DIQ230", "DIQ240", "DID250", "DID260", "DIQ260U", "DIQ275", "DIQ280", 
    "DIQ291", "DIQ300S", "DIQ300D", "DID310D", "DID310S", "DID320", "DID330", 
    # asking about doctor checking feet and eyes
    "DID341", "DID350", "DIQ350U", "DIQ360", "DIQ080",
    # moving onto the demographics columns; dropping mechanics data
    "SDDSRVYR", "RIDSTATR", "RIDEXMON", 
    # service in american armed forces
    "DMQMILIZ", "DMQADFC", 
    # interview and interviewee questions
    "SIALANG", "SIAPROXY", "SIAINTRP", "FIALANG", "FIAINTRP", 
    "FIAPROXY", "MIALANG", "MIAPROXY", "MIAINTRP", "AIALANGA", 
    # variance in stratums
    "SDMVPSU", "SDMVSTRA",
    # dropping asian subpopulation for now
    "RIDRETH3",
    # dropping suvey weights (I can always add this back in)
    "WTMEC2YR", "WTINT2YR"
]

# checking which columns are missing in the drop_columns in the merged_df
# missing_columns = [col for col in drop_columns if col not in merged_df.columns]
# print(missing_columns)


# dropping list of irrelevant columns
df = df.drop(columns=drop_columns)
# print(merged_df.columns)



df.rename(columns={
# Demographics dataset being renamed
    "SEQN": "Participant ID",
    "RIAGENDR": "Gender",
    "RIDAGEYR": "Age in Years at Screening",
    "RIDAGEMN": "Age in Months at Screening (0-24 months)",
    "RIDRETH1": "Race/Hispanic Origin",
    "RIDEXAGM": "Age in Months at Exam (0-19 years)",
    "DMDBORN4": "Country of Birth",
    "DMDCITZN": "Citizenship Status",
    "DMDYRSUS": "Length of Time in US",
    "DMDEDUC3": "Education Level - Ages 6-19",
    "DMDEDUC2": "Education Level - Adults 20+",
    "DMDMARTL": "Marital Status",
    "RIDEXPRG": "Pregnancy Status at Exam",
    "INDHHIN2": "Annual Household Income",
    "INDFMIN2": "Annual Family Income",
    "INDFMPIR": "Ratio of Family Income to Poverty",
#   Diabetes dataset being renamed
    "DIQ010": "Doctor said you have Diabetes",
    "DID040": "Age when first told you had Diabetes",
    "DIQ160": "Ever told you have Prediabtes",
    "DIQ170": "Ever told you have Health Risk for Diabetes",
    "DIQ172": "Feel they could be at risk for Diabetes",
    "DIQ175A": "Family History",
    "DIQ175B": "Overweight",
    "DIQ175C": "Age",
    "DIQ175D": "Poor Diet",
    "DIQ175E": "Race",
    "DIQ175F": "Had a Baby Weigh over 9lbs at birth",
    "DIQ175G": "Lack of Physical Activity",
    "DIQ175H": "High Blood Pressure",
    "DIQ175I": "High Blood Sugar",
    "DIQ175J": "High Cholestrol",
    "DIQ175K": "Hypoglycemic",
    "DIQ175L": "Extreme Hunger",
    "DIQ175M": "Tingling/Numbness in Hands or Feet",
    "DIQ175N": "Blurred Vision",
    "DIQ175O": "Increased Fatigue",
    "DIQ175P": "Anyone could be at Risk",
    "DIQ175Q": "Doctor Warning",
    "DIQ175R": "Other, Specify",
    "DIQ175S": "Gestational Diabetes",
    "DIQ175T": "Frequent Urination",
    "DIQ175U": "Thirst",
    "DIQ175V": "Craving for Sweets/Eating a lot of Sugar",
    "DIQ175W": "Medication",
    "DIQ175X": "Polycystic Ovarian Syndrome",
    "DIQ180": "Had Blood Tested in the past Three Years"
}, inplace=True)

# print(merged_df.rename)

# inspecting the merged and relevant data
# print(merged_df.head())
# print(merged_df.dtypes)
# print(merged_df.isnull().sum().sort_values(ascending=False))


# coded_columns = [
    # "Doctor said you have Diabetes",
    # "Ever told you have Prediabtes",
    # "Ever told you have Health Risk for Diabetes",
    # "Feel they could be at risk for Diabetes",
    # "Had Blood Tested in the past Three Years"

# ]

# code_map = {
    # 1: "Yes",
    # 2: "No",
    # 3: "Borderline",
    # 7: "Refused",
    # 9: "Don't Know",
    # ".": "Missing"
# }

# converting to integers first (some may be float)
# for col in coded_columns:
#     if col in merged_df.columns:
#         # making errors apear as N/A and making the type Int64 which can handle N/As
#         merged_df[col] = pd.to_numeric(merged_df[col], errors="coerce").astype("Int64") 
#         # maping the coded_columns to the code map and reassigning values
#         merged_df[col] = merged_df[col].map(code_map)
#         # replacing certain values? check this
#         merged_df[col] = merged_df[col].replace(["Refused", "Don't Know"], "Unknown")



# I was wanting to see the NHANES like responses
# for col in merged_df.columns:
#     print(f"{col}:\n", merged_df[col].value_counts(dropna=False), "\n")

# review this function 
# def audit_column_distribution(df):
#     for col in merged_df:
#         print(f"=== {col} ===")
#         print(df[col].value_counts(dropna=False))
#         print("\n")



# coverting all the DIQ data into yes, no and missing (n/a) values
diq_coded_columns = [
    "Doctor said you have Diabetes",
    "Ever told you have Prediabtes",
    "Ever told you have Health Risk for Diabetes",
    "Feel they could be at risk for Diabetes",
    "Family History",
    "Overweight",
    "Age",
    "Poor Diet",
    "Race",
    "Had a Baby Weigh over 9lbs at birth",
    "Lack of Physical Activity",
    "High Blood Pressure",
    "High Blood Sugar",
    "High Cholestrol",
    "Hypoglycemic",
    "Extreme Hunger",
    "Tingling/Numbness in Hands or Feet",
    "Blurred Vision",
    "Increased Fatigue",
    "Anyone could be at Risk",
    "Doctor Warning",
    "Other, Specify",
    "Gestational Diabetes",
    "Frequent Urination",
    "Thirst",
    "Craving for Sweets/Eating a lot of Sugar",
    "Medication",
    "Polycystic Ovarian Syndrome",
    "Had Blood Tested in the past Three Years"
    ]

# using the code map from the DIQ datset to rename outputs
value_map = {
    1: "Yes/Information Given",
    10: "Yes/Information Given",
    11: "Yes/Information Given",
    12: "Yes/Information Given",
    13: "Yes/Information Given",
    14: "Yes/Information Given",
    15: "Yes/Information Given",
    16: "Yes/Information Given",
    17: "Yes/Information Given",
    18: "Yes/Information Given",
    19: "Yes/Information Given",
    20: "Yes/Information Given",
    21: "Yes/Information Given",
    22: "Yes/Information Given",
    23: "Yes/Information Given",
    24: "Yes/Information Given",
    25: "Yes/Information Given",
    26: "Yes/Information Given",
    27: "Yes/Information Given",
    28: "Yes/Information Given",
    29: "Yes/Information Given",
    30: "Yes/Information Given",
    31: "Yes/Information Given",
    32: "Yes/Information Given",
    33: "Yes/Information Given",
    2: "No",
    7: "Refused",
    9: "Don't Know",
    77: "Refused",
    99: "Don't Know"
}

# mapping the diq data columns so they are strings not integers
for col in diq_coded_columns:
    df[col] = df[col].map(value_map).fillna("missing")


# code maping for "age when you where first told you have diabetes"
def map_age_of_diabetes_diagnosis(val):
    if 1 <= val <= 79:
        return val
    elif val == 80:
        return "80+"
    elif val == 666:
        return "<1 year"
    elif val == 777:
        return "refused"
    elif val == 999:
        return "don't know"
    elif pd.isna(val):
        return "missing"
    else:
        return "out of range"

# calling diabetes age of diagnosis function
df["Age when first told you had Diabetes"] = df["Age when first told you had Diabetes"].apply(map_age_of_diabetes_diagnosis)


demo_coded_columns = [
    "Participant ID",
    "Gender",
    "Age in Years at Screening",
    "Age in Months at Screening (0-24 months)",
    "Race/Hispanic Origin",
    "Age in Months at Exam (0-19 years)",
    "Country of Birth",
    "Citizenship Status",
    "Length of Time in US",
    "Education Level - Ages 6-19",
    "Education Level - Adults 20+",
    "Marital Status",
    "Pregnancy Status at Exam",
    # "Annual Household Income",
    # "Annual Family Income",
    "Ratio of Family Income to Poverty"
]

# changing the coded values in the demographic data to reflect their actual meaning
df["Citizenship Status"] = df["Citizenship Status"].map({
    1: "Citizen",
    2: "Not a citizen",
    3: "Refused",
    4: "Don't Know"
}).fillna("missing")

df["Gender"] = df["Gender"].map({
    1: "Male",
    2: "Female"
}).fillna("missing")

def map_age_during_screening(val):
    if 1 <= val <= 79:
        return val
    elif val == 80:
        return "80+"
    elif pd.isna(val):
        return "missing"
    else: 
        return "out of range"
    

def age_in_months_at_screening(val):
    if 0 <= val <= 24:
        return val
    elif pd.isna(val):
        return "missing"
    else:
        return "out of range"
    
df["Race/Hispanic Origin"] = df["Race/Hispanic Origin"].map({
    1: "Mexican American",
    2: "Other Hispanic",
    3: "Non-Hispanic White",
    4: "Non-Hispanic Black",
    5: "Other Race (including multi-racial)"
}).fillna("missing")

def age_in_months_at_exam(val):
    if 0 <= val <= 239:
        return val
    elif pd.isna(val):
        return "missing"
    else:
        return "out of range"
# am i fucking stupid this function (all of them? are not pulling data from where i want)

def country_of_birth(val):
    if val == 1:
        return "born in the US"
    elif val == 2:
        return "others"
    elif val == 77:
        return "refused"
    elif val == 99:
        return "don't know"
    elif pd.isna(val):
        return "missing"
    else:
        return "out of range"
    

def citizenship_status(val):
    if val == 1:
        return "citizen of the US"
    elif val == 2: 
        return "not a citizen of the US"
    elif val == 7:
        return "refused"
    elif val == 9:
        return "don't know"
    elif pd.isna(val):
        return "missing"
    else:
        return "is out of range"
    
demo_column_maps = {
    "Length of Time in US": {
        1: "Less than one year",
        2: "1 year or more (but less than 5)",
        3: "5 years or more (but less than 10)",
        4: "10 years or more (but less than 15 years)",
        5: "15 years or more (but less than 20 years)",
        6: "20 years or more (but less than 30 years)",
        7: "30 years or more (but less than 40 years)",
        8: "40 years or more (but less than 50 years)",
        9: "50 years or more",
        77: "refused",
        99: "don't know"
    },
    "Education Level - Ages 6-19": {
        0: "never attended/kindergarten only",
        1: "1st grade",
        2: "2nd grade",
        3: "3rd grade",
        4: "4th grade",
        5: "5th grade",
        6: "6th grade",
        7: "7th grade",
        8: "8th grade",
        9: "9th grade",
        10: "10th grade",
        11: "11th grade",
        12: "12 grade, no diploma",
        13: "high school graduate",
        14: "GED or equivalent",
        15: "more than high school",
        55: "less than 5th grade",
        66: "less than 9th grade",
        77: "refused",
        99: "don't know",
        # don't for get to add .isna("missing")
    },
    "Education Level - 20+": {
        1: "less than 9th grade",
        2: "9th-11th grade (includes grade 12 with no diploma)",
        3: "high school graduate/GED or equivalent",
        4: "some college or AA degree",
        5: "college graduate or above",
        7: "refused",
        9: "don't know"
    },
    "Marital Status": {
        1: "married",
        2: "widowed",
        3: "divorced",
        4: "seperated",
        5: "never married",
        6: "living with partner",
        77: "refused",
        99: "don't know",
    },
    "Pregnancy Status at Exam": {
        1: "positive lab pregnancy or self-reported pregnancy",
        2: "not pregnant",
        3: "cannot determine if participant is pregnant",
    },
    "Annual Household Income": {
        1: "$0 to $4999",
        2: "$5000 to $9999",
        3: "$10000 to $14999",
        4: "$15000 to $19999",
        5: "$20000 to $24999",
        6: "$25000 to $34999",
        7: "$35000 to $44999",
        8: "$45000 to $54999",
        9: "$55000 to $64999",
        10: "$65000 to $74999",
        12: "$20000 and over",
        13: "under $20000",
        14: "$75000 to 99999",
        15: "$100000 and over",
        77: "refused",
        99: "don't know"
    },
    "Annual Family Income": {
        1: "$0 to $4999",
        2: "$5000 to $9999",
        3: "$10000 to $14999",
        4: "$15000 to $19999",
        5: "$20000 to $24999",
        6: "$25000 to $34999",
        7: "$35000 to $44999",
        8: "$45000 to $54999",
        9: "$55000 to $64999",
        10: "$65000 to $74999",
        12: "$20000 and over",
        13: "under $20000",
        14: "$75000 to 99999",
        15: "$100000 and over",
        77: "refused",
        99: "don't know"
    }
}
       

def income_to_poverty_ratio(val):
    if 0 <= val <= 4.98:
        return val
    elif val == 5:
        return "value greater than or equal to 5.00"
    elif pd.isna(val):
        return "missing"
    else:
        return "out of range"
#  end of the diq coded columns being mapped from integers to strings


# Apply custom functions
df["Age in Years at Screening"] = df["Age in Years at Screening"].apply(map_age_during_screening)
df["Age in Months at Screening (0-24 months)"] = df["Age in Months at Screening (0-24 months)"].apply(age_in_months_at_screening)
df["Age in Months at Exam (0-19 years)"] = df["Age in Months at Exam (0-19 years)"].apply(age_in_months_at_exam)
df["Country of Birth"] = df["Country of Birth"].apply(country_of_birth)
df["Citizenship Status"] = df["Citizenship Status"].apply(citizenship_status)
df["Ratio of Family Income to Poverty"] = df["Ratio of Family Income to Poverty"].apply(income_to_poverty_ratio)

# this is to make sure these columns stay as integers
df["Annual Household Income"] = pd.to_numeric(df["Annual Household Income"], errors="coerce")
df["Annual Family Income"] = pd.to_numeric(df["Annual Family Income"], errors="coerce")


# Apply mappings for all demo-coded categorical columns
for col, mapping in demo_column_maps.items():
    if col in df.columns and "Income" not in col:
        df[col] = df[col].map(mapping).fillna("missing")

print("All demo-coded columns processed!")
# print(merged_df[demo_coded_columns].head())

# getting a feel for the data for like the 10th time
# merged_df.shape
# merged_df.head()
# merged_df.info()
# merged_df.describe(include="all")

# ching for missing values
df.isnull().sum().sort_values(ascending=False)
missing_summary = df.isnull().sum().sort_values(ascending=False)
print(missing_summary[missing_summary > 0])
print((df == "missing").sum().sort_values(ascending=False))
df = df.replace("missing", np.nan)


# print(df_demographics.columns[df_demographics.columns.str.contains("Race", case=False)])
# df_demographics[['SEQN', 'RIDRETH1']].head()  # RIDRETH1 is often used for race in NHANES

# dropping duplicate columns
df = df.loc[:, ~df.columns.duplicated()]

# convert "missing" back to real NaN (why did I even do this to begin with)
df = df.replace("missing", np.nan).infer_objects()

# making column names normal
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# convert numeric columns??? DOUBLE CHECK THIS
# merged_df['age'] = pd.to_numeric(merged_df["age"], errors="coerce")

df['gender'] = df['gender'].replace({
    'M': 'Male', 'F': 'Female', 
    'male': 'Male', 'female': 'Female',
    'Missing': np.nan
})


# converting strings to numerical values
df["annual_family_income"] = pd.to_numeric(df["annual_family_income"], errors="coerce")
df["annual_household_income"] = pd.to_numeric(df["annual_household_income"], errors="coerce")
df["ratio_of_family_income_to_poverty"] = pd.to_numeric(df["ratio_of_family_income_to_poverty"], errors="coerce")

# I NEED TO STANDARDIZE CATEGORICAL COLUMNS RIPPPP

# standardizing gender
df['gender'] = df['gender'].replace({
    'M': 'Male', 'F': 'Female', 'male': 'Male', 'female': 'Female',
    'unknown': np.nan
})

# standardizing race WAIT SHOULD I EVEN STANDARDIZE THEM WILL THAT BIAS INTERPRETATION


# I NEED TO FIGURE OUT HOW TO HANDLE MISSING VALUES


# merged_df.to_csv('cleaned_data_final.csv', index=False)
missing_percent = df.isna().mean().sort_values(ascending=False)
print(missing_percent)


# df_demographics['race_hispanic_origin'] = df_demographics['RIDRETH1'].map(race_map)

# df = pd.merge(df_demographics[['SEQN', 'race_hispanic_origin']], df, on='SEQN', how='right')


# checking if columns that were over 60% empty were conditionally skipped
def conditional_missing_audit(df, columns, condition_col):
    for col in columns:
        try:
            result = df.groupby(condition_col).apply(lambda g: g[col].isna().mean())
            print(f"\n--- {col} ---")
            print(result.sort_index())
        except KeyError:
            print(f"Column not found: {col}")


columns_to_check = [
    "polycystic_ovarian_syndrome", "medication", "craving_for_sweets/eating_a_lot_of_sugar",
    "other,_specify", "hypoglycemic", "gestational_diabetes", "had_a_baby_weigh_over_9lbs_at_birth",
    "extreme_hunger", "high_blood_sugar", "blurred_vision", "thirst", "frequent_urination",
    "anyone_could_be_at_risk", "tingling/numbness_in_hands_or_feet", "high_cholestrol",
    "increased_fatigue", "doctor_warning", "race", "age", "high_blood_pressure",
    "lack_of_physical_activity", "poor_diet", "overweight", "age_when_first_told_you_had_diabetes",
    "pregnancy_status_at_exam", "family_history"
]

# Run the audit
conditional_missing_audit(df, columns_to_check, "doctor_said_you_have_diabetes")

# Example for DIQ175A (Family History)
print(df_diabetes["DIQ175A"].value_counts(dropna=False))
# Compare before/after mapping
print("Original DIQ175X codes:")
print(df_diabetes["DIQ175X"].value_counts(dropna=False))

print("\nAfter renaming/mapping:")
print(df["polycystic_ovarian_syndrome"].value_counts(dropna=False))


# === ETHICAL AUDIT COMMENT: DIABETES FOLLOW-UP QUESTIONS ===
#
# Goal: To audit whether follow-up diabetes questions (like symptoms, risk factors, etc.)
#       were conditionally skipped based on the participant's response to
#       "Doctor said you have Diabetes" (DIQ010).
#
# Approach:
# - Used group-wise missingness checks (via groupby + isna().mean()) to determine if
#   fields were skipped by design.
# - Found that even for participants who answered "Yes/Information Given" to DIQ010,
#   many follow-up fields (e.g., polycystic_ovarian_syndrome) still showed 100% missing.
#
# Diagnosis:
# - Verified that some columns (e.g., DIQ175X) had almost no valid responses even in raw data.
# - .map() and .replace() operations likely erased valid but unmapped values.
# - NHANES skip logic may limit questions to subgroups (e.g., only females, only adults).
#
# Status:
# - Audit logic worked correctly.
# - Missingness appears to be driven by a mix of skip patterns AND data loss during transformation.
# - Will pause further deep dive for now and revisit with fresh eyes.
