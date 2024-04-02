import React, { useState } from 'react';
import LoyaltyPointsSlider from '../components/LoyaltyPointsSlider';
import Choose_Payment from '../components/Choose_Payment';
import fetchData from '../utils/apiUtils';
import { useSearchParams, useNavigate } from 'react-router-dom';

function Payment() {
  //get seat selections 
  const seatString = localStorage.getItem('selectedSeats')
  const seats = JSON.parse(seatString)
  //get flight selections
  const selectionsString = localStorage.getItem('flightSelection');
  const selections = JSON.parse(selectionsString)
  //get passenger selections
  const passengerString = localStorage.getItem('passengerDetails')
  const passengers = JSON.parse(passengerString)

  const navigate = useNavigate()

  let basePrice = 0
  let totalPrice = 0

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

  //fetch loyalty points for user

  const [loyaltyPoints, setLoyaltyPoints] = useState(0);
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState('Credit Card');

  const handleLoyaltyPointsChange = (value) => {
    setLoyaltyPoints(value);
  };

  const handlePaymentMethodChange = (method) => {
    setSelectedPaymentMethod(method);
  };

  const calculateTotal = () => {
    totalPrice = basePrice - loyaltyPoints * 0.1;
    return totalPrice.toFixed(2); // Format total price to 2 decimal places
  };

  const deconstruct_flight = (payload, flight, type) => {
    console.log(flight)
    payload[`${type}_id`] = flight["id"]
    payload[`${type}_origin`] = flight["origin"]
    payload[`${type}_destination`] = flight["destination"]
    payload[`${type}_departure_time`] = flight["departure"]
    payload[`${type}_arrival_time`] = flight["arrival"]
    payload[`${type}_seat_id`] = flight["seating_id"]
    payload[`${type}_flight_number`] = flight["flight_number"]
    return payload
  }

  const handlePayment = async() => {
  
    const payment_url = await fetchData("payment/stripe", 5004, {
      method: 'POST',
      body: {"flight_number": "Hotwings Air", 
              "total_price":totalPrice,
              "loyalty_points":loyaltyPoints}
    })
    console.log(payment_url)
    window.location.href = payment_url
  }


  const dispatchPayload = async() => {

    let payload = {}
    const first_flight = selections[0]
    const first_seat = seats["depart"]
    payload["depart_seats"] = first_seat
    payload = deconstruct_flight(payload, first_flight, "depart")
    if (selections[1]){
      const second_flight = selections[1]
      deconstruct_flight(payload, second_flight, "return")
      const second_seat = seats["return"]
      payload["return_seats"] = second_seat
    }
    payload["loyalty_points"] = loyaltyPoints
    payload["base_price"] = basePrice
    payload["total_price"] = totalPrice

    payload["other_passengers"] = []

    for (let key in passengers) {
      //identify booker
      const details = passengers[key]
      if (key == 0){
        payload["user_email"] = details["email"]
        payload["user_gender"] = details["gender"]
        payload["user_first"] = details["firstName"]
        payload["user_last"] = details["lastName"]
        payload["user_phone"] = details["phone"]
      }
      else {
        payload["other_passengers"].push(details)
      }
    }
    console.log(payload)
    const response = await fetchData("payment", 5004, {
      method: 'POST',
      body: payload
    })
    console.log(response)
    if(response.status = 200) {
      navigate("Success")
    }
  }


  const [searchParams] = useSearchParams();
  const paymentStatus = searchParams.get('status');
  //check return link
  if (paymentStatus === 'success') {
      // Handle different statuses
      dispatchPayload()
  } else if (paymentStatus === 'canceled'){
    return (<h1>Payment Canceled</h1>)
  }

  return (
    <div className='booking-page'>
      <div className='booking-container'>

        <div className='itinerary-breakdown'>
          <h1>Itinerary</h1>
            {itineraryDetails.map((flightDetail) => (
              <div key={flightDetail.direction} className='itinerary-details'> 
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