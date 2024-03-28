import {React, useState} from 'react';

function Seat(props) {
    const details = props["seat_details"]
    const seat_number = details["seat_number"]
    const planeType = props["type"]
    let seatClass = false

    if (planeType === 'large') {
        seatClass = true
    }

    console.log(seatClass)
    return (
        <li className={`seat ${seatClass? "seat-large" : ""}`}>
            <input type="checkbox" id={seat_number} />
            <label htmlFor={seat_number}>{seat_number}</label>
        </li>
    )
}

export default Seat