const hre = require("hardhat");

async function main() {
  console.log("Начинаем деплой контракта SkillDNA...");
  
  // Получаем фабрику контракта
  const SkillDNA = await hre.ethers.getContractFactory("SkillDNA");
  
  // Деплоим контракт
  console.log("Деплоим контракт...");
  const skilldna = await SkillDNA.deploy();
  
  // Ждем подтверждения деплоя
  await skilldna.waitForDeployment();
  
  const contractAddress = await skilldna.getAddress();
  
  console.log("✅ SkillDNA успешно задеплоен!");
  console.log("📍 Адрес контракта:", contractAddress);
  console.log("🔗 Ссылка на Etherscan:", `https://sepolia.etherscan.io/address/${contractAddress}`);
  
  // Сохраняем адрес контракта в файл для использования в Django
  const fs = require('fs');
  const contractInfo = {
    address: contractAddress,
    network: "sepolia",
    deployedAt: new Date().toISOString()
  };
  
  fs.writeFileSync('contract-info.json', JSON.stringify(contractInfo, null, 2));
  console.log("📄 Информация о контракте сохранена в contract-info.json");
  
  // Проверяем работу контракта
  console.log("\n🧪 Тестируем контракт...");
  
  const totalSkills = await skilldna.totalSkills();
  console.log("📊 Общее количество навыков:", totalSkills.toString());
  
  console.log("\n🎉 Деплой завершен успешно!");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Ошибка при деплое:", error);
    process.exit(1);
  });
