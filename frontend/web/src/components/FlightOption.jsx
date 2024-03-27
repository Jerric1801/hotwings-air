
function FlightOption(props) {
  const options = props.options
  const countryCode = {
    "Singapore": "SIN",
    "Kuala Lumpur": "KUL",
    "Jakarta": "JKT",
    "Manila": "MNL",
    "Dubai": "DXB",
    "Paris": "CDG", 
    "Los Angeles": "LAX",
    "Tokyo": "TYO",
    "Bangkok": "BKK",
    "Sydney": "SYD",
    "Hong Kong": "HKG",
    "London": "LHR", 
    "New York": "JFK" 
  };

  function formatPrice(price) {
    // Convert price to a number
    const numericPrice = Number(price);

    // Check if price is a valid number
    if (isNaN(numericPrice)) {
        return "Invalid Price";
    }

    // Round the price to two decimal places
    const roundedPrice = Math.round(numericPrice * 100) / 100;

    // Convert the rounded price to a string with exactly two decimal places
    const formattedPrice = roundedPrice.toFixed(2);

    return formattedPrice;
}

  const getTime = (dateStr) => {
    const dateObject = new Date(dateStr);

    const pstOffset = -7; 
    const millisecondsInHour = 60 * 60 * 1000;
    const dateObjectPST = new Date(dateObject.getTime() + pstOffset * millisecondsInHour);

    // Extract hours and minutes (adjusting to 12-hour format)
    let hours = dateObjectPST.getHours() % 12;  // % 12 for 12-hour format 
    hours = hours ? hours : 12; // Handle midnight as 12 AM
    const minutes = dateObjectPST.getMinutes().toString().padStart(2, '0'); // Pad with zero

    // Format the time
    const desiredTime = `${hours}:${minutes}`; 

    return desiredTime
  }

  const convertDate = (dateStr) => {
    const dateObj = new Date(dateStr)
    const daysOfWeek = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    const dayOfWeek = daysOfWeek[dateObj.getDay()];
  
    const formattedDate = dateObj.toLocaleDateString('en-US', {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
    })

    return`${formattedDate} (${dayOfWeek})`
  }

  const handleClick = () => { 
    const selectedData = {
      "flightSummary": departureDate.split(",")[0] + ", "+ originCode + " - " + destinationCode,
      "flightDetails": {
        "id": options["_id"]["$oid"],
        "seating_id":options["aircraft"]["seating_plan_id"]["$oid"],
        "origin": origin,
        "destination": destination,
        "price": price,
        "seatClass": seat_class,
        "departure": options["departure"]["$date"],
        "arrival": options["arrival"]["$date"],
        "pax": options["pax"]
      }
                          };  
    props.onSelect(selectedData); 
  }

  const departureDate =  convertDate(options["departure"]["$date"]);
  const arrivalDate = convertDate(options["arrival"]["$date"]);
  const origin = options["origin"]
  const destination = options["destination"]
  const originCode = `${countryCode[options["origin"]]} ${getTime(options["departure"]["$date"])}`
  const destinationCode = `${countryCode[options["destination"]]} ${getTime(options["arrival"]["$date"])}`
  const price = formatPrice(options["price"])

  const timeDifferenceMs = new Date(options["arrival"]["$date"]) - new Date(options["departure"]["$date"]);
  const hoursDifference = Math.floor(timeDifferenceMs / (1000 * 60 * 60));
  const minutesDifference = Math.floor((timeDifferenceMs % (1000 * 60 * 60)) / (1000 * 60));

  const timeDifference = `${hoursDifference}h ${minutesDifference}min`;
  const seat_class = options["seatClass"]
  
  return (
    <div className="flight-option">
      <div className="flight-option-details">
        <h1>{originCode}</h1>
        <p>{origin}</p>
        <p>{departureDate}</p>
      </div>

      <div className="flight-option-timeline">
        <div className="timeline">
          <h2>{timeDifference}</h2>
        </div>
      </div>

      <div className="flight-option-details">
        <h1>{destinationCode}</h1>
        <p>{destination}</p>
        <p>{arrivalDate}</p>
      </div>

      <div className="flight-option-book">
        <div className="flight-option-class"> 
          <button onClick={handleClick}>{seat_class}</button>
        </div>
        <div className="flight-option-price">
          <p>From SGD</p>
          <h2>{price}</h2>
        </div>
      </div>
    </div>

  );
}



export default FlightOption;

