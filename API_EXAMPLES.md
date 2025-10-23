# SkillDNA API Examples

## Аутентификация

Сначала войдите в систему через браузер на http://localhost:8000/admin/ или создайте пользователя через Django shell.

## Примеры запросов

### 1. Создание навыка

```bash
curl -X POST http://localhost:8000/api/skills/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "skill_name": "Python разработка",
    "description": "Опыт разработки на Python более 3 лет. Создание веб-приложений, API, автоматизация задач.",
    "proof_url": "https://github.com/username/python-projects"
  }'
```

### 2. Получение всех навыков пользователя

```bash
curl -X GET http://localhost:8000/api/skills/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

### 3. Получение конкретного навыка

```bash
curl -X GET http://localhost:8000/api/skills/1/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

### 4. Обновление навыка

```bash
curl -X PUT http://localhost:8000/api/skills/1/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "skill_name": "Python разработка (обновлено)",
    "description": "Обновленное описание навыка",
    "proof_url": "https://github.com/username/updated-projects"
  }'
```

### 5. Удаление навыка

```bash
curl -X DELETE http://localhost:8000/api/skills/1/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

## Примеры с использованием Python requests

```python
import requests

# Базовый URL
BASE_URL = "http://localhost:8000/api"

# Сессия для сохранения куки
session = requests.Session()

# Вход в систему (если используете токены)
# session.headers.update({'Authorization': 'Token YOUR_TOKEN'})

# Создание навыка
skill_data = {
    "skill_name": "JavaScript разработка",
    "description": "Создание интерактивных веб-приложений на JavaScript, React, Node.js",
    "proof_url": "https://github.com/username/js-projects"
}

response = session.post(f"{BASE_URL}/skills/", json=skill_data)
print(f"Статус: {response.status_code}")
print(f"Ответ: {response.json()}")

# Получение навыков
response = session.get(f"{BASE_URL}/skills/")
skills = response.json()
print(f"Найдено навыков: {len(skills)}")

for skill in skills:
    print(f"- {skill['skill_name']}: {skill['tx_hash']}")
```

## Примеры с использованием JavaScript (fetch)

```javascript
const BASE_URL = 'http://localhost:8000/api';

// Создание навыка
async function createSkill(skillData) {
    const response = await fetch(`${BASE_URL}/skills/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        credentials: 'include',
        body: JSON.stringify(skillData)
    });
    
    return await response.json();
}

// Получение навыков
async function getSkills() {
    const response = await fetch(`${BASE_URL}/skills/`, {
        credentials: 'include'
    });
    
    return await response.json();
}

// Использование
const skillData = {
    skill_name: "Blockchain разработка",
    description: "Разработка смарт-контрактов на Solidity",
    proof_url: "https://github.com/username/smart-contracts"
};

createSkill(skillData)
    .then(skill => {
        console.log('Навык создан:', skill);
        console.log('Хэш транзакции:', skill.tx_hash);
    })
    .catch(error => console.error('Ошибка:', error));
```

## Проверка навыка в блокчейне

После создания навыка вы можете проверить его в блокчейне:

1. Скопируйте `tx_hash` из ответа API
2. Откройте https://sepolia.etherscan.io/tx/YOUR_TX_HASH
3. Убедитесь, что транзакция подтверждена

## Обработка ошибок

### Ошибка аутентификации (401)
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### Ошибка валидации (400)
```json
{
    "skill_name": ["Это поле обязательно."],
    "description": ["Это поле обязательно."]
}
```

### Ошибка блокчейна (400)
```json
{
    "non_field_errors": ["Ошибка выпуска NFT: insufficient funds for gas"]
}
```
