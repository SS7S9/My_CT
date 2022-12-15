import React, { useEffect } from "react";
import { useNavigate, useLocation, useSearchParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import Stack from "@mui/material/Stack";
import CircularProgress from "@mui/material/CircularProgress";

import TaskAltIcon from "@mui/icons-material/TaskAlt";
import ErrorIcon from "@mui/icons-material/Error";

import { cleanupData, getProductDetails } from "../store/detailSlice";

export default function ValidatorModal(props) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const location = useLocation();
  const [searchParams] = useSearchParams();

  const { status, details, error } = useSelector((state) => state.details);
  const uid = searchParams.has("uid") && searchParams.get("uid");

  useEffect(() => {
    if (!status && uid) {
      dispatch(getProductDetails(uid));
      return () => dispatch(cleanupData());
    }
    return null;
  }, [status, uid, dispatch]);

  const loading = status === "PENDING";
  const invalid =
    location.pathname.startsWith("/invalid") ||
    (status === "FULFILLED" && !details);
  const valid = !!uid && status === "FULFILLED" && !!details;
  const failed = status === "REJECTED" || (!loading && !invalid && !valid);

  return (
    <Modal
      open={
        location.pathname.startsWith("/valid") ||
        location.pathname.startsWith("/invalid")
      }
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
          height: "min-content",
          background: "rgba(0, 0, 0, 0.7)",
          p: 3,
          transition: ".5s ease",
          textAlign: "center",
        }}
      >
        {invalid && (
          <Box>
            <ErrorIcon
              color="error"
              sx={{
                height: "100px",
                width: "100px",
              }}
            />
            <Typography variant="h4" noWrap color="primary">
              Potentially fake
            </Typography>
            <Typography variant="subtitle1" color="primary">
              This may not be an authentic product
            </Typography>
          </Box>
        )}
        {valid && (
          <Box>
            <TaskAltIcon
              color="success"
              sx={{
                height: "100px",
                width: "100px",
              }}
            />
            <Typography variant="h4" noWrap color="primary">
              Authentic Product
            </Typography>
            <Typography variant="subtitle1" color="primary">
              This is an authentic Lowdina Orchard product
            </Typography>
          </Box>
        )}
        {failed && (
          <Box>
            <ErrorIcon
              color="error"
              sx={{
                height: "100px",
                width: "100px",
              }}
            />
            <Typography variant="h4" noWrap color="primary">
              Failed to Verify
            </Typography>
            <Typography variant="subtitle1" color="primary" sx={{ p: 1 }}>
              Sorry, an error occured while we were trying to validate your
              product.
            </Typography>
            <Typography
              variant="subtitle1"
              sx={{ pt: 2, fontSize: ".7em" }}
              color="primary"
            >
              Error details: {error || (!uid && "No UID specified")}
            </Typography>
          </Box>
        )}
        {loading && (
          <Box>
            <Stack
              direction="row"
              spacing={2}
              sx={{
                marginLeft: { sx: 0, md: "auto" },
                marginRight: "auto",
                width: "min-content",
                p: 1,
              }}
            >
              <CircularProgress color="secondary" />
              <Typography variant="h4" noWrap color="primary">
                Checking product
              </Typography>
            </Stack>
            <Typography variant="subtitle1" color="primary" sx={{ p: 1 }}>
              Please wait a moment, we are checking your product...
            </Typography>
          </Box>
        )}
      </Box>
    </Modal>
  );
}
