import React, { useEffect, useState } from 'react';
import FlightSearchForm from '../components/FlightSearchForm';
// import FeaturedDestinations from '../components/FeaturedDestinations';
// import PromotionsBanner from '../components/PromotionsBanner'; // If you have any

function HomePage() {
  // Potentially a state variable for promotional offerings 
//   const [promotions, setPromotions] = useState([]);

//   // Example: Fetching promotions upon mount 
//   useEffect(() => {
//     // Simulates an asynchronous call to get promotions
//     const fetchPromotions = async () => {
//       const samplePromotions = [ /* ...data */ ]; 
//       setPromotions(samplePromotions);
//     };

//     fetchPromotions();
//   }, []); 

  const [user, setUser] = useState(null);

  

  return (
    <div className="home-page">
        <FlightSearchForm/>
    </div>
  );
}

export default HomePage;