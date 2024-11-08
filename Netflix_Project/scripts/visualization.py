import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud

# Bar chart to show content type distribution over years
def plot_content_type_over_years(df):
    """
    Plots a stacked bar chart showing the distribution of content types (Movies, TV Shows) over the years.

    Parameters:
    - df: DataFrame, dataset containing columns 'release_year' and 'type'
    """
    content_counts = df.groupby(['release_year', 'type']).size().unstack()
    content_counts.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title('Distribution of Content Type Over Years')
    plt.xlabel('Release Year')
    plt.ylabel('Count')
    plt.show()

# Pie chart for distribution of content by type
def plot_content_distribution(df):
    """
    Plots a pie chart showing the distribution of Movies and TV Shows.

    Parameters:
    - df: DataFrame, dataset containing a 'type' column
    """
    fig = px.pie(df, names='type', title='Content Type Distribution')
    fig.show()

# Wordcloud for directors
def plot_director_wordcloud(df):
    """
    Generates a word cloud for directors' names.

    Parameters:
    - df: DataFrame, dataset containing a 'director' column
    """
    directors = ' '.join(df['director'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='black').generate(directors)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
