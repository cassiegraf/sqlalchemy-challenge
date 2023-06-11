import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(autoload_with=engine)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)


# /
# - start at the homepage
# - list all the available routes

@app.route("/")
def Climate_Data():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/vi.0/tobs"
    )

# /api/v1.0/precipitation
# - convert the query results from your precipitation analysis 
#(retrieve only the last 12 months of data) to a dictionary
#using 'date' as the key and 'prcp' as the value
# - return the JSON representation of your dictionary    
@ap.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    precipitation_year = []
    for precipitation in results:
            precipitation_dict ={}
    ###NEED TO WORK ON THIS ^        



# /api/v1.0/stations
# - return a JSON list of stations from the dataset
# I THINK THIS PART IS OKAY NEED TO TEST
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(station.name).all()

    session.close()    

    station_name = list(np.ravel(results))

    return jsonify(station_name)


# /api/v1.0/tobs
 # - query the dates and temperature observations of the most-active 
#station for the previous year of data
# - return a JSON list of temperature observations for the previous 
 #year
@app.route("/api/v1.0/tobs")
    session = Session(engine)
    results = session.query(measurement.date, measurement.tobs).filter(measurement.date >= '2016-8-23', measurement.station == 'USC00519281').all()

    session.close()

    tobs = list(np.ravel(results))

    return jsonify(tobs)


# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# - return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified 
#start or start-end range
# - for a specified start, calculate 'TMIN','TAVG', and 'TMAX' for all the dates greater than or equal to the start date
# - for a specified start date and end date, calculate 'TMIN', 'TAVG', and 'TMAX' for the dates from the start date to end date
#inclusive


    