import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

from flask import Flask, jsonify

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(autoload_with=engine)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)


#starting at homepage, list all available routes
@app.route("/")
def Climate_Data():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/20140522<br/>"
        f"/api/v1.0/start/end"
    )

#return last 12 months of precipitation data, include date and precipitation    
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-23').all()

    session.close()

    tobs = list(np.ravel(results))

    return jsonify(tobs)

    ###NEED TO WORK ON THIS ^ It's not how the school is asking but the results are loading into webpage       



#return a JSON list of stations from the dataset
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(station.name).all()

    session.close()    

    station_name = list(np.ravel(results))

    return jsonify(station_name)

#query dates/temps of most-active station (USC0051928) and return JSON list of temps for previous year 
@app.route("/api/v1.0/tobs")
def tob():
    session = Session(engine)
    results = session.query(measurement.date, measurement.tobs).filter(measurement.date >= '2016-08-23', measurement.station == 'USC00519281').all()

    session.close()

    tobs = list(np.ravel(results))

    return jsonify(tobs)


# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# - return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified 
#start or start-end range
# - for a specified start, calculate 'TMIN','TAVG', and 'TMAX' for all the dates greater than or equal to the start date
# - for a specified start date and end date, calculate 'TMIN', 'TAVG', and 'TMAX' for the dates from the start date to end date
#inclusive
@app.route("/api/v1.0/20140522")
def start():

    session = Session(engine)

    #sel = [measurement.station,
     #   func.min(measurement.tobs),
      #  func.max(measurement.tobs),
       # func.avg(measurement.tobs)]

    results = session.query(measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= '2014-05-22').all()

    session.close()

    start_date = list(np.ravel(results))

    return jsonify(start_date)

if __name__ == '__main__':
    app.run(debug=True)


    