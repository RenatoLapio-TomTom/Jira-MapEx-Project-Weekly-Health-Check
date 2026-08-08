# Jira MapEx Project Health Check Report - 2026-08-08

_Generated on 2026-08-08 by automated GitHub Actions workflow._


## 1. Executive Summary

**Overall Health:** 🔴

**Scope:** 1165 tickets analyzed | 2026-05-10 → 2026-08-08 <span style="color:red"><strong>**Remark: only tickets created by Non-Map Experts are considered here*</strong></span>

**Rejection Rate:** 6 disputed/flagged vs 873 total closed tickets in the last 90 days

**Schedule Health:**

- 39 overdue (3 critical, 6 high)
- 2 blocked tickets with due dates
- 34 due within 14 days, not started
- 3 stale (no update 30+ days)

**Top 5 Urgent Tickets:**

- **MAPEX-8926** (Critical) — Source validation IM: ESP [82d overdue]
- **MAPEX-8995** (Critical) — Admin Area Maintenance 2026 Q3 – Source scouting and delivery for APA [50d overdue]
- **MAPEX-11706** (Critical) — Minimum polygon area for areas and postal layer [1d overdue]
- **MAPEX-9291** (High) — Area & Postal language coverage [71d overdue]
- **MAPEX-9223** (High) — TTI - QC June-July 2026 - Global Events - APA [61d overdue]

**Assignee Overload (3+ flagged tickets):**

- Nikki Royce: 17 flagged tickets
- Daniel Jooste: 5 flagged tickets
- Daniel Roy: 4 flagged tickets
- Lahu Navsupe: 4 flagged tickets
- Massimo Vallainc: 4 flagged tickets
- Kristian Georg Klem: 4 flagged tickets
- Berk Ulupinar: 3 flagged tickets
- Carole Vallee: 3 flagged tickets
- Dario Spinazzola: 3 flagged tickets
- Dana Stepitova: 3 flagged tickets

**Recommendations:**

1. 🔴 Immediately review and address 3 critical overdue ticket(s) — these are >90 days late or blocker priority.
2. 🟡 Unblock 2 ticket(s) that are blocked and have due dates to prevent further schedule slippage.
3. 🟡 Triage 3 stale ticket(s) with no updates for 30+ days — close if obsolete or reassign/re-prioritize.


## 2. Rejected / Disputed Tickets

Tickets where work was potentially rejected or challenged, identified through resolution status, reopening history, comment keywords, or reporter post-closure activity.

| Key | Summary | Status | Resolution | Reporter | Assignee | Signal | Evidence | Severity |
|-----|---------|--------|------------|----------|----------|--------|----------|----------|
| MAPEX-11762 | Source Validation: USA_Admin_Area_Alignment_Support(County Subdivision_Batch 3) | Closed | Done | Vaishali Patil | Nikki Royce | Dissatisfaction keyword in comment | Comment by Nikki Royce: "Hi  , I've updated the country val db. You may still get the neighborhood count failures in rerun and if so please reope…" | High |
| MAPEX-10851 | Source Validation Support: Postal IRL | Open | — | Prakash Mahirarao | Nikki Royce | Reopened after closure | Status WAS Closed, now reopened | Medium |
| MAPEX-11565 | Need to support for OM-372756 (Q3 Street Name Centerline Maintenance - Open data — AUS Source Prep) | Closed | Done | SitaRamireddy Tippireddy | Kuntida Uampranee | Reporter commented after closure | Reporter comment after resolution: "Thank you for feedback and missing green arrow marks in feedback PPT, KIndly review and provide the feedback , Thank y…" | Low |
| MAPEX-11616 | Please provide source for airport geometry issue at -37.00462,174.79160 | Closed | Done | Parul Mittal | Peter LeGras | Reporter commented after closure | Reporter comment after resolution: "Hi   , As per your input we have updated MDS at -37.0048434, 174.7913311, 19, below find the snapshot. Kindly let us kno…" | Low |
| MAPEX-11618 | POI IM-73563 DEU - Request to verify and confirm existence | Closed | Done | Amrapali Shirsat | Andreas Leißner | Reporter commented after closure | Reporter comment after resolution: "Hi  , Thank you for your feedback. Could you please confirm whether we can add the Parking Area POI together with its ne…" | Low |
| MAPEX-11563 | Confirmation needed for Street Name update and Duplicate APT resolution | USA-TN | Closed | Done | Sonal Hardikar | Luca Comi | Reporter commented after closure | Reporter comment after resolution: "Thank you for the feedback. The database has been updated.…" | Low |


