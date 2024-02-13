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
        trend_header_csv = collect_metric_values(results_files,
                                                 metrics,
                                                 TTFB,
                                                 'statistics_trend_ttfb.csv')
        generate_trend_chart(trend_header_csv,
                             'statistics_trend_ttfb.csv',
                             './trend_ttfb.png',
                             'Trend of TTFB, ms',
                             'blue')

        trend_header_csv = collect_metric_values(results_files,
                                                 metrics,
                                                 LCP,
                                                 'statistics_trend_lcp.csv')
        generate_trend_chart(trend_header_csv,
                             'statistics_trend_lcp.csv',
                             './trend_lcp.png',
                             'Trend of LCP, ms',
                             'orange'
                             )

        trend_header_csv = collect_metric_values(results_files,
                                                 metrics,
                                                 END_TO_END_RESPONSE_TIME,
                                                 'statistics_trend_end_to_end_response_time.csv')

        generate_trend_chart(trend_header_csv,
                             'statistics_trend_end_to_end_response_time.csv',
                             './trend_end_to_end_response_time.png',
                             'Trend of End-to-End Response Time, ms',
                             'purple')
        #
        trend_header_csv = collect_metric_values(results_files,
                                                 metrics,
                                                 PAGE_LOAD_TIME,
                                                 'statistics_trend_page_load_time.csv')
        generate_trend_chart(trend_header_csv,
                             'statistics_trend_page_load_time.csv',
                             './trend_page_load_time.png',
                             'Trend of Page Load Time, ms',
                             'green')

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

        pdf.add_chart('./trend_ttfb.png')
        pdf.add_chart('./trend_lcp.png')
        pdf.add_chart('./trend_page_load_time.png')
        pdf.add_chart('./trend_end_to_end_response_time.png')

        report_file_name = f'./{site} - Performance Results {datetime.now().strftime("%Y-%m-%d")}.pdf'
        pdf.output(report_file_name, 'F')

        print(f'Report {report_file_name} is prepared')
        print('...Done!')
    except OSError as err:
        print("Analyzing cannot be performed. OS error: {0}".format(err))
