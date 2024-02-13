ACCURACY = 3

TTFB = "TTFB"

LCP = "LCP"

PAGE_LOAD_TIME = "PageLoadTime"

END_TO_END_RESPONSE_TIME = "EndToEndResponseTime"

ADDITIONAL_METRICS = [LCP, END_TO_END_RESPONSE_TIME, PAGE_LOAD_TIME]

CHANGE_TITLE = "% Change"

METRIC_TITLE = "Metric"

URL = "URL"

MEDIAN_VALUES = "Median Values"

METRICS_MAPPER = {
    "URL": "URL, ms",
    "TTFB": "TTFB, ms",
    "LCP": "LCP, ms",
    "PageLoadTime": "Page Load Time, ms",
    "EndToEndResponseTime": "End-to-End Response Time, ms"
}

TABLE_STYLE = [
    ('text-align', 'center'), 
    ('border-style', 'solid'), 
    ('border-width', '1px'), 
    ('border-color', 'grey'), 
    ('background-color', '#87CEFA'),
    ('text-transform', 'uppercase'),
    ('line-height', '17pt')
]

CELL_HEIGHT = 7

MAX_NUMBER_OF_RESULTS_FOR_RENDER = 30
