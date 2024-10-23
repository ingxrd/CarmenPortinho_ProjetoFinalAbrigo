from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = "Formulário de Cadastro de Pet"
    name = 'cadastro_pet'
