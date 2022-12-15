import React from "react";
import { BrowserRouter } from "react-router-dom";
import { Provider } from "react-redux";
import { ThemeProvider } from "@mui/material/styles";

import * as dayjs from "dayjs";

import { routes } from "./apps/appsConfig";
import PageLayout from "./layout/PageLayout";
import theme from "./theme";
import store from "./store";

if (process.env.REACT_APP_API_URL) {
  const axios = require("axios");
  axios.defaults.baseURL = process.env.REACT_APP_API_URL;
  // axios.defaults.timeout = process.env.REACT_APP_API_TIMEOUT;
}

const localizedFormat = require("dayjs/plugin/localizedFormat");

dayjs.extend(localizedFormat);

function App() {
  return (
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <BrowserRouter>
          <PageLayout routes={routes} />
        </BrowserRouter>
      </ThemeProvider>
    </Provider>
  );
}

export default App;
