from django.db import migrations


INITIAL_TILES = [
    {
        'icon': 'bi bi-people-fill',
        'label': 'NGOs & Development Partners',
        'description': (
            'Governance, financial management and compliance training for '
            'civil society organisations and their implementing partners.'
        ),
        'order': 1,
    },
    {
        'icon': 'bi bi-building-fill',
        'label': 'Government Institutions',
        'description': (
            'Public financial management, accountability and performance '
            'improvement programmes for ministries, departments and agencies.'
        ),
        'order': 2,
    },
    {
        'icon': 'bi bi-heart-fill',
        'label': 'Faith-Based Organisations',
        'description': (
            'Stewardship, internal controls and organisational governance '
            'tailored to the structure and values of faith-based bodies.'
        ),
        'order': 3,
    },
    {
        'icon': 'bi bi-mortarboard-fill',
        'label': 'Educational Institutions',
        'description': (
            'Financial oversight, compliance and institutional strengthening '
            'for schools, colleges and universities.'
        ),
        'order': 4,
    },
    {
        'icon': 'bi bi-cash-stack',
        'label': 'SACCOs & Cooperatives',
        'description': (
            'Credit management, regulatory compliance and sound governance '
            'practices for savings and credit cooperative organisations.'
        ),
        'order': 5,
    },
    {
        'icon': 'bi bi-briefcase-fill',
        'label': 'Boards of Directors',
        'description': (
            'Strategic oversight, fiduciary responsibilities and board '
            'effectiveness for directors across all sectors.'
        ),
        'order': 6,
    },
    {
        'icon': 'bi bi-graph-up-arrow',
        'label': 'Private Sector Organisations',
        'description': (
            'Corporate governance, risk management and internal audit '
            'capacity building for businesses seeking sustainable growth.'
        ),
        'order': 7,
    },
]


def seed_training_audience(apps, schema_editor):
    TrainingAudience = apps.get_model('core', 'TrainingAudience')
    for tile in INITIAL_TILES:
        TrainingAudience.objects.create(**tile)


def unseed_training_audience(apps, schema_editor):
    # No-op: admin-managed content must not be silently destroyed on rollback.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_add_training_audience'),
    ]

    operations = [
        migrations.RunPython(seed_training_audience, unseed_training_audience),
    ]
