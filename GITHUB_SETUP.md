# Инструкция по загрузке SkillDNA на GitHub

## 🚀 Пошаговая инструкция

### Шаг 1: Установка Git

1. **Скачайте Git для Windows:**
   - Перейдите на https://git-scm.com/download/win
   - Скачайте последнюю версию Git для Windows
   - Запустите установщик и следуйте инструкциям

2. **Проверьте установку:**
   ```bash
   git --version
   ```

### Шаг 2: Настройка Git

1. **Настройте имя пользователя:**
   ```bash
   git config --global user.name "Ваше Имя"
   git config --global user.email "ваш@email.com"
   ```

2. **Проверьте настройки:**
   ```bash
   git config --list
   ```

### Шаг 3: Инициализация репозитория

1. **Перейдите в папку проекта:**
   ```bash
   cd C:\Users\socra\OneDrive\Desktop\skilldna1.0
   ```

2. **Инициализируйте Git репозиторий:**
   ```bash
   git init
   ```

3. **Добавьте все файлы:**
   ```bash
   git add .
   ```

4. **Сделайте первый коммит:**
   ```bash
   git commit -m "Initial commit: SkillDNA NFT Portfolio Project"
   ```

### Шаг 4: Создание репозитория на GitHub

1. **Войдите в GitHub:**
   - Перейдите на https://github.com
   - Войдите в свой аккаунт (или создайте новый)

2. **Создайте новый репозиторий:**
   - Нажмите кнопку "New repository"
   - Название: `skilldna-nft-portfolio`
   - Описание: `NFT Portfolio Skills Management System with Django and Ethereum`
   - Выберите "Public" или "Private"
   - НЕ добавляйте README, .gitignore или лицензию (они уже есть)

3. **Скопируйте URL репозитория:**
   - Скопируйте URL вида: `https://github.com/ваш-username/skilldna-nft-portfolio.git`

### Шаг 5: Подключение к GitHub

1. **Добавьте удаленный репозиторий:**
   ```bash
   git remote add origin https://github.com/ваш-username/skilldna-nft-portfolio.git
   ```

2. **Переименуйте основную ветку в main:**
   ```bash
   git branch -M main
   ```

3. **Загрузите код на GitHub:**
   ```bash
   git push -u origin main
   ```

### Шаг 6: Проверка

1. **Обновите страницу GitHub:**
   - Перейдите в ваш репозиторий
   - Убедитесь, что все файлы загружены

2. **Проверьте структуру проекта:**
   - Django проект должен быть в корне
   - Все файлы должны быть видны

## 📁 Структура проекта на GitHub

```
skilldna-nft-portfolio/
├── README.md                    # Основная документация
├── requirements.txt             # Python зависимости
├── env.example                  # Пример конфигурации
├── demo.html                    # Демо страница в крипто-стиле
├── start-demo.sh               # Скрипт запуска
├── deploy-contract.sh          # Скрипт деплоя контракта
├── .gitignore                  # Git исключения
├── skilldna/                   # Django проект
│   ├── settings.py            # Настройки с Jazzmin
│   ├── urls.py                # URL маршруты
│   └── ...
├── core/                       # Django приложение
│   ├── models.py              # Модели с русскими названиями
│   ├── views.py               # API с русскими сообщениями
│   ├── admin.py               # Админка с Jazzmin
│   ├── serializers.py         # Сериализаторы
│   ├── utils.py               # Web3 утилиты
│   └── static/admin/css/      # Кастомные стили
└── blockchain/                 # Solidity и Hardhat
    ├── SkillDNA.sol           # Контракт
    ├── package.json           # Node.js зависимости
    ├── hardhat.config.js      # Конфигурация Hardhat
    └── test/                  # Тесты контракта
```

## 🔧 Дополнительные команды Git

### Просмотр статуса:
```bash
git status
```

### Просмотр истории коммитов:
```bash
git log --oneline
```

### Добавление изменений:
```bash
git add .
git commit -m "Описание изменений"
git push
```

### Создание новой ветки:
```bash
git checkout -b feature/new-feature
git push -u origin feature/new-feature
```

## 🌐 После загрузки на GitHub

1. **Обновите README.md** с актуальной информацией
2. **Добавьте Issues** для отслеживания задач
3. **Настройте GitHub Pages** для демо страницы
4. **Добавьте Actions** для автоматического тестирования
5. **Создайте Releases** для версий проекта

## 📝 Полезные ссылки

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Django Deployment](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

**После выполнения всех шагов ваш проект SkillDNA будет доступен на GitHub!** 🚀
