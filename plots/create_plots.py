import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def generate_rankings_plot(module):
    data = pd.read_csv("../csv/" + module + ".csv")
    df = pd.DataFrame(data, columns=["Rank"])

    # Sort according to metasploit ranking score
    rank_order = ["excellent", "great", "good", "normal", "average", "low", "manual"]

    df.sort_values(by="Rank", key=lambda column: column.map(lambda e: rank_order.index(e)), inplace=True)
    df = df.groupby(["Rank"])["Rank"].count()

    # Reindex to add missing ranks and fill NaN values with 0
    df = df.reindex(rank_order, fill_value=0)

    # Exclude bars with 0 value
    df = df[df != 0]

    # Plot the data using bar() method
    ax = df.plot.bar()
    ax.bar_label(ax.containers[0])
    plt.title("Overall ranking of all " + module + " modules")
    plt.xlabel("Ranking")
    plt.ylabel("Number of modules")

    # Rotate x labels
    plt.xticks(rotation=45)

    # Save the plot
    plt.tight_layout()
    plt.savefig(module + "/overall_ranking.pdf", dpi=1500)
    plt.savefig(module + "/overall_ranking.png", dpi=300)
    plt.figure()

def generate_platform_ranking_plot(module):
    path = "../platforms_ranking/platform_results/" + module + "/"

    old_path = os.getcwd()
    os.chdir(path)
    csv_files = glob.glob("*.csv")

    rank_counts = {}
    for file in csv_files:
        # Read in the CSV file using pandas
        df = pd.read_csv(file)

        # Count the number of different ranks in the 'Rank' column of the DataFrame
        counts = df['Rank'].value_counts()

        # Add the counts to the rank_counts dictionary
        rank_counts[file] = counts

    # Convert the rank_counts dictionary to a DataFrame
    df = pd.DataFrame(rank_counts)
    rank_order = ["excellent", "great", "good", "normal", "average", "low", "manual"]
    df = df.reindex(rank_order)

    df = df.loc[df.sum(axis=1) > 0]

    # Plot a stacked bar chart of the rank counts
    ax = df.plot(kind='bar', stacked=True)
    handles, labels = ax.get_legend_handles_labels()

    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    # Set the axis labels and title
    ax.set_xlabel('Rank')
    ax.set_ylabel('Count')
    ax.set_title('Platform ranking results for ' + module + ' modules')
    plt.xticks(rotation=45)

    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:.0f}'.format(y)))

    # Relabel the color values
    handles, labels = ax.get_legend_handles_labels()
    new_labels = [label.split('.')[0] for label in labels]
    ax.legend(handles=handles, labels=new_labels, fontsize=5)

    os.chdir(old_path)
    plt.tight_layout()
    plt.savefig("platform/" + module + "/" + module + ".pdf", dpi=1500, bbox_inches="tight")
    plt.savefig("platform/" + module + "/" + module + ".png", dpi=300, bbox_inches="tight")
    plt.figure()


if __name__ == "__main__":
    modules = ["auxiliary", "encoder", "evasion", "exploit", "nop", "payload", "post"]
    for module in modules:
        generate_rankings_plot(module)
        if module == "auxiliary": 
            continue
        generate_platform_ranking_plot(module)

# TODO: Sort bar colors according to legend 
# TODO: Set total bar height above bar
