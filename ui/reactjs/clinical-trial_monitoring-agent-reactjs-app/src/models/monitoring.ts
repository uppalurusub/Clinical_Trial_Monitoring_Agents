// src/types/monitoring.ts

/**
 * ============================================================
 * Clinical Trial Monitoring Agent - TypeScript Models
 * ============================================================
 *
 * API Endpoints:
 *
 * POST /monitoring/analyze
 * GET  /monitoring/health
 * GET  /monitoring/info
 *
 * ============================================================
 */


/* ============================================================
 * MONITORING ANALYZE REQUEST
 * ============================================================
 */

export interface MonitoringRequest {
  adverse_events: number;

  compliance_score: number;

  country: string;

  critical_findings: number;

  ctms_site_status: string;

  ctms_study_status: string;

  days_since_last_visit: number;

  dropout_subjects: number;

  enrolled_subjects: number;

  informed_consent_compliance: number;

  investigator_name: string;

  key_risk_indicators_triggered: number;

  last_monitoring_visit_date: string;

  major_findings: number;

  major_protocol_deviations: number;

  minor_findings: number;

  minor_protocol_deviations: number;

  missing_data_points: number;

  monitoring_findings: number;

  monitoring_frequency_days: number;

  open_queries: number;

  overdue_queries: number;

  protocol_deviations: number;

  quality_tolerance_limit_breaches: number;

  randomized_subjects: number;

  risk_indicator_score: number;

  screened_subjects: number;

  serious_adverse_events: number;

  site_id: string;

  site_name: string;

  source_data_verification_rate: number;

  study_id: string;

  study_name: string;

  suspected_unexpected_serious_adverse_reactions: number;

  training_completion_rate: number;
}


/* ============================================================
 * MONITORING METRICS
 * ============================================================
 */

export interface MonitoringMetrics {
  enrollment_rate: number;

  screen_failure_rate: number;

  dropout_rate: number;

  protocol_deviation_rate: number;

  missing_data_rate: number;

  query_resolution_rate: number;

  compliance_score: number;

  training_completion_rate: number;

  adverse_event_rate: number;

  serious_adverse_event_rate: number;
}


/* ============================================================
 * RISK ASSESSMENT
 * ============================================================
 */

export interface RiskAssessment {
  risk_score: number;

  risk_level: string;

  site_risk: string;

  safety_risk: string;

  compliance_risk: string;

  data_quality_risk: string;

  key_risk_indicators_triggered: number;

  quality_tolerance_limit_breaches: number;
}


/* ============================================================
 * COMPLIANCE ASSESSMENT
 * ============================================================
 */

export interface ComplianceAssessment {
  compliance_status: string;

  protocol_compliance: string;

  informed_consent_compliance: string;

  training_compliance: string;

  audit_readiness_status: string;

  major_findings: number;

  critical_findings: number;
}


/* ============================================================
 * MONITORING VISIT PLAN
 * ============================================================
 */

export interface MonitoringVisitPlan {
  monitoring_strategy: string;

  next_visit_required: boolean;

  recommended_visit_type: string;

  recommended_visit_within_days: number;

  monitoring_priority: string;
}


/* ============================================================
 * AGENT ANALYSIS
 * ============================================================
 */

export interface AgentAnalysis {
  monitoring_agent_summary: string;

  risk_agent_summary: string;

  compliance_agent_summary: string;
}


/* ============================================================
 * MONITORING RECOMMENDATION
 * ============================================================
 */

export interface MonitoringRecommendation {
  category: string;

  priority: string;

  recommendation: string;
}


/* ============================================================
 * MONITORING ANALYZE RESPONSE
 * ============================================================
 */

export interface MonitoringResponse {
  success: boolean;

  study_id: string;

  site_id: string;

  site_name: string;

  monitoring_status: string;

  monitoring_metrics: MonitoringMetrics;

  risk_assessment: RiskAssessment;

  compliance_assessment: ComplianceAssessment;

  monitoring_visit_plan: MonitoringVisitPlan;

  agent_analysis: AgentAnalysis;

  recommendations: MonitoringRecommendation[];

  generated_by: string;

  message: string;
}


/* ============================================================
 * MONITORING SERVICE INFO
 * ============================================================
 */

export interface ServiceInfo {
  application: string;

  version: string;

  framework: string;

  autogen_version: string;

  agents: string[];

  capabilities: string[];
}


/* ============================================================
 * MONITORING HEALTH RESPONSE
 * ============================================================
 *
 * Health endpoint response model is not explicitly defined
 * in the supplied router.
 *
 * Flexible typing is provided for compatibility.
 *
 * ============================================================
 */

export interface MonitoringHealthResponse {
  status?: string;

  service?: string;

  version?: string;

  message?: string;

  [key: string]: unknown;
}


/* ============================================================
 * MONITORING FORM STATE
 * ============================================================
 */

export type MonitoringFormData = MonitoringRequest;


/* ============================================================
 * RISK LEVEL TYPES
 * ============================================================
 */

export type RiskLevel =
  | "Low"
  | "Medium"
  | "High"
  | "Critical";


/* ============================================================
 * PRIORITY TYPES
 * ============================================================
 */

export type MonitoringPriority =
  | "Low"
  | "Medium"
  | "High"
  | "Critical";


/* ============================================================
 * COMPLIANCE STATUS TYPES
 * ============================================================
 */

export type ComplianceStatus =
  | "Compliant"
  | "Partially Compliant"
  | "Non-Compliant";


/* ============================================================
 * AUDIT READINESS TYPES
 * ============================================================
 */

export type AuditReadinessStatus =
  | "Ready"
  | "Partially Ready"
  | "Not Ready";


/* ============================================================
 * MONITORING STATUS TYPES
 * ============================================================
 */

export type MonitoringStatus =
  | "Pending"
  | "In Progress"
  | "Completed"
  | "Failed";


/* ============================================================
 * RECOMMENDATION CATEGORY TYPES
 * ============================================================
 */

export type RecommendationCategory =
  | "Risk"
  | "Compliance"
  | "Data Quality"
  | "CAPA"
  | "Safety"
  | "Monitoring";


/* ============================================================
 * API ERROR RESPONSE
 * ============================================================
 */

export interface ApiErrorResponse {
  detail: string;
}

