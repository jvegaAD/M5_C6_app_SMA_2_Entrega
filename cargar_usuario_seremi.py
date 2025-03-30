from django.contrib.auth.models import User

username = 'seremi_usuario'
email = 'seremi@mma.cl'
password = 'seremi123'

if not User.objects.filter(username=username).exists():
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    user.is_staff = True        # Puede entrar al panel de admin
    user.is_superuser = False   # No tiene control total
    user.save()
    print(f"Usuario '{username}' creado correctamente.")
else:
    print(f"El usuario '{username}' ya existe.")