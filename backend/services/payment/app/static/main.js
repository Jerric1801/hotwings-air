console.log("Sanity check!");

// Get Stripe publishable key
fetch("/config")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  // new
  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    const paymentData = {
      "total_price": 90000,
      "seat_number": "12A",
      "flight_id": "FL123",
      "loyalty_points": 600,
      "user_id": "user123",
      "user_email": "user@example.com"
    };
    // Get Checkout Session ID
    fetch("/payment/stripe", {
      method: "POST", // Specify the method
      headers: {
        "Content-Type": "application/json" // Specify the content type as JSON
      },
      body: JSON.stringify(paymentData) // Convert the JavaScript object to a JSON string
    })
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
})