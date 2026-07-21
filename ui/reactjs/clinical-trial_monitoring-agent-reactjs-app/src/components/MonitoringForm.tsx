// src/components/MonitoringForm.tsx

import {
  FormEvent,
  useState,
} from "react";

import {
  Activity,
  ClipboardCheck,
  FileWarning,
  GraduationCap,
  LoaderCircle,
  MapPin,
  RotateCcw,
  ShieldAlert,
  Stethoscope,
  Users,
} from "lucide-react";

import type {
  MonitoringRequest,
} from "../models/monitoring";

import "../styles/global.css"

/* ============================================================
 * COMPONENT PROPERTIES
 * ============================================================
 */

interface MonitoringFormProps {
  onSubmit: (
    request: MonitoringRequest
  ) => Promise<void>;

  loading: boolean;
}


/* ============================================================
 * INITIAL MONITORING REQUEST
 *
 * Values mapped directly from monitoring_analyze_request.json
 * ============================================================
 */

const INITIAL_MONITORING_REQUEST: MonitoringRequest = {

  adverse_events: 12,

  compliance_score: 85,

  country: "India",

  critical_findings: 1,

  ctms_site_status: "Active",

  ctms_study_status: "Active",

  days_since_last_visit: 39,

  dropout_subjects: 10,

  enrolled_subjects: 180,

  informed_consent_compliance: 95,

  investigator_name: "Dr. John Smith",

  key_risk_indicators_triggered: 4,

  last_monitoring_visit_date: "2026-05-15",

  major_findings: 3,

  major_protocol_deviations: 3,

  minor_findings: 8,

  minor_protocol_deviations: 5,

  missing_data_points: 15,

  monitoring_findings: 12,

  monitoring_frequency_days: 30,

  open_queries: 25,

  overdue_queries: 8,

  protocol_deviations: 8,

  quality_tolerance_limit_breaches: 2,

  randomized_subjects: 170,

  risk_indicator_score: 78,

  screened_subjects: 220,

  serious_adverse_events: 2,

  site_id: "SITE-101",

  site_name: "Apollo Research Center",

  source_data_verification_rate: 88,

  study_id: "STUDY-001",

  study_name: "Phase III Diabetes Study",

  suspected_unexpected_serious_adverse_reactions: 1,

  training_completion_rate: 92,
};


/* ============================================================
 * FORM COMPONENT
 * ============================================================
 */

