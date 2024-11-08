import pandas as pd
import sys
import os

# Add the scripts folder to the Python path
sys.path.append(os.path.abspath("scripts"))

# Import custom functions
from scripts.data_preprocessing import load_data, clean_data
from scripts.visualization import plot_content_type_over_years, plot_content_distribution, plot_director_wordcloud
from scripts.network_analysis import create_network, plot_network

# Define the file path for the data
data_filepath = 'data/netflix_titles_nov_2019.csv'

def main():
    # Step 1: Load the data
    print("Loading data...")
    df = load_data(data_filepath)
    if df is None:
        print("Error: Data file could not be loaded.")
        return

    # Step 2: Clean the data
    print("Cleaning data...")
    df_cleaned = clean_data(df)
    
    # Step 3: Perform Analysis and Visualization
    print("Generating visualizations...")
    
    # 1. Bar chart: Netflix content type distribution over years
    plot_content_type_over_years(df_cleaned)
    
    # 2. Pie chart: Content distribution by type
    plot_content_distribution(df_cleaned)
    
    # 3. Wordcloud: Directors
    plot_director_wordcloud(df_cleaned)
    
    # Step 4: Network Analysis of Actors/Directors
    print("Creating network analysis...")
    G = create_network(df_cleaned)
    plot_network(G)

if __name__ == "__main__":
    main()
