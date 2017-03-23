# An easy way to lazily iterate over all the records from a database table

Usage
-----

```python
from lazyiter import LazyIterator

columns = ['city', 'state', 'population']
yield_per = 100

state_population_iterator = LazyIterator('postgres:///db', 'state_populations', columns, yield_per)

total_population = 0
for city, state, population in state_population_iterator:
  total_population += population
  ....
    
```

Requirements
-----
Python 3, a database that supports SQLAlchemy `yield_per` (postgres).