## 3. At-Risk / Late Tickets

Tickets that are overdue, blocked, stale, or at risk of missing their deadline. Tickets with status _On Hold_, _Blocked_, or _Closed_ are excluded from this table (though relevant metrics appear in the Executive Summary).

| Key | Summary | Status | Due Date | Closed Date | Days Overdue | Assignee | Priority | Risk Category | Risk Level |
|-----|---------|--------|----------|-------------|--------------|----------|----------|---------------|------------|
| MAPEX-8926 | Source validation IM: ESP | Open | 2026-05-18 | — | 82 | Nikki Royce | Blocker | Open Overdue | Critical |
| MAPEX-8995 | Admin Area Maintenance 2026 Q3 – Source scouting and delivery for APA | Open | 2026-06-19 | — | 50 | Tanawat Chamnongkijphanich | Blocker | Open Overdue | Critical |
| MAPEX-11706 | Minimum polygon area for areas and postal layer | In Progress | 2026-08-07 | — | 1 | Ben Esquivel | Blocker | Open Overdue | Critical |
| MAPEX-9291 | Area & Postal language coverage | Open | 2026-05-29 | — | 71 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-9223 | TTI - QC June-July 2026 - Global Events - APA | Open | 2026-06-08 | — | 61 | Daniel Jooste | Major | Open Overdue | High |
| MAPEX-9377 | SO_TMC Source 2026 TUR HERE 7 | Open | 2026-06-10 | — | 59 | Berk Ulupinar | Major | Open Overdue | High |
| MAPEX-9922 | USA - New Mexico: Speed limit values not conforming to current maxspeed rule (non-multiples of 5) — USA | In Progress | 2026-06-22 | — | 47 | Tim Bethke | Major | Open Overdue | High |
| MAPEX-10123 | Source Validation Support: KOR IM-63984 | Backlog | 2026-06-26 | — | 43 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-10042 | MapReady Source Missing from Source Inventory | Open | 2026-06-26 | — | 43 | Chiara Angiolini | Major | Open Overdue | High |
| MAPEX-10706 | COL orbis admin area source validation Q3 | Backlog | 2026-07-10 | — | 29 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-10707 | SRB orbis admin area source validation Q3 | Backlog | 2026-07-13 | — | 26 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-10704 | ISL orbis admin area source validation Q3 | Backlog | 2026-07-13 | — | 26 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-10851 | Source Validation Support: Postal IRL | Open | 2026-07-15 | — | 24 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-10263 | Scoping inconsistency of PlaceChain members | Backlog | 2026-07-18 | — | 21 | Nikki Royce | Critical | Open Overdue | Medium |
| MAPEX-10262 | Scoping Germany AA issues | In Progress | 2026-07-18 | — | 21 | Nikki Royce | Critical | Open Overdue | Medium |
| MAPEX-10881 | GEN source -EGY Postal source delivery | Backlog | 2026-07-21 | — | 18 | Daniel Jooste | Major | Open Overdue | Medium |
| MAPEX-10880 | GEN source -ZAF Postal source delivery | Backlog | 2026-07-21 | — | 18 | Daniel Jooste | Major | Open Overdue | Medium |
| MAPEX-10879 | GEN source -MAR Postal source delivery | Backlog | 2026-07-21 | — | 18 | Daniel Jooste | Major | Open Overdue | Medium |
| MAPEX-10863 | Availability of Reliable Sources for Road–Boundary Topology Validation (FRA) | In Progress | 2026-07-21 | — | 18 | Carole Vallee | Major | Open Overdue | Medium |
| MAPEX-11045 | DZA Orbis admin source validation Q3 | Backlog | 2026-07-24 | — | 15 | Nikki Royce | Critical | Open Overdue | Medium |
| MAPEX-10690 | Investigate Additional Countries with Secondary Addresses | In Progress | 2026-07-30 | — | 9 | Paulina Olszak | Major | Open Overdue | Medium |
| MAPEX-10882 | Do we need continuity script after primer? | In Progress | 2026-07-31 | — | 8 | Lukasz Urbaniak | Major | Open Overdue | Medium |
| MAPEX-10552 | MSFT ACI NSM Support - East Europe & Central Asia - JULY 2026 | In Progress | 2026-07-31 | — | 8 | Dario Spinazzola | Critical | Open Overdue | Medium |
| MAPEX-10387 | Onboarding & Training for Szabolcs | In Progress | 2026-07-31 | — | 8 | Szabolcs Szász | Major | Open Overdue | Medium |
| MAPEX-11441 | IND Orbis Admin Area Maintenance: source validation Q3 POC | Backlog | 2026-08-03 | — | 5 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11452 | Source Validation Support - Q3Postal - NOR | Backlog | 2026-08-04 | — | 4 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11417 | Required exonyms in multiple languages for Kumpupintil Lake | Backlog | 2026-08-04 | — | 4 | Dario Spinazzola | Major | Open Overdue | Medium |
| MAPEX-11263 | Surface RM in LM (LM) | In Progress | 2026-08-04 | — | 4 | Daniel Roy | Major | Open Overdue | Medium |
| MAPEX-10884 | GEN source -TUR Postal source delivery | Open | 2026-08-05 | — | 3 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-11503 | LTU Orbis Admin area source validation Q3 | Backlog | 2026-08-06 | — | 2 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11707 | IDN Orbis Admin Area Maintenance: IDN_Phase_2_Batch_2_Merge source validation Q3 | Backlog | 2026-08-07 | — | 1 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11669 | Changes in JFK Terminal 5, Queens, NY | USA-NY | In Progress | 2026-08-07 | — | 1 | Tim Bethke | Major | Open Overdue | Medium |
| MAPEX-11538 | Truck restriction at Wrocław - Poland | Backlog | 2026-08-07 | — | 1 | Dario Spinazzola | Major | Open Overdue | Medium |
| MAPEX-11537 | RM | Speed bumps ADE Stats query per country kms | In Progress | 2026-08-07 | — | 1 | Lahu Navsupe | Minor | Open Overdue | Medium |
| MAPEX-11353 | Is it possible to improve Orbis MBP with Genesis barriers? | In Progress | 2026-08-07 | — | 1 | Daniel Roy | Major | Open Overdue | Medium |
| MAPEX-10788 | Remove old LEZ ADE queries | In Progress | 2026-08-07 | — | 1 | Daniel Roy | Major | Open Overdue | Medium |
| MAPEX-10779 | [LM]  Pedestrian crossings CC rule identification [Q3] | In Progress | 2026-08-07 | — | 1 | Lahu Navsupe | Major | Open Overdue | Medium |
| MAPEX-10047 | TUR - Procurement Request: Amazon Gift Cards — OSM League 2026 | In Progress | 2026-08-07 | — | 1 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-9825 | check LEZ polys and alignment with roads in Genesis | Backlog | 2026-08-07 | — | 1 | Daniel Roy | Critical | Open Overdue | Medium |
| MAPEX-11800 | Tyne Tunnel has a 4.8m height limit, while TomTom shows 13’2”. | Backlog | 2026-08-10 | — | n/a | Dana Stepitova | Major | Due Soon – Not Started | Medium |
| MAPEX-11799 | Q3 APT Maintenance - Open data — HKG- Queries | Backlog | 2026-08-11 | — | n/a | Sunny Ji | Major | Due Soon – Not Started | Medium |
| MAPEX-11798 | Need to support for IM-73523 (Corrective action:Additional Scope the APTs that need HN normalization and if they need to be spread (instead of keeping them stacked APTs)) | Backlog | 2026-08-11 | — | n/a | Dana Stepitova | Critical | Due Soon – Not Started | Medium |
| MAPEX-11796 | Truck Restriction- Ostiglia- ITA | Backlog | 2026-08-11 | — | n/a | Massimo Vallainc | Minor | Due Soon – Not Started | Medium |
| MAPEX-11795 | Challenge Notification | Serbia - Missing Brand Names on POIs | Backlog | 2026-08-10 | — | n/a | Mile Milkovski | Major | Due Soon – Not Started | Medium |
| MAPEX-11782 | Suggestion for Area Element Update in EGY | Backlog | 2026-08-12 | — | n/a | Ziad Abd Alhamed | Major | Due Soon – Not Started | Medium |
| MAPEX-11777 | FRA_Lock2 Genesis admin area source observations | Backlog | 2026-08-10 | — | n/a | Carole Vallee | Major | Due Soon – Not Started | Medium |
| MAPEX-11775 | LE Feedback- On English Latin language Notation | Planned | 2026-08-10 | — | n/a | Alberto Saini | Major | Due Soon – Not Started | Medium |
| MAPEX-11771 | Orbis-Road–Boundary Topology Validation for — FRA Queries | Backlog | 2026-08-12 | — | n/a | Massimo Vallainc | Major | Due Soon – Not Started | Medium |
| MAPEX-11768 | Required exonyms for toll gate POI- ARE | Backlog | 2026-08-12 | — | n/a | Devidas Thite | Major | Due Soon – Not Started | Medium |
| MAPEX-11760 | Parking Garage in Amazonas - Brazil | Backlog | 2026-08-10 | — | n/a | Zorka Marinovic | Major | Due Soon – Not Started | Medium |
| MAPEX-11758 | IM Support: Admin_GBR | Backlog | 2026-08-10 | — | n/a | Nikki Royce | Blocker | Due Soon – Not Started | Medium |
| MAPEX-11751 | IDN Orbis Admin Area Maintenance: IDN_Phase_2_Batch_3_Merge source validation Q3 | Backlog | 2026-08-11 | — | n/a | Nikki Royce | Major | Due Soon – Not Started | Medium |
| MAPEX-11744 | POI IM-73269 ISR - Request to verify and confirm existence | Backlog | 2026-08-11 | — | n/a | Massimo Vallainc | Major | Due Soon – Not Started | Medium |
| MAPEX-11741 | Need more source support to remove MD (Coutry FRA) | Backlog | 2026-08-12 | — | n/a | Carole Vallee | Major | Due Soon – Not Started | Medium |
| MAPEX-11697 | Customer request to Need to assign one-way at -22.812440343180246 | Open | 2026-08-11 | — | n/a | Maximiliano Jaida Santander | Major | Due Soon – Not Started | Medium |
| MAPEX-11659 | NOR Name Library- Prefix and Suffix component feedback (LE) | Backlog | 2026-08-14 | — | n/a | Kristian Georg Klem | Critical | Due Soon – Not Started | Medium |
| MAPEX-11657 | Realign Geometry at 38.76902189107443, -9.129564338476435, | Open | 2026-08-11 | — | n/a | Maximiliano Jaida Santander | Major | Due Soon – Not Started | Medium |
| MAPEX-11617 | Analysis Rule traffic calming [speed bump] Toyota delivery August | Backlog | 2026-08-16 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-11614 | CC rule Analysis Traffic light at connector Toyota delivery (August) | Backlog | 2026-08-16 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-11464 | Assess and determine causes of RNF for restriction islands | Backlog | 2026-08-14 | — | n/a | Supannachat Metta | Major | Due Soon – Not Started | Medium |
| MAPEX-11446 | IDN Orbis Admin Area Maintenance: IDN_Phase_2_Batch_1_Merge source validation Q3 | Planned | 2026-08-11 | — | n/a | Nikki Royce | Major | Due Soon – Not Started | Medium |
| MAPEX-11440 | EST SCaaS: Street Name Pair Validation by Native Estonian Speakers — EST | Backlog | 2026-08-14 | — | n/a | Anna Mesterhazy | Major | Due Soon – Not Started | Medium |
| MAPEX-11265 | [School Zones] additional analysis based on Cariad feedback | Planned | 2026-08-14 | — | n/a | Erik Follensbee | Major | Due Soon – Not Started | Medium |
| MAPEX-11182 | [OA33/ON35] Gradient: Ensure new tag confidence:property:gradient is aligned with gradient:linear | Backlog | 2026-08-17 | — | n/a | Ted Yates | Major | Due Soon – Not Started | Medium |
| MAPEX-11106 | ISL SCaaS: Street Name Pair Validation by Native Speakers — ISL | Backlog | 2026-08-14 | — | n/a | Kristian Georg Klem | Critical | Due Soon – Not Started | Medium |
| MAPEX-10974 | MapEXP Analysis- USA 10 States for APT Sync at Orbis Side - July,26 | Planned | 2026-08-19 | — | n/a | Rajendra Nirgude | Critical | Due Soon – Not Started | Medium |
| MAPEX-10878 | GEN source -NOR Postal source delivery | Open | 2026-08-17 | — | n/a | Kristian Georg Klem | Major | Due Soon – Not Started | Medium |
| MAPEX-10874 | GEN source -DNK Postal source delivery | Open | 2026-08-17 | — | n/a | Kristian Georg Klem | Major | Due Soon – Not Started | Medium |
| MAPEX-10737 | SWE: Building Names Handling in Auto Source Process – Proposal & Data Normalization | Backlog | 2026-08-14 | — | n/a | Sneha Deshpande | Major | Due Soon – Not Started | Medium |
| MAPEX-10377 | Onboarding & Training for Dana | Planned | 2026-08-15 | — | n/a | Dana Stepitova | Major | Due Soon – Not Started | Medium |
| MAPEX-10024 | COL: Scan existing data to identify sub-address scope and normalization needs | Planned | 2026-08-17 | — | n/a | Sneha Deshpande | Major | Due Soon – Not Started | Medium |
| MAPEX-9694 | Toll GTD - Local Expert checks for US-IL (prio 5) | Open | 2026-08-21 | — | n/a | Kate Meyer | Critical | Due Soon – Not Started | Medium |
| MAPEX-9382 | SO_TMC Source 2026 ARE HERE 11 | Open | 2026-08-17 | — | n/a | Devidas Thite | Major | Due Soon – Not Started | Medium |
| MAPEX-10013 | TTI - TTI Support Q2-Q3-Q4 2026 - AFR | In Progress | — | — | n/a | Daniel Jooste | Major | Stale | Low |
| MAPEX-10008 | TTI - TTI Support Q2-Q3-Q4 2026 - SWE | Planned | — | — | n/a | Massimo Vallainc | Major | Stale | Low |
| MAPEX-9989 | TTI - TTI Support Q2-Q3-Q4 2026 - NCE | In Progress | — | — | n/a | Bernhard Braun | Major | Stale | Low |


