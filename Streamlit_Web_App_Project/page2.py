import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

sns.set_theme(style="darkgrid", palette="deep", font="monospace")

@st.cache_data
def load_data():
    df = pd.read_csv("donor.csv")
    return df

df = load_data()

def app():
    st.title("Visualization with Seaborn")
    st.write("Please select a page on the left sidebar")
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage",
            "Count Plot",
            "Violin & Strip Plot",
            "Bar Plot",
            "Line Plot",
            "Sub Plots",
            "Figure & Axes",
            "WordCloud",
        ],
    )

    if page == "Homepage":
        st.balloons()
        st.write(df.head(100))
        st.caption("This table shows only first 100 rows due to large file size.")
    elif page == "Count Plot":
        st.header("Count Plot")
        count_plot()
    elif page == "Violin & Strip Plot":
        st.header("Violin & Strip Plot")
        violin_strip()
    elif page == "Bar Plot":
        st.header("Bar Plot")
        bar_plot()
    elif page == "Line Plot":
        st.header("Line Plot")
        line_plot()
    elif page == "Sub Plots":
        st.header("Sub Plots")
        subplots()
    elif page == "Figure & Axes":
        st.header("Figure & Axes")
        figure_axes()
    elif page == "WordCloud":
        st.header("WordCloud")
        worldcloud()


def count_plot():
    fig = plt.figure(figsize=(8, 6))
    plt.title("Prefix Countplot")
    plt.xticks(rotation=60, fontsize=12)
    sns.countplot(x="teacher_prefix", hue="project_is_approved", data=df)
    st.pyplot(fig)


def violin_strip():
    plot = st.selectbox("Select a Plot", ["Violin Plot", "Strip Plot"])

    ca = df[df["school_state"] == "CA"]
    fig = plt.figure(figsize=(12, 6))
    if plot == "Violin Plot":
        sns.violinplot(
            x="teacher_prefix",
            y="teacher_number_of_previously_posted_projects",
            data=ca,
        )
    elif plot == "Strip Plot":
        hue_order = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        sns.stripplot(
            x="teacher_prefix",
            y="teacher_number_of_previously_posted_projects",
            data=ca,
            hue="day",
            dodge=True,
            palette="Set2",
            hue_order=hue_order,
        )
    st.pyplot(fig)


def bar_plot():
    dff = (
        df.groupby("school_state")["teacher_number_of_previously_posted_projects"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(15)
    )
    fig = plt.figure(figsize=(12, 6))

    orientation = st.selectbox("Select a plot", ["Vertical", "Horizontal"])
    if orientation == "Vertical":
        sns.barplot(
            x="school_state", y="teacher_number_of_previously_posted_projects", data=dff
        )
    elif orientation == "Horizontal":
        sns.barplot(
            y="school_state",
            x="teacher_number_of_previously_posted_projects",
            data=dff,
        )

    st.pyplot(fig)


def line_plot():
    data = (
        df.groupby("project_submitted_date")[
            "teacher_number_of_previously_posted_projects"
        ]
        .sum()
        .reset_index()
    )
    data["project_submitted_date"] = pd.to_datetime(data["project_submitted_date"])
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(
        x="project_submitted_date",
        y="teacher_number_of_previously_posted_projects",
        data=data,
        color="r",
    )
    st.pyplot(fig)


def subplots():
    dff = (
        df.groupby("school_state")["teacher_number_of_previously_posted_projects"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(15)
    )
    fig = plt.figure(figsize=(15, 8))
    plt.subplot(1, 2, 1)
    sns.barplot(
        x="school_state", y="teacher_number_of_previously_posted_projects", data=dff
    )
    plt.subplot(1, 2, 2)
    sns.countplot(x="teacher_prefix", hue="project_is_approved", data=df)
    st.pyplot(fig)


def figure_axes():
    dff = (
        df.groupby("school_state")["teacher_number_of_previously_posted_projects"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(15)
    )
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    sns.barplot(
        x="school_state",
        y="teacher_number_of_previously_posted_projects",
        data=dff,
        ax=ax[0],
    )
    sns.countplot(x="teacher_prefix", hue="project_is_approved", data=df, ax=ax[1])
    st.pyplot(fig)


def worldcloud():
    corpus = " ".join(df["project_subject_categories"].astype(str))
    wordcloud = WordCloud(
        stopwords=STOPWORDS, width=2400, background_color="white", height=2000
    ).generate(corpus)

    fig = plt.figure(figsize=(12, 15))
    plt.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig)