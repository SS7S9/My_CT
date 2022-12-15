import React from "react";
import { useNavigate, useLocation } from "react-router-dom";

import useMediaQuery from "@mui/material/useMediaQuery";

import Box from "@mui/material/Box";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import Button from "@mui/material/Button";
import Avatar from "@mui/material/Avatar";
import Fab from "@mui/material/Fab";

import MapIcon from "@mui/icons-material/Map";
import InfoIcon from "@mui/icons-material/Info";
import CallIcon from "@mui/icons-material/Call";
// import CloseIcon from "@mui/icons-material/Close";
import HomeIcon from "@mui/icons-material/Home";

export default function PageNavBar() {
  const navigate = useNavigate();
  const location = useLocation();
  const smallScreen = useMediaQuery((theme) => theme.breakpoints.down("sm"));

  return (
    <>
      <AppBar position="static" sx={{ overscrollBehavior: "none" }}>
        <Toolbar sx={{ height: "min-content" }} disableGutters>
          <Box
            sx={{
              width: "100%",
              height: "min-content",
              display: "flex",
              flexDirection: { xs: "column", md: "row" },
              overflow: "hidden",
            }}
          >
            <Box
              sx={{
                width: "100%",
                height: "100%",
                display: "flex",
                flexDirection: "row",
              }}
            >
              <Avatar
                alt="Lowdina Orchard"
                src="/assets/images/264853133_4584177905032426_4674773930942450269_n.jpg"
                sx={{ width: "90px", height: "90px", m: 2 }}
              />
              <Box
                sx={{
                  width: "100%",
                  height: "min-content",
                  display: "flex",
                  flexDirection: "column",
                  mt: "auto",
                  mb: "auto",
                }}
              >
                <Typography
                  variant={(smallScreen && "h5") || "h4"}
                  component="div"
                  color="secondary"
                  sx={{
                    flexGrow: 1,
                    height: "min-content",
                  }}
                  noWrap
                >
                  Lowdina Orchard
                </Typography>
                <Typography
                  variant="subtitle"
                  component="div"
                  sx={{
                    flexGrow: 1,
                    height: "min-content",
                  }}
                >
                  Premium quality Tasmanian Cherries and Moorpark Apricots
                </Typography>
              </Box>
            </Box>
            <Stack
              direction="row"
              spacing={1}
              sx={{
                width: "min-content",

                height: "min-content",
                display: { xs: "none", md: "flex" },
                mr: { xs: "auto", md: 3 },
                ml: "auto",
                mt: "auto",
                mb: { xs: 1, md: "auto" },
              }}
            >
              <Button
                variant="outlined"
                color="secondary"
                endIcon={<MapIcon />}
                onClick={() => navigate("/map")}
              >
                Map
              </Button>
              <Button
                variant="outlined"
                color="secondary"
                endIcon={<CallIcon />}
                onClick={() => navigate("/contact")}
              >
                Contact
              </Button>
            </Stack>
          </Box>
        </Toolbar>
      </AppBar>
      <Stack
        spacing={2}
        sx={{
          position: "absolute",
          display: { xs: "flex", md: "none" },
          right: 16,
          bottom: 16,
          zIndex: "snackbar",
          overscrollBehavior: "none",
        }}
      >
        {(location.pathname === "/" && (
          <>
            <Fab color="secondary" onClick={() => navigate("/map")}>
              <MapIcon />
            </Fab>
            <Fab color="secondary" onClick={() => navigate("/contact")}>
              <CallIcon />
            </Fab>
          </>
        )) || (
          <Fab color="secondary" onClick={() => navigate("/")}>
            <HomeIcon />
          </Fab>
        )}
      </Stack>
    </>
  );
}
