import Box from "@mui/material/Box";

export default function SenseTFooter() {
  return (
    <Box
      sx={{
        position: "absolute",
        right: 0,
        bottom: 0,
        width: "100%",
        maxWidth: "min-content",
        height: "60px",
        backgroundColor: "white",
      }}
    >
      <a href="https://www.sense-t.org.au/">
        <img
          src="assets/logos/sense-t-utas-logo-horizontal-white-bg.png"
          alt="powered by sense-t"
          height="60px"
        />
      </a>
    </Box>
  );
}
