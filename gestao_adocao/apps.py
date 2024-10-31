from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = "Formulário de solicitações de adoção"
    name = 'gestao_adocao'
