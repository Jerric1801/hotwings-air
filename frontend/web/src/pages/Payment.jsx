import React, { useState } from 'react';
import LoyaltyPointsSlider from '../components/LoyaltyPointsSlider';
import Choose_Payment from '../components/Choose_Payment';

function Payment() {

  const selectionsString = localStorage.getItem('flightSelection');
  const selections = JSON.parse(selectionsString)
  let basePrice = 0

  const itineraryDetails = []

  for (let i in selections) {
    const flight = selections[i]
    const origin = flight['origin']
    const destination = flight['destination']
    const pax = flight['pax']
    const price = flight['price']
    basePrice += parseFloat(price) * parseInt(pax)
    itineraryDetails.push({
      direction: i == 0 ? "Departure" : "Return",
      trip: `${origin} --- ${destination}`,
      pax: `${pax}`,
      price: `${price}`
    });
  }

  const [loyaltyPoints, setLoyaltyPoints] = useState(0);
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState('Credit Card');

  const handleLoyaltyPointsChange = (value) => {
    setLoyaltyPoints(value);
  };

  const handlePaymentMethodChange = (method) => {
    setSelectedPaymentMethod(method);
  };

  const calculateTotal = () => {
    let totalPrice = basePrice - loyaltyPoints * 0.1;
    return totalPrice.toFixed(2); // Format total price to 2 decimal places
  };

  const handlePayment = () => {
    
  }

  return (
    <div className='booking-page'>
      <div className='booking-container'>

        <div className='itinerary-breakdown'>
          <h1>Itinerary</h1>
            {itineraryDetails.map((flightDetail) => (
              <div key={flightDetail.direction} className='itinerary-details'>  {/* Added a key */}
                <h3>{flightDetail.direction}</h3>
                <p>{flightDetail.trip}</p>
                <p>{flightDetail.pax} pax</p>
                <p>${flightDetail.price}</p>
              </div>
            ))}
          <h2>Total:  ${basePrice}</h2>
        </div>

        <div className="booking-payment">

          <h1>Select Payment Method</h1>

          <div className='payment-options'>
            <Choose_Payment onMethodChange={handlePaymentMethodChange} />
          </div>

          <div className='payment-slider-container'>
            <LoyaltyPointsSlider onChange={handleLoyaltyPointsChange} />
          </div>

          <div className='payment-checkout'>
            <h2>Subtotal: ${calculateTotal()}</h2>
            <button onClick={handlePayment}>Make Payment</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Payment;