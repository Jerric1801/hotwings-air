function SignUp() {
    return (
        <>
            <div className="sign-up-page">
                <form action="post">
                    <div>
                        <label htmlFor="name">Name:</label>
                        <input type="text" id="name" />
                    </div>

                    <div>
                        <label htmlFor="email">Email:</label>
                        <input type="email" id="email" />
                    </div>

                    <div>
                        <label htmlFor="password">Password:</label>
                        <input type="password" id="password" />
                    </div>
                </form>
            </div>
        </>
    )
}
export default SignUp;