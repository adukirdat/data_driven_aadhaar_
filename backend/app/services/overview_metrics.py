from app.services.enrolment_metrics import compute_child_enrolment_delay
from app.services.biometric_metrics import compute_update_neglect
from app.services.migration_metrics import compute_migration_mismatch
from app.services.asi_metrics import compute_asi


def compute_overview_summary():
    enrolment = compute_child_enrolment_delay()
    update_neglect = compute_update_neglect()
    migration = compute_migration_mismatch()
    asi = compute_asi()

    summary = {
        "highRiskDistricts": len([s for s in asi if s["category"] == "High"]),
        "delayedChildEnrolmentDistricts": len(
            [e for e in enrolment if e["child_delay_percentage"] > 20]
        ),
        "highUpdateNeglectDistricts": len(
            [u for u in update_neglect if u["update_neglect_percentage"] > 35]
        ),
        "highBiometricStressDistricts": len(
            [s for s in asi if s["update_neglect"] > 40]
        )
    }

    return summary


def compute_top_priority_states(limit: int = 5):
    asi = compute_asi()

    top_states = []
    for row in asi[:limit]:
        issue = (
            "Severe enrolment delays"
            if row["enrolment_delay"] > row["update_neglect"]
            else "High update neglect"
        )

        top_states.append({
            "state": row["state"],
            "severity": row["category"],
            "primaryIssue": issue
        })

    return top_states
