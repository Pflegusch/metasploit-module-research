import pandas as pd
import matplotlib.pyplot as plt

def generate_overall_plot():
    data = pd.read_csv("../data/post/overall_rankings")
    df = pd.DataFrame(data)
    
    x = list(df.iloc[:, 0])
    y = list(df.iloc[:, 1])
    
    # Plot the data using bar() method
    plt.bar(x, y, color="#00bc79")
    plt.title("Overall ranking of all post modules")
    plt.xlabel("Rank")
    plt.ylabel("Number of modules")

    # Rotate x labels
    plt.xticks(rotation=45)

    for index,data in enumerate(y):
        plt.text(x=index-0.4, y=data+0.05, s=f"{data}", fontdict=dict(fontsize=10))
    
    # Save the plot
    plt.tight_layout()
    plt.savefig("post/overall_ranking.png")

def generate_platform_plot():
    data = pd.read_csv("../data/post/overall_platforms")
    df = pd.DataFrame(data)
    
    x = list(df.iloc[:, 0])
    y = list(df.iloc[:, 1])
    
    # Plot the data using bar() method
    plt.bar(x, y, color="#00bc79")
    plt.title("Overall number of post modules for different platforms")
    plt.xlabel("Platform")
    plt.ylabel("Number of modules")

    # Rotate x labels
    plt.xticks(rotation=45)

    for index,data in enumerate(y):
        plt.text(x=index-0.4, y=data+0.075, s=f"{data}", fontdict=dict(fontsize=10))
    
    # Save the plot
    plt.tight_layout()
    plt.savefig("post/overall_platforms.png")

if __name__ == "__main__":
    generate_overall_plot()
    plt.clf()
    generate_platform_plot()