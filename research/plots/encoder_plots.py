import pandas as pd
import matplotlib.pyplot as plt
import math

def generate_overall_plot():
    data = pd.read_csv("../data/encoder/overall_rankings")
    df = pd.DataFrame(data)
    
    x = list(df.iloc[:, 0])
    y = list(df.iloc[:, 1])
    
    # Plot the data using bar() method
    plt.bar(x, y, color="#00bc79")
    plt.title("Overall ranking of all encoder modules")
    plt.xlabel("Rank")
    plt.ylabel("Number of modules")

    # Rotate x labels
    plt.xticks(rotation=45)

    for index,data in enumerate(y):
        plt.text(x=index-0.4, y=data+0.15, s=f"{data}", fontdict=dict(fontsize=10))
    
    # Save the plot
    plt.tight_layout()
    plt.savefig("encoder/overall_ranking.png")

def generate_platform_plot():
    data = pd.read_csv("../data/encoder/overall_platforms")
    df = pd.DataFrame(data)
    
    x = list(df.iloc[:, 0])
    y = list(df.iloc[:, 1])
    
    # Plot the data using bar() method
    plt.bar(x, y, color="#00bc79")
    plt.title("Overall number of encoder modules for different platforms")
    plt.xlabel("Platform")
    plt.ylabel("Number of modules")

    convert_to_int = range(math.floor(min(y)), math.ceil(max(y)) + 1, 2)
    plt.yticks(convert_to_int)

    # Rotate x labels
    plt.xticks(rotation=45)

    for index,data in enumerate(y):
        plt.text(x=index-0.4, y=data+0.1, s=f"{data}", fontdict=dict(fontsize=10))
    
    # Save the plot
    plt.tight_layout()
    plt.savefig("encoder/overall_platforms.png")

if __name__ == "__main__":
    generate_overall_plot()
    plt.clf()
    generate_platform_plot()