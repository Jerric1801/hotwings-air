import React from "react"
import { useLocation } from 'react-router-dom';

function Success() {
    const location = useLocation();
    const dispatchCompleted = location.state?.dispatchCompleted;
  
    return (
        <div>
        {dispatchCompleted ? (
          <h1>Payment and Booking Successful!</h1>
        ) : (
          // This should not happen under normal circumstances
          <p>Something went wrong...</p> 
        )}
      </div>
    );
  }
export default Success