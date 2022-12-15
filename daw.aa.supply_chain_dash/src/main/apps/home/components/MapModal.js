import React, { useRef } from "react";
import { useParams, useNavigate } from "react-router-dom";

import useMediaQuery from "@mui/material/useMediaQuery";

import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemIcon from "@mui/material/ListItemIcon";
import IconButton from "@mui/material/IconButton";

import LocationOnIcon from "@mui/icons-material/LocationOn";
import CloseIcon from "@mui/icons-material/Close";

const mapURI =
  "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5222.482136499574!2d147.42586363043236!3d-42.62630588828294!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xaa6e0359033012c3%3A0x3458f6048e873b62!2sLowdina%20Orchard!5e1!3m2!1sen!2sau!4v1642297115503!5m2!1sen!2sau";

export default function MapModal(props) {
  const { subPath } = useParams();
  const navigate = useNavigate();
  const smallRef = useRef(null);

  const smallScreen = useMediaQuery((theme) => theme.breakpoints.down("sm"));

  return (
    <Modal
      open={subPath === "map"}
      onClose={() => navigate("/")}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      {(smallScreen && (
        <Box
          sx={{
            position: "absolute",
            width: "100%",
            height: "100%",
            display: "flex",
            flexDirection: "column",
          }}
        >
          <iframe
            title="Lowdina Orchard Map"
            src={mapURI}
            style={{
              border: "0",
              width: "100%",
              height: "300px",
              flexGrow: 1,
            }}
            allowFullScreen
            loading="lazy"
          />
          <List
            sx={{
              height: "min-content",
              bgcolor: "background.paper",
              pr: "72px",
              pt: 0,
              m: 0,
            }}
          >
            <ListItem>
              <ListItemIcon>
                <LocationOnIcon />
              </ListItemIcon>
              <ListItemText
                primary="Lowdina Orchard"
                secondary="1321 Colebrook Road Campania, TAS, Australia 7026"
              />
            </ListItem>
          </List>
        </Box>
      )) || (
        <Box
          sx={{
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: "100%",
            maxWidth: "min-content",
            height: "min-content",
            bgcolor: "background.paper",
            border: "2px solid #000",
            boxShadow: 24,
            p: 5,
          }}
        >
          <Box
            sx={{
              display: { xs: "none", md: "block" },
              position: "absolute",
              right: "5px",
              top: "5px",
            }}
          >
            <IconButton onClick={() => navigate("/")}>
              <CloseIcon />
            </IconButton>
          </Box>
          <iframe
            title="Lowdina Orchard Map"
            src={mapURI}
            style={{
              width: 600,
              height: 450,
              border: "0",
              flexGrow: { xs: 1, md: 0 },
            }}
            allowFullScreen
            loading="lazy"
          />
          <List
            sx={{
              width: "100%",
              bgcolor: "background.paper",
              p: 0,
              m: 0,
              display: { xs: "none", md: "block" },
            }}
          >
            <ListItem>
              <ListItemIcon>
                <LocationOnIcon />
              </ListItemIcon>
              <ListItemText
                primary="Lowdina Orchard"
                secondary="1321 Colebrook Road Campania, TAS, Australia 7026"
              />
            </ListItem>
          </List>
        </Box>
      )}
    </Modal>
  );
}
