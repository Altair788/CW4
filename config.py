from pathlib import Path

ROOT_PATH = Path(__file__).parent
VACANCIES_PATH = ROOT_PATH.joinpath("data", "vacancies.json")
FILE_WORKER_PATH = ROOT_PATH.joinpath("data", "file_worker")


TEXT = ''
PAGE = 0
PER_PAGE = 100
