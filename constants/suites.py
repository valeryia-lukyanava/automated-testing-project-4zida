from enum import Enum


class Suite(str, Enum):
    UI = 'UI Functional Tests'
    SEO = 'SEO Tests'
    PERFORMANCE = 'Performance Tests'
    # SANITY = 'Sanity'
    # SMOKE = 'Smoke'
    # CORE_REGRESSION = 'Core Regression',
    # EXTENDED_REGRESSION = 'Extended Regression'
