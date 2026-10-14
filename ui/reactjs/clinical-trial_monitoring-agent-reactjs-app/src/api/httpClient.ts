import axios from "axios";
import type { AxiosError, InternalAxiosRequestConfig } from "axios";


const MONITORING_ANALYZE_URL =
  "http://127.0.0.1:8000/api/v1/monitoring/analyze";

const API_TIMEOUT = 12000000;

export const httpClient = axios.create({
  timeout: API_TIMEOUT,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

httpClient.interceptors.request.use(
  (config: InternalAxiosRequestConfig): InternalAxiosRequestConfig => {
    console.info(`[API REQUEST] ${config.method?.toUpperCase() ?? "UNKNOWN"} ${config.url ?? ""}`);
    return config;
  },
  (error: AxiosError): Promise<never> => Promise.reject(error)
);

httpClient.interceptors.response.use(
  (response) => response,
  (error: AxiosError): Promise<never> => Promise.reject(error)
);

interface FastApiErrorResponse {
  detail?: string | Array<{ loc?: unknown[]; msg?: string; type?: string }>;
}

export const getApiErrorMessage = (error: unknown): string => {
  if (axios.isAxiosError<FastApiErrorResponse>(error)) {
    const detail = error.response?.data?.detail;
    if (typeof detail === "string") return detail;
    if (Array.isArray(detail)) {
      return detail.map((item) => item.msg ?? "Validation error").join("; ");
    }
    if (error.code === "ERR_NETWORK") {
      return "Unable to connect to http://127.0.0.1:8000. Verify the FastAPI service and CORS configuration.";
    }
    if (error.code === "ECONNABORTED") return "Monitoring analysis request timed out.";
    if (error.response?.status === 422) return "Monitoring request validation failed.";
    if (error.response?.status === 500) return "Monitoring analysis failed with an internal server error.";
    return error.message || "Monitoring API request failed.";
  }
  return error instanceof Error ? error.message : "Unexpected monitoring API error.";
};

export const apiConfig = {
  analyzeUrl: MONITORING_ANALYZE_URL,
  timeout: API_TIMEOUT,
};

export default httpClient;
