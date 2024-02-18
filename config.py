from functools import lru_cache

from pydantic import BaseModel, Field, BaseSettings
from webdriver.factory.browser import Browser


class DriverConfig(BaseSettings):
    browser: Browser = Field(default=Browser.CHROME, env="BROWSER")
    remote_url: str = Field(default="", env="REMOTE_URL")
    wait_time: int = 5
    page_load_wait_time: int = 0
    options: list[str] = [
        "ignore-certificate-errors",
        "--no-sandbox",
        "disable-infobars",
        "--incognito",
        # '--headless', TODO: compare metrics for headless and non-headless modes
        '--disable-extensions',
        '--disable-gpu'
    ]
    capabilities: dict[str, str] = {}
    # experimental_options: list[dict] | None = None
    experimental_options: list[dict] = [{"mobileEmulation": {"deviceMetrics": {"width": 393, "height": 873}}}]
    seleniumwire_options: dict = {}
    extension_paths: list[str] | None = None
    webdriver_kwargs: dict | None = None
    version: str | None
    # for local running only
    local_path: str = "D:/Python/Project4zida/chromedriver-win64/chromedriver.exe"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class LoggingConfig(BaseSettings):
    log_level: str = "INFO"
    screenshots_on: bool = Field(default=True, env="SCREENSHOTS_ON")
    screenshots_dir: str = Field(
        default='./screenshots', env="SCREENSHOTS_DIR"
    )
    performance_results_dir: str = Field(
        default='./performance-results', env="PERFORMANCE_RESULTS_DIR"
    )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class ViewportConfig(BaseModel):
    maximize: bool = True
    width: int = 393
    height: int = 873
    orientation: str = "portrait"


class UIConfig(BaseSettings):
    base_url: str = Field(env="BASE_URL")
    api_check_links: bool = Field(env="API_CHECK_LINKS")
    driver: DriverConfig = DriverConfig()
    logging: LoggingConfig = LoggingConfig()
    viewport: ViewportConfig = ViewportConfig()
    custom: dict = {}

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class PerformanceMeasurementConfig(BaseSettings):
    number_of_measurements: int = Field(default=3, env="NUMBER_OF_MEASUREMENTS")
    lcp: int = Field(env="LCP")
    ttfb: int = Field(env="TTFB")

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_ui_config() -> UIConfig:
    return UIConfig()
