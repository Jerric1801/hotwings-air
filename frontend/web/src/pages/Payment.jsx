import React, { useState } from 'react';
import LoyaltyPointsSlider from '../components/LoyaltyPointsSlider';
import Choose_Payment from '../components/Choose_Payment';
import MakePaymentButton from '../components/Make_Payment_Button';

function Payment() {
  const [loyaltyPoints, setLoyaltyPoints] = useState(0);
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState('Credit Card');
  const basePrice = 1290;

  const handleLoyaltyPointsChange = (value) => {
    setLoyaltyPoints(value);
  };

  const handlePaymentMethodChange = (method) => {
    setSelectedPaymentMethod(method);
  };

  const calculateTotal = () => {
    let totalPrice = basePrice - loyaltyPoints*0.1; 
    return totalPrice.toFixed(2); // Format total price to 2 decimal places
  };

  return (
    <div className='Booking_page'>
      <div className='Booking_Title'>
        <h1>Review your Booking</h1>
      </div>
      <div className='Itinerary_total'>
        <div className='Itinerary_word'>
          <h2>Itinerary</h2>
        </div>
        <div className='Price'>
          <h2>Total: ${basePrice}</h2>
        </div>
      </div>
      <div className='Payment_method'>
        <h1>Select Payment Method</h1>
      </div>
      <div className='Loyalty_Points_Slider'>
        <LoyaltyPointsSlider onChange={handleLoyaltyPointsChange} />
      </div>
      <div className='Payment_Option'>
        <Choose_Payment onMethodChange={handlePaymentMethodChange} />
      </div>
      <div className='Total_After_Deduction'>
        <div className='Total_After_Deduction_Title'>
          <h2>Total to be paid now</h2>
        </div>
        <div className='Total_After_Deduction_Price'>
          <h2>Total: ${calculateTotal()}</h2>
        </div>
      </div>
      <div className='Make_payment_button'>
        <MakePaymentButton />
      </div>
    </div>
  );
}

export default Payment;