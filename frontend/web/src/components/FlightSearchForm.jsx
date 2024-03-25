import { React, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import arrow from '../assets/images/brand/arrow.svg'
import Select from 'react-select'
//datepicker
import DatePicker from 'react-date-picker';
import 'react-date-picker/dist/DatePicker.css';
import 'react-calendar/dist/Calendar.css';
import fetchData from '../utils/apiUtils';

function FlightSearchForm() {

    const flightDataOptions = {
        locations: [
            { value: "Singapore", label: "Singapore (SIN)" },
            { value: "Kuala Lumpur", label: "Kuala Lumpur (KUL)" },
            { value: "Jakarta", label: "Jakarta (JKT)" },
            { value: "Manila", label: "Manila (MNL)" },
            { value: "Dubai", label: "Dubai (DXB)" },
            { value: "Paris", label: "Paris (CDG)" },
            { value: "Los Angeles", label: "Los Angeles (LAX)" },
            { value: "Tokyo", label: "Tokyo (TYO)" },
            { value: "Bangkok", label: "Bangkok (BKK)" },
            { value: "Sydney", label: "Sydney (SYD)" },
            { value: "Hong Kong", label: "Hong Kong (HKG)" },
            { value: "London", label: "London (LHR)" },
            { value: "New York", label: "New York (JFK)" },
        ],
        pax: [
            { value: 1, label: "1" },
            { value: 2, label: "2" },
            { value: 3, label: "3" },
            { value: 4, label: "4" },
            { value: 5, label: "5" },
            { value: 6, label: "6" },
        ],
        classes: [
            { value: "Economy", label: "Economy" },
            { value: "Premium Economy", label: "Premium Economy" },
            { value: "Business", label: "Business" },
            { value: "First", label: "First" },
        ]
    };

    //for custom inputs (see React-Select)
    const [isClearable, setIsClearable] = useState(true);
    const [isSearchable, setIsSearchable] = useState(true);
    const [isDisabled, setIsDisabled] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [isRtl, setIsRtl] = useState(false);

    //location
    const [origin, setOrigin] = useState('Singapore');
    const [destination, setDestination] = useState(null)

    //dates
    const [departureDate, setDepartureDate] = useState(new Date());
    const [returnDate, setReturnDate] = useState(new Date());

    //dates
    const [pax, setPax] = useState(0);
    const [seatClass, setSeatClass] = useState(null);

    //tripway
    const handleTripwayChange = (event) => {
        setTripway(event.target.value);
    };
    const [tripway, setTripway] = useState("roundtrip");

    const [searchParams, setSearchParams] = useSearchParams();
    const navigate = useNavigate();

    const fetchFlights = (event) => {
        console.log(departureDate)
        event.preventDefault()
        //calls Util API, pass (route, port, body)
        const payload = {
            "origin": origin.value,
            "destination": destination.value,
            "departureDate": departureDate,
            "returnDate": returnDate,
            "pax": pax.value,
            "seatClass": seatClass.value,
            "tripType": tripway 
        }
        console.log(payload)
        try{
        const data = fetchData(`flight_search`, 5001,  {
            method: 'POST',
            body: payload
        })
        console.log(data)
        }catch (error) {
            console.error("An error occurred while fetching data:", error);
            // Handle the error appropriately (e.g., display error message, retry)
        }
        // setSearchParams({ name: 'Alice', age: 30 });
        // navigate('/selection'); 
    }


    return (
        <div className="flight-search-container">
            <div className="flight-search-header">
                <h2>Find your Flight</h2>
            </div>
            <form onSubmit={fetchFlights}>
                <div className="flight-search-inputs">
                    <div className="flight-search-input">
                        <Select options={flightDataOptions.locations}
                            className="origin custom-input"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            name="color"
                            placeholder="From..."
                            value = {origin}
                            onChange = {setOrigin} />
                        <img src={arrow}></img>
                        <Select options={flightDataOptions.locations}
                            className="destination custom-input"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            name="color"
                            placeholder="To..."
                            value = {destination}
                            onChange = {setDestination} />
                    </div>
                    <div className="flight-search-input">
                        <DatePicker className="custom-input" value={departureDate} onChange={setDepartureDate} />
                        <DatePicker className="custom-input" value={returnDate} onChange={setReturnDate} />
                    </div>
                    <div className="flight-search-input">
                        <Select options={flightDataOptions.classes}
                            className="class custom-input"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            name="color"
                            placeholder="Class..."
                            value = {seatClass}
                            onChange = {setSeatClass} />
                        <Select options={flightDataOptions.pax}
                            className="passengers custom-input"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            name="color"
                            placeholder="Pax..."
                            value = {pax}
                            onChange = {setPax} />
                    </div>
                </div>

                <div className="flight-search-submit">
                    <div className="flight-search-radio">
                        <label>
                            <input type="radio" name="trip-type" value="oneway" checked={tripway === 'oneway'} onChange={handleTripwayChange}></input>
                            ONE WAY
                        </label>
                        <label>
                            <input type="radio" name="trip-type" value="roundtrip" checked={tripway === 'roundtrip'} onChange={handleTripwayChange}></input>
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