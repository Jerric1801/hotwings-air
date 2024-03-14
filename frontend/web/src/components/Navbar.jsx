import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/images/brand/logo.svg'
import Button from './Button';
import { useSelector, useDispatch } from 'react-redux';

function Navbar() {

    const user = useSelector((state) => state.navbar);
    const GET_USER_API = `http://localhost:8080/user/${user.value.payload}`;

    const [displayName, setDisplayName] = useState('');

    useEffect(() => {
        if (user != undefined) {
            fetch(GET_USER_API, {
                method: 'GET',
                headers: {'Content-Type':'application/json'},
            }).then((res) => {
                return res.json();
            }).then((data) => {
                setDisplayName(data.name);
            })
        }
    })

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
        <ul className={displayName ? 'loggedIn' : ''}>
            <li>
                <Link to="/signup">
                    <Button>Sign up yo</Button>
                </Link>
            </li>
            <li>
                <Link to="/login">
                    <Button>Login yo</Button>
                </Link>
            </li>
        </ul>
        <div className={displayName ? '' : 'loggedIn'}>
            {displayName}
        </div>
    </nav>
  );
}

export default Navbar;