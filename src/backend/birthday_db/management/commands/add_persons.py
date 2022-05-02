from django.core.management.base import BaseCommand, CommandError
from birthday_db.models import Person

from typing import Any, Optional

import random
from datetime import date

FIRST_NAMES = [
    'Alex',
    'Carol',
    'John',
    'Jennifer',
    'Leonie',
    'Pablo',
    'Stefan',
    'Axel'
]

LAST_NAMES = [
    'Schmidt',
    'Müller',
    'Schneider',
    'Fischer',
    'Weber',
    'Meyer',
    'Wagner',
    'Becker'
]

class Command(BaseCommand):
    help = 'Add 20 Persons to the database'

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        start_date = date(1960, 1, 1).toordinal()
        end_date = date(2005, 12, 31).toordinal()
        for _ in range(0, 20):
            first_name = FIRST_NAMES[random.randint(0, len(FIRST_NAMES)-1)]
            last_name = LAST_NAMES[random.randint(0, len(LAST_NAMES)-1)]

            birthday = date.fromordinal(random.randint(start_date, end_date))
        
            try:
                p = Person(
                    first_name=first_name,
                    last_name=last_name,
                    birthday=birthday
                )
                p.save()
            except BaseException:
                raise CommandError('Could not create Person')
            
        self.stdout.write(self.style.SUCCESS('Successfully added Persons'))