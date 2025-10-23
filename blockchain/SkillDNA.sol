// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title SkillDNA
 * @dev Контракт для выпуска NFT-доказательств навыков
 * @author SkillDNA Team
 */
contract SkillDNA {
    /**
     * @dev Структура навыка
     */
    struct Skill {
        address owner;       // Владелец навыка
        string name;        // Название навыка
        string proof;      // URL доказательства
        uint256 timestamp; // Время выпуска
    }

    // Массив всех выпущенных навыков
    Skill[] public skills;
    
    // Событие выпуска навыка
    event SkillIssued(
        address indexed owner, 
        string name, 
        string proof, 
        uint256 timestamp
    );

    /**
     * @dev Выпускает новый навык
     * @param name Название навыка
     * @param proof URL доказательства навыка
     */
    function issueSkill(string memory name, string memory proof) public {
        require(bytes(name).length > 0, "Название навыка не может быть пустым");
        require(bytes(proof).length > 0, "Доказательство не может быть пустым");
        
        skills.push(Skill(msg.sender, name, proof, block.timestamp));
        
        emit SkillIssued(msg.sender, name, proof, block.timestamp);
    }

    /**
     * @dev Получает информацию о навыке по индексу
     * @param index Индекс навыка в массиве
     * @return skill Структура навыка
     */
    function getSkill(uint256 index) public view returns (Skill memory) {
        require(index < skills.length, "Индекс вне диапазона");
        return skills[index];
    }

    /**
     * @dev Возвращает общее количество выпущенных навыков
     * @return Количество навыков
     */
    function totalSkills() public view returns (uint256) {
        return skills.length;
    }

    /**
     * @dev Получает навыки владельца
     * @param owner Адрес владельца
     * @return Массив индексов навыков владельца
     */
    function getOwnerSkills(address owner) public view returns (uint256[] memory) {
        uint256[] memory ownerSkills = new uint256[](skills.length);
        uint256 count = 0;
        
        for (uint256 i = 0; i < skills.length; i++) {
            if (skills[i].owner == owner) {
                ownerSkills[count] = i;
                count++;
            }
        }
        
        // Создаем массив нужного размера
        uint256[] memory result = new uint256[](count);
        for (uint256 i = 0; i < count; i++) {
            result[i] = ownerSkills[i];
        }
        
        return result;
    }

    /**
     * @dev Проверяет, является ли адрес владельцем навыка
     * @param index Индекс навыка
     * @param owner Адрес для проверки
     * @return true если адрес является владельцем
     */
    function isOwner(uint256 index, address owner) public view returns (bool) {
        require(index < skills.length, "Индекс вне диапазона");
        return skills[index].owner == owner;
    }
}
