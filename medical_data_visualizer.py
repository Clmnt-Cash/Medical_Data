import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
# Calculate IMC (height in meters)
df["IMC"] = df["weight"] / (df["height"] / 100) ** 2
# Create the 'overweight' column (1 if IMC > 25 else 0)
df["overweight"] = (df["IMC"] > 25).astype(int)
# Drop the IMC column
df = df.drop(columns=["IMC"])

# 3
# Normalize 'cholesterol' and 'gluc'
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars="cardio",
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )
    # 6
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    )
    print(df_cat)
    # 7
    cat_plot = sns.catplot(
        x="variable",  # categorical features
        y="total",  # count of occurrences
        hue="value",  # Split by the binary value (0 or 1)
        col="cardio",  # Separate plots for each cardio value (0 and 1)
        data=df_cat,  # grouped DataFrame
        kind="bar",  # bar plot
        height=5,  # Height of each facet
        aspect=1.2,
    )
    # Add labels and adjust the layout
    cat_plot.set_axis_labels("Variable", "Total Count")
    cat_plot.set_titles("Cardio = {col_name}")
    cat_plot.despine(left=True)
    plt.tight_layout()

    # 8
    fig = cat_plot.fig

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    # clean height
    df_heat = df[
        (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
    ]
    # clean weight
    df_heat = df[
        (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]
    # 12
    corr = df_heat.corr()
    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        square=True,
        linewidths=0.5,
        ax=ax,
    )
    plt.tight_layout()
    # 16
    fig.savefig("heatmap.png")
    return fig