export default function MonitoringForm({
  onSubmit,
  loading,
}: MonitoringFormProps) {

  const [
    form,
    setForm,
  ] = useState<MonitoringRequest>(
    INITIAL_MONITORING_REQUEST
  );


  /* ==========================================================
   * UPDATE STRING FIELD
   * ==========================================================
   */

  const updateStringField = (
    field: keyof MonitoringRequest,
    value: string
  ): void => {

    setForm(
      (previous) => ({
        ...previous,
        [field]: value,
      })
    );
  };


  /* ==========================================================
   * UPDATE NUMBER FIELD
   * ==========================================================
   */

  const updateNumberField = (
    field: keyof MonitoringRequest,
    value: string
  ): void => {

    setForm(
      (previous) => ({
        ...previous,
        [field]:
          value === ""
            ? 0
            : Number(value),
      })
    );
  };


  /* ==========================================================
   * SUBMIT FORM
   * ==========================================================
   */

  const handleSubmit = (
    event: FormEvent<HTMLFormElement>
  ): void => {

    event.preventDefault();

    void onSubmit(form);
  };


  /* ==========================================================
   * RESET FORM
   * ==========================================================
   */

  const handleReset = (): void => {

    setForm({
      ...INITIAL_MONITORING_REQUEST,
    });
  };


  /* ==========================================================
   * RENDER
   * ==========================================================
   */

  return (

    <form
      className="card"
      onSubmit={handleSubmit}
    >

      {/* ======================================================
          HEADER
          ====================================================== */}

      <div className="section-title">

        <ClipboardCheck size={24} />

        <div>

          <h2>
            Monitoring Analysis Request
          </h2>

          <p>
            Enter clinical trial site monitoring,
            risk, compliance and data quality
            indicators.
          </p>

        </div>

      </div>


      <div className="form-grid">


        {/* ====================================================
            STUDY INFORMATION
            ==================================================== */}

        <div className="form-section">

          <h3>
            <Stethoscope size={16} />
            Study Information
          </h3>

          <p>
            Clinical study identification and CTMS status.
          </p>

        </div>


        <label>
          Study ID

          <input
            type="text"
            value={form.study_id}
            onChange={
              (event) =>
                updateStringField(
                  "study_id",
                  event.target.value
                )
            }
            required
          />
        </label>


        <label>
          Study Name

          <input
            type="text"
            value={form.study_name}
            onChange={
              (event) =>
                updateStringField(
                  "study_name",
                  event.target.value
                )
            }
            required
          />
        </label>


        <label>
          CTMS Study Status

          <select
            value={form.ctms_study_status}
            onChange={
              (event) =>
                updateStringField(
                  "ctms_study_status",
                  event.target.value
                )
            }
          >

            <option value="Active">
              Active
            </option>

            <option value="Planned">
              Planned
            </option>

            <option value="Recruiting">
              Recruiting
            </option>

            <option value="Suspended">
              Suspended
            </option>

            <option value="Completed">
              Completed
            </option>

            <option value="Closed">
              Closed
            </option>

          </select>

        </label>


        {/* ====================================================
            SITE INFORMATION
            ==================================================== */}

        <div className="form-section">

          <h3>
            <MapPin size={16} />
            Site Information
          </h3>

          <p>
            Investigational site and investigator details.
          </p>

        </div>


        <label>
          Site ID

          <input
            type="text"
            value={form.site_id}
            onChange={
              (event) =>
                updateStringField(
                  "site_id",
                  event.target.value
                )
            }
            required
          />
        </label>


        <label>
          Site Name

          <input
            type="text"
            value={form.site_name}
            onChange={
              (event) =>
                updateStringField(
                  "site_name",
                  event.target.value
                )
            }
            required
          />
        </label>


        <label>
          Country

          <input
            type="text"
            value={form.country}
            onChange={
              (event) =>
                updateStringField(
                  "country",
                  event.target.value
                )
            }
            required
          />
        </label>


        <label>
          Investigator Name

          <input
            type="text"
            value={form.investigator_name}
            onChange={
              (event) =>
                updateStringField(
                  "investigator_name",
                  event.target.value
                )
            }
            required
          />
        </label>


        <label>
          CTMS Site Status

          <select
            value={form.ctms_site_status}
            onChange={
              (event) =>
                updateStringField(
                  "ctms_site_status",
                  event.target.value
                )
            }
          >

            <option value="Active">
              Active
            </option>

            <option value="Initiated">
              Initiated
            </option>

            <option value="Recruiting">
              Recruiting
            </option>

            <option value="Suspended">
              Suspended
            </option>

            <option value="Closed">
              Closed
            </option>

          </select>

        </label>


        {/* ====================================================
            SUBJECT ENROLLMENT
            ==================================================== */}

        <div className="form-section">

          <h3>
            <Users size={16} />
            Subject Enrollment
          </h3>

          <p>
            Screening, enrollment, randomization and dropout metrics.
          </p>

        </div>


        <label>
          Screened Subjects

          <input
            type="number"
            min="0"
            value={form.screened_subjects}
            onChange={
              (event) =>
                updateNumberField(
                  "screened_subjects",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Enrolled Subjects

          <input
            type="number"
            min="0"
            value={form.enrolled_subjects}
            onChange={
              (event) =>
                updateNumberField(
                  "enrolled_subjects",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Randomized Subjects

          <input
            type="number"
            min="0"
            value={form.randomized_subjects}
            onChange={
              (event) =>
                updateNumberField(
                  "randomized_subjects",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Dropout Subjects

          <input
            type="number"
            min="0"
            value={form.dropout_subjects}
            onChange={
              (event) =>
                updateNumberField(
                  "dropout_subjects",
                  event.target.value
                )
            }
          />
        </label>


        {/* ====================================================
            PROTOCOL COMPLIANCE
            ==================================================== */}

        <div className="form-section">

          <h3>
            <ShieldAlert size={16} />
            Protocol Compliance
          </h3>

          <p>
            Protocol deviation and compliance indicators.
          </p>

        </div>


        <label>
          Protocol Deviations

          <input
            type="number"
            min="0"
            value={form.protocol_deviations}
            onChange={
              (event) =>
                updateNumberField(
                  "protocol_deviations",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Major Protocol Deviations

          <input
            type="number"
            min="0"
            value={form.major_protocol_deviations}
            onChange={
              (event) =>
                updateNumberField(
                  "major_protocol_deviations",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Minor Protocol Deviations

          <input
            type="number"
            min="0"
            value={form.minor_protocol_deviations}
            onChange={
              (event) =>
                updateNumberField(
                  "minor_protocol_deviations",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Compliance Score (%)

          <input
            type="number"
            min="0"
            max="100"
            value={form.compliance_score}
            onChange={
              (event) =>
                updateNumberField(
                  "compliance_score",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Informed Consent Compliance (%)

          <input
            type="number"
            min="0"
            max="100"
            value={form.informed_consent_compliance}
            onChange={
              (event) =>
                updateNumberField(
                  "informed_consent_compliance",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Training Completion Rate (%)

          <input
            type="number"
            min="0"
            max="100"
            value={form.training_completion_rate}
            onChange={
              (event) =>
                updateNumberField(
                  "training_completion_rate",
                  event.target.value
                )
            }
          />
        </label>


        {/* ====================================================
            DATA QUALITY
            ==================================================== */}

        <div className="form-section">

          <h3>
            <Activity size={16} />
            Data Quality
          </h3>

          <p>
            Missing data, query management and SDV indicators.
          </p>

        </div>


        <label>
          Missing Data Points

          <input
            type="number"
            min="0"
            value={form.missing_data_points}
            onChange={
              (event) =>
                updateNumberField(
                  "missing_data_points",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Open Queries

          <input
            type="number"
            min="0"
            value={form.open_queries}
            onChange={
              (event) =>
                updateNumberField(
                  "open_queries",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Overdue Queries

          <input
            type="number"
            min="0"
            value={form.overdue_queries}
            onChange={
              (event) =>
                updateNumberField(
                  "overdue_queries",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Source Data Verification Rate (%)

          <input
            type="number"
            min="0"
            max="100"
            value={form.source_data_verification_rate}
            onChange={
              (event) =>
                updateNumberField(
                  "source_data_verification_rate",
                  event.target.value
                )
            }
          />
        </label>


        {/* ====================================================
            SAFETY
            ==================================================== */}

        <div className="form-section">

          <h3>
            <FileWarning size={16} />
            Safety Assessment
          </h3>

          <p>
            Adverse events, serious adverse events and SUSARs.
          </p>

        </div>


        <label>
          Adverse Events

          <input
            type="number"
            min="0"
            value={form.adverse_events}
            onChange={
              (event) =>
                updateNumberField(
                  "adverse_events",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Serious Adverse Events

          <input
            type="number"
            min="0"
            value={form.serious_adverse_events}
            onChange={
              (event) =>
                updateNumberField(
                  "serious_adverse_events",
                  event.target.value
                )
            }
          />
        </label>


        <label className="span-2">
          Suspected Unexpected Serious Adverse Reactions

          <input
            type="number"
            min="0"
            value={
              form
                .suspected_unexpected_serious_adverse_reactions
            }
            onChange={
              (event) =>
                updateNumberField(
                  "suspected_unexpected_serious_adverse_reactions",
                  event.target.value
                )
            }
          />
        </label>


        {/* ====================================================
            MONITORING FINDINGS
            ==================================================== */}

        <div className="form-section">

          <h3>
            <ClipboardCheck size={16} />
            Monitoring Findings
          </h3>

          <p>
            Monitoring findings and severity classification.
          </p>

        </div>


        <label>
          Monitoring Findings

          <input
            type="number"
            min="0"
            value={form.monitoring_findings}
            onChange={
              (event) =>
                updateNumberField(
                  "monitoring_findings",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Critical Findings

          <input
            type="number"
            min="0"
            value={form.critical_findings}
            onChange={
              (event) =>
                updateNumberField(
                  "critical_findings",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Major Findings

          <input
            type="number"
            min="0"
            value={form.major_findings}
            onChange={
              (event) =>
                updateNumberField(
                  "major_findings",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Minor Findings

          <input
            type="number"
            min="0"
            value={form.minor_findings}
            onChange={
              (event) =>
                updateNumberField(
                  "minor_findings",
                  event.target.value
                )
            }
          />
        </label>


        {/* ====================================================
            RISK INDICATORS
            ==================================================== */}

        <div className="form-section">

          <h3>
            <ShieldAlert size={16} />
            Risk Indicators
          </h3>

          <p>
            KRI, QTL and overall site risk indicators.
          </p>

        </div>


        <label>
          Risk Indicator Score

          <input
            type="number"
            min="0"
            max="100"
            value={form.risk_indicator_score}
            onChange={
              (event) =>
                updateNumberField(
                  "risk_indicator_score",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Key Risk Indicators Triggered

          <input
            type="number"
            min="0"
            value={
              form.key_risk_indicators_triggered
            }
            onChange={
              (event) =>
                updateNumberField(
                  "key_risk_indicators_triggered",
                  event.target.value
                )
            }
          />
        </label>


        <label className="span-2">
          Quality Tolerance Limit Breaches

          <input
            type="number"
            min="0"
            value={
              form.quality_tolerance_limit_breaches
            }
            onChange={
              (event) =>
                updateNumberField(
                  "quality_tolerance_limit_breaches",
                  event.target.value
                )
            }
          />
        </label>


        {/* ====================================================
            MONITORING SCHEDULE
            ==================================================== */}

        <div className="form-section">

          <h3>
            <GraduationCap size={16} />
            Monitoring Schedule
          </h3>

          <p>
            Last visit and monitoring frequency information.
          </p>

        </div>


        <label>
          Last Monitoring Visit Date

          <input
            type="date"
            value={
              form.last_monitoring_visit_date
            }
            onChange={
              (event) =>
                updateStringField(
                  "last_monitoring_visit_date",
                  event.target.value
                )
            }
          />
        </label>


        <label>
          Days Since Last Visit

          <input
            type="number"
            min="0"
            value={form.days_since_last_visit}
            onChange={
              (event) =>
                updateNumberField(
                  "days_since_last_visit",
                  event.target.value
                )
            }
          />
        </label>


        <label className="span-2">
          Monitoring Frequency (Days)

          <input
            type="number"
            min="1"
            value={
              form.monitoring_frequency_days
            }
            onChange={
              (event) =>
                updateNumberField(
                  "monitoring_frequency_days",
                  event.target.value
                )
            }
          />
        </label>

      </div>


      {/* ======================================================
          ACTIONS
          ====================================================== */}

      <div className="actions">

        <button
          type="button"
          className="secondary"
          onClick={handleReset}
          disabled={loading}
        >

          <RotateCcw size={17} />

          Reset

        </button>


        <button
          type="submit"
          disabled={loading}
        >

          {
            loading
              ? (
                <LoaderCircle
                  className="spin"
                  size={18}
                />
              )
              : (
                <ClipboardCheck
                  size={18}
                />
              )
          }

          {
            loading
              ? "Analyzing..."
              : "Analyze Monitoring"
          }

        </button>

      </div>

    </form>

  );
}

