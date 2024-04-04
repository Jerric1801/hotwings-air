import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/images/brand/logo.svg'
import Button from './Button';
import { useSelector, useDispatch } from 'react-redux';
import { logout } from '../redux/navbarSlice';

function Navbar() {

    const user = useSelector((state) => state.navbar);
    const dispatch = useDispatch();
    const GET_USER_API = `http://localhost:5003/user/${user.value.payload}`;

    const [displayName, setDisplayName] = useState('');

    useEffect(() => {
        if (user.login == true) {
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

    function call_logout() {
        dispatch(logout);
        setDisplayName('');
        window.location.reload(true);
    }

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
            <li className={displayName ? 'loggedIn' : ''}>
                <Link to="/signup">
                    <Button>Sign Up</Button>
                </Link>
            </li>
            <li className={displayName ? 'loggedIn' : ''}>
                <Link to="/login">
                    <Button>Login</Button>
                </Link>
            </li>
            <li className={displayName ? '' : 'loggedIn'}>
                {displayName}
            </li>
            <li className={displayName ? '' : 'loggedIn'} onClick={call_logout}>
                <Link to="/">
                    <Button>Logout</Button>
                </Link>
            </li>
        </ul>
    </nav>
  );
}

export default Navbar;