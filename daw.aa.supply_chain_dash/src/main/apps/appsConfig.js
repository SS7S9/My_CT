import HomeAppConfig from "./home/HomeAppConfig";
import homeReducers from "./home/store";

export const routes = [...HomeAppConfig];
export const reducers = { ...homeReducers };
