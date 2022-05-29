from django.core.management.base import BaseCommand, CommandError
from ....user_app import rules

#Managements of adding and deleting groups depending of the user role through the group permissions

class Command(BaseCommand):
    help = "Create or delete groups"

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, choices=['create', 'delete'])
    
    def handle(self, *args, **options):
        action = options['action']
        if action == 'create':
            self.stdout.write(self.style.SUCCESS('Creating groups'))
            self.create_groups()
        elif action == 'delete':
            self.stdout.write(self.style.SUCCESS('Deleting groups'))
            self.delete_groups()
        else:
            raise CommandError('Invalid action')
        self.stdout.write(self.style.SUCCESS('Ok'))
    
    def create_groups(self):
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from apps.user_app.models import User

        # Create groups
        staff_group = Group.objects.get_or_create(name=rules.STAFF[1])[0]
        student_group = Group.objects.get_or_create(name=rules.PREGRADO[1])[0]
        teacher_group = Group.objects.get_or_create(name=rules.DOCENTE[1])[0]
        entrance_group = Group.objects.get_or_create(name='entrance')[0]
        locker_group = Group.objects.get_or_create(name='locker')[0]
        secretary_group = Group.objects.get_or_create(name='secretary')[0]

        ct = ContentType.objects.get_for_model(User)
        # Create permissions
        # Mas adelante se deben definir los permisos de forma mas personalizada
        # de acuedo a cada grupo, ejemplo de permisos para el grupo de de locker
        Permission.objects.create(codename= 'reader_qr_entrance', name= 'Reader Entrance QR', content_type= ct)
        Permission.objects.create(codename= 'reader_qr_exit', name= 'Reader Exit QR', content_type= ct)

    def delete_groups(self):
        from django.contrib.auth.models import Group
        from apps.user_app.models import User

        # Delete groups
        Group.objects.filter(name=rules.STAFF[1]).delete()
        Group.objects.filter(name=rules.PREGRADO[1]).delete()
        Group.objects.filter(name=rules.DOCENTE[1]).delete()
        Group.objects.filter(name='entrance').delete()
        Group.objects.filter(name='locker').delete()
        Group.objects.filter(name='secretary').delete()

        # Delete permissions
        # Ejemplo de como deberia borrarse
        from django.contrib.auth.models import Permission
        Permission.objects.filter(codename= 'reader_qr_entrance').delete()
        Permission.objects.filter(codename= 'reader_qr_exit').delete()
        


