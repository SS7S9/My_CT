import { configureStore } from "@reduxjs/toolkit";
import { reducers } from "./apps/appsConfig";

export default configureStore({
  reducer: reducers,
});
