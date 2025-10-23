#!/usr/bin/env bash

echo "🔗 Деплой SkillDNA контракта в Ethereum Sepolia..."

# Переходим в директорию blockchain
cd blockchain

# Проверяем наличие Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js не найден. Установите Node.js и попробуйте снова."
    exit 1
fi

# Проверяем наличие npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm не найден. Установите npm и попробуйте снова."
    exit 1
fi

# Устанавливаем зависимости
echo "📦 Устанавливаем зависимости..."
npm install

# Проверяем наличие .env файла
if [ ! -f ".env" ]; then
    echo "⚠️  Файл .env не найден в директории blockchain/"
    echo "📝 Создайте файл blockchain/.env со следующим содержимым:"
    echo ""
    echo "API_URL=https://sepolia.infura.io/v3/YOUR_INFURA_API_KEY"
    echo "PRIVATE_KEY=YOUR_PRIVATE_KEY_HERE"
    echo ""
    echo "После создания файла запустите скрипт снова."
    exit 1
fi

# Компилируем контракт
echo "🔨 Компилируем контракт..."
npx hardhat compile

# Деплоим контракт
echo "🚀 Деплоим контракт в Sepolia..."
npx hardhat run deploy.js --network sepolia

echo ""
echo "✅ Деплой завершен!"
echo "📄 Проверьте файл blockchain/contract-info.json для получения адреса контракта"
echo "🔗 Скопируйте адрес контракта в файл .env как CONTRACT_ADDRESS"
