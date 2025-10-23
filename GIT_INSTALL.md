# Установка Git для Windows

## 🚀 Быстрая установка

### Вариант 1: Скачать с официального сайта

1. **Перейдите на сайт Git:**
   - Откройте https://git-scm.com/download/win
   - Скачайте последнюю версию для Windows

2. **Запустите установщик:**
   - Запустите скачанный файл `Git-x.x.x-64-bit.exe`
   - Следуйте инструкциям установщика
   - Оставьте все настройки по умолчанию

3. **Проверьте установку:**
   - Откройте PowerShell или Command Prompt
   - Выполните команду: `git --version`

### Вариант 2: Через Chocolatey (если установлен)

```powershell
choco install git
```

### Вариант 3: Через Winget (Windows 10/11)

```powershell
winget install --id Git.Git -e --source winget
```

## ⚙️ Настройка Git

После установки Git выполните следующие команды:

```bash
# Настройте ваше имя
git config --global user.name "Ваше Имя"

# Настройте ваш email
git config --global user.email "ваш@email.com"

# Проверьте настройки
git config --list
```

## 🔑 Настройка SSH ключей (опционально)

Для удобной работы с GitHub рекомендуется настроить SSH ключи:

1. **Сгенерируйте SSH ключ:**
   ```bash
   ssh-keygen -t ed25519 -C "ваш@email.com"
   ```

2. **Добавьте ключ в SSH агент:**
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

3. **Скопируйте публичный ключ:**
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

4. **Добавьте ключ в GitHub:**
   - Перейдите в Settings → SSH and GPG keys
   - Нажмите "New SSH key"
   - Вставьте скопированный ключ

## ✅ Проверка установки

Выполните команду для проверки:

```bash
git --version
```

Должно появиться сообщение вида:
```
git version 2.x.x.windows.1
```

## 🎉 Готово!

Теперь вы можете использовать Git для работы с проектом SkillDNA!

---

**После установки Git следуйте инструкциям в файле GITHUB_SETUP.md** 🚀
