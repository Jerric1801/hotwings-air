import React from 'react';

function FlightSearchForm() {

  return (
    <form>
        <label>
            FROM
            <input type = "text" name = "origin" placeholder = "FROM"></input>
        </label>
        <label>
            TO
            <input type = "text" name = "destination" placeholder='TO'></input>
        </label>
        <label>
            DEPART DATE
            <input type = "text" name = "departure_date"></input>
        </label>
        <label>
            RETURN DATE
            <input type = "text" name = "return_date"></input>
        </label>
        <label>
            CLASS 
            <input type = "text" name = "class"></input>
        </label>
        <label>
            PASSENGERS
            <input type = "text" name = "passengers"></input>
        </label>
    </form>
  );
}

export default FlightSearchForm;