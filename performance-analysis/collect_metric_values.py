from config import METRIC_TITLE
import csv
import json


def collect_metric_values(results_files, median_values, target_metric, target_output_file, need_header=False):
    trend_header = []
    results_files = dict(sorted(results_files.items()))
    for test_date, result_file in results_files.items():
        trend_header.append(test_date)
        with open(result_file.path, "r") as file:
            file_data = json.load(file)

    trend_info_series = {}
    for test_date in trend_header:
        trend_info = {}
        with open(results_files[test_date].path, "r") as file:
            file_data = json.load(file)
            for metrics in median_values:
                metric = ""
                if metrics in file_data.keys():
                    metric = file_data[metrics][target_metric]
                trend_info[metrics] = metric
        trend_info_series[str(test_date)] = trend_info

    trend_info_rows = []
    trend_header_csv = [METRIC_TITLE] + [i.strftime('%Y-%m-%d %H:%M') for i in trend_header]
    with open(target_output_file, 'a', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        if need_header:
            writer.writerow(trend_header_csv)
        # for target_metric in median_values:
        row = [target_metric]
        for test_date in trend_header:
            row += [trend_info_series[str(test_date)][metrics]]
        writer.writerow(row)
        trend_info_rows.append(row)
    return trend_header_csv
