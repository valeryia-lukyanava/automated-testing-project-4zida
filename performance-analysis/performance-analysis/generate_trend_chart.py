import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_trend_chart(trend_header_csv, input_file, output_file, chart_title, color):
    df_trend = pd.read_csv(input_file, index_col=[0])
    df_trend_largest = df_trend.nlargest(10, trend_header_csv[-1])

    with sns.axes_style("whitegrid"):
        sns.set_context("poster", font_scale=.6, rc={"grid.linewidth": 0.5, "lines.linewidth": 1.5})
        fig, ax = plt.subplots(1, 1, figsize=(20, 5))
        ax.xaxis_date()
        if len(trend_header_csv) > 9:
            fig.autofmt_xdate()
        df_trend_largest = df_trend.nlargest(10, trend_header_csv[-1])
        sns.lineplot(data=df_trend_largest.T, palette=[color], linewidth=2.5, dashes=False)
        plt.title(f"{chart_title}", fontsize=20, fontweight='bold')
        plt.savefig(output_file, transparent=False, facecolor='white', bbox_inches="tight")
        plt.close()
