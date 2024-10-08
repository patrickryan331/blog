# Generated by Django 5.1 on 2024-08-20 22:17

from django.db import migrations


def populate_role(apps, schhhemaeditor):
    entries = {
        "member": "A member of the site",
        "editor": "Someone who can edit others posts",
        "moderator": "Someone who can edit posts and moderate editors"
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()

def populate_team(apps, scheamaeditor):
    enteries =  {
        "alpha": "The A Team",
        "bravo": "The B Team",
        "charlie": "The C Team"
    }
    Team = apps.get_model("accounts", "Team")
    for key, value in enteries.items():
        team_obj = Team(name=key, description=value)
        team_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_role),
        migrations.RunPython(populate_team),
    ]
