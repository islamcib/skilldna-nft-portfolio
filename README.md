# 🏆 SkillDNA - NFT Сертификаты Навыков

SkillDNA - это инновационная платформа для создания цифрового портфолио навыков, где каждый навык представлен как NFT-доказательство в сети Ethereum Sepolia.

## ✨ Новые возможности

### 🎓 Динамические NFT Сертификаты
Теперь каждый навык имеет красивый NFT сертификат в крипто-стиле:

- **Python разработка:** http://localhost:8000/api/certificate/1/
- **Django разработка:** http://localhost:8000/api/certificate/2/
- **Blockchain разработка:** http://localhost:8000/api/certificate/3/

### 🎨 Особенности сертификатов:
- **Крипто-стиль** с неоновыми эффектами
- **Уникальные NFT ID** (#001, #002, #003)
- **Динамические данные** из базы данных
- **Блокчейн хэш** для проверки подлинности
- **Анимированный фон** с плавающими элементами
- **Ссылка на Etherscan** для верификации

## 🏗️ Архитектура

```
SkillDNA/
├── skilldna/           # Django проект
├── core/              # Django приложение
├── blockchain/        # Solidity контракт и Hardhat
├── requirements.txt   # Python зависимости
├── start-demo.sh     # Скрипт запуска
└── README.md         # Документация
```

## 🚀 Быстрый старт

### 1. Запуск проекта
```bash
# Активация виртуального окружения
.\venv\Scripts\Activate.ps1

# Запуск сервера
python manage.py runserver
```

### 2. Доступные адреса
- **🌐 Главная страница:** http://localhost:8000
- **🔗 API:** http://localhost:8000/api/skills/
- **⚙️ Админка:** http://localhost:8000/admin/
- **🎓 Сертификаты:** http://localhost:8000/api/certificate/{id}/

### 3. Данные для входа в админку
- **Логин:** `admin`
- **Пароль:** `admin123`

### 2. Настройка блокчейна

#### Получение Infura API ключа
1. Зарегистрируйтесь на [Infura](https://infura.io/)
2. Создайте новый проект
3. Скопируйте API ключ

#### Получение приватного ключа
1. Создайте новый кошелек MetaMask
2. Экспортируйте приватный ключ
3. Убедитесь, что у вас есть Sepolia ETH для газа

#### Деплой контракта

```bash
# Создайте файл blockchain/.env
cat > blockchain/.env << EOF
API_URL=https://sepolia.infura.io/v3/YOUR_INFURA_API_KEY
PRIVATE_KEY=YOUR_PRIVATE_KEY_HERE
EOF

# Деплой контракта
./deploy-contract.sh
```

После деплоя скопируйте адрес контракта из `blockchain/contract-info.json`.

### 3. Настройка Django

```bash
# Создайте файл .env
cp env.example .env

# Отредактируйте .env файл
nano .env
```

Добавьте в `.env`:
```env
WEB3_PROVIDER=https://sepolia.infura.io/v3/YOUR_INFURA_API_KEY
CONTRACT_ADDRESS=0x... # Адрес задеплоенного контракта
PRIVATE_KEY=YOUR_PRIVATE_KEY_HERE
```

### 4. Запуск приложения

```bash
# Запуск демо
./start-demo.sh
```

Приложение будет доступно по адресу: http://localhost:8000

## 📚 API Документация

### Базовый URL
```
http://localhost:8000/api/
```

### Аутентификация
Все API запросы требуют аутентификации. Используйте Django сессии или токены.

### Эндпоинты

#### Создание навыка
```http
POST /api/skills/
Content-Type: application/json

{
    "skill_name": "Python разработка",
    "description": "Опыт разработки на Python 3+ лет",
    "proof_url": "https://github.com/username/python-projects"
}
```

#### Получение навыков пользователя
```http
GET /api/skills/
```

#### Получение конкретного навыка
```http
GET /api/skills/{id}/
```

#### Обновление навыка
```http
PUT /api/skills/{id}/
Content-Type: application/json

{
    "skill_name": "Обновленное название",
    "description": "Обновленное описание",
    "proof_url": "https://new-proof-url.com"
}
```

#### Удаление навыка
```http
DELETE /api/skills/{id}/
```

### Примеры ответов

#### Успешное создание навыка
```json
{
    "id": 1,
    "owner": {
        "id": 1,
        "username": "user123",
        "email": "user@example.com"
    },
    "skill_name": "Python разработка",
    "description": "Опыт разработки на Python 3+ лет",
    "proof_url": "https://github.com/username/python-projects",
    "issued_at": "2024-01-15T10:30:00Z",
    "tx_hash": "0x1234567890abcdef..."
}
```

## 🔧 Разработка

### Структура проекта

#### Django модели
- `SkillNFT`: Модель навыка с привязкой к пользователю и хэшем транзакции

#### Solidity контракт
- `SkillDNA`: Основной контракт для выпуска NFT навыков
- События для отслеживания выпуска навыков
- Функции для получения информации о навыках

#### Web3 интеграция
- Автоматический выпуск NFT при создании навыка
- Обработка ошибок блокчейна
- Сохранение хэша транзакции

### Локальная разработка

```bash
# Активация виртуального окружения
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Миграции
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск сервера разработки
python manage.py runserver
```

### Тестирование контракта

```bash
cd blockchain
npx hardhat test
```

## 🔒 Безопасность

- Приватные ключи хранятся в переменных окружения
- Все транзакции подписываются локально
- Проверка прав доступа на уровне Django
- Валидация данных на уровне контракта

## 🌐 Сеть Ethereum Sepolia

- **RPC URL**: https://sepolia.infura.io/v3/YOUR_KEY
- **Chain ID**: 11155111
- **Explorer**: https://sepolia.etherscan.io/
- **Faucet**: https://sepoliafaucet.com/

## 📝 Примеры использования

### Создание навыка через curl

```bash
# Сначала войдите в систему через браузер
# Затем используйте сессионные куки

curl -X POST http://localhost:8000/api/skills/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "skill_name": "React разработка",
    "description": "Создание современных веб-приложений на React",
    "proof_url": "https://github.com/username/react-portfolio"
  }'
```

### Проверка навыка в блокчейне

```javascript
// Используя Web3.js
const contract = new web3.eth.Contract(abi, contractAddress);
const skill = await contract.methods.getSkill(0).call();
console.log(skill);
```

## 🐛 Устранение неполадок

### Ошибка подключения к блокчейну
- Проверьте правильность WEB3_PROVIDER
- Убедитесь, что Infura API ключ действителен

### Ошибка деплоя контракта
- Проверьте наличие Sepolia ETH
- Убедитесь в правильности приватного ключа

### Ошибка выпуска NFT
- Проверьте баланс ETH для газа
- Убедитесь, что контракт задеплоен

## 📄 Лицензия

MIT License - см. файл LICENSE для деталей.

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request

## 📞 Поддержка

- GitHub Issues: [Создать issue](https://github.com/your-repo/issues)
- Email: support@skilldna.com
- Telegram: @skilldna_support

---

**SkillDNA** - Ваши навыки в блокчейне! 🚀
