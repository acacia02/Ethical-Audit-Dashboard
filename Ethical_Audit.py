import pandas as pd

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
merged_df = pd.merge(df_demographics, df_diabetes, on="SEQN", how="inner")


# check/show the resutls
# print(merged_df.info())
# print(df_merged.head())

# finding demographic participants that HAVE NOT answered wether they have diabetes
demographics_valid = merged_df[merged_df["DIQ010"].notna()]


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

household_df = merged_df[["SEQN"] + [col for col in hh_cols if col in merged_df.columns]]
merged_df = merged_df.drop(columns=[col for col in hh_cols if col in merged_df.columns])

# to merge the household variables back in later use:
# merged_df = merged_df[["SEQN"] + [col for col in hh_cols if col in merged_df.columns]]

# saving sliced data so that I can use it again
household_df.to_csv("household_variables_backup.csv", index=True)
# to bring it back use:
# household_df = pd.read_csv("household_variables_backup.csv")

merged_df.to_csv("merged_df_backup.csv", index=False)
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
merged_df = merged_df.drop(columns=drop_columns)
print(merged_df.columns)



merged_df.rename(columns={
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
    "DIQ175X": "Polycycstic Ovarian Syndrome",
    "DIQ180": "Had Blood Tested in the past Three Years"
}, inplace=True)

# print(merged_df.rename)

# inspecting the merged and relevant data
print(merged_df.head())
print(merged_df.dtypes)
print(merged_df.isnull().sum().sort_values(ascending=False))


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
for col in merged_df.columns:
    print(f"{col}:\n", merged_df[col].value_counts(dropna=False), "\n")

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
    "Polycycstic Ovarian Syndrome",
    "Had Blood Tested in the past Three Years"
    ]

# using the code map from the DIQ datset to rename outputs
diq_code_map = dict.fromkeys([1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], "Yes/Information Given")
diq_code_map.update({2: "No", 7: "Refused", 9: "Don't Know", ".": "Missing Information", 77: "Refused", 99: "Don't Know"})


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
    else:
        return "other"


# DUFFY DO NOT EXIT THIS TAB JUST MINIMIZE IT PLEASE!!!!!!
# THANK YOU KING
# YOUR TAB IS STILL OPEN

