// src/components/JsonSection.tsx

import type { ReactNode } from "react";

import ReactMarkdown from "react-markdown";


/* ============================================================
 * COMPONENT PROPERTIES
 * ============================================================
 */

interface JsonSectionProps {
  title: string;
  value: unknown;
}


/* ============================================================
 * JSON OBJECT
 * ============================================================
 */

type JsonObject =
  Record<string, unknown>;


/* ============================================================
 * TITLE CASE
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
 * PERCENTAGE FIELDS
 * ============================================================
 */

const PERCENTAGE_FIELDS =
  new Set<string>([

    "enrollment_rate",

    "screen_failure_rate",

    "dropout_rate",

    "protocol_deviation_rate",

    "missing_data_rate",

    "query_resolution_rate",

    "compliance_score",

    "training_completion_rate",

    "adverse_event_rate",

    "serious_adverse_event_rate",

    "source_data_verification_rate",

    "informed_consent_compliance",

  ]);


/* ============================================================
 * SCORE FIELDS
 * ============================================================
 */

const SCORE_FIELDS =
  new Set<string>([

    "risk_score",

    "risk_indicator_score",

  ]);


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
 * VALUE FORMATTER
 * ============================================================
 */

const formatValue = (
  key: string,
  value: unknown
): string => {


  if (
    value === null ||
    value === undefined
  ) {

    return "—";

  }


  if (
    typeof value === "boolean"
  ) {

    return value
      ? "Yes"
      : "No";

  }


  if (
    typeof value === "number"
  ) {


    if (
      PERCENTAGE_FIELDS.has(key)
    ) {

      return `${formatNumber(value)}%`;

    }


    if (
      SCORE_FIELDS.has(key)
    ) {

      return `${formatNumber(value)} / 100`;

    }


    return formatNumber(value);

  }


  if (
    typeof value === "string"
  ) {

    return value;

  }


  return String(value);

};


/* ============================================================
 * BADGE CLASS
 * ============================================================
 */

const getBadgeClass = (
  value: unknown
): string | null => {


  if (
    typeof value !== "string"
  ) {

    return null;

  }


  const normalized =
    value
      .toLowerCase()
      .trim();


  if (
    normalized === "low"
  ) {

    return "badge badge-low";

  }


  if (
    normalized === "medium"
  ) {

    return "badge badge-medium";

  }


  if (
    normalized === "high"
  ) {

    return "badge badge-high";

  }


  if (
    normalized === "critical"
  ) {

    return "badge badge-critical";

  }


  return null;

};


/* ============================================================
 * SIMPLE VALUE
 * ============================================================
 */

const renderSimpleValue = (
  key: string,
  value: unknown
): ReactNode => {


  const badgeClass =
    getBadgeClass(value);


  if (
    badgeClass
  ) {

    return (

      <span
        className={badgeClass}
      >

        {
          formatValue(
            key,
            value
          )
        }

      </span>

    );

  }


  return (

    <strong>

      {
        formatValue(
          key,
          value
        )
      }

    </strong>

  );

};


/* ============================================================
 * MARKDOWN CONTENT
 * ============================================================
 */

const renderMarkdownContent = (
  value: string
): ReactNode => {

  return (

    <div className="agent-markdown">

      <ReactMarkdown>

        {value}

      </ReactMarkdown>

    </div>

  );

};


/* ============================================================
 * ARRAY
 * ============================================================
 */

const renderArray = (
  values: unknown[]
): ReactNode => {


  if (
    values.length === 0
  ) {

    return (

      <p className="empty-value">

        No records available.

      </p>

    );

  }


  return (

    <div className="json-array">

      {
        values.map(
          (
            item,
            index
          ) => {


            if (
              item !== null &&
              typeof item === "object"
            ) {

              return (

                <div
                  className="json-array-item"
                  key={index}
                >

                  {
                    renderObject(
                      item as JsonObject
                    )
                  }

                </div>

              );

            }


            return (

              <div
                className="json-array-simple-item"
                key={index}
              >

                {
                  formatValue(
                    "",
                    item
                  )
                }

              </div>

            );

          }
        )
      }

    </div>

  );

};


/* ============================================================
 * OBJECT
 * ============================================================
 */

const renderObject = (
  value: JsonObject
): ReactNode => {

  return (

    <div className="kv">

      {
        Object.entries(
          value
        ).map(
          ([
            key,
            nestedValue,
          ]) => (

            <div
              className="kv-row"
              key={key}
            >

              <span>

                {titleCase(key)}:

              </span>


              <div className="kv-value">

                {
                  renderNestedValue(
                    key,
                    nestedValue
                  )
                }

              </div>

            </div>

          )
        )
      }

    </div>

  );

};


/* ============================================================
 * NESTED VALUE
 * ============================================================
 */

function renderNestedValue(
  key: string,
  value: unknown
): ReactNode {


  if (
    Array.isArray(value)
  ) {

    return renderArray(value);

  }


  if (
    value !== null &&
    typeof value === "object"
  ) {

    return renderObject(
      value as JsonObject
    );

  }


  if (
    typeof value === "string" &&
    (
      value.includes("\n") ||
      value.includes("**") ||
      value.includes("- ") ||
      /^\d+\./m.test(value)
    )
  ) {

    return renderMarkdownContent(
      value
    );

  }


  return renderSimpleValue(
    key,
    value
  );

}


/* ============================================================
 * JSON SECTION
 * ============================================================
 */

export default function JsonSection({
  title,
  value,
}: JsonSectionProps) {


  /* ==========================================================
   * MARKDOWN STRING
   * ==========================================================
   */

  if (
    typeof value === "string" &&
    (
      value.includes("\n") ||
      value.includes("**") ||
      value.includes("- ") ||
      /^\d+\./m.test(value)
    )
  ) {

    return (

      <article className="agent-summary-section">

        {
          renderMarkdownContent(
            value
          )
        }

      </article>

    );

  }


  /* ==========================================================
   * ARRAY
   * ==========================================================
   */

  if (
    Array.isArray(value)
  ) {

    return (

      <article className="result-card">

        <h3>

          {titleCase(title)}

        </h3>


        {
          renderArray(value)
        }

      </article>

    );

  }


  /* ==========================================================
   * OBJECT
   * ==========================================================
   */

  if (
    value !== null &&
    typeof value === "object"
  ) {

    return (

      <article className="result-card">

        <h3>

          {titleCase(title)}

        </h3>


        {
          renderObject(
            value as JsonObject
          )
        }

      </article>

    );

  }


  /* ==========================================================
   * SIMPLE VALUE
   * ==========================================================
   */

  return (

    <article className="result-card">

      <h3>

        {titleCase(title)}

      </h3>


      <div className="simple-value">

        {
          renderSimpleValue(
            title,
            value
          )
        }

      </div>

    </article>

  );

}