from enum import Enum


class JS(str, Enum):
    DOCUMENT_READY_STATE = "return document.readyState"
    CONSOLE_CLEAR = 'console.clear()'
    TTFB = "return (window.performance.timing.responseStart-window.performance.timing.navigationStart)"
    PAGE_LOAD_TIME = "return (window.performance.timing.loadEventEnd-window.performance.timing.responseStart)"
    ENDTOEND_RESPONSE_TIME = "return (window.performance.timing.loadEventEnd-window.performance.timing.navigationStart)"
    LCP = """const observer = new PerformanceObserver((list) => {
                const entries = list.getEntries();
                const lastEntry = entries[entries.length - 1]; // Use the latest LCP candidate
                console.warn("LCP:", lastEntry.startTime);
                console.warn(lastEntry);
                });
                observer.observe({ type: "largest-contentful-paint", buffered: true });"""



