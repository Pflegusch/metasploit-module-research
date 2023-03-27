import pandas as pd
import matplotlib.pyplot as plt

def generate_rankings_plot(module):
    data = pd.read_csv("../csv/" + module + ".csv")
    df = pd.DataFrame(data, columns=["Rank"]).groupby(["Rank"])["Rank"].count()

    # Plot the data using bar() method
    ax = df.plot.bar(color="#00bc79") 
    ax.bar_label(ax.containers[0])
    plt.title("Overall ranking of all " + module + " modules")
    plt.xlabel("Ranking")
    plt.ylabel("Number of modules")

    # Rotate x labels
    plt.xticks(rotation=45)
    
    # # Save the plot
    plt.tight_layout()
    plt.savefig(module + "/overall_ranking.png")
    plt.figure()

if __name__ == "__main__":
    modules = ["auxiliary", "encoder", "evasion", "exploit", "nop", "payload", "post"]
    for module in modules:
        generate_rankings_plot(module)
