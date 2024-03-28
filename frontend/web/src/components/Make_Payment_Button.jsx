import React, { useState } from 'react';
function MakePaymentButton() {
    const handlePayment = () => {
      // Add your payment logic here
      console.log('Payment logic goes here');
    };
  
    return (
      <button onClick={handlePayment}>Make Payment</button>
    );
  }
  
  export default MakePaymentButton;


