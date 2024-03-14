import { React, useState } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { login } from '../redux/navbarSlice';
import { useNavigate } from "react-router-dom";

const CREATE_USER_API = 'http://localhost:8080/user/login';

function Login() {

    const user = useSelector((state) => state.navbar.value);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const user = {email, password};
        fetch(CREATE_USER_API, {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify(user)
        }).then((res) => {
            return res.json();
        }).then((data) => {
            if (data.status) {
                dispatch(login(email));
                navigate("/");
            };
        })
    }
 
    return (
        <>
            <div className="login-page">
                <form action="post">
                    <div>
                        <label htmlFor="email">Email:</label>
                        <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                    </div>

                    <div>
                        <label htmlFor="password">Password:</label>
                        <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                    </div>

                    <div>
                        <button type="submit" onClick={handleSubmit}>Login</button>
                    </div>
                </form>
            </div>
        </>
    )
}
export default Login;