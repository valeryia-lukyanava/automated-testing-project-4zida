from config import ACCURACY, CHANGE_TITLE, MAX_NUMBER_OF_RESULTS_FOR_RENDER, METRIC_TITLE, METRICS_MAPPER, \
    MEDIAN_VALUES, URL
import csv
import json
import os
from datetime import datetime


def read_all_results(results_path):
    n = 0
    results_files = {}
    with os.scandir(results_path) as files:
        for file in files:
            if ".json" in file.name:
                n += 1
                timestamp_str = file.name.rsplit("metrics_")[1].rsplit(".json")[0]
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H%M')
                results_files[timestamp] = file
    print(f"Total number of results files in .json format: {n}")
    results_files = dict(sorted(results_files.items(), reverse=True))

    if n > MAX_NUMBER_OF_RESULTS_FOR_RENDER:
        results_files = dict(list(results_files.items())[:MAX_NUMBER_OF_RESULTS_FOR_RENDER])

    current_results_path = list(results_files.values())[0].path
    print(f"Current results file: {current_results_path}")
    current_results_date = list(results_files.keys())[0].strftime('%Y-%m-%d %H:%M')
    with open(current_results_path, "r") as current_results_file:
        print(f"Current results file size: {os.path.getsize(current_results_path)}")
        current_results = json.load(current_results_file)

    if n > 1:
        previous_results_path = list(results_files.values())[1].path
        previous_results_date = list(results_files.keys())[1].strftime('%Y-%m-%d %H:%M')
    else:
        previous_results_path = current_results_path
        previous_results_date = current_results_date
    print(f"Previous results file: {previous_results_path}")
    with open(previous_results_path, "r") as previous_results_file:
        print(f"Previous results file size: {os.path.getsize(previous_results_path)}")
        previous_results = json.load(previous_results_file)

    info = []
    info_total = [[METRIC_TITLE, previous_results_date, current_results_date, CHANGE_TITLE]]

    for metrics in current_results.keys():
        if metrics == MEDIAN_VALUES:
            current_results_metrics = current_results[metrics]
            if metrics.strip() in previous_results.keys():
                previous_results_metrics = previous_results[metrics]
                for metric in current_results_metrics.keys():
                    if metric != URL:
                        previous_results_value = previous_results_metrics[metric]
                        current_results_value = current_results_metrics[metric]
                        abs_diff = current_results_value - previous_results_value
                        if abs_diff != 0:
                            if previous_results_value != 0:
                                rel_diff = round(abs_diff / previous_results_value * 100, ACCURACY)
                            else:
                                rel_diff = 100.0
                        else:
                            rel_diff = 0
                        list_total = [
                            METRICS_MAPPER[metric],
                            previous_results_value,
                            current_results_value,
                            rel_diff
                        ]
                        info_total.append(list_total)

    table_data = []

    table_data.extend(info)

    with open('statistics.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        for line in table_data:
            writer.writerow(line)

    with open('statistics_median_values.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        for line in info_total:
            writer.writerow(line)

    return current_results_date, previous_results_date, results_files
