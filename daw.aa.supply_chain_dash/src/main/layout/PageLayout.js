import React from "react";
import { useRoutes } from "react-router-dom";

import { Box } from "@mui/material";

import TimeoutLoader from "../shared-components/TimeoutLoader";
import PageNavBar from "./PageNavBar";

function PageLayout({ routes }) {
  const routingElement = useRoutes(routes);

  return (
    <Box
      sx={{
        position: "absolute",
        width: "100%",
        height: "100%",
        overflow: "hidden",
        display: "flex",
        flexDirection: "column",
        overscrollBehavior: "none",
      }}
    >
      <PageNavBar />
      <Box
        sx={{
          flexGrow: 1,
          paddingTop: 0,
          marginLeft: 0,
          display: "flex",
          flexDirection: "column",
          overflow: "hidden",
        }}
      >
        <React.Suspense fallback={<TimeoutLoader />}>
          {routingElement}
        </React.Suspense>
      </Box>
    </Box>
  );
}

export default PageLayout;
