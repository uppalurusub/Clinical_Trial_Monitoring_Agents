import { useState } from "react";
import { ShieldCheck } from "lucide-react";

import { monitoringApi } from "./api/monitoringApi";
import MonitoringForm from "./components/MonitoringForm";
import MonitoringResults from "./components/MonitoringResults";
import StatusBanner from "./components/StatusBanner";

import type {
  MonitoringRequest,
  MonitoringResponse,
} from "./models/monitoring";

export default function App() {
  const [result, setResult] = useState<MonitoringResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAnalyzeMonitoring = async (
    request: MonitoringRequest
  ): Promise<void> => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await monitoringApi.analyze(request);
      setResult(response);

      window.requestAnimationFrame(() => {
        document.getElementById("monitoring-results")?.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      });
    } catch (analysisError) {
      setError(monitoringApi.getErrorMessage(analysisError));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <header className="hero">
        <div className="hero-icon">
          <ShieldCheck size={34} />
        </div>
        <div className="hero-content">
          <p className="eyebrow">AUTOGEN CLINICAL OPERATIONS</p>
          <h1>Clinical Trial Monitoring Agent</h1>
          <p>
            Risk-based site monitoring, compliance assessment and monitoring
            visit planning.
          </p>
        </div>
      </header>

      <main className="layout single-column-layout">
        <section className="workspace">
          <StatusBanner error={error} onDismiss={() => setError("")} />
          <MonitoringForm onSubmit={handleAnalyzeMonitoring} loading={loading} />
          <div id="monitoring-results" className="monitoring-results-anchor">
            <MonitoringResults data={result} />
          </div>
        </section>
      </main>

      <footer className="app-footer">
        <div className="app-footer-content">
          <div className="app-footer-brand">
            <ShieldCheck size={17} />
            <span>Clinical Trial Monitoring Agent</span>
          </div>
          <div className="app-footer-meta">
            <span>POST /api/v1/monitoring/analyze</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
