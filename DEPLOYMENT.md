# Инструкции по развертыванию SkillDNA

## 🚀 Полное развертывание проекта

### Шаг 1: Подготовка окружения

```bash
# Убедитесь, что у вас установлены:
# - Python 3.8+
# - Node.js 16+
# - Git

# Клонируйте проект
git clone <repository-url>
cd skilldna1.0
```

### Шаг 2: Настройка блокчейна

#### 2.1 Получение Infura API ключа
1. Зайдите на https://infura.io/
2. Создайте аккаунт
3. Создайте новый проект
4. Выберите сеть "Ethereum"
5. Скопируйте Project ID

#### 2.2 Создание кошелька
1. Установите MetaMask
2. Переключитесь на сеть Sepolia
3. Получите тестовые ETH с https://sepoliafaucet.com/
4. Экспортируйте приватный ключ

#### 2.3 Деплой контракта

```bash
# Создайте файл конфигурации блокчейна
cat > blockchain/.env << EOF
API_URL=https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID
PRIVATE_KEY=YOUR_PRIVATE_KEY_WITHOUT_0x_PREFIX
EOF

# Деплой контракта
./deploy-contract.sh
```

После успешного деплоя скопируйте адрес контракта из `blockchain/contract-info.json`.

### Шаг 3: Настройка Django

```bash
# Создайте файл конфигурации Django
cp env.example .env

# Отредактируйте .env файл
nano .env
```

Добавьте в `.env`:
```env
WEB3_PROVIDER=https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID
CONTRACT_ADDRESS=0x... # Адрес из contract-info.json
PRIVATE_KEY=YOUR_PRIVATE_KEY_WITHOUT_0x_PREFIX
SECRET_KEY=django-insecure-your-unique-secret-key-here
DEBUG=True
```

### Шаг 4: Запуск приложения

```bash
# Запуск полного демо
./start-demo.sh
```

### Шаг 5: Проверка работы

1. Откройте http://localhost:8000/admin/
2. Войдите как admin/admin123
3. Перейдите в раздел "Skill NFTs"
4. Создайте новый навык
5. Проверьте хэш транзакции в Etherscan

## 🔧 Ручная настройка (альтернативный способ)

### Установка зависимостей Python

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Настройка базы данных

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Установка зависимостей Node.js

```bash
cd blockchain
npm install
```

### Компиляция и деплой контракта

```bash
npx hardhat compile
npx hardhat run deploy.js --network sepolia
```

### Запуск Django сервера

```bash
python manage.py runserver
```

## 🧪 Тестирование

### Тестирование контракта

```bash
cd blockchain
npx hardhat test
```

### Тестирование API

```bash
# Создание навыка
curl -X POST http://localhost:8000/api/skills/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "skill_name": "Тестовый навык",
    "description": "Описание тестового навыка",
    "proof_url": "https://example.com/proof"
  }'
```

## 🐛 Устранение неполадок

### Ошибка "insufficient funds for gas"
- Убедитесь, что у вас есть Sepolia ETH
- Получите тестовые ETH с https://sepoliafaucet.com/

### Ошибка подключения к Infura
- Проверьте правильность API ключа
- Убедитесь, что проект активен в Infura

### Ошибка "contract not deployed"
- Проверьте адрес контракта в .env
- Убедитесь, что контракт задеплоен в Sepolia

### Ошибка Django миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

## 📊 Мониторинг

### Проверка логов Django
```bash
tail -f logs/django.log
```

### Проверка статуса блокчейна
```bash
cd blockchain
npx hardhat console --network sepolia
```

### Проверка баланса кошелька
```javascript
// В Hardhat console
await ethers.provider.getBalance("YOUR_ADDRESS")
```

## 🔒 Безопасность

### Продакшн настройки

1. Измените `DEBUG=False` в settings.py
2. Используйте сильный SECRET_KEY
3. Настройте HTTPS
4. Используйте продакшн базу данных
5. Ограничьте ALLOWED_HOSTS

### Безопасность приватных ключей

- Никогда не коммитьте .env файлы
- Используйте переменные окружения в продакшне
- Рассмотрите использование Hardware Wallet

## 📈 Масштабирование

### Горизонтальное масштабирование

1. Используйте Redis для сессий
2. Настройте load balancer
3. Используйте CDN для статических файлов
4. Рассмотрите использование Docker

### Оптимизация блокчейна

1. Используйте batch операции
2. Оптимизируйте gas usage
3. Рассмотрите использование Layer 2 решений

## 📞 Поддержка

При возникновении проблем:

1. Проверьте логи приложения
2. Убедитесь в правильности конфигурации
3. Проверьте статус сети Sepolia
4. Создайте issue в репозитории

---

**Удачного развертывания SkillDNA!** 🚀
