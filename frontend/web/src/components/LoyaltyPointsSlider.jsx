import React, { useState } from 'react';
function LoyaltyPointsSlider({ onChange }) {
  const [value, setValue] = useState(0); 

  const handleChange = (event) => {
    const newValue = parseInt(event.target.value);
    setValue(newValue);
    onChange(newValue); 
  };

  return (
    <div className='payment-slider'>
      <h3>Loyalty Points</h3>
      <input
        type="range"
        min="0"
        max="1000"
        value={value}
        onChange={handleChange}
      />
      <p>Points: {value}</p>
    </div>
  );
}

export default LoyaltyPointsSlider;