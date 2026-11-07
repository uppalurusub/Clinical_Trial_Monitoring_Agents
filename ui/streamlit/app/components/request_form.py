import streamlit as st


def render_request_form():
    with st.form("claim_form"):
        st.header("Patient Information")
        col1, col2 = st.columns(2)

        with col1:
            claim_id = st.text_input("Claim ID", "CLM20260001")
            patient_id = st.text_input("Patient ID", "PAT10001")
            patient_name = st.text_input("Patient Name", "John Doe")
            dob = st.date_input("Date of Birth")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        with col2:
            service_date = st.date_input("Service Date")
            total_claim_amount = st.number_input(
                "Total Claim Amount", min_value=0.0, value=500.0
            )

        st.divider()
        st.header("Insurance Information")
        col1, col2 = st.columns(2)

        with col1:
            insurance_provider_name = st.text_input(
                "Insurance Provider", "Blue Cross Blue Shield"
            )
            policy_number = st.text_input("Policy Number", "POL987654321")
            group_number = st.text_input("Group Number", "GRP10001")

        with col2:
            member_id = st.text_input("Member ID", "MEM123456789")
            authorization_number = st.text_input(
                "Authorization Number", "AUTH567890"
            )

        st.divider()
        st.header("Provider Information")
        col1, col2 = st.columns(2)

        with col1:
            provider_id = st.text_input("Provider ID", "PRV10001")
            provider_name = st.text_input("Provider Name", "Dr. Sarah Johnson")

        with col2:
            specialty = st.text_input("Specialty", "Cardiology")
            facility_name = st.text_input(
                "Facility Name", "City Heart Medical Center"
            )

        st.divider()
        st.header("Diagnosis Codes")
        diagnosis_count = st.number_input(
            "Number of Diagnosis Codes", min_value=1, max_value=10, value=2
        )
        diagnosis_codes = []

        for i in range(diagnosis_count):
            st.subheader(f"Diagnosis {i + 1}")
            c1, c2 = st.columns(2)
            with c1:
                code = st.text_input(
                    f"Diagnosis Code {i + 1}",
                    value="I10" if i == 0 else "E11.9",
                    key=f"dcode{i}",
                )
            with c2:
                description = st.text_input(
                    f"Description {i + 1}",
                    value=(
                        "Essential Hypertension"
                        if i == 0
                        else "Type 2 Diabetes Mellitus Without Complications"
                    ),
                    key=f"ddesc{i}",
                )
            diagnosis_codes.append({"code": code, "description": description})

        st.divider()
        st.header("Procedure Codes")
        procedure_count = st.number_input(
            "Number of Procedure Codes", min_value=1, max_value=20, value=3
        )
        procedure_codes = []
        defaults = [
            ("99214", "Office or Outpatient Visit", 1, 250),
            ("93000", "Electrocardiogram Complete", 1, 150),
            ("80053", "Comprehensive Metabolic Panel", 1, 100),
        ]

        for i in range(procedure_count):
            st.subheader(f"Procedure {i + 1}")
            p1, p2 = st.columns(2)
            default = defaults[i] if i < len(defaults) else ("", "", 1, 0)
            with p1:
                code = st.text_input(
                    f"Procedure Code {i + 1}", value=default[0], key=f"pcode{i}"
                )
                units = st.number_input(
                    f"Units {i + 1}",
                    min_value=1,
                    max_value=20,
                    value=default[2],
                    key=f"units{i}",
                )
            with p2:
                description = st.text_input(
                    f"Procedure Description {i + 1}",
                    value=default[1],
                    key=f"pdesc{i}",
                )
                charge_amount = st.number_input(
                    f"Charge Amount {i + 1}",
                    min_value=0.0,
                    value=float(default[3]),
                    key=f"amt{i}",
                )
            procedure_codes.append(
                {
                    "code": code,
                    "description": description,
                    "units": units,
                    "charge_amount": charge_amount,
                }
            )

        st.divider()
        notes = st.text_area(
            "Clinical Notes",
            "Follow-up visit for hypertension and diabetes management. "
            "ECG and laboratory tests performed.",
        )
        submitted = st.form_submit_button(
            "Process Claim", use_container_width=True
        )

    payload = {
        "claim_id": claim_id,
        "patient_id": patient_id,
        "patient_name": patient_name,
        "date_of_birth": str(dob),
        "gender": gender,
        "service_date": str(service_date),
        "insurance": {
            "provider_name": insurance_provider_name,
            "policy_number": policy_number,
            "group_number": group_number,
            "member_id": member_id,
            "authorization_number": authorization_number,
        },
        "provider": {
            "provider_id": provider_id,
            "provider_name": provider_name,
            "specialty": specialty,
            "facility_name": facility_name,
        },
        "diagnosis_codes": diagnosis_codes,
        "procedure_codes": procedure_codes,
        "total_claim_amount": total_claim_amount,
        "notes": notes,
    }
    return submitted, payload
