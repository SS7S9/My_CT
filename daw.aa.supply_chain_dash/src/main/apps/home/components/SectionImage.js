import React from "react";

import Box from "@mui/material/Box";

export default function SectionComponent(props) {
  return (
    <Box
      sx={{
        maxWidth: "600px",
        width: "100%",
        mr: "auto",
        ml: "auto",
        p: { xs: 0, md: 1 },
      }}
    >
      <img src={props.src} alt={props.alt} width="100%" />
    </Box>
  );
}
