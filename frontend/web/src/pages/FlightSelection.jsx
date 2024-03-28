import { React, useState }from 'react';
import FlightOption from '../components/FlightOption';
import { useNavigate } from 'react-router-dom';
import arrow from '../assets/images/down-arrow.svg'
import fetchData from '../utils/apiUtils';

function FlightSelection() {
  const flightDataString = localStorage.getItem('flightData');
  const flightData = JSON.parse(flightDataString);

  const departOptions = flightData[0]
  const departDestination = departOptions[0]["destination"]
  const departOrigin = departOptions[0]["origin"]
  const returnOptions = flightData[1]

  const navigate = useNavigate()

  const handleDepartSelection = (selectedOption) => {
    setDepartSummary(selectedOption["flightSummary"]);
    setDepartSelection(selectedOption["flightDetails"]);
  };
  const handleReturnSelection = (selectedOption) => {
    setReturnSummary(selectedOption["flightSummary"]);
    setReturnSelection(selectedOption["flightDetails"]);
  };

  const handleContinue = async() => {
    const selections = [departSelection, returnSelection]
    localStorage.setItem('flightSelection', JSON.stringify(selections));
    const departFlightId = selections[0]['seating_id']
    const returnFlightId = selections[1]['seating_id']
    const payload = {
      "departId": departFlightId ,
      "returnId": returnFlightId 
    }
    // fetch seating plan and store in local storage
    const seating_plan = await fetchData(`flight_search/seating`, 5001,  {
      method: 'POST',
      body: payload
    })

    localStorage.setItem('flightSelectionSeats', JSON.stringify(seating_plan))

    navigate("/passenger")

  }

  const [departSummary, setDepartSummary] = useState("No selection")
  const [returnSummary, setReturnSummary] = useState("No selection")

  const [departSelection, setDepartSelection] = useState()
  const [returnSelection, setReturnSelection] = useState()

  return (
    <div className="selection-page">
      <div className="selection-flight-selected">
        <div className="selection-flight-depart">
          <p>Departure:</p>
          <div className="selection-depart-option selection-option">
            <p>{departSummary}</p>
          </div>
        </div>
        <div className="selection-flight-return">
          <p>Return:</p>
          <div className="selection-return-option selection-option">
              <p>{returnSummary}</p>
          </div>
        </div>
        <div className="selection-flight-submit">
          <button onClick={handleContinue}>Continue</button>
        </div>
        <div className="selection-flight-expand">
          <img src={arrow}></img>
        </div>
      </div>
      <div className="selection-flight-options">
        <h2>{departOrigin} to {departDestination}</h2>
        {departOptions.map((option, index) => (
          <FlightOption key={index} options={option} onSelect={handleDepartSelection}/>
        ))}
        <h2>{departDestination} to {departOrigin}</h2>
        {returnOptions.map((option, index) => (
          <FlightOption key={index} options={option} onSelect={handleReturnSelection}/>
        ))}
      </div>
    </div>
  );
}


export default FlightSelection;