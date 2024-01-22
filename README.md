# Встановлення git-leak-pre-commit
Виконати команду для встановлення git-leak-pre-commit<br />
`curl -sSL https://raw.githubusercontent.com/vsk44/git-leak-pre-commit-hook-script/main/install-git-leak-pre-commit | sh`

# Опис git-leak-pre-commit
Сам приклад скрипта був взятий з Git Leaks репо: https://github.com/gitleaks/gitleaks/blob/master/scripts/pre-commit.py.<br />
Який був доповнений автоматичним встановленням gitleaks залежно від операційної системи. Хук написаний на мові програмування python, інсталятор на bash.

За допомогою команди для встановлення, виконується скрипт - **install-git-leak-pre-commit**. Після виконання скрипта створюється в .git/hooks/ два файли **git-leak-pre-commit** та **pre-commit**. Якщо **pre-commit** вже був раніше створений, просто наповнює його новим хуком **git-leak-pre-commit**. <br />

Після проведення інсталяції перед кожним комітом буде автоматично тригериться хук **git-leak-pre-commit** для пошуку чутливої інформації в файлах проекту.
