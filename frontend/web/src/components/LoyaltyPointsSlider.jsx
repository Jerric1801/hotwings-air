import React, { useState } from 'react';
function LoyaltyPointsSlider({ onChange }) {
  const [value, setValue] = useState(0); 

  const handleChange = (event) => {
    const newValue = parseInt(event.target.value);
    setValue(newValue);
    onChange(newValue); 
  };

  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', borderRadius: '5px' }}>
      <h2 style={{ textAlign: 'center', marginBottom: '10px' }}>Loyalty Points</h2>
      <input
        type="range"
        min="0"
        max="10000"
        value={value}
        onChange={handleChange}
        style={{ width: '100%' }}
      />
      <p>Value: {value}</p>
    </div>
  );
}

export default LoyaltyPointsSlider;