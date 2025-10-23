const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SkillDNA", function () {
  let skillDNA;
  let owner;
  let addr1;
  let addr2;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();
    
    const SkillDNA = await ethers.getContractFactory("SkillDNA");
    skillDNA = await SkillDNA.deploy();
    await skillDNA.waitForDeployment();
  });

  describe("Деплой", function () {
    it("Должен установить правильного владельца", async function () {
      expect(await skillDNA.totalSkills()).to.equal(0);
    });
  });

  describe("Выпуск навыков", function () {
    it("Должен выпустить навык", async function () {
      const skillName = "Python разработка";
      const proof = "https://github.com/user/python-projects";
      
      await expect(skillDNA.connect(addr1).issueSkill(skillName, proof))
        .to.emit(skillDNA, "SkillIssued")
        .withArgs(addr1.address, skillName, proof, await getBlockTimestamp());
      
      expect(await skillDNA.totalSkills()).to.equal(1);
    });

    it("Должен получить информацию о навыке", async function () {
      const skillName = "React разработка";
      const proof = "https://github.com/user/react-portfolio";
      
      await skillDNA.connect(addr1).issueSkill(skillName, proof);
      
      const skill = await skillDNA.getSkill(0);
      expect(skill.owner).to.equal(addr1.address);
      expect(skill.name).to.equal(skillName);
      expect(skill.proof).to.equal(proof);
    });

    it("Должен получить навыки владельца", async function () {
      await skillDNA.connect(addr1).issueSkill("Навык 1", "proof1");
      await skillDNA.connect(addr2).issueSkill("Навык 2", "proof2");
      await skillDNA.connect(addr1).issueSkill("Навык 3", "proof3");
      
      const ownerSkills = await skillDNA.getOwnerSkills(addr1.address);
      expect(ownerSkills.length).to.equal(2);
      expect(ownerSkills[0]).to.equal(0);
      expect(ownerSkills[1]).to.equal(2);
    });

    it("Должен проверить владельца навыка", async function () {
      await skillDNA.connect(addr1).issueSkill("Тест", "proof");
      
      expect(await skillDNA.isOwner(0, addr1.address)).to.be.true;
      expect(await skillDNA.isOwner(0, addr2.address)).to.be.false;
    });

    it("Не должен выпустить навык с пустым названием", async function () {
      await expect(skillDNA.connect(addr1).issueSkill("", "proof"))
        .to.be.revertedWith("Название навыка не может быть пустым");
    });

    it("Не должен выпустить навык с пустым доказательством", async function () {
      await expect(skillDNA.connect(addr1).issueSkill("Название", ""))
        .to.be.revertedWith("Доказательство не может быть пустым");
    });
  });

  async function getBlockTimestamp() {
    const block = await ethers.provider.getBlock("latest");
    return block.timestamp;
  }
});
