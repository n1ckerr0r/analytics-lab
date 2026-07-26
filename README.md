# Analytics Lab

Сборник моих учебных и практических проектов по аналитике данных в `Jupyter Notebook`.

## Проекты

- `marketing-campaign/` - анализ маркетинговой кампании и проверка гипотез
- `netflix/` - исследовательский анализ каталога Netflix

## Что нужно для запуска

В этом окружении есть `python3`, но системные `pip` и полноценный `jupyter notebook` не настроены для проекта. Самый простой способ запустить ноутбуки здесь - через `uv` и локальное виртуальное окружение.

## Быстрый старт

```bash
cd /home/n1ckerr0r/maindir/projects/analytics-lab
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
jupyter notebook
```

После этого в браузере откроется интерфейс Jupyter, где можно зайти в:

- `marketing-campaign/marketing-campaign.ipynb`
- `netflix/netflix.ipynb`

Альтернатива: если у вас уже установлен `JupyterLab`, можно запускать его командой:

```bash
jupyter lab
```

