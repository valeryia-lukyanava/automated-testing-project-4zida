from statistics import median

from config import UIConfig
from utils.logger import logger


def calculate_median_value(metric_name: str, performance_metrics: dict) -> int:
    median_value = round(median([i[metric_name] for i in performance_metrics.values()]))
    logger.info(f"Median value for the metric '{metric_name}': {median_value}")
    return median_value


def get_median_values_for_metrics(performance_metrics: dict, ui_config: UIConfig) -> dict:
    median_values = {"URL": ui_config.base_url,
                     "TTFB": calculate_median_value("TTFB", performance_metrics),
                     "LCP": calculate_median_value("LCP", performance_metrics),
                     "PageLoadTime": calculate_median_value("PageLoadTime", performance_metrics),
                     "EndToEndResponseTime": calculate_median_value("EndToEndResponseTime", performance_metrics)}
    performance_metrics["Median Values"] = median_values
    return median_values
