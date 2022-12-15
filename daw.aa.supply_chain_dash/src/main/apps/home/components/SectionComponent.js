import React from "react";

import useMediaQuery from "@mui/material/useMediaQuery";

import Box from "@mui/material/Box";
import SectionContent from "./SectionContent";
import SectionImage from "./SectionImage";

export default function SectionComponent(props) {
  const smallScreen = useMediaQuery((theme) => theme.breakpoints.down("sm"));

  const childComponents = React.Children.toArray(props.children);
  const content = childComponents.find((c) => c.type === SectionContent);
  const image = childComponents.find((c) => c.type === SectionImage);

  return (
    <Box
      bgcolor={(props.alt && "primary.main") || "secondary.main"}
      sx={{
        width: "100%",
        display: "flex",
        flexDirection: { xs: "column", md: "row" },
      }}
    >
      {(props.alt && !smallScreen && (
        <>
          {content}
          {image}
        </>
      )) || (
        <>
          {image}
          {content}
        </>
      )}
    </Box>
  );
}
