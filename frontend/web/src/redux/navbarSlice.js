import { createSlice } from "@reduxjs/toolkit";

const navbarSlice = createSlice({
    name: 'navbar',
    initialState: {
        value: '',
        login: false,
    },
    reducers: {
        login: (state, email) => {
            state.value = email;
            state.login = true;
        },
        logout: state => {
            state.value = '';
            state.login = false;
        }
    }
})

export const { login, logout } = navbarSlice.actions;

export default navbarSlice;