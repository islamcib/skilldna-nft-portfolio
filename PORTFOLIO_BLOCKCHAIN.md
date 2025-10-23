e# ⛓️ Blockchain Разработка - Портфолио навыков

## 📋 Описание навыка
**Blockchain разработка** - создание смарт-контрактов на Solidity и интеграция с Web3.

## 🎯 Демонстрируемые навыки

### 1. Solidity Smart Contracts
- **Файл:** `blockchain/SkillDNA.sol` - основной смарт-контракт
- **Функции:** Выпуск NFT навыков, получение информации
- **События:** Отслеживание выпуска навыков в блокчейне

### 2. Hardhat Development Environment
- **Файл:** `hardhat.config.js` - конфигурация Hardhat
- **Тесты:** `test/SkillDNA.test.js` - тестирование контракта
- **Деплой:** `deploy.js` - скрипт развертывания

### 3. Web3 Integration
- **Файл:** `core/utils.py` - Python Web3 интеграция
- **Функции:** Автоматический выпуск NFT при создании навыка
- **Сеть:** Ethereum Sepolia testnet

## 🔧 Технические детали

### Solidity контракт:
```solidity
contract SkillDNA {
    struct Skill {
        string name;
        string proof;
        address owner;
        uint256 timestamp;
    }
    
    function issueSkill(string memory _name, string memory _proof) public;
    function getSkill(uint256 _id) public view returns (Skill memory);
}
```

### Web3 интеграция:
- **Библиотека:** Web3.py 6.11.3
- **Сеть:** Ethereum Sepolia (Chain ID: 11155111)
- **Провайдер:** Infura API
- **Подпись:** Локальная подпись транзакций

### Тестирование:
- **Hardhat тесты** для проверки функциональности
- **Автоматическое тестирование** при деплое
- **Проверка газовых затрат**

## 📊 Результаты

✅ **Создан смарт-контракт SkillDNA на Solidity**
✅ **Настроена среда разработки Hardhat**
✅ **Реализована Web3 интеграция с Python**
✅ **Добавлены тесты и автоматический деплой**

## 🚀 Демо

**Контракт в блокчейне:**
- **Сеть:** Ethereum Sepolia
- **Explorer:** https://sepolia.etherscan.io/
- **Функции:** Выпуск NFT навыков

**Интеграция:**
- Автоматический выпуск NFT при создании навыка в Django
- Сохранение хэша транзакции в базе данных
- Ссылки на Etherscan для проверки транзакций

---

*Этот файл демонстрирует навыки blockchain разработки на примере проекта SkillDNA.*
