from collect_metric_values import collect_metric_values
from config import CELL_HEIGHT, END_TO_END_RESPONSE_TIME, PAGE_LOAD_TIME, TTFB, LCP
from generate_comparative_analysis_total_table import generate_comparative_analysis_median_values_table
from generate_trend_chart import generate_trend_chart
from pdf import PDF
from read_all_results import read_all_results
import sys
from datetime import datetime


def main():
    print(f"Arguments: {sys.argv}")
    results_path = sys.argv[1]
    site = sys.argv[2]
    page_url = sys.argv[3]
    measurement_number = sys.argv[4]
    workflow_link = sys.argv[5]

    current_results_date = datetime.now()
    previous_results_date = datetime.now()

    try:
        current_results_date, previous_results_date, results_files = read_all_results(results_path)
        generate_comparative_analysis_median_values_table(current_results_date, previous_results_date)
        metrics = ["Median Values"]
        target_metrics = [TTFB, LCP, PAGE_LOAD_TIME, END_TO_END_RESPONSE_TIME]
        need_header = True
        for target_metric in target_metrics:
            trend_header_csv = collect_metric_values(results_files,
                                                     metrics,
                                                     target_metric,
                                                     'statistics_trend.csv',
                                                     need_header)
            if need_header:
                need_header = False

        generate_trend_chart(trend_header_csv,
                             'statistics_trend.csv',
                             './trend.png',
                             'Trend of Median Metrics, ms')

        # Generate PDF
        pdf = PDF()
        pdf.add_page()
        pdf.set_font('Times', 'B', 22)
        pdf.set_text_color(0, 0, 150)
        pdf.cell(w=0, h=20, txt=f"Performance Test Results Analysis - {site}", ln=1, align='C')
        pdf.cell(w=60, h=CELL_HEIGHT, txt="", ln=1)
        pdf.set_text_color(0, 0, 0)

        pdf.set_font('Arial', 'B', 12)
        pdf.cell(w=100, h=2 * CELL_HEIGHT, txt="General Information about Performance Test:", ln=0)

        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=2 * CELL_HEIGHT, txt="GitHub Actions Workflow:", ln=1, align='R')

        pdf.set_text_color(0, 0, 0)

        pdf.add_general_info_with_border("Date: ", current_results_date, 'T')

        pdf.add_link("", workflow_link, workflow_link)
        pdf.add_general_info("Website: ", site, new_line=1)
        pdf.add_general_info("Page URL: ", page_url, new_line=1, is_link=True)
        pdf.add_general_info("Number of Measurements: ", measurement_number, new_line=1)
        pdf.add_general_info_with_border("Previous Performance Test Run: ", previous_results_date, 'B')

        pdf.set_font('Arial', '', 10)
        pdf.cell(w=60, h=CELL_HEIGHT, txt="", ln=1)
        pdf.cell(w=60, h=CELL_HEIGHT, txt="", ln=1)
        pdf.cell(w=60, h=CELL_HEIGHT, txt="", ln=1)

        pdf.add_header("Comparative Analysis of Median Values (Previous vs Current Performance Test Results)")
        pdf.image('./ComparativeAnalisysMedianValues.png', x=70, w=155, type='PNG', link='')

        pdf.ln(CELL_HEIGHT)

        pdf.add_chart('./trend.png')

        report_file_name = f'./{site} - Performance Results {datetime.now().strftime("%Y-%m-%d")}.pdf'
        pdf.output(report_file_name, 'F')

        print(f'Report {report_file_name} is prepared')
        print('...Done!')
    except OSError as err:
        print("Analyzing cannot be performed. OS error: {0}".format(err))
