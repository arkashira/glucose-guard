# Glucose Guard – Product Requirements Document (PRD)

**Document Version:** 1.0  
**Last Updated:** 2026‑06‑26  
**Owner:** Senior Product/Engineering Lead, Axentx OS  
**Repository:** `glucose-guard`  

---

## 1. Problem Statement

People with diabetes rely on continuous glucose monitoring (CGM) devices to stay within safe glucose ranges. Existing consumer‑grade CGM apps provide raw data but often lack:

* **Real‑time, actionable alerts** (e.g., “high glucose – consider insulin”).
* **User‑friendly snooze/dismiss workflows** that respect daily activities.
* **A lightweight, extensible simulation layer** for developers, researchers, and device manufacturers to prototype alert logic without needing hardware.

The current open‑source `GlucoseGuard` repository is a minimal stub that only simulates data updates and basic alert checks. It does not provide a production‑ready API, configurability, or integration hooks, limiting its adoption and commercial potential.

---

## 2. Target Users & Personas

| Persona | Description | Pain Points | Desired Outcome |
|---------|-------------|-------------|-----------------|
| **Diabetes Tech Developers** | Engineers building CGM‑related software (apps, dashboards, hardware firmware). | Need a sandbox to test alert algorithms without physical devices. | A deterministic, configurable simulation API with plug‑in support. |
| **Clinical Researchers** | Scientists evaluating glucose‑control interventions. | Require reproducible glucose streams and controlled alert scenarios for studies. | Ability to script patient profiles, inject events, and export logs. |
| **Product Managers (Health‑Tech)** | Leaders evaluating market fit of new CGM features. | Need rapid prototyping to validate user‑experience concepts. | A ready‑to‑demo UI mock‑up and API that can be showcased to stakeholders. |
| **End‑User Advocates** | Non‑technical advocates who test accessibility and usability. | Lack of a simple UI to experience alerts and snooze flows. | A minimal web/mobile UI that demonstrates the alert lifecycle. |

---

## 3. Goals & Success Metrics

| Goal | Success Metric (quantitative) | Target |
|------|------------------------------|--------|
| **Deliver a production‑grade simulation engine** | Unit‑test coverage ≥ 90% | Achieved |
| **Enable configurable alert thresholds & policies** | Number of configurable parameters exposed via JSON/YAML | ≥ 12 |
| **Provide a pluggable alert‑handler framework** | Number of third‑party adapters shipped in first release | ≥ 3 (e.g., email, SMS, webhook) |
| **Expose a simple UI for demo & accessibility testing** | Monthly active demo users (via hosted demo) | ≥ 500 within 3 months |
| **Validate market interest** | Signed letters of intent (LOIs) from at least 2 CGM device partners | Within 6 weeks of beta launch |
| **Maintain low latency** | End‑to‑end alert propagation ≤ 150 ms (simulated) | Measured in CI performance tests |

---

## 4. Scope

### In‑Scope (Phase 1 – MVP)

1. **Core Simulation Engine**  
   * `GlucoseGuard` class with:
     * Real‑time glucose stream generator (configurable sampling rate, noise model).  
     * Alert detection based on configurable high/low thresholds and rate‑of‑change rules.  
     * State machine for alert lifecycle: *Active → Snoozed → Dismissed → Resolved*.  

2. **Configuration Layer**  
   * JSON/YAML schema to define:
     * Patient profile (baseline glucose, variability).  
     * Alert policies (thresholds, hysteresis, snooze duration).  
     * Output sinks (log file, stdout, webhook).  

3. **Pluggable Alert Handlers**  
   * Interface `AlertHandler` with methods `on_alert`, `on_snooze`, `on_dismiss`.  
   * Built‑in adapters:
     * Console logger (default).  
     * HTTP webhook sender.  
     * Email (SMTP) notifier.  

4. **CLI & Test Harness**  
   * `glucose_guard/run.py` – command‑line entry point to start a simulation with a config file.  
   * Full pytest suite covering engine, config parsing, and each handler.  

5. **Documentation & SDK**  
   * Auto‑generated API docs (Sphinx).  
   * Quick‑start guide, example configs, and contribution guidelines.  

### Out‑of‑Scope (Phase 2+)

| Item | Reason |
|------|--------|
| **Hardware integration** (direct CGM device communication) | Requires regulatory compliance; deferred to partner co‑development. |
| **Full‑featured mobile app** | MVP UI will be a lightweight web demo; native apps are future work. |
| **Machine‑learning predictive alerts** | Scope limited to rule‑based alerts; ML models can be added as plug‑ins later. |
| **Regulatory certification (e.g., FDA)** | Not a medical device; intended for simulation and prototyping only. |
| **Multi‑user authentication & data privacy** | Out of scope for a sandbox environment; can be layered by downstream products. |

