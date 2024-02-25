from config import CHANGE_TITLE, METRIC_TITLE, TABLE_STYLE
import dataframe_image as dfi
import pandas as pd


def generate_comparative_analysis_median_values_table(current_results_date, previous_results_date):
    df_total = pd.read_csv('statistics_median_values.csv')

    df_total_styled = df_total.style \
        .set_table_styles([dict(selector='th', props=TABLE_STYLE)]) \
        .format(precision=2, thousands=" ", decimal=".") \
        .format({
        current_results_date: "{:.2f}",
        previous_results_date: "{:.2f}",
        CHANGE_TITLE: "{:.2f}%"
    }) \
        .set_properties(
        subset=[METRIC_TITLE, CHANGE_TITLE],
        **{'font-weight': 'bold'}
    )

    dfi.export(df_total_styled, 'ComparativeAnalisysMedianValues.png')