## 4. Follow-up

The table below lists all flagged tickets (excluding _Due Soon – Not Started_ and _Closed Late_ categories) that require follow-up action. Assignees are asked to review their tickets, provide a status update in the **Follow-up Status** column, and propose a recommendation in the **User Recommendation** column.

**Why follow-up matters:** Timely follow-up on flagged tickets prevents recurring issues, supports continuous improvement, and ensures the project maintains healthy delivery rhythms. For the **User Recommendation** column, consider actions such as: adjusting the process that led to the delay, updating documentation, re-scoping the ticket, or escalating blockers.

| Key | Assignee | Follow-up Status | Reason for Flagging | User Recommendation |
|-----|----------|-----------------|---------------------|---------------------|
| MAPEX-8926 | Nikki Royce | _(to be filled)_ | Open Overdue — Critical risk | _(to be filled)_ |
| MAPEX-8995 | Tanawat Chamnongkijphanich | _(to be filled)_ | Open Overdue — Critical risk | _(to be filled)_ |
| MAPEX-11706 | Ben Esquivel | _(to be filled)_ | Open Overdue — Critical risk | _(to be filled)_ |
| MAPEX-9291 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-9223 | Daniel Jooste | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-9377 | Berk Ulupinar | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-9922 | Tim Bethke | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10123 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10042 | Chiara Angiolini | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10706 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10707 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10704 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10851 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10263 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10262 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10881 | Daniel Jooste | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10880 | Daniel Jooste | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10879 | Daniel Jooste | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10863 | Carole Vallee | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11045 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10690 | Paulina Olszak | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10882 | Lukasz Urbaniak | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10552 | Dario Spinazzola | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10387 | Szabolcs Szász | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11441 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11452 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11417 | Dario Spinazzola | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11263 | Daniel Roy | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10884 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11503 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11707 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11669 | Tim Bethke | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11538 | Dario Spinazzola | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11537 | Lahu Navsupe | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11353 | Daniel Roy | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10788 | Daniel Roy | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10779 | Lahu Navsupe | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10047 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-9825 | Daniel Roy | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10013 | Daniel Jooste | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-10008 | Massimo Vallainc | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-9989 | Bernhard Braun | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
