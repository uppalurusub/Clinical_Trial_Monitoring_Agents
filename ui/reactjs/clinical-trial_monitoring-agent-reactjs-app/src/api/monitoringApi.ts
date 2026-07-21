import type {
  MonitoringRequest,
  MonitoringResponse,
} from "../models/monitoring";

import {
  apiConfig,
  getApiErrorMessage,
  httpClient,
} from "./httpClient";

export const monitoringApi = {
  async analyze(request: MonitoringRequest): Promise<MonitoringResponse> {
    const response = await httpClient.post<MonitoringResponse>(
      apiConfig.analyzeUrl,
      request
    );
    return response.data;
  },

  getErrorMessage(error: unknown): string {
    return getApiErrorMessage(error);
  },
};

export const analyzeMonitoring = async (
  request: MonitoringRequest
): Promise<MonitoringResponse> => monitoringApi.analyze(request);

export default monitoringApi;
