import React, { useState } from 'react';
function Choose_Payment(){
  const [selectedOption, setSelectedOption] = useState('Credit Card'); 

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <h2>Payment Options</h2>
      <div>
        <div className="payment-option">
          <label className={selectedOption === 'Credit Card' ? 'selected' : ''}>
            <input
              type="radio"
              value="Credit Card"
              checked={selectedOption === 'Credit Card'}
              onChange={handleOptionChange}
            />Credit Card
            <img src={process.env.PUBLIC_URL + '/credit_card.jpg'}style={{ width: '50px', marginRight: '10px' }} />
          </label>
        </div>
        <div className="payment-option">
          <label className={selectedOption === 'PayNow' ? 'selected' : ''}>
            <input
              type="radio"
              value="PayNow"
              checked={selectedOption === 'PayNow'}
              onChange={handleOptionChange}
            />
            PayNow
            <img src={process.env.PUBLIC_URL + '/pay_now.jpg'}style={{ width: '50px', marginRight: '10px' }} />
          </label>
        </div>
        <div className="payment-option">
          <label className={selectedOption === 'bankTransfer' ? 'selected' : ''}>
            <input
              type="radio"
              value="bankTransfer"
              checked={selectedOption === 'bankTransfer'}
              onChange={handleOptionChange}
            />
            Bank Transfer
          </label>
        </div>
      </div>
    </div>
  );
}

export default Choose_Payment;
