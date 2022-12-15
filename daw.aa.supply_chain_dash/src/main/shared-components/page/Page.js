import React from "react";
import Box from "@mui/material/Box";
import SenseTFooter from "../SenseTFooter";

export default function Page(props) {
  return (
    <Box
      className="App"
      sx={{
        position: "fixed",
        width: "100%",
        height: "100vh",
      }}
    >
      {props.children}
      <SenseTFooter />
    </Box>
  );
}
