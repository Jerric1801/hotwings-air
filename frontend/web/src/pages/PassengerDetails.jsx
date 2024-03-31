import {React,useState} from 'react';
import PassengerForm from '../components/PassengerForm';
import { useNavigate } from 'react-router-dom';

function PassengerDetails() {

    const updateContent = (index, passengerData) => {
        content[index] = passengerData;
    }

    const flightSelectionString = localStorage.getItem('flightSelection');
    const flightSelection = JSON.parse(flightSelectionString);
    const pax = flightSelection[0]["pax"]
    const content = {}

    const passengerForms = []; 
    for (let i = 0; i < pax; i++) {
        passengerForms.push(<PassengerForm key = {i} index={i} updateContent={updateContent}/>); 
    }

    const navigate = useNavigate()
    const handleContinue = () => {
        // check whether fields are valid
        localStorage.setItem("passengerDetails", JSON.stringify(content))
        navigate("/seats")
    }


    return (

        <div className="passenger-details">
            <div className = "passenger-details-submit">
                <button onClick = {handleContinue}>Continue</button>
            </div>
            <div className="passenger-details-wrapper">
                {passengerForms}
            </div>
        </div>

    );
}


export default PassengerDetails;

