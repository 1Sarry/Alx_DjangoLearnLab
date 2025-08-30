LibraryProject with Django

# RBAC with Groups & Permissions in Django

### Permissions

Defined in `Article` model:

- can_view
- can_create
- can_edit
- can_delete

### Groups

- **Viewers** → [can_view]
- **Editors** → [can_view, can_create, can_edit]
- **Admins** → [can_view, can_create, can_edit, can_delete]

### Usage

- Permissions are enforced with @permission_required in `views.py`
- Groups can be managed via Django Admin or `python manage.py setup_groups`
- Assign users to groups → their permissions update automatically

### Testing

1. Create users.
2. Assign them to groups.
3. Log in and attempt restricted actions.
