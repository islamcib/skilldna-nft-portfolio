# ⚡ SkillDNA - NFT Портфолио Навыков

[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://djangoproject.com/)
[![Solidity](https://img.shields.io/badge/Solidity-0.8.20-blue.svg)](https://soliditylang.org/)
[![Ethereum](https://img.shields.io/badge/Ethereum-Sepolia-purple.svg)](https://ethereum.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**SkillDNA** - это инновационная платформа для создания цифрового портфолио навыков, где каждый навык представлен как NFT-доказательство в сети Ethereum Sepolia.

## 🎯 Особенности

- **🎨 Современный дизайн** в крипто-стиле с неоновыми эффектами
- **⛓️ NFT-доказательства навыков** в блокчейне Ethereum
- **🔧 Красивая админка** с Django Jazzmin
- **🌐 Русский интерфейс** с понятными сообщениями
- **📡 REST API** для управления навыками
- **🔒 Максимальная безопасность** с локальным подписанием транзакций
- **📱 Интуитивный UX** с валидацией данных

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.8+
- Node.js 16+
- Git

### Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/ваш-username/skilldna-nft-portfolio.git
   cd skilldna-nft-portfolio
   ```

2. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # или
   venv\Scripts\activate     # Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте переменные окружения:**
   ```bash
   cp env.example .env
   # Отредактируйте .env файл
   ```

5. **Выполните миграции:**
   ```bash
   python manage.py migrate
   ```

6. **Создайте суперпользователя:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```

## 🎨 Демонстрация

Откройте `demo.html` в браузере для интерактивной демонстрации проекта в крипто-стиле.

## 🔧 API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `GET` | `/api/skills/` | Получить все навыки пользователя |
| `POST` | `/api/skills/` | Создать новый навык (выпускает NFT) |
| `GET` | `/api/skills/{id}/` | Получить конкретный навык |
| `PUT` | `/api/skills/{id}/` | Обновить навык |
| `DELETE` | `/api/skills/{id}/` | Удалить навык |

### Пример создания навыка

```bash
curl -X POST http://localhost:8000/api/skills/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "skill_name": "Python разработка",
    "description": "Опыт разработки на Python более 3 лет",
    "proof_url": "https://github.com/username/python-projects"
  }'
```

## ⛓️ Блокчейн интеграция

### Настройка контракта

1. **Установите зависимости Node.js:**
   ```bash
   cd blockchain
   npm install
   ```

2. **Настройте переменные окружения:**
   ```bash
   # Создайте blockchain/.env
   API_URL=https://sepolia.infura.io/v3/YOUR_INFURA_API_KEY
   PRIVATE_KEY=YOUR_PRIVATE_KEY_HERE
   ```

3. **Деплойте контракт:**
   ```bash
   npx hardhat run deploy.js --network sepolia
   ```

4. **Обновите .env файл** с адресом контракта

## 🏗️ Архитектура

```
skilldna-nft-portfolio/
├── skilldna/           # Django проект
│   ├── settings.py    # Настройки с Jazzmin
│   └── urls.py        # URL маршруты
├── core/              # Django приложение
│   ├── models.py      # Модели с русскими названиями
│   ├── views.py       # API с русскими сообщениями
│   ├── admin.py       # Админка с Jazzmin
│   ├── serializers.py # Сериализаторы с валидацией
│   └── utils.py       # Web3 утилиты
├── blockchain/        # Solidity контракт
│   ├── SkillDNA.sol   # Основной контракт
│   ├── package.json   # Node.js зависимости
│   └── test/          # Тесты контракта
└── demo.html          # Демо страница в крипто-стиле
```

## 🎨 Дизайн

- **Цветовая схема**: Темная с неоновыми акцентами (cyan, magenta, yellow)
- **Шрифты**: Orbitron (заголовки), Exo 2 (текст)
- **Анимации**: Плавные переходы и эффекты свечения
- **Тематика**: NFT, блокчейн, криптовалюты

## 🔒 Безопасность

- Приватные ключи хранятся в переменных окружения
- Все транзакции подписываются локально
- Проверка прав доступа на уровне Django
- Валидация данных на уровне контракта

## 📊 Мониторинг

- Все навыки публично доступны в блокчейне
- Транзакции можно отслеживать в Etherscan
- Django админка для управления навыками
- Логирование всех операций

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект лицензирован под лицензией MIT - см. файл [LICENSE](LICENSE) для деталей.

## 📞 Поддержка

- **GitHub Issues**: [Создать issue](https://github.com/ваш-username/skilldna-nft-portfolio/issues)
- **Email**: support@skilldna.com
- **Telegram**: @skilldna_support

## 🙏 Благодарности

- Django команде за отличный фреймворк
- Ethereum сообществу за блокчейн технологии
- Jazzmin за красивую админку
- Всем контрибьюторам проекта

---

**SkillDNA - Ваши навыки в блокчейне!** 🚀⚡

[![Star this repo](https://img.shields.io/github/stars/ваш-username/skilldna-nft-portfolio?style=social)](https://github.com/ваш-username/skilldna-nft-portfolio)
[![Fork this repo](https://img.shields.io/github/forks/ваш-username/skilldna-nft-portfolio?style=social)](https://github.com/ваш-username/skilldna-nft-portfolio)
