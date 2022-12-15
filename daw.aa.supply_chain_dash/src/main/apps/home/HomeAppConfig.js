import React from "react";
import HomeApp from "./HomeApp";

const HomeAppConfig = [
  ...["/", "/:subPath", "/valid/:mac", "/invalid"].map((p) => ({
    title: "Home Page",
    path: p,
    element: <HomeApp />,
  })),
];

export default HomeAppConfig;
