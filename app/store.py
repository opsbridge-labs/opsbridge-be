from datetime import datetime

EVENTS = [
    {"id": "evt-1", "title": "change request state machine", "status": "requested", "severity": "high", "updatedAt": datetime.utcnow().date().isoformat()},
    {"id": "evt-2", "title": "approval console", "status": "approved", "severity": "medium", "updatedAt": datetime.utcnow().date().isoformat()},
]

METRICS = [
    {"key": "audit_search_p95_ms", "label": "audit search p95 ms", "value": 184, "unit": "ms", "target": 220},
    {"key": "rollback_duration_ms", "label": "rollback duration ms", "value": 92, "unit": "%", "target": 90},
    {"key": "state_transition_success_rate", "label": "state transition success rate", "value": 37, "unit": "events", "target": 30},
]
