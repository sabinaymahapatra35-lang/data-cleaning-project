import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("🚢 Titanic Data Dashboard")

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

st.subheader("Dataset Preview")
st.write(df.head())

# ---------------- DASHBOARD ---------------- #

st.subheader("1. Survival Count")
fig1 = plt.figure()
sns.countplot(x='Survived', data=df)
st.pyplot(fig1)

st.subheader("2. Gender vs Survival")
fig2 = plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)
st.pyplot(fig2)

st.subheader("3. Class vs Survival")
fig3 = plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=df)
st.pyplot(fig3)

st.subheader("4. Age Distribution")
fig4 = plt.figure()
df['Age'].hist(bins=20)
st.pyplot(fig4)

st.subheader("📌 Insights")
st.write("""
- Most passengers did not survive
- Females had higher survival rate
- 1st class passengers had better survival chances
- Most passengers were aged 20–40
""")
