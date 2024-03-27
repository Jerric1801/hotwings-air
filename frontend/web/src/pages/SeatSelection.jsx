import React, { useState } from 'react';
import Row from '../components/seating/row'

function SeatSelection() {
  return (
    <div class="plane">
      <div className='seat-title'>
        <h1>Seat Selection</h1>
      </div>
      <div class="cockpit">
      </div>
      <div class="exit exit--front fuselage">

      </div>
      <ol class="cabin fuselage">
        <Row />
        <Row />
        <Row />
        <Row />
        <Row />
        <Row />
        <Row />
        <Row />
      </ol>
      <div class="exit exit--back fuselage">
      </div>

      <div className='Submit_button'>

      </div>
    </div>

  )
}



export default SeatSelection;