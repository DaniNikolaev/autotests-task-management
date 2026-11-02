from pathlib import Path

from tools.ui.playwright.temp import use_project_temp_dir

# Playwright создаёт артефакты браузера в системной временной директории,
# которая может быть недоступна. Перенаправляем её в каталог проекта
# до старта драйвера Playwright.
use_project_temp_dir(Path(__file__).resolve().parent / "tmp")

pytest_plugins = (
    'api.fixtures.authentication',
    'api.fixtures.users',
    'api.fixtures.projects',
    'api.fixtures.tasks',
    'api.fixtures.attachments',
    'api.fixtures.comments',
    'ui.fixtures.browsers',
    'ui.fixtures.pages'

    #'fixtures.allure'
)
