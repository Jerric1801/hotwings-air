import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/images/brand/logo.svg'
import Button from './Button';
import { useSelector, useDispatch } from 'react-redux';
import { logout } from '../redux/navbarSlice';

function Navbar() {

    const user = useSelector((state) => state.navbar);
    const dispatch = useDispatch();
    const GET_USER_API = `http://localhost:8080/user/${user.value.payload}`;

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
        </ul>
        <ul className={displayName ? 'loggedIn' : ''}>
            <li>
                <Link to="/signup">
                    <Button>Sign up</Button>
                </Link>
            </li>
            <li>
                <Link to="/login">
                    <Button>Login</Button>
                </Link>
            </li>
        </ul>
        <ul className={displayName ? '' : 'loggedIn'}>
            <li>
                {displayName}
            </li>
            <li onClick={call_logout}>
                <Button>Logout</Button>
            </li>
        </ul>
    </nav>
  );
}

export default Navbar;