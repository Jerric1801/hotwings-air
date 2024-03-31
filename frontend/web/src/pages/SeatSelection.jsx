import { React, useState } from 'react';
import Plane from '../components/Plane';
import { useNavigate } from 'react-router-dom';

function SeatSelection() {
  //fetch seats from local
  const seat_plan = JSON.parse(localStorage.getItem("flightSelectionSeats"))
  const planes = []
  const [seatSelections, setSeatSelections] = useState({});
  let selected_seats = []
  const [planeIndex, setPlaneIndex] = useState(0)
  const [buttonText, setButtonText] = useState("Next Flight")
  const navigate = useNavigate()

  const handleSeatChange = (newSelectedSeats) => {
    selected_seats = newSelectedSeats;
  };

  for (let key in seat_plan) {
    const plan = seat_plan[key]
    planes.push(<Plane content={plan} handleSeatChange={handleSeatChange} />)
  }

  const nextPage = () => {
    if (planeIndex < planes.length - 1 ) {
      console.log(selected_seats)
      setSeatSelections( 
        ({depart: selected_seats})
      );
      console.log(seatSelections)
      setButtonText("Payment")
      setPlaneIndex(planeIndex + 1)
    }
    else {
      setSeatSelections(prevSelections => ({ 
        ...prevSelections, 

        return: selected_seats   
      }));
      console.log(seatSelections)
      // localStorage.setItem(JSON.stringify(seatSelections), "selectedSeats")
      // navigate("/payment")
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