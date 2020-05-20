from .. import PeriodIterator, PeriodCursor
from libfaketime import fake_time
from datetime import datetime
import pytest

@pytest.fixture()
def timezone_name():
    yield 'Asia/Bangkok'

@fake_time('2019-12-31 17:00:00', tz_offset=7) # It is 2020-01-01T00:00:00+0700
class TestPeriodIterator():
    def test_period_with_start_end(self, timezone_name):
        period = PeriodIterator('lastmonth,thismonth', timezone_name)
        assert period.start == '2019-12-01T00:00:00+07:00'
        assert period.end == '2020-01-31T23:59:59+07:00'
    
    def test_period_with_single_timestamp(self, timezone_name):
        period = PeriodIterator('2019-12-31T00:00:00+07:00', timezone_name)
        assert period.start == '2019-12-31T00:00:00+07:00'
        assert period.end == '2019-12-31T00:00:00+07:00'

    def test_period_with_single_timestamp_with_colon_in_timezone(self, timezone_name):
        period = PeriodIterator('2019-12-31T00:00:00+07:00', timezone_name)
        assert period.start == '2019-12-31T00:00:00+07:00'
        assert period.end == '2019-12-31T00:00:00+07:00'

    def test_yesterday(self, timezone_name):
        period = PeriodIterator('yesterday', timezone_name)
        assert period.start == '2019-12-31T00:00:00+07:00'
        assert period.end == '2019-12-31T23:59:59+07:00'

    def test_lastmonth(self, timezone_name):
        period = PeriodIterator('lastmonth', timezone_name)
        assert period.start == '2019-12-01T00:00:00+07:00'
        assert period.end == '2019-12-31T23:59:59+07:00'

    def test_thismonth(self, timezone_name):
        period = PeriodIterator('thismonth', timezone_name)
        assert period.start == '2020-01-01T00:00:00+07:00'
        assert period.end == '2020-01-31T23:59:59+07:00'

    def test_daybeforeyesterday(self, timezone_name):
        period = PeriodIterator('daybeforeyesterday', timezone_name)
        assert period.start == '2019-12-30T00:00:00+07:00'
        assert period.end == '2019-12-30T23:59:59+07:00'

    def test_today(self, timezone_name):
        period = PeriodIterator('today', timezone_name)
        assert period.start == '2020-01-01T00:00:00+07:00'
        assert period.end == '2020-01-01T23:59:59+07:00'

    def test_lasthour(self, timezone_name):
        period = PeriodIterator('lasthour', timezone_name)
        assert period.start == '2019-12-31T23:00:00+07:00'
        assert period.end == '2019-12-31T23:59:59+07:00'

    def test_lastonequarterhour(self, timezone_name):
        period = PeriodIterator('lastonequarterhour', timezone_name)
        assert period.start == '2019-12-31T23:45:00+07:00'
        assert period.end == '2019-12-31T23:59:59+07:00'

    def test_dateonly(self, timezone_name):
        period = PeriodIterator('2020-02-01', timezone_name)
        assert period.start == '2020-02-01T00:00:00+07:00'
        assert period.end == '2020-02-01T23:59:59+07:00'

    def test_cursor_initialize(self, timezone_name):
        period = PeriodIterator('2020-02-01', timezone_name)
        assert period.cursor == PeriodCursor(period.start, timezone_name)

    def test_cursor_initialize_from_start_end(self, timezone_name):
        period = PeriodIterator('2020-02-01,2020-02-03', timezone_name)
        assert period.cursor == PeriodCursor(period.start, timezone_name)

    def test_cursor_iteration(self, timezone_name):
        period = PeriodIterator('2020-02-01,2020-02-03', timezone_name)
        
        assert period.next()
        assert period.next()
        assert not period.next()