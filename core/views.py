from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import SkillNFT
from .serializers import SkillNFTSerializer
from .utils import issue_nft

class SkillNFTViewSet(viewsets.ModelViewSet):
    serializer_class = SkillNFTSerializer
    queryset = SkillNFT.objects.all()
    
    def get_queryset(self):
        return SkillNFT.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        skill_nft = serializer.save()
        
        # Выпускаем NFT в блокчейне
        try:
            tx_hash = issue_nft(skill_nft.skill_name, skill_nft.proof_url)
            skill_nft.tx_hash = tx_hash
            skill_nft.save()
        except Exception as e:
            # В случае ошибки блокчейна, удаляем запись
            skill_nft.delete()
            raise serializers.ValidationError(f"Ошибка выпуска NFT в блокчейне: {str(e)}")
    
    @action(detail=False, methods=['get'])
    def my_skills(self, request):
        """Получить все навыки текущего пользователя"""
        skills = self.get_queryset()
        serializer = self.get_serializer(skills, many=True)
        return Response({
            'message': 'Навыки успешно получены',
            'count': len(skills),
            'results': serializer.data
        })
    
    @action(detail=True, methods=['get'])
    def blockchain_info(self, request, pk=None):
        """Получить информацию о навыке в блокчейне"""
        skill = self.get_object()
        return Response({
            'skill_name': skill.skill_name,
            'is_issued': skill.is_issued(),
            'tx_hash': skill.tx_hash,
            'tx_url': skill.get_tx_url(),
            'issued_at': skill.issued_at,
            'message': 'NFT выпущен в блокчейне' if skill.is_issued() else 'NFT ожидает выпуска'
        })
    
    def list(self, request, *args, **kwargs):
        """Переопределяем list для добавления информации"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': f'Найдено навыков: {len(queryset)}',
            'results': serializer.data
        })
    
    def create(self, request, *args, **kwargs):
        """Переопределяем create для добавления информации"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'message': 'Навык успешно создан и NFT выпущен в блокчейне',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)
