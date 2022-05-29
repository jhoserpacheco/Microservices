from django.db import connections
from django.contrib.auth.models import Group
from apps.user_app.models import User, Program
from apps.user_app.rules import get_role

def handle_register(user_json: dict) -> User:
    user = User()
    user.google_id = user_json['sub']
    user.first_name = user_json['given_name']
    user.last_name = user_json['family_name']
    user.email = user_json['email']
    user.picture = user_json['picture']
    user.save()
    # Check roles in external database and add to user
    print("bruh")
    with connections['ext_db'].cursor() as cursor:
        cursor.execute(
            """
            SELECT r.rol, p.program_name FROM users u INNER JOIN roles r ON r.role_id=u.role_id INNER JOIN programs p ON p.program_id=u.program_id WHERE u.email=%s
            """,
            [user.email]
        )
        print("its ok")
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            if not user.program:
                user.program = Program.objects.get_or_create(name=row[1])[0]
            group_name = get_role(row[0])
            if group_name:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
                user.save()                
    return user