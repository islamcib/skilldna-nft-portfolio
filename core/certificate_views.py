from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from core.models import SkillNFT
from datetime import datetime

class CertificateView(View):
    """Отображение NFT сертификата навыка"""
    
    def get(self, request, skill_id):
        try:
            skill = SkillNFT.objects.get(id=skill_id)
        except SkillNFT.DoesNotExist:
            return HttpResponse("Сертификат не найден", status=404)
        
        # Цвета для разных типов навыков
        colors = {
            "Python разработка": {
                "primary": "#00ffff",
                "secondary": "#00ff00",
                "accent": "#ffffff"
            },
            "Django разработка": {
                "primary": "#00ff00", 
                "secondary": "#ffff00",
                "accent": "#ffffff"
            },
            "Blockchain разработка": {
                "primary": "#ff00ff",
                "secondary": "#00ffff", 
                "accent": "#ffffff"
            }
        }
        
        color_scheme = colors.get(skill.skill_name, colors["Python разработка"])
        
        # NFT ID на основе ID навыка
        nft_id = f"#{skill.id:03d}"
        
        # Дата выпуска
        issue_date = skill.issued_at.strftime("%Y-%m-%d") if skill.issued_at else datetime.now().strftime("%Y-%m-%d")
        
        # Хэш транзакции (если есть)
        tx_hash = skill.tx_hash[:8] + "..." + skill.tx_hash[-8:] if skill.tx_hash else "Pending..."
        
        context = {
            'skill': skill,
            'nft_id': nft_id,
            'issue_date': issue_date,
            'tx_hash': tx_hash,
            'color_scheme': color_scheme
        }
        
        return render(request, 'certificate.html', context)
