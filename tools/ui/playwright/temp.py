import os
from pathlib import Path


def use_project_temp_dir(temp_dir: Path) -> Path:
    """Перенаправляет временную директорию процесса в каталог проекта.

    Playwright создаёт каталог артефактов через mkdtemp в системной временной
    директории (os.tmpdir() в Node-драйвере читает TMP/TEMP/TMPDIR). В
    ограниченных окружениях запись в системный %TEMP% запрещена, и запуск
    браузера падает с EPERM: operation not permitted, mkdtemp ....

    Функцию нужно вызывать до старта драйвера Playwright, то есть на этапе
    импорта conftest.py: драйвер наследует окружение процесса при запуске.
    """
    temp_dir.mkdir(parents=True, exist_ok=True)

    for variable in ("TMP", "TEMP", "TMPDIR"):
        os.environ[variable] = str(temp_dir)

    return temp_dir
