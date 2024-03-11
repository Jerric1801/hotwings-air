import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/images/brand/logo.svg'
import Button from './Button';

function Navbar() {

  return (
    <nav>
        <img src = {logo} alt = ""></img>
        <ul>
            <li>
                <Link to="/">Flights</Link>
            </li>
            <li>
                <Link to="/">Bookings</Link>
            </li>
            <li>
                <Link to="/">Destinations</Link>
            </li>
        </ul>
        <ul>
            <li>
                <Link to="/signup">
                    <Button>Sign up yo</Button>
                </Link>
            </li>
            <li>
                <Link to="/">Login</Link>
            </li>
        </ul>
    </nav>
  );
}

export default Navbar;