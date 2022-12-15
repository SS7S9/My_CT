import React from "react";

import useMediaQuery from "@mui/material/useMediaQuery";

import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";

export default function SectionContent(props) {
  const smallScreen = useMediaQuery((theme) => theme.breakpoints.down("sm"));

  return (
    <Box
      sx={{
        height: "min-content",
        flexGrow: 1,
        mt: "auto",
        mb: "auto",
        pl: { xs: 1, md: 5 },
        pr: { xs: 1, md: 5 },
        p: { xs: 3 },
      }}
    >
      <Typography
        variant="h5"
        color={(props.alt && "secondary") || "primary"}
        align={(props.alt && !smallScreen && "right") || "left"}
        sx={{
          fontSize: { xs: ".8em", md: "1.5em" },
        }}
      >
        {props.children}
      </Typography>
    </Box>
  );
}
