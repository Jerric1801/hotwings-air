import { configureStore } from '@reduxjs/toolkit';
import navbarReducer from './navbarSlice';

export default configureStore({
  reducer: {
    navbar: navbarReducer
  },
})