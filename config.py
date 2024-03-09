from functools import lru_cache

from pydantic import Field, BaseSettings
from webdriver.factory.browser import Browser


class ViewportConfig(BaseSettings):
    width: int = Field(default=393, env="CLIENT_WINDOW_WIDTH")
    height: int = Field(default=873, env="CLIENT_WINDOW_HEIGHT")
    maximize: bool = True
    orientation: str = "portrait"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class DriverConfig(BaseSettings):
    browser: Browser = Field(default=Browser.CHROME, env="BROWSER")
    remote_url: str = Field(default="", env="REMOTE_URL")
    wait_time: int = Field(default=5, env="MAX_WAIT_TIME")
    local_path: str = Field(default="D:/Python/Project4zida/chromedriver-win64/chromedriver.exe", env="LOCAL_PATH")
    page_load_wait_time: int = 30
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
    experimental_options: list[dict] = [{"mobileEmulation": {
        "deviceMetrics": {"width": ViewportConfig().width, "height": ViewportConfig().height}}}]
    seleniumwire_options: dict = {}
    extension_paths: list[str] | None = None
    webdriver_kwargs: dict | None = None
    version: str | None

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


class UIConfig(BaseSettings):
    base_url: str = Field(env="BASE_URL")
    production_base_url: str = Field(env="PRODUCTION_BASE_URL")
    api_check_links: bool = Field(env="API_CHECK_LINKS")
    viewport: ViewportConfig = ViewportConfig()
    driver: DriverConfig = DriverConfig()
    logging: LoggingConfig = LoggingConfig()
    custom: dict = {}

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class QACredentials(BaseSettings):
    qa_email: str = Field(env="QA_EMAIL")
    qa_password: str = Field(env="QA_PASSWORD")
    google_qa_email: str = Field(env="GOOGLE_QA_EMAIL")
    google_qa_password: str = Field(env="GOOGLE_QA_PASSWORD")

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
