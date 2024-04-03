import { React, useState } from 'react';
import Plane from '../components/Plane';
import { useNavigate } from 'react-router-dom';

function SeatSelection() {
  localStorage.setItem("paymentSuccess", false)
  //fetch seats from local
  const seat_plan = JSON.parse(localStorage.getItem("flightSelectionSeats"))
  const planes = []
  const [seatSelections, setSeatSelections] = useState({});
  let selected_seats = []
  let depart_seats = []
  let return_seats = []
  const [planeIndex, setPlaneIndex] = useState(0)
  const [buttonText, setButtonText] = useState("Next Flight")

  const navigate = useNavigate()

  const nextPage = () => {
    console.log(planeIndex)
    if (planeIndex == 0) {
      depart_seats = selected_seats
      setSeatSelections(prevSelections => ({
        ...prevSelections,
        "depart": depart_seats
      }));

      setButtonText("Continue");
      setPlaneIndex(planeIndex + 1);
    }
    else if (planeIndex != 0) {
      return_seats = selected_seats
      setSeatSelections(prevSelections => ({
        ...prevSelections,
        "return": return_seats
      }));
      setButtonText("Payment");
      if (planeIndex == 2){
        console.log(seatSelections)
        localStorage.setItem("selectedSeats", JSON.stringify(seatSelections))
        navigate("/payment")
      }
      setPlaneIndex(planeIndex + 1);
    }
  }


  const handleSeatChange = (newSelectedSeats) => {
    selected_seats = newSelectedSeats;
  };


  for (let key in seat_plan) {
    const plan = seat_plan[key]
    planes.push(<Plane content={plan} handleSeatChange={handleSeatChange} />)
  }

  return (
    <div className="plane-seat-selection">
      <div className='plane-seat-header'>
        <h2>Seat Selection</h2>
        <button type="submit" onClick={nextPage}>{buttonText}</button>
      </div>
      <div className="plane-container">
        {planes[planeIndex]}
      </div>
    </div>
  )
}



export default SeatSelection;