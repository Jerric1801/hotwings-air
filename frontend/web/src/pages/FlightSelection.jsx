import React from 'react';
import FlightOption from '../components/FlightOption';
import { useSearchParams } from 'react-router-dom';

function FlightSelection() {
  const flightDataString = localStorage.getItem('flightData');
  const flightData = JSON.parse(flightDataString);
  console.log(flightData)

  const departOptions = flightData[0]
  const departDestination = departOptions[0]["destination"]
  const departOrigin = departOptions[0]["origin"]
  const returnOptions = flightData[1]
  
  const flightData1 = {
    countryInitials: { title: "SIN 16:40" },
    countryName: { title: "Singapore" },
    date: { title: "2024-03-15" },
  };
  
  return (
    <div className="selection-page">
      <div className="selection-flight-options">
        <h2>{departOrigin} to {departDestination}</h2>
        {departOptions.map((option, index) => (
          <FlightOption key={index} {...option} /> 
        ))}
        <h2>{departDestination} to {departOrigin}</h2>
        {returnOptions.map((option, index) => (
          <FlightOption key={index} {...option} /> 
        ))}
      </div>
    </div>
  );
}


export default FlightSelection;