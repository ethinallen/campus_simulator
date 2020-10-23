## Saving Campus State
#### [Clock]("./scripts/campus_clock.py")
- save the current time of the simulation

#### [Campus]("./script/campus.py")
- Save all of buildings that are on campus
- Need to retain building id
- Need to retain any relevant outages associated with the building

#### [Building]("./script/building.py")
- Save structure of rooms and corridors
- Retain room and corridor id

#### [Room + Corridor]("./script/room.py")
- Needs to save all of the uuids for every sensor
- save the structure of sensors in each area

#### [Sensor]("./script/sensor.py")
- ID of each sensor
- TTL of each sensor
- Age of sensor
- replacement_wait
-

---   

- save snapshot of campus
- load snapshot of campus
- builings have appropriate building names
- csv's are written by building

---   

- normalize the power consumption by building appropriately  
  - between 30MW and 150MW
- thermostats register higher right before the power increase fort he building
- each building has set amounts of events
  - failing hvac
  - lots of people n the building
  - occupancy goes up sometimes when there are large surges in the power
  - buildings power consumptions are based on offset days from the dataset
