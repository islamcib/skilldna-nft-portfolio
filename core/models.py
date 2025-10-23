from django.contrib.auth.models import User
from django.db import models

class SkillNFT(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    skill_name = models.CharField(max_length=100, verbose_name="Название навыка")
    description = models.TextField(verbose_name="Описание навыка")
    proof_url = models.URLField(blank=True, verbose_name="Ссылка на доказательство")
    issued_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата выпуска")
    tx_hash = models.CharField(max_length=100, blank=True, verbose_name="Хэш транзакции")

    class Meta:
        ordering = ['-issued_at']
        verbose_name = "NFT Навык"
        verbose_name_plural = "NFT Навыки"

    def __str__(self):
        return f"{self.skill_name} - {self.owner.username}"
    
    def get_tx_url(self):
        """Возвращает URL для просмотра транзакции в Etherscan"""
        if self.tx_hash:
            return f"https://sepolia.etherscan.io/tx/{self.tx_hash}"
        return None
    
    def is_issued(self):
        """Проверяет, выпущен ли NFT в блокчейне"""
        return bool(self.tx_hash)
