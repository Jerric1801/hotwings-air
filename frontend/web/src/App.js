import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import FlightSelection from './pages/FlightSelection';
import SignUp from './pages/SignUp';
import Login from './pages/Login';

function App() {
  // Global state variables are handled here

  return (
    <BrowserRouter>
      <Navbar />
      <Routes> 
        <Route path="/" element={<HomePage/>} />
        <Route path="/selection" element={<FlightSelection/>} />
        <Route path="/signup" element={<SignUp/>} />
        <Route path="/login" element={<Login/>} />
      </Routes>   
    </BrowserRouter>
  );
}

export default App;