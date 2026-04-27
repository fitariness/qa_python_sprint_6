# Самокат — автотесты

- Яндекс.Самокат, стек: Selenium, pytest, Allure, Page Object
- Python 3 и зависимости из `requirements.txt`
- Браузер: Firefox
- Отчёт Allure
- `allure_results/` и `allure-report/` в `.gitignore`.
- `config.py` — `BASE_URL` и таймауты.
- `data.py` — тестовые данные заказа
- `conftest.py` — фикстура `base_url`
- `locators/` — `main_page_locators.py`, `order_page_locators.py`
- `pages/` — `base_page.py`, `main_page.py`, `order_page.py`
- `tests/` — `test_main_page.py`, `test_order_page.py`, `browser_base.py` с `setup_class` / `teardown_class` под Firefox

Команды (из корня репозитория, в терминале):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```bash
pytest -v --alluredir=allure_results tests/
pytest -v --alluredir=allure_results tests/test_main_page.py
pytest -v --alluredir=allure_results tests/test_order_page.py
```

Флаг `--alluredir=allure_results` нужен, чтобы Allure собрал сырые данные (папку можно не коммитить, она в `.gitignore`).

```bash
allure serve allure_results
```

```bash
allure generate allure_results -o allure-report --clean
open allure-report/index.html
```
