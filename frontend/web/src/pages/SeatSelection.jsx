import { React, useState } from 'react';
import Plane from '../components/Plane';
import { useNavigate } from 'react-router-dom';

function SeatSelection() {
  //fetch seats from local
  const seat_plan = JSON.parse(localStorage.getItem("flightSelectionSeats"))
  const planes = []
  const [planeIndex, setPlaneIndex] = useState(0)
  const [buttonText, setButtonText] = useState("Next Flight")
  const navigate = useNavigate()

  for (let key in seat_plan) {
    const plan = seat_plan[key]
    planes.push(<Plane content={plan}/>)
  }

  console.log(planes)
  const nextPage = () => {
    if (planeIndex < planes.length - 1 ) {
      setPlaneIndex(planeIndex + 1)
      if (planeIndex == planes.length - 2){
        setButtonText("Continue")
      }
      else {
        setButtonText("Next Flight")
      }
    }
    else {
      navigate("/payment")
    }
  }

  return (
    <div className = "plane-seat-selection">
        <div className='plane-seat-header'>
            <h2>Seat Selection</h2>
            <button type="submit" onClick={nextPage}>{buttonText}</button>
        </div>
        <div className= "plane-container">
          {planes[planeIndex]}
        </div>
    </div>
  )
}



export default SeatSelection;