---

## 5. Key Features (Prioritized)

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **P1** | **Configurable Glucose Stream** | Generate synthetic glucose readings with realistic variability. | • Config file defines mean, variance, sampling interval.<br>• Stream can be paused/resumed via CLI. |
| **P1** | **Rule‑Based Alert Engine** | Detect high/low glucose and rapid changes per policy. | • Alerts fire when readings cross thresholds for ≥ N seconds.<br>• No false positives on noise within hysteresis band. |
| **P1** | **Alert Lifecycle (Snooze/Dismiss)** | Users can snooze (delay) or dismiss alerts; system respects state. | • Snooze duration configurable.<br>• Dismissed alerts do not re‑trigger until new condition. |
| **P2** | **Pluggable Alert Handlers** | Extensible interface for custom notification channels. | • At least three built‑in handlers pass integration tests.<br>• Third‑party handler can be loaded via entry‑point. |
| **P2** | **CLI Control & Monitoring** | Start/stop simulations, view live stats, export logs. | • `--config`, `--duration`, `--output` flags work as documented.<br>• Real‑time console dashboard shows current glucose & alert state. |
| **P3** | **Web Demo UI** | Minimal Flask/React UI to visualize glucose curve and alerts. | • UI updates in < 200 ms after each simulated reading.<br>• Users can click “Snooze” or “Dismiss” on alerts. |
| **P3** | **Persisted Session Replay** | Export simulation run to JSON for later replay. | • `--export` flag writes complete event log.<br>• Replay mode reproduces identical alert timeline. |
| **P4** | **Metrics Exporter** | Emit Prometheus metrics (alert count, latency). | • `/metrics` endpoint exposes standard counters and histograms. |

---

## 6. Success Metrics (Detailed)

| Metric | Measurement Method | Target | Frequency |
|--------|--------------------|--------|-----------|
| **Unit Test Coverage** | `coverage.py` report | ≥ 90 % | Every CI run |
| **Alert Latency** | Timestamp diff between reading crossing threshold and handler invocation | ≤ 150 ms | CI performance test |
| **Configuration Flexibility** | Count of top‑level keys in schema | ≥ 12 | Release audit |
| **Third‑Party Handler Adoption** | GitHub stars/forks of external adapters | ≥ 5 forks within 3 months | Quarterly |
| **Demo Adoption** | Unique IPs hitting demo UI | ≥ 500/mo | Monthly |
| **Partner LOIs** | Signed PDFs stored in `partners/` | ≥ 2 by Q3 2026 | Milestone |
| **Customer Satisfaction (Beta)** | Survey NPS on beta participants | ≥ 8/10 | Post‑beta |

---

## 7. Milestones & Timeline (MVP – 8 weeks)

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| 1 | Project Kick‑off & Requirements Freeze | Final PRD, repo scaffolding |
| 2 | Core Engine & Config Parser | `GlucoseGuard` class, schema validation |
| 3 | Alert Lifecycle & State Machine | Unit tests for snooze/dismiss |
| 4 | Alert Handler Interface + 2 Built‑ins | Console logger, webhook adapter |
| 5 | CLI & Test Harness | `run.py`, full pytest suite |
| 6 | Documentation & SDK | Sphinx docs, quick‑start guide |
| 7 | Web Demo UI (beta) | Flask server + React component |
| 8 | Performance Testing, Release Candidate | CI benchmarks, packaging, version bump to v0.1.0 |

*Post‑MVP (Phase 2) roadmap will address out‑of‑scope items.*

---

## 8. Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **Simulation realism insufficient** | Low adoption by researchers | Medium | Provide multiple noise models; allow custom RNG seeds. |
| **Alert handler security (webhook injection)** | Potential abuse if demo exposed publicly | Low | Validate URLs, enforce HTTPS, rate‑limit. |
| **Performance bottleneck on high‑frequency streams** | Missed latency targets | Medium | Optimize using `asyncio`; benchmark early. |
| **Scope creep into medical‑device certification** | Delays, regulatory overhead | Low | Explicitly label as “simulation only”; include legal disclaimer. |
| **Insufficient partner interest** | Failure to validate market | Medium | Early outreach to 3 CGM OEMs during design phase; incorporate feedback. |

---

## 9. Open Questions

1. **Data Export Format:** JSON vs. CSV for replay – need stakeholder preference.  
2. **Snooze Granularity:** Fixed duration vs. configurable per‑alert – decide in design review.  
3. **Authentication for Web Demo:** Anonymous vs. simple token – evaluate based on security review.

---

## 10. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | *[Name]* |  |  |
| Engineering Lead | *[Name]* |  |  |
| QA Lead | *[Name]* |  |  |
| Legal / Compliance | *[Name]* |  |  |

--- 

*End of Document*
