import allure
from playwright.sync_api import Playwright, Page

from config import Browser, settings


def initialize_playwright_page(playwright: Playwright,
                               test_name: str,
                               browser_type: Browser,
                               storage_state: str | None = None) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(storage_state=storage_state,
                                  base_url=settings.get_base_url()
                                  # record_video_dir = settings.videos_dir
                                  )
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    # context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()
    # allure.attach.file(source=settings.tracing_dir.joinpath(f'{test_name}.zip'), name="trace", extension="zip")
    # allure.attach.file(source=page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)
