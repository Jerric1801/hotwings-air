import React from 'react';
import arrow from '../assets/images/brand/arrow.svg'

function FlightSearchForm() {

    return (
        <div className="flight-search-container">
            <div className="flight-search-header">
                <h2>Find your Flight</h2>
            </div>
            <form>
                <div class="flight-search-inputs">
                    <div class="flight-search-input">
                        <input type="text" name="origin" placeholder="FROM"></input>
                        <img src={arrow}></img>
                        <input type="text" name="destination" placeholder='TO'></input>
                    </div>
                    <div class="flight-search-input">
                        <input type="text" name="departure_date"></input>
                        <input type="text" name="return_date"></input>
                    </div>
                    <div class="flight-search-input">
                        <input type="text" name="class"></input>
                        <input type="text" name="passengers"></input>
                    </div>
                </div>

                <div class="flight-search-submit">
                    <div class="flight-search-radio">
                        <label>
                            <input type="radio" name="trip-type"></input>
                            ONE WAY
                        </label>
                        <label>
                            <input type="radio" name="trip-type"></input>
                            ROUND TRIP
                        </label>
                    </div>
                    <input type="submit" value='Find Flight'></input>
                </div>
            </form>
        </div>
    );
}

export default FlightSearchForm;