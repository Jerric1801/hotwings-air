import { useState } from "react";

const CREATE_USER_API = 'http://localhost:8080/user/login';

function Login() {

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
            console.log(data);
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