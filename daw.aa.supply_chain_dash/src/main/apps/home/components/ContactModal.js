import * as React from "react";
import { useParams, useNavigate } from "react-router-dom";

import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import Stack from "@mui/material/Stack";

import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemIcon from "@mui/material/ListItemIcon";
import IconButton from "@mui/material/IconButton";

import EmailIcon from "@mui/icons-material/Email";
import CallIcon from "@mui/icons-material/Call";
import LocationOnIcon from "@mui/icons-material/LocationOn";
import CloseIcon from "@mui/icons-material/Close";

export default function ContactModal(props) {
  const { subPath } = useParams();
  const navigate = useNavigate();

  return (
    <Modal
      open={subPath === "contact"}
      onClose={() => navigate("/")}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      <Box
        sx={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: "100%",
          maxWidth: 1000,
          maxHeight: "100%",
          overflow: "auto",
          bgcolor: "background.paper",
          border: "2px solid #000",
          boxShadow: 24,
          p: 4,
        }}
      >
        <Box
          sx={{
            position: "absolute",
            right: "5px",
            top: "5px",
          }}
        >
          <IconButton onClick={() => navigate("/")}>
            <CloseIcon />
          </IconButton>
        </Box>
        <Box
          sx={{
            width: "100%",
            height: "100%",
          }}
        >
          <Box
            sx={{
              width: "100%",
              height: "100%",
              display: "flex",
              flexDirection: { xs: "column", md: "row" },
            }}
          >
            <Box
              sx={{
                minWidth: { xs: "100%", md: "300px" },
                ml: { xs: "auto", md: 0 },
                mr: { xs: "auto", md: 0 },
                mt: { xs: 0, md: "auto" },
                mb: { xs: 0, md: "auto" },
                pr: { xs: 0, md: 2 },
              }}
            >
              <img
                src="/assets/images/270061901_4655511991232350_1001443903045383351_n.jpg"
                width="100%"
                alt="Cherry Sign"
              />
            </Box>

            <Stack
              direction="column"
              spacing={2}
              sx={{
                mt: "auto",
                mb: "auto",
                p: { xs: 2, md: 0 },
              }}
            >
              <Typography id="modal-modal-title" variant="h6" component="h2">
                Contact Us
              </Typography>
              <List sx={{ width: "100%", bgcolor: "background.paper" }}>
                <ListItem>
                  <ListItemIcon>
                    <CallIcon />
                  </ListItemIcon>
                  <ListItemText primary="(03) 6260 4372" />
                </ListItem>
                <ListItem>
                  <ListItemIcon>
                    <EmailIcon />
                  </ListItemIcon>
                  <ListItemText primary="leadall@bigpond.com.au" />
                </ListItem>
                <ListItem>
                  <ListItemIcon>
                    <LocationOnIcon />
                  </ListItemIcon>
                  <ListItemText primary="1321 Colebrook Road Campania, TAS, Australia 7026" />
                </ListItem>
                {/* <ListItem>
                <ListItemIcon>
                  <ImageIcon />
                </ListItemIcon>
                <ListItemText primary="Facebook" secondary="July 20, 2014" />
              </ListItem> */}
              </List>
            </Stack>
          </Box>
        </Box>
      </Box>
    </Modal>
  );
}
