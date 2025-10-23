#!/usr/bin/env bash

echo "🚀 Запуск SkillDNA Demo..."

# Проверяем наличие Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 не найден. Установите Python 3.8+ и попробуйте снова."
    exit 1
fi

# Создаем виртуальное окружение если его нет
if [ ! -d "venv" ]; then
    echo "📦 Создаем виртуальное окружение..."
    python3 -m venv venv
fi

# Активируем виртуальное окружение
echo "🔧 Активируем виртуальное окружение..."
source venv/bin/activate

# Устанавливаем зависимости
echo "📚 Устанавливаем зависимости..."
pip install -r requirements.txt

# Проверяем наличие .env файла
if [ ! -f ".env" ]; then
    echo "⚠️  Файл .env не найден. Создаем из примера..."
    cp env.example .env
    echo "📝 Пожалуйста, отредактируйте файл .env и добавьте ваши ключи:"
    echo "   - WEB3_PROVIDER (Infura API URL)"
    echo "   - CONTRACT_ADDRESS (адрес задеплоенного контракта)"
    echo "   - PRIVATE_KEY (ваш приватный ключ)"
    echo ""
    echo "После настройки .env файла запустите скрипт снова."
    exit 1
fi

# Выполняем миграции
echo "🗄️  Выполняем миграции базы данных..."
python manage.py migrate

# Создаем суперпользователя если его нет
echo "👤 Создаем суперпользователя (если не существует)..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@skilldna.com', 'admin123')
    print('✅ Суперпользователь создан: admin/admin123')
else:
    print('ℹ️  Суперпользователь уже существует')
"

# Запускаем сервер
echo "🌐 Запускаем Django сервер..."
echo "📍 Сервер будет доступен по адресу: http://localhost:8000"
echo "🔗 API: http://localhost:8000/api/skills/"
echo "⚙️  Админка: http://localhost:8000/admin/"
echo ""
echo "Для остановки сервера нажмите Ctrl+C"
echo ""

python manage.py runserver 0.0.0.0:8000
