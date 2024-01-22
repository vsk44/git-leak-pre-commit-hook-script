# Встановлення git-leak-pre-commit
1. Виконати скрипт install-git-leak-pre-commit<br />
`chmod +x install-git-leak-pre-commit`<br />
`install-git-leak-pre-commit`
2. Оновити або створити хук pre-commit у директорії .git/hooks<br /> 
Додати до нього виконання git-leak-pre-commit. Приклад файлу pre-commit в ./scripts.
3. Хук успішно створений. Тепер при коміті буде відбуватися скан репо на наявність чутливої інформації.

# Опис git-leak-pre-commit
Сам приклад скрипта був взятий з Git Leaks репо: https://github.com/gitleaks/gitleaks/blob/master/scripts/pre-commit.py.<br />
Який був доповнений автоматичним встановленням gitleaks залежно від операційної системи(при потребі).
Також написаний скрипт по встановленню хука install-git-leak-pre-commit за методом “curl pipe sh”.
