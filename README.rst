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
        print(period.cursor)
        if period.next():
            break

-------
License
-------

MIT_

.. _MIT: LICENSE
