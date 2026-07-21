// src/components/StatusBanner.tsx

import {
  AlertCircle,
  AlertTriangle,
  Ban,
  Clock,
  ServerCrash,
  ShieldAlert,
  WifiOff,
  X,
} from "lucide-react";


/* ============================================================
 * COMPONENT PROPERTIES
 * ============================================================
 */

interface StatusBannerProps {
  error: string;

  onDismiss?: () => void;
}


/* ============================================================
 * ERROR TYPE
 * ============================================================
 */

type ErrorType =
  | "validation"
  | "network"
  | "timeout"
  | "authentication"
  | "authorization"
  | "not-found"
  | "service"
  | "server"
  | "general";


/* ============================================================
 * ERROR CONFIGURATION
 * ============================================================
 */

interface ErrorConfiguration {
  type: ErrorType;

  title: string;

  description: string;
}


/* ============================================================
 * CLASSIFY ERROR
 * ============================================================
 */

const classifyError = (
  error: string
): ErrorConfiguration => {

  const normalized =
    error
      .toLowerCase()
      .trim();


  /* ----------------------------------------------------------
   * VALIDATION ERROR
   * ----------------------------------------------------------
   */

  if (
    normalized.includes("validation") ||
    normalized.includes("invalid monitoring request") ||
    normalized.includes("required field") ||
    normalized.includes("verify all required fields") ||
    normalized.includes("unprocessable")
  ) {

    return {
      type: "validation",

      title: "Monitoring Request Validation Failed",

      description:
        "Please review the clinical trial monitoring " +
        "data and verify all required fields.",
    };
  }


  /* ----------------------------------------------------------
   * NETWORK ERROR
   * ----------------------------------------------------------
   */

  if (
    normalized.includes("unable to connect") ||
    normalized.includes("network") ||
    normalized.includes("err_network") ||
    normalized.includes("failed to fetch")
  ) {

    return {
      type: "network",

      title: "Monitoring Service Connection Failed",

      description:
        "Unable to connect to the Clinical Trial " +
        "Monitoring API. Verify that the FastAPI " +
        "service is running.",
    };
  }


  /* ----------------------------------------------------------
   * TIMEOUT ERROR
   * ----------------------------------------------------------
   */

  if (
    normalized.includes("timeout") ||
    normalized.includes("timed out") ||
    normalized.includes("exceeded the api timeout") ||
    normalized.includes("econnaborted")
  ) {

    return {
      type: "timeout",

      title: "Monitoring Analysis Timed Out",

      description:
        "The AutoGen monitoring agents exceeded the " +
        "configured API timeout while processing the request.",
    };
  }


  /* ----------------------------------------------------------
   * AUTHENTICATION ERROR
   * ----------------------------------------------------------
   */

  if (
    normalized.includes("authentication") ||
    normalized.includes("unauthorized") ||
    normalized.includes("401")
  ) {

    return {
      type: "authentication",

      title: "Authentication Required",

      description:
        "Authentication is required to access the " +
        "Clinical Trial Monitoring service.",
    };
  }


  /* ----------------------------------------------------------
   * AUTHORIZATION ERROR
   * ----------------------------------------------------------
   */

  if (
    normalized.includes("not authorized") ||
    normalized.includes("forbidden") ||
    normalized.includes("403")
  ) {

    return {
      type: "authorization",

      title: "Monitoring Service Access Denied",

      description:
        "You do not have permission to access the " +
        "Clinical Trial Monitoring service.",
    };
  }


  /* ----------------------------------------------------------
   * NOT FOUND ERROR
   * ----------------------------------------------------------
   */

  if (
    normalized.includes("not found") ||
    normalized.includes("404")
  ) {

    return {
      type: "not-found",

      title: "Monitoring API Endpoint Not Found",

      description:
        "The requested monitoring API endpoint could " +
        "not be found. Verify the configured API prefix.",
    };
  }


  /* ----------------------------------------------------------
   * SERVICE UNAVAILABLE
   * ----------------------------------------------------------
   */

  if (
    normalized.includes("service is currently unavailable") ||
    normalized.includes("service unavailable") ||
    normalized.includes("503")
  ) {

    return {
      type: "service",

      title: "Monitoring Service Unavailable",

      description:
        "The Clinical Trial Monitoring service is " +
        "temporarily unavailable. Please try again.",
    };
  }


  /* ----------------------------------------------------------
   * INTERNAL SERVER ERROR
   * ----------------------------------------------------------
   */

  if (
    normalized.includes("internal server error") ||
    normalized.includes("server error") ||
    normalized.includes("500")
  ) {

    return {
      type: "server",

      title: "Monitoring Analysis Failed",

      description:
        "The monitoring service encountered an internal " +
        "error while executing the AutoGen agent workflow.",
    };
  }


  /* ----------------------------------------------------------
   * GENERAL ERROR
   * ----------------------------------------------------------
   */

  return {
    type: "general",

    title: "Monitoring Request Failed",

    description:
      "An unexpected error occurred while processing " +
      "the clinical trial monitoring request.",
  };
};


/* ============================================================
 * ERROR ICON
 * ============================================================
 */

const getErrorIcon = (
  type: ErrorType
) => {

  switch (type) {

    case "validation":

      return (
        <AlertCircle size={22} />
      );


    case "network":

      return (
        <WifiOff size={22} />
      );


    case "timeout":

      return (
        <Clock size={22} />
      );


    case "authentication":

      return (
        <ShieldAlert size={22} />
      );


    case "authorization":

      return (
        <Ban size={22} />
      );


    case "not-found":

      return (
        <AlertTriangle size={22} />
      );


    case "service":

      return (
        <ServerCrash size={22} />
      );


    case "server":

      return (
        <ServerCrash size={22} />
      );


    default:

      return (
        <AlertTriangle size={22} />
      );
  }
};


/* ============================================================
 * STATUS BANNER COMPONENT
 * ============================================================
 */

export default function StatusBanner({
  error,
  onDismiss,
}: StatusBannerProps) {


  /* ==========================================================
   * NO ERROR
   * ==========================================================
   */

  if (!error) {

    return null;
  }


  /* ==========================================================
   * ERROR CONFIGURATION
   * ==========================================================
   */

  const configuration =
    classifyError(error);


  /* ==========================================================
   * RENDER
   * ==========================================================
   */

  return (

    <div
      className={
        `status-banner status-banner-${configuration.type}`
      }
      role="alert"
    >

      {/* ======================================================
          ERROR ICON
          ====================================================== */}

      <div className="status-banner-icon">

        {
          getErrorIcon(
            configuration.type
          )
        }

      </div>


      {/* ======================================================
          ERROR CONTENT
          ====================================================== */}

      <div className="status-banner-content">

        <strong className="status-banner-title">

          {configuration.title}

        </strong>


        <p className="status-banner-description">

          {configuration.description}

        </p>


        <div className="status-banner-detail">

          <span>
            Error Details:
          </span>

          <strong>
            {error}
          </strong>

        </div>

      </div>


      {/* ======================================================
          DISMISS BUTTON
          ====================================================== */}

      {
        onDismiss && (

          <button
            type="button"
            className="status-banner-dismiss"
            onClick={onDismiss}
            aria-label="Dismiss error"
            title="Dismiss"
          >

            <X size={18} />

          </button>

        )
      }

    </div>

  );
}

