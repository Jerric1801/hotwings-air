import { useState } from 'react'
import Row from './Row'

function Plane(props) {
  const details = props['content']
  const num_seats = props['content'].length
  let planeClass = false
  let seats_per_row = 6

  if (num_seats > 200) {
    seats_per_row = 9
    planeClass = true
  }

  const num_rows = num_seats / seats_per_row

  const rows = []

  for (let num = 0; num < num_rows; num++) {
    let start_index = num * seats_per_row;
    let end_index = start_index + seats_per_row;
    let row_details = details.slice(start_index, end_index); 
    rows.push(<Row key={num} num_seats={seats_per_row} row_details={row_details}/>)
  }

  return (
    <div className={`plane ${planeClass ? "plane-large" : ""}`} >
      <div className="cockpit">
      </div>
      <div className="exit exit--front fuselage">

      </div>
      <ol className="cabin fuselage">
        {rows}
      </ol>
      <div className="exit exit--back fuselage">
      </div>
    </div>

  )
}

export default Plane