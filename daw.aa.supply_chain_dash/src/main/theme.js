import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#ffffff",
    },
    secondary: {
      // main: "#830000",
      main: "#570009",
    },
  },
  typography: {
    fontFamily: ['"Merriweather"', "serif"].join(","),
  },
});

export default theme;
