import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# df_melt = pd.melt(
#    df,
#    id_vars="cardio",
#    value_vars=["cholesterol", "gluc", "alco", "active", "smoke"],
# )
## plot using seaborn
# g = sns.catplot(
#    x="variable",
#    hue="value",
#    col="cardio",
#    data=df_melt,
#    kind="count",
#    height=5,
#    aspect=1.2,
# )
## Add titles and labels
# g.set_axis_labels("Variable", "Count")
# g.set_titles("Cardio = {col_name}")
# g.despine(left=True)
# plt.tight_layout()
# plt.show()

# 2
df["overweight"] = None

# 3


# 4
def draw_cat_plot():
    # 5
    df_cat = None

    # 6
    df_cat = None

    # 7

    # 8
    fig = None

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None

    # 14
    fig, ax = None

    # 15

    # 16
    fig.savefig("heatmap.png")
    return fig
