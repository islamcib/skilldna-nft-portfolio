from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SkillNFT

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SkillNFTSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    tx_url = serializers.SerializerMethodField()
    is_issued = serializers.SerializerMethodField()
    
    class Meta:
        model = SkillNFT
        fields = ['id', 'owner', 'skill_name', 'description', 'proof_url', 'issued_at', 'tx_hash', 'tx_url', 'is_issued']
        read_only_fields = ['owner', 'issued_at', 'tx_hash']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
    
    def get_tx_url(self, obj):
        """Возвращает URL для просмотра транзакции в Etherscan"""
        return obj.get_tx_url()
    
    def get_is_issued(self, obj):
        """Проверяет, выпущен ли NFT в блокчейне"""
        return obj.is_issued()
    
    def validate_skill_name(self, value):
        """Валидация названия навыка"""
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Название навыка должно содержать минимум 3 символа")
        return value.strip()
    
    def validate_description(self, value):
        """Валидация описания навыка"""
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Описание навыка должно содержать минимум 10 символов")
        return value.strip()
    
    def validate_proof_url(self, value):
        """Валидация URL доказательства"""
        if value and not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError("URL должен начинаться с http:// или https://")
        return value
