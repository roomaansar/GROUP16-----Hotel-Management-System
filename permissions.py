
'''
cat permissions.py | python manage.py shell
'''
from django.contrib.auth.models import Group, Permission
from accounts.models import User

permissions_names = [
    'Can change hotel',
    'Can add room',
    'Can change room',
    'Can delete hotel',
    'Can change booking',
]
permissions = []
for perm_name in permissions_names:
    permissions.append(Permission.objects.get(name=perm_name))
manager_perms = Group.objects.get_or_create(name='Manager Permissions')[0]
manager_perms.permissions.set(permissions)
managers = User.objects.filter(is_manager=True)
for manager in managers:
    manager.groups.add(manager_perms)
