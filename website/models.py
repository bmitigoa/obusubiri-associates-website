from django.db import models


class TrainingIntro(models.Model):
    """Singleton model for the Training page introduction section."""

    heading = models.CharField(
        max_length=200,
        default='Building Stronger Organisations',
        help_text='Main heading shown in the intro section of the Training page.',
    )

    lead = models.TextField(
        default=(
            'At Obusubiri & Associates, we provide practical, '
            'results-oriented training programs designed to strengthen '
            'governance, financial management, compliance, '
            'accountability and organisational performance.'
        ),
        help_text='Lead paragraph shown below the heading.',
    )

    pullquote = models.TextField(
        default=(
            'Our programs are tailored for NGOs, Development Partners, '
            'Government Institutions, Faith-Based Organisations, '
            'Educational Institutions, SACCOs and Private Sector '
            'Organisations.'
        ),
        help_text='Pull-quote (gold-bordered blockquote) shown below the lead.',
    )

    class Meta:
        verbose_name = 'Training page intro'
        verbose_name_plural = 'Training page intro'

    def __str__(self):
        return self.heading

    @classmethod
    def get_solo(cls):
        """Return the single TrainingIntro row, creating it with defaults if absent."""
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
