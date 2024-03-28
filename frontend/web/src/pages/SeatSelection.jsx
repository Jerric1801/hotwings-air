import { React, useState } from 'react';
import Plane from '../components/Plane';

function SeatSelection() {
  //fetch seats from local
  const seat_plan = JSON.parse(localStorage.getItem("flightSelectionSeats"))
  const planes = []
  const [planeIndex, setPlaneIndex] = useState(0)

  for (let key in seat_plan) {
    const plan = seat_plan[key]
    planes.push(<Plane content={plan}/>)
  }

  console.log(planes)
  const handleSubmit = () => {
    setPlaneIndex(1)
  }

  return (
    <div className = "plane-seat-selection">
        <div className='plane-seat-header'>
            <h2>Seat Selection</h2>
            <button type="submit" onClick={handleSubmit}>Next Flight</button>
        </div>
        <div className= "plane-container">
          {planes[planeIndex]}
        </div>
    </div>
  )
}



export default SeatSelection;