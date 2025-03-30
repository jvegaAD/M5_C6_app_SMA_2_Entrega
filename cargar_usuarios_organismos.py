from django.contrib.auth.models import User

usuarios = [
    {'username': 'organismo1_user', 'email': 'organismo1@example.com', 'password': 'org1pass'},
    {'username': 'organismo2_user', 'email': 'organismo2@example.com', 'password': 'org2pass'},
    {'username': 'organismo3_user', 'email': 'organismo3@example.com', 'password': 'org3pass'},
    {'username': 'organismo4_user', 'email': 'organismo4@example.com', 'password': 'org4pass'},
    {'username': 'organismo5_user', 'email': 'organismo5@example.com', 'password': 'org5pass'},
    {'username': 'organismo6_user', 'email': 'organismo6@example.com', 'password': 'org6pass'},
    {'username': 'organismo7_user', 'email': 'organismo7@example.com', 'password': 'org7pass'},
    {'username': 'organismo8_user', 'email': 'organismo8@example.com', 'password': 'org8pass'},
    {'username': 'organismo9_user', 'email': 'organismo9@example.com', 'password': 'org9pass'},
    {'username': 'organismo10_user', 'email': 'organismo10@example.com', 'password': 'org10pass'},
]


for usuario in usuarios:
    if not User.objects.filter(username=usuario["username"]).exists():
        u = User.objects.create_user(
            username=usuario["username"],
            email=usuario["email"],
            password=usuario["password"]
        )
        u.is_staff = False
        u.save()