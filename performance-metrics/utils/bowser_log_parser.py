def get_lcp_from_logs(logs: list) -> int:
    lcp = None
    for entry in logs:
        if entry['level'] == "WARNING" and "LCP" in entry['message']:
            lcp = round(float(str(entry['message']).split()[3]))
    return lcp
