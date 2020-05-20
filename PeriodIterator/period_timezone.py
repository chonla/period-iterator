import re

class PeriodTimezone:
    def format(self, z):
        if re.match(r'^[+-]\d{2}$', z):
            return '{}:00'.format(z)
        return z
