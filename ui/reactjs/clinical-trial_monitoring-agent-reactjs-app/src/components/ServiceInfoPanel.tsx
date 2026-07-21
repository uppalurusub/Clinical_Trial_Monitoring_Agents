
// src/components/ServiceInfoPanel.tsx

import {
  Activity,
  Bot,
  Boxes,
  CheckCircle2,
  Cpu,
  Database,
  HeartPulse,
  Info,
  Server,
  ShieldCheck,
  Sparkles,
  Tag,
  Workflow,
} from "lucide-react";

import type {
  ServiceInfo,
} from "../models/monitoring";


/* ============================================================
 * COMPONENT PROPERTIES
 * ============================================================
 */

interface ServiceInfoPanelProps {
  info: ServiceInfo | null;
}


/* ============================================================
 * SERVICE INFO PANEL
 * ============================================================
 */

export default function ServiceInfoPanel({
  info,
}: ServiceInfoPanelProps) {


  /* ==========================================================
   * SERVICE INFORMATION UNAVAILABLE
   * ==========================================================
   */

  if (!info) {

    return (

      <section className="card sticky">

        <div className="section-title">

          <Info size={24} />

          <div>

            <h2>
              Service Information
            </h2>

            <p>
              Clinical trial monitoring service metadata.
            </p>

          </div>

        </div>


        <div className="service-unavailable">

          <Server size={32} />

          <strong>
            Service metadata unavailable
          </strong>

          <p>
            Unable to retrieve monitoring
            service information.
          </p>

        </div>

      </section>

    );
  }


  /* ==========================================================
   * RENDER
   * ==========================================================
   */

  return (

    <section className="card sticky service-info-panel">


      {/* ======================================================
          HEADER
          ====================================================== */}

      <div className="section-title">

        <Cpu size={24} />

        <div>

          <h2>
            Service Information
          </h2>

          <p>
            FastAPI and AutoGen monitoring service.
          </p>

        </div>

      </div>


      {/* ======================================================
          APPLICATION
          ====================================================== */}

      <div className="service-application">

        <div className="service-application-icon">

          <HeartPulse size={26} />

        </div>


        <div>

          <span className="service-label">
            Application
          </span>

          <strong className="service-application-name">
            {info.application}
          </strong>

        </div>

      </div>


      {/* ======================================================
          SERVICE METADATA
          ====================================================== */}

      <div className="service-metadata">

        <div className="service-metadata-row">

          <div className="service-metadata-label">

            <Tag size={15} />

            <span>
              Version:
            </span>

          </div>

          <strong>
            {info.version}
          </strong>

        </div>


        <div className="service-metadata-row">

          <div className="service-metadata-label">

            <Server size={15} />

            <span>
              Framework:
            </span>

          </div>

          <strong>
            {info.framework}
          </strong>

        </div>


        <div className="service-metadata-row">

          <div className="service-metadata-label">

            <Workflow size={15} />

            <span>
              AutoGen Version:
            </span>

          </div>

          <strong>
            {info.autogen_version}
          </strong>

        </div>


        <div className="service-metadata-row">

          <div className="service-metadata-label">

            <Activity size={15} />

            <span>
              Service Status:
            </span>

          </div>

          <span className="badge badge-low">

            <CheckCircle2 size={13} />

            Available

          </span>

        </div>

      </div>


      {/* ======================================================
          AUTOGEN AGENTS
          ====================================================== */}

      <div className="service-section">

        <h3 className="mini-title">

          <Bot size={17} />

          AutoGen Agents

        </h3>


        <p className="service-section-description">

          Specialized AI agents participating
          in the monitoring analysis workflow.

        </p>


        <div className="agent-list">

          {
            info.agents.map(
              (
                agent,
                index
              ) => (

                <div
                  className="service-agent-card"
                  key={agent}
                >

                  <div className="service-agent-number">

                    {index + 1}

                  </div>


                  <div className="service-agent-details">

                    <strong>
                      {agent}
                    </strong>

                    <span>

                      {
                        getAgentDescription(
                          agent
                        )
                      }

                    </span>

                  </div>

                </div>

              )
            )
          }

        </div>

      </div>


      {/* ======================================================
          CAPABILITIES
          ====================================================== */}

      <div className="service-section">

        <h3 className="mini-title">

          <Sparkles size={17} />

          Capabilities

        </h3>


        <p className="service-section-description">

          Clinical monitoring and
          risk-management capabilities.

        </p>


        <div className="capability-list">

          {
            info.capabilities.map(
              (capability) => (

                <div
                  className="capability-item"
                  key={capability}
                >

                  <ShieldCheck size={15} />

                  <span>
                    {capability}
                  </span>

                </div>

              )
            )
          }

        </div>

      </div>


      {/* ======================================================
          TECHNOLOGY STACK
          ====================================================== */}

      <div className="service-section">

        <h3 className="mini-title">

          <Boxes size={17} />

          Technology Stack

        </h3>


        <div className="technology-stack">

          <div className="technology-item">

            <Server size={15} />

            <span>
              FastAPI
            </span>

          </div>


          <div className="technology-item">

            <Bot size={15} />

            <span>
              AutoGen
            </span>

          </div>


          <div className="technology-item">

            <Database size={15} />

            <span>
              CTMS Analytics
            </span>

          </div>

        </div>

      </div>

    </section>

  );
}


/* ============================================================
 * AGENT DESCRIPTION
 * ============================================================
 */

function getAgentDescription(
  agent: string
): string {

  const normalized =
    agent
      .toLowerCase()
      .trim();


  if (
    normalized.includes("monitoring")
  ) {

    return (
      "Evaluates site performance and " +
      "monitoring indicators."
    );
  }


  if (
    normalized.includes("risk")
  ) {

    return (
      "Performs risk-based monitoring " +
      "and KRI assessment."
    );
  }


  if (
    normalized.includes("compliance")
  ) {

    return (
      "Assesses protocol and regulatory " +
      "compliance."
    );
  }


  return (
    "Participates in the clinical " +
    "monitoring workflow."
  );
}

