from django.contrib import admin
from django.utils.html import format_html
from .models import SkillNFT

@admin.register(SkillNFT)
class SkillNFTAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'owner', 'issued_at', 'tx_hash_display', 'proof_url_display']
    list_filter = ['issued_at', 'owner']
    search_fields = ['skill_name', 'description', 'owner__username']
    readonly_fields = ['issued_at', 'tx_hash']
    list_per_page = 20
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('owner', 'skill_name', 'description')
        }),
        ('Доказательства', {
            'fields': ('proof_url',)
        }),
        ('Блокчейн данные', {
            'fields': ('issued_at', 'tx_hash'),
            'classes': ('collapse',)
        }),
    )
    
    def tx_hash_display(self, obj):
        if obj.tx_hash:
            return format_html(
                '<a href="https://sepolia.etherscan.io/tx/{}" target="_blank" style="color: #00ff00; text-decoration: none;">'
                '🔗 {}...{}</a>',
                obj.tx_hash,
                obj.tx_hash[:8],
                obj.tx_hash[-8:]
            )
        return format_html('<span style="color: #ffaa00;">⏳ Ожидает выпуска</span>')
    tx_hash_display.short_description = 'Хэш транзакции'
    tx_hash_display.admin_order_field = 'tx_hash'
    
    def proof_url_display(self, obj):
        if obj.proof_url:
            return format_html(
                '<a href="{}" target="_blank" style="color: #00ffff; text-decoration: none;">'
                '🔗 Открыть доказательство</a>',
                obj.proof_url
            )
        return format_html('<span style="color: #888;">Нет ссылки</span>')
    proof_url_display.short_description = 'Доказательство'
    proof_url_display.admin_order_field = 'proof_url'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('owner')
    
    class Media:
        css = {
            'all': ('admin/css/skilldna_admin.css',)
        }
