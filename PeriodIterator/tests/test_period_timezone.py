from ..period_timezone import PeriodTimezone

class TestPeriodTimezone():
    def test_period_timezone_format_2_positive_digits(self):
        tzfmt = PeriodTimezone()
        assert tzfmt.format('+07') == '+07:00'

    def test_period_timezone_format_2_negative_digits(self):
        tzfmt = PeriodTimezone()
        assert tzfmt.format('-07') == '-07:00'

    def test_period_timezone_format_default(self):
        tzfmt = PeriodTimezone()
        assert tzfmt.format('-07aa') == '-07aa'