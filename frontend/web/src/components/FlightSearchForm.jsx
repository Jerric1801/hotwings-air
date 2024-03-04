import { React, useState } from 'react';
import arrow from '../assets/images/brand/arrow.svg'
import Select from 'react-select'
import DatePicker from 'react-date-picker';

import 'react-date-picker/dist/DatePicker.css';
import 'react-calendar/dist/Calendar.css';

function FlightSearchForm() {

    const options = [
        { value: 'chocolate', label: 'Chocolate' },
        { value: 'strawberry', label: 'Strawberry' },
        { value: 'vanilla', label: 'Vanilla' }
    ]
    const [isClearable, setIsClearable] = useState(true);
    const [isSearchable, setIsSearchable] = useState(true);
    const [isDisabled, setIsDisabled] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [isRtl, setIsRtl] = useState(false);

    const [departureDate, setDepartureDate] = useState(new Date());
    const [returnDate, setReturnDate] = useState(new Date());

    return (
        <div className="flight-search-container">
            <div className="flight-search-header">
                <h2>Find your Flight</h2>
            </div>
            <form>
                <div class="flight-search-inputs">
                    <div class="flight-search-input">
                        <Select options={options}
                            className="origin custom-input"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            name="color"
                            placeholder="From..." />
                        <img src={arrow}></img>
                        <Select options={options}
                            className="destination custom-input"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            name="color"
                            placeholder="To..." />
                    </div>
                    <div class="flight-search-input">
                        <DatePicker className = "custom-input" value={departureDate} onChange={(date) => setDepartureDate(date)} />
                        <DatePicker className = "custom-input" value={returnDate} onChange={(date) => setReturnDate(date)} />
                    </div>
                    <div class="flight-search-input">
                        <Select options={options}
                            className="class custom-input"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            name="color"
                            placeholder="From..." />
                        <Select options={options}
                            className="passengers custom-input"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            name="color"
                            placeholder="From..." />
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