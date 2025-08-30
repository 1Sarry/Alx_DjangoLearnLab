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


# Django Security Best Practices Applied

1. settings.py
   - DEBUG = False
   - Configured XSS, CSRF, Clickjacking, HSTS protections

2. Templates
   - All forms include {% csrf_token %}

3. Views
   - ORM used instead of raw SQL
   - User input validated via Django forms

4. Content Security Policy
   - Implemented via django-csp middleware

Testing
   - Manually tested CSRF protection by removing token (request blocked)
   - Checked XSS by entering <script> tags (escaped by Django templates)
   - Verified only allowed domains load external scripts/styles