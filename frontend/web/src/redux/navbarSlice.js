import { createSlice } from '@reduxjs/toolkit';

export const navbarSlice = createSlice({
    name: 'navbar',
    initialState: {
        value: ''
    },
    reducers: {
        login: (state, email) => {
            state.value = email;
        },
        logout: (state) => {
            state.value = 'hi';
        }
    }
})

export const { login, logout } = navbarSlice.actions;

export default navbarSlice.reducer;