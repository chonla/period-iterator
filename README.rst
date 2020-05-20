===============
Period Iterator
===============

Period Iterator is a library easing you to iterate through given period.

-----
Usage
-----

::

    period = PeriodIterator('2020-02-01,2020-02-03', 'Asia/Bangkok')

    while True:
        print(period.cursor.begin()) # Begin of day
        print(period.cursor.end()) # End of day
        if period.next():
            break

-------
License
-------

MIT_

.. _MIT: https://github.com/chonla/period-iterator/blob/master/LICENSE
