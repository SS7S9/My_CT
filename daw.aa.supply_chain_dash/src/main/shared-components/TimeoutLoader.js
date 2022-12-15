import React, { useState, useEffect } from "react";

import LinearProgress from "@mui/material/LinearProgress";
import Typography from "@mui/material/Typography";

function TimeoutLoader({ timeout, loadingMesage, failedMessage }) {
  const [hasTimedOut, setHasTimedOut] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setHasTimedOut(true);
    }, timeout || 10000);
    return () => clearTimeout(timer);
  }, [timeout]);

  return (
    <div className="flex flex-1 flex-col items-center justify-center p-12">
      {(!hasTimedOut && (
        <>
          <Typography className="text-20 mb-16" color="textSecondary">
            {loadingMesage || "Loading..."}
          </Typography>
          <LinearProgress className="w-xs max-w-full" color="secondary" />
        </>
      )) || (
        <Typography className="text-20 mb-16" color="textSecondary">
          {failedMessage || "Failed to load page."}
        </Typography>
      )}
    </div>
  );
}

export default TimeoutLoader;
