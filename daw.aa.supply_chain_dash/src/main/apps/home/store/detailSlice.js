import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

export const getProductDetails = createAsyncThunk(
  "landing/details/getProductDetails",
  async (uid) => {
    const response = await axios.get(`/api/details/${uid}`);
    const data = await response.data;
    return data;
  }
);

export const detailsSlice = createSlice({
  name: "landing/details",
  initialState: {},
  reducers: {
    cleanupData: {
      reducer: (state, action) => {
        state = {};
      },
    },
  },
  extraReducers: {
    [getProductDetails.pending]: (state, action) => {
      state.status = "PENDING";
    },
    [getProductDetails.fulfilled]: (state, action) => {
      state.status = "FULFILLED";
      state.details = action.payload;
    },
    [getProductDetails.rejected]: (state, action) => {
      state.status = "REJECTED";
      state.error = action.error.message;
    },
  },
});

export const { cleanupData } = detailsSlice.actions;
export default detailsSlice.reducer;
