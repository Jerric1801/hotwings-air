import {React, useState} from 'react';

function Seat(props) {
    const details = props["seat_details"]
    const seat_number = details["seat_number"]
    const isAvailable = details["available"]
    const planeType = props["type"]
    const selected_seats = props["selected_seats"]
    let seatClass = false
    

    if (planeType === 'large') {
        seatClass = true
    }

    const add_seat = (e) => {
        const seat = e.target.id
        selected_seats.push(seat)
    }

    

    return (
        <li className={`seat ${seatClass? "seat-large" : ""}`}>
            <input type="checkbox" id={seat_number} disabled={isAvailable} onChange={e => add_seat(e)}/>
            <label htmlFor={seat_number}>{seat_number}</label>
        </li>
    )
}

export default Seat