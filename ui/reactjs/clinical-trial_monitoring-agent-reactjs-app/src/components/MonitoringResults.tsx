
// src/components/MonitoringResults.tsx

import {
  Activity,
  AlertTriangle,
  Bot,
  CalendarClock,
  CheckCircle2,
  ClipboardCheck,
  FileCheck2,
  Lightbulb,
  ShieldAlert,
  ShieldCheck,
  TrendingUp,
} from "lucide-react";

import type {
  MonitoringResponse,
} from "../models/monitoring";

import JsonSection from "./JsonSection";


/* ============================================================
 * COMPONENT PROPERTIES
 * ============================================================
 */

interface MonitoringResultsProps {
  data: MonitoringResponse | null;
}


/* ============================================================
 * TEXT FORMATTER
 * ============================================================
 */

const titleCase = (
  value: string
): string => {

  return value
    .replace(/_/g, " ")
    .replace(
      /\b\w/g,
      (character) =>
        character.toUpperCase()
    );
};


/* ============================================================
 * NUMBER FORMATTER
 * ============================================================
 */

const formatNumber = (
  value: number
): string => {

  return new Intl.NumberFormat(
    "en-US",
    {
      maximumFractionDigits: 2,
    }
  ).format(value);
};


/* ============================================================
 * BADGE CLASS
 * ============================================================
 */

const getBadgeClass = (
  value: string
): string => {

  const normalized =
    value
      .toLowerCase()
      .trim();


  if (
    normalized.includes("critical") ||
    normalized.includes("high") ||
    normalized.includes("not ready") ||
    normalized.includes("poor") ||
    normalized.includes("non-compliant")
  ) {

    return "badge badge-high";
  }


  if (
    normalized.includes("medium") ||
    normalized.includes("partial")
  ) {

    return "badge badge-medium";
  }


  if (
    normalized.includes("low") ||
    normalized.includes("ready") ||
    normalized.includes("compliant") ||
    normalized.includes("completed")
  ) {

    return "badge badge-low";
  }


  return "badge";
};


/* ============================================================
 * METRIC CARD
 * ============================================================
 */

interface MetricCardProps {
  label: string;

  value: number;

  suffix?: string;
}


function MetricCard({
  label,
  value,
  suffix = "%",
}: MetricCardProps) {

  return (

    <div className="metric-card">

      <span className="metric-label">
        {label}
      </span>

      <span className="metric-value">

        {formatNumber(value)}

        {suffix}

      </span>

    </div>

  );
}


/* ============================================================
 * STATUS VALUE
 * ============================================================
 */

interface StatusValueProps {
  label: string;

  value: string;
}


function StatusValue({
  label,
  value,
}: StatusValueProps) {

  return (

    <div className="kv-row">

      <span>
        {label}:
      </span>

      <strong>

        <span
          className={
            getBadgeClass(value)
          }
        >
          {value}
        </span>

      </strong>

    </div>

  );
}


/* ============================================================
 * NUMERIC VALUE
 * ============================================================
 */

interface NumericValueProps {
  label: string;

  value: number;

  suffix?: string;
}


function NumericValue({
  label,
  value,
  suffix = "",
}: NumericValueProps) {

  return (

    <div className="kv-row">

      <span>
        {label}:
      </span>

      <strong>

        {formatNumber(value)}

        {suffix}

      </strong>

    </div>

  );
}


/* ============================================================
 * MONITORING RESULTS
 * ============================================================
 */

export default function MonitoringResults({
  data,
}: MonitoringResultsProps) {


  /* ==========================================================
   * EMPTY STATE
   * ==========================================================
   */

  if (!data) {

    return (

      <div className="empty-state">

        <Bot size={38} />

        <h3>
          Analysis results will appear here
        </h3>

        <p>
          Submit clinical trial site monitoring
          data to run the Monitoring Agent,
          Risk Agent and Compliance Agent.
        </p>

      </div>

    );
  }


  /* ==========================================================
   * RESPONSE DATA
   * ==========================================================
   */

  const {
    monitoring_metrics,
    risk_assessment,
    compliance_assessment,
    monitoring_visit_plan,
    agent_analysis,
    recommendations,
  } = data;


  /* ==========================================================
   * RENDER
   * ==========================================================
   */

  return (

    <section className="results-container">


      {/* ======================================================
          SUCCESS MESSAGE
          ====================================================== */}

      <div className="success-banner">

        <CheckCircle2 size={20} />

        <div>

          <strong>
            {data.message}
          </strong>

          <div>
            {data.generated_by}
          </div>

        </div>

      </div>


      {/* ======================================================
          ANALYSIS SUMMARY
          ====================================================== */}

      <section className="card">

        <div className="section-title">

          <ClipboardCheck size={24} />

          <div>

            <h2>
              Monitoring Analysis
            </h2>

            <p>
              Clinical trial site monitoring
              analysis summary.
            </p>

          </div>

        </div>


        <div className="kv">

          <div className="kv-row">

            <span>
              Study ID:
            </span>

            <strong>
              {data.study_id}
            </strong>

          </div>


          <div className="kv-row">

            <span>
              Site ID:
            </span>

            <strong>
              {data.site_id}
            </strong>

          </div>


          <div className="kv-row">

            <span>
              Site Name:
            </span>

            <strong>
              {data.site_name}
            </strong>

          </div>


          <StatusValue
            label="Monitoring Status"
            value={data.monitoring_status}
          />

        </div>

      </section>


      {/* ======================================================
          MONITORING METRICS
          ====================================================== */}

      <section className="card">

        <div className="section-title">

          <TrendingUp size={24} />

          <div>

            <h2>
              Monitoring Metrics
            </h2>

            <p>
              Site performance, quality and
              safety monitoring indicators.
            </p>

          </div>

        </div>


        <div className="metrics-grid">

          <MetricCard
            label="Enrollment Rate"
            value={
              monitoring_metrics.enrollment_rate
            }
          />

          <MetricCard
            label="Screen Failure Rate"
            value={
              monitoring_metrics.screen_failure_rate
            }
          />

          <MetricCard
            label="Dropout Rate"
            value={
              monitoring_metrics.dropout_rate
            }
          />

          <MetricCard
            label="Protocol Deviation Rate"
            value={
              monitoring_metrics.protocol_deviation_rate
            }
          />

          <MetricCard
            label="Missing Data Rate"
            value={
              monitoring_metrics.missing_data_rate
            }
          />

          <MetricCard
            label="Query Resolution Rate"
            value={
              monitoring_metrics.query_resolution_rate
            }
          />

          <MetricCard
            label="Compliance Score"
            value={
              monitoring_metrics.compliance_score
            }
          />

          <MetricCard
            label="Training Completion Rate"
            value={
              monitoring_metrics.training_completion_rate
            }
          />

          <MetricCard
            label="Adverse Event Rate"
            value={
              monitoring_metrics.adverse_event_rate
            }
          />

          <MetricCard
            label="Serious Adverse Event Rate"
            value={
              monitoring_metrics.serious_adverse_event_rate
            }
          />

        </div>

      </section>


      {/* ======================================================
          RISK AND COMPLIANCE
          ====================================================== */}

      <div className="result-grid">


        {/* ====================================================
            RISK ASSESSMENT
            ==================================================== */}

        <section className="card">

          <div className="section-title">

            <ShieldAlert size={24} />

            <div>

              <h2>
                Risk Assessment
              </h2>

              <p>
                Risk-based monitoring assessment.
              </p>

            </div>

          </div>


          <div className="kv">

            <NumericValue
              label="Risk Score"
              value={
                risk_assessment.risk_score
              }
              suffix=" / 100"
            />

            <StatusValue
              label="Risk Level"
              value={
                risk_assessment.risk_level
              }
            />

            <StatusValue
              label="Site Risk"
              value={
                risk_assessment.site_risk
              }
            />

            <StatusValue
              label="Safety Risk"
              value={
                risk_assessment.safety_risk
              }
            />

            <StatusValue
              label="Compliance Risk"
              value={
                risk_assessment.compliance_risk
              }
            />

            <StatusValue
              label="Data Quality Risk"
              value={
                risk_assessment.data_quality_risk
              }
            />

            <NumericValue
              label="Key Risk Indicators Triggered"
              value={
                risk_assessment
                  .key_risk_indicators_triggered
              }
            />

            <NumericValue
              label="Quality Tolerance Limit Breaches"
              value={
                risk_assessment
                  .quality_tolerance_limit_breaches
              }
            />

          </div>

        </section>


        {/* ====================================================
            COMPLIANCE ASSESSMENT
            ==================================================== */}

        <section className="card">

          <div className="section-title">

            <ShieldCheck size={24} />

            <div>

              <h2>
                Compliance Assessment
              </h2>

              <p>
                Protocol and regulatory compliance.
              </p>

            </div>

          </div>


          <div className="kv">

            <StatusValue
              label="Compliance Status"
              value={
                compliance_assessment
                  .compliance_status
              }
            />

            <StatusValue
              label="Protocol Compliance"
              value={
                compliance_assessment
                  .protocol_compliance
              }
            />

            <StatusValue
              label="Informed Consent Compliance"
              value={
                compliance_assessment
                  .informed_consent_compliance
              }
            />

            <StatusValue
              label="Training Compliance"
              value={
                compliance_assessment
                  .training_compliance
              }
            />

            <StatusValue
              label="Audit Readiness Status"
              value={
                compliance_assessment
                  .audit_readiness_status
              }
            />

            <NumericValue
              label="Major Findings"
              value={
                compliance_assessment.major_findings
              }
            />

            <NumericValue
              label="Critical Findings"
              value={
                compliance_assessment.critical_findings
              }
            />

          </div>

        </section>

      </div>


      {/* ======================================================
          MONITORING VISIT PLAN
          ====================================================== */}

      <section className="card">

        <div className="section-title">

          <CalendarClock size={24} />

          <div>

            <h2>
              Monitoring Visit Plan
            </h2>

            <p>
              Recommended risk-based monitoring
              visit strategy.
            </p>

          </div>

        </div>


        <div className="kv">

          <div className="kv-row">

            <span>
              Monitoring Strategy:
            </span>

            <strong>
              {
                monitoring_visit_plan
                  .monitoring_strategy
              }
            </strong>

          </div>


          <div className="kv-row">

            <span>
              Next Visit Required:
            </span>

            <strong>

              {
                monitoring_visit_plan
                  .next_visit_required
                  ? "Yes"
                  : "No"
              }

            </strong>

          </div>


          <div className="kv-row">

            <span>
              Recommended Visit Type:
            </span>

            <strong>
              {
                monitoring_visit_plan
                  .recommended_visit_type
              }
            </strong>

          </div>


          <NumericValue
            label="Recommended Visit Within"
            value={
              monitoring_visit_plan
                .recommended_visit_within_days
            }
            suffix=" Days"
          />


          <StatusValue
            label="Monitoring Priority"
            value={
              monitoring_visit_plan
                .monitoring_priority
            }
          />

        </div>

      </section>


      {/* ======================================================
          RECOMMENDATIONS
          ====================================================== */}

      <section className="card">

        <div className="section-title">

          <Lightbulb size={24} />

          <div>

            <h2>
              Recommendations
            </h2>

            <p>
              Monitoring, risk, compliance and
              CAPA recommendations.
            </p>

          </div>

        </div>


        <div className="recommendations">

          {
            recommendations.map(
              (
                recommendation,
                index
              ) => (

                <div
                  className="recommendation-card"
                  key={
                    `${recommendation.category}-${index}`
                  }
                >

                  <div className="recommendation-category">

                    {
                      recommendation.category
                    }

                  </div>


                  <div>

                    <span
                      className={
                        getBadgeClass(
                          recommendation.priority
                        )
                      }
                    >

                      {
                        recommendation.priority
                      }

                    </span>

                  </div>


                  <div className="recommendation-text">

                    {
                      recommendation.recommendation
                    }

                  </div>

                </div>

              )
            )
          }

        </div>

      </section>


      {/* ======================================================
          AGENT ANALYSIS
          ====================================================== */}

      <section className="card">

        <div className="section-title">

          <Bot size={24} />

          <div>

            <h2>
              AutoGen Agent Analysis
            </h2>

            <p>
              Detailed analysis generated by
              specialized monitoring agents.
            </p>

          </div>

        </div>


        <div className="agent-analysis">


          {/* ==================================================
              MONITORING AGENT
              ================================================== */}

          <div className="agent-card">

            <div className="agent-header">

              <Activity size={18} />

              Monitoring Agent

            </div>


            <JsonSection
              title="Monitoring Agent Summary"
              value={
                agent_analysis
                  .monitoring_agent_summary
              }
            />

          </div>


          {/* ==================================================
              RISK AGENT
              ================================================== */}

          <div className="agent-card">

            <div className="agent-header">

              <AlertTriangle size={18} />

              Risk Agent

            </div>


            <JsonSection
              title="Risk Agent Summary"
              value={
                agent_analysis
                  .risk_agent_summary
              }
            />

          </div>


          {/* ==================================================
              COMPLIANCE AGENT
              ================================================== */}

          <div className="agent-card">

            <div className="agent-header">

              <FileCheck2 size={18} />

              Compliance Agent

            </div>


            <JsonSection
              title="Compliance Agent Summary"
              value={
                agent_analysis
                  .compliance_agent_summary
              }
            />

          </div>

        </div>

      </section>

    </section>

  );
}

