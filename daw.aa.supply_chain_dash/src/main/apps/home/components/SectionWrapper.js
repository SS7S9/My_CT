import React from "react";

import Box from "@mui/material/Box";

export default function SectionWrapper(props) {
  return (
    <Box
      sx={{
        width: "100%",
        height: "calc(100% - 122px)", // A bit hackish, but have run out of time to fix properly
        display: "flex",
        flexDirection: "column",
        overflow: "auto",
      }}
    >
      {props.children}
    </Box>
  );
}
