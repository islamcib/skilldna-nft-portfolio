import os
import json
from web3 import Web3

# Глобальные переменные для ленивой инициализации
w3 = None
contract = None
account = None
abi = None
contract_address = None

def _init_web3():
    """Инициализация Web3 соединения"""
    global w3, contract, account, abi, contract_address
    
    if w3 is not None:
        return  # Уже инициализировано
    
    # Инициализация Web3
    web3_provider = os.getenv("WEB3_PROVIDER")
    if not web3_provider:
        raise Exception("WEB3_PROVIDER не установлен в переменных окружения")
    
    w3 = Web3(Web3.HTTPProvider(web3_provider))
    
    if not w3.is_connected():
        raise Exception("Не удалось подключиться к Ethereum сети")

    contract_address_str = os.getenv("CONTRACT_ADDRESS")
    if not contract_address_str:
        raise Exception("CONTRACT_ADDRESS не установлен в переменных окружения")
    
    contract_address = Web3.to_checksum_address(contract_address_str)
    private_key = os.getenv("PRIVATE_KEY")

    if not private_key:
        raise Exception("PRIVATE_KEY не установлен в переменных окружения")

    account = w3.eth.account.from_key(private_key)

    # Загрузка ABI контракта
    try:
        with open("blockchain/SkillDNA.json", "r") as f:
            contract_data = json.load(f)
            abi = contract_data["abi"]
    except FileNotFoundError:
        # Fallback ABI если файл не найден
        abi = [
            {
                "inputs": [
                    {"internalType": "string", "name": "name", "type": "string"},
                    {"internalType": "string", "name": "proof", "type": "string"}
                ],
                "name": "issueSkill",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "anonymous": False,
                "inputs": [
                    {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
                    {"indexed": False, "internalType": "string", "name": "name", "type": "string"},
                    {"indexed": False, "internalType": "string", "name": "proof", "type": "string"},
                    {"indexed": False, "internalType": "uint256", "name": "timestamp", "type": "uint256"}
                ],
                "name": "SkillIssued",
                "type": "event"
            }
        ]

    contract = w3.eth.contract(address=contract_address, abi=abi)

def issue_nft(name, proof):
    """
    Выпускает NFT навыка в блокчейне
    
    Args:
        name (str): Название навыка
        proof (str): URL доказательства навыка
    
    Returns:
        str: Хэш транзакции
    """
    try:
        # Инициализируем Web3 соединение
        _init_web3()
        
        # Получаем приватный ключ
        private_key = os.getenv("PRIVATE_KEY")
        
        # Получаем текущий nonce
        nonce = w3.eth.get_transaction_count(account.address)
        
        # Строим транзакцию
        tx = contract.functions.issueSkill(name, proof).build_transaction({
            "from": account.address,
            "nonce": nonce,
            "gas": 200000,
            "gasPrice": w3.to_wei("10", "gwei")
        })
        
        # Подписываем транзакцию
        signed_tx = w3.eth.account.sign_transaction(tx, private_key)
        
        # Отправляем транзакцию
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        
        return tx_hash.hex()
        
    except Exception as e:
        raise Exception(f"Ошибка при выпуске NFT: {str(e)}")

def get_skill_count():
    """
    Получает общее количество выпущенных навыков
    
    Returns:
        int: Количество навыков
    """
    try:
        _init_web3()
        return contract.functions.totalSkills().call()
    except Exception as e:
        raise Exception(f"Ошибка при получении количества навыков: {str(e)}")

def get_skill(index):
    """
    Получает информацию о навыке по индексу
    
    Args:
        index (int): Индекс навыка
    
    Returns:
        dict: Информация о навыке
    """
    try:
        _init_web3()
        skill = contract.functions.getSkill(index).call()
        return {
            "owner": skill[0],
            "name": skill[1],
            "proof": skill[2],
            "timestamp": skill[3]
        }
    except Exception as e:
        raise Exception(f"Ошибка при получении навыка: {str(e)}")
