- 1. Start campus simulation
  - define how many of each type of building
- 2. Each building calls how many rooms it has dependent on the type
  - define how many rooms there are in each building
  - rooms have type
- 3. Each rooms /  corridor calls its sensor
  - each sensor has its own type
  - each type has its own failure rate
    - need to work with Zach on these equations
- 4. Every sensor reports a given metric
---
# Meerschaum Integration

- turn 2d array of data into a pandas dataframe
- create a meerschaum connector
- use meerschaum.to_sql in order for us to write
