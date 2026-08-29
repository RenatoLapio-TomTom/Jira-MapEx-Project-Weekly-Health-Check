# Jira MapEx Project Health Check Report - 2026-08-29

_Generated on 2026-08-29 by automated GitHub Actions workflow._


## 1. Executive Summary

**Overall Health:** 🟡

**Scope:** 1392 tickets analyzed | 2026-05-31 → 2026-08-29 <span style="color:red"><strong>**Remark: only tickets created by Non-Map Experts are considered here*</strong></span>

**Rejection Rate:** 25 disputed/flagged vs 941 total closed tickets in the last 90 days

**Schedule Health:**

- 48 overdue (0 critical, 13 high)
- 3 blocked tickets with due dates
- 29 due within 14 days, not started
- 4 stale (no update 30+ days)

**Top 5 Urgent Tickets:**

- **MAPEX-9377** (High) — SO_TMC Source 2026 TUR HERE 7 [80d overdue]
- **MAPEX-9922** (High) — USA - New Mexico: Speed limit values not conforming to current maxspeed rule (non-multiples of 5) — USA [68d overdue]
- **MAPEX-10123** (High) — Source Validation Support: KOR IM-63984 [64d overdue]
- **MAPEX-10042** (High) — MapReady Source Missing from Source Inventory [64d overdue]
- **MAPEX-10706** (High) — COL orbis admin area source validation Q3 [50d overdue]

**Assignee Overload (3+ flagged tickets):**

- Nikki Royce: 21 flagged tickets
- Sneha Deshpande: 6 flagged tickets
- Daniel Roy: 6 flagged tickets
- Daniel Jooste: 4 flagged tickets
- Kalyan Dhaytonde: 3 flagged tickets
- Erik Follensbee: 3 flagged tickets

**Recommendations:**

2. 🟡 Unblock 3 ticket(s) that are blocked and have due dates to prevent further schedule slippage.
3. 🟡 Triage 4 stale ticket(s) with no updates for 30+ days — close if obsolete or reassign/re-prioritize.


## 2. Rejected / Disputed Tickets

Tickets where work was potentially rejected or challenged, identified through resolution status, reopening history, comment keywords, or reporter post-closure activity.

| Key | Summary | Status | Resolution | Reporter | Assignee | Signal | Evidence | Severity |
|-----|---------|--------|------------|----------|----------|--------|----------|----------|
| MAPEX-12209 | [CC] investigation violations for CA ON34 | In Progress | — | Olga Simakova | Kalyan Dhaytonde | Reopened after closure; Dissatisfaction keyword in comment | Status WAS Closed, now reopened | Comment by Kalyan Dhaytonde: "Hi    Please find analysis PPT. New RID 60901 & 60928 also included.       RID 60228: increase due to CA=yes added (repl…" | High |
| MAPEX-12539 | PAK default name issue | Closed | Done | Hiraman Chorghade | Devidas Thite | Dissatisfaction keyword in comment | Comment by Devidas Thite: "Hello    , Please find attached the English and Urdu names for all shared city/place entries across the three files. I f…" | High |
| MAPEX-10087 | POC: Airport POI Maintenance – Local Expert Validation (Top 05 Airports) | Open | — | Sathiya Seelan | Rico Kock | Dissatisfaction keyword in comment | Comment by Rico Kock: "Airport POI maintenance — where we stand (27 August 2026) Ground truth collected by Local Experts, scored against Orbis…" | High |
| MAPEX-12456 | RM Orbis Lane Information FRA Lane divider claryfikcation_2 | Closed | Done | Beata Kacprzak | Laurent Di Marzo | Dissatisfaction keyword in comment | Comment by Laurent Di Marzo: "Hi    CC    These 2 double white lines are considered as a Dual carriage way under the French Highway Code and must not…" | High |
| MAPEX-12308 | 60869 - Missing Traffic Light At Connector relation | Closed | Done | svc_Ops_Autotriggers | Anil Kasar | Dissatisfaction keyword in comment | Comment by Anil Kasar: "Examples -  After Crossing Light 10438_16148673856727613440_13129633898521607912 47.54981,7.71496 10438_1015561164300451…" | High |
| MAPEX-11706 | Minimum polygon area for areas and postal layer | Closed | Done | Diego Burgos Sancho | Ben Esquivel | Reporter commented after closure; Dissatisfaction keyword in comment | Comment by Diego Burgos Sancho: "Status update — MEX postal V18 (Postal Val) Source file:  ORPA_MEX_OM-368697_LayerId_27594_RevisionId_1_V18.gpkg  Event:…" | Reporter comment after resolution: "Status update — MEX postal V18 (Postal Val) Source file:  ORPA_MEX_OM-368697_LayerId_27594_RevisionId_1_V18.gpkg  Event:…" | High |
| MAPEX-12545 | POI IM-74517 FRA - Request to verify and confirm existence of Rest Area | Closed | Done | Amrapali Shirsat | Vincent Penalba | Dissatisfaction keyword in comment | Comment by Vincent Penalba: "Hi   , I have reviewed this POI and can confirm that it appears to be a junk POI. The name "Pause Clope" literally trans…" | High |
| MAPEX-12400 | Confirmation on Correct Character for Street Names in Taiwan | Closed | Done | Avej Shaikh | HC Yen | Dissatisfaction keyword in comment | Comment by HC Yen: "Hi,    The character  臺  is not incorrect. 台 is a variant of 臺. They have the same pronunciation and meaning.  台 & 臺 can…" | High |
| MAPEX-12359 | SAU Orbis Admin Area Maintenance:  Conformation about the Orbis Admin structure and geometry alignment | Open | — | Hiraman Chorghade | Nikki Royce | Reopened after closure; Dissatisfaction keyword in comment | Status WAS Closed, now reopened | Comment by Nikki Royce: "Hi Hiraman, Vaishali, I've reviewed this against the Orbis spec ( Has Index Info  feature group). The short answer is th…" | High |
| MAPEX-12150 | IM-71356- [CS0011435] [Nissan Motor Co., LTD] - School category changes in MEX after Orbis migration | Closed | Done | Prashant Kangude | Vicente Perez Nunez | Dissatisfaction keyword in comment | Comment by Vicente Perez Nunez: "Yes, the categories are generally fine; I only found a few isolated POIs that were in the Incorrect category.…" | High |
| MAPEX-11585 | Geopol Orbis 2026.Q4 JPN - Kit Review | Open | — | Milind Gaikwad | Moeka Tsuzuki | Dissatisfaction keyword in comment | Comment by Moeka Tsuzuki: "Thanks for the heads-up, and sorry for the wrong tagging.…" | High |
| MAPEX-12439 | NLD Amsterdam: incorrect lane direction attribution at s104 x A10 (Bos en Lommerplein) - middle lane mapped LEFT+STRAIGHT, reality STRAIGHT-only | Closed | Done | Živorad Baralić | Ron Bos | Dissatisfaction keyword in comment | Comment by Živorad Baralić: "thanks for fast reply. Initial assessment was that mapping was incorrect but if this is lates visual data from the fiel…" | High |
| MAPEX-12543 | Confirmation required to solve the IM-73893 | Open | — | Madhuri Nikam | Alberto Saini | Reopened after closure | Status WAS Closed, now reopened | Medium |
| MAPEX-10123 | Source Validation Support: KOR IM-63984 | Open | — | Vinayak Patil | Nikki Royce | Reopened after closure | Status WAS Closed, now reopened | Medium |
| MAPEX-12527 | ECA_North and Central Europe_Exonyms | Closed | Done | Pallavi Ghodake | Bernhard Braun | Reporter commented after closure | Reporter comment after resolution: "Hi   ,   ,    Sorry for the inconvenience. Could you please provide one more exonym in mentioned below? or should we con…" | Low |
| MAPEX-12526 | ECA_Eastern Europe and Central Asia_Exonyms | Closed | Done | Pallavi Ghodake | Dario Spinazzola | Reporter commented after closure | Reporter comment after resolution: "Hi   ,    Sorry for the inconvenience. Could you please provide one more exonym in mentioned below? English_Latin Polish…" | Low |
| MAPEX-12524 | APA_South East Asia and Oceania_Exonyms_IDN | Closed | Done | Pallavi Ghodake | Dino Afrianto | Reporter commented after closure | Reporter comment after resolution: "Hi   , Sorry for the inconvenience. Could you please provide one more exonym in mentioned below? Country English_Latin I…" | Low |
| MAPEX-12523 | APA_South East Asia and Oceania_Exonyms_CHE | Closed | Done | Pallavi Ghodake | HC Yen | Reporter commented after closure | Reporter comment after resolution: "Hi   Thank you.…" | Low |
| MAPEX-12479 | Source Required for Missing Island Names in Saudi Arabia | Closed | Done | Pallavi Ghodake | Devidas Thite | Reporter commented after closure | Reporter comment after resolution: "Hi   Thank you for the feedback.…" | Low |
| MAPEX-12495 | ESP - Built-up areas - queries | Closed | Done | Patrycja Bala | Massimo Vallainc | Reporter commented after closure | Reporter comment after resolution: "Hello   &   , Sorry, I didn't clarify in the description what exactly I meant. The production team is correcting these B…" | Low |
| MAPEX-12460 | RM Orbis Lane Information FRA Lane divider claryfikcation_3 | Closed | Done | Beata Kacprzak | Laurent Di Marzo | Reporter commented after closure | Reporter comment after resolution: "Hi   , I know this is the marking that separates the regular lane from the shoulder, but I want to know how it’s treated…" | Low |
| MAPEX-12434 | POI IM-74308 & IM-74316 ESP - Request to provide Rest Area details | Closed | Done | Amrapali Shirsat | Massimo Vallainc | Reporter commented after closure | Reporter comment after resolution: "Thanks for the feedback…" | Low |
| MAPEX-12405 | RM Orbis Lane Information FRA Lane divider claryfikcation | Closed | Done | Beata Kacprzak | Massimo Vallainc | Reporter commented after closure | Reporter comment after resolution: "Hi   , thank you Could you please update the section in ADi that lacks basic guidelines on this topic?…" | Low |
| MAPEX-12407 | POI IM-74203 FRA - Verify and confirm existence of Railway Station POI | Closed | Done | Amrapali Shirsat | Vincent Penalba | Reporter commented after closure | Reporter comment after resolution: "Thanks for the feedback…" | Low |
| MAPEX-11837 | Need Support on IM-73787 ([CS0012969] [Aspiegel SE] - Urgent：Missing ferry route in Italy OEM：BAIC) | Closed | Done | BalaMurali Tata | Gennaro Pesce | Reporter commented after closure | Reporter comment after resolution: "Thank you for providing the feedback. We observed that some ferry connections are already present in the database as p…" | Low |


## 3. At-Risk / Late Tickets

Tickets that are overdue, blocked, stale, or at risk of missing their deadline. Tickets with status _On Hold_, _Blocked_, or _Closed_ are excluded from this table (though relevant metrics appear in the Executive Summary).

| Key | Summary | Status | Due Date | Closed Date | Days Overdue | Assignee | Priority | Risk Category | Risk Level |
|-----|---------|--------|----------|-------------|--------------|----------|----------|---------------|------------|
| MAPEX-9377 | SO_TMC Source 2026 TUR HERE 7 | In Progress | 2026-06-10 | — | 80 | Berk Ulupinar | Major | Open Overdue | High |
| MAPEX-9922 | USA - New Mexico: Speed limit values not conforming to current maxspeed rule (non-multiples of 5) — USA | In Progress | 2026-06-22 | — | 68 | Tim Bethke | Major | Open Overdue | High |
| MAPEX-10123 | Source Validation Support: KOR IM-63984 | Open | 2026-06-26 | — | 64 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-10042 | MapReady Source Missing from Source Inventory | Open | 2026-06-26 | — | 64 | Chiara Angiolini | Major | Open Overdue | High |
| MAPEX-10706 | COL orbis admin area source validation Q3 | Backlog | 2026-07-10 | — | 50 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-10707 | SRB orbis admin area source validation Q3 | Backlog | 2026-07-13 | — | 47 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-10704 | ISL orbis admin area source validation Q3 | Backlog | 2026-07-13 | — | 47 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-10263 | Scoping inconsistency of PlaceChain members | Backlog | 2026-07-18 | — | 42 | Nikki Royce | Critical | Open Overdue | High |
| MAPEX-10262 | Scoping Germany AA issues | In Progress | 2026-07-18 | — | 42 | Nikki Royce | Critical | Open Overdue | High |
| MAPEX-10881 | GEN source -EGY Postal source delivery | Backlog | 2026-07-21 | — | 39 | Daniel Jooste | Major | Open Overdue | High |
| MAPEX-10880 | GEN source -ZAF Postal source delivery | Backlog | 2026-07-21 | — | 39 | Daniel Jooste | Major | Open Overdue | High |
| MAPEX-10879 | GEN source -MAR Postal source delivery | Backlog | 2026-07-21 | — | 39 | Daniel Jooste | Major | Open Overdue | High |
| MAPEX-11045 | DZA Orbis admin source validation Q3 | Backlog | 2026-07-24 | — | 36 | Nikki Royce | Critical | Open Overdue | High |
| MAPEX-10387 | Onboarding & Training for Szabolcs | In Progress | 2026-07-31 | — | 29 | Szabolcs Szász | Major | Open Overdue | Medium |
| MAPEX-11441 | IND Orbis Admin Area Maintenance: source validation Q3 POC | Planned | 2026-08-03 | — | 26 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11452 | Source Validation Support - Q3Postal - NOR | Backlog | 2026-08-04 | — | 25 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11503 | LTU Orbis Admin area source validation Q3 | Backlog | 2026-08-06 | — | 23 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-9985 | IDN phase 1 Orbis postal source validation Q2 | Planned | 2026-08-06 | — | 23 | Nikki Royce | Critical | Open Overdue | Medium |
| MAPEX-11751 | IDN Orbis Admin Area Maintenance: IDN_Phase_2_Batch_3_Merge source validation Q3 | Backlog | 2026-08-11 | — | 18 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11872 | Source validation DZA postal | Backlog | 2026-08-13 | — | 16 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12117 | THA orbis admin area source validation Q3 | Backlog | 2026-08-14 | — | 15 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11666 | TUR Guidance on the Regular Provinces | In Progress | 2026-08-14 | — | 15 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-11626 | PLJ RID : 60716 Analysis – suspicious gap in Plural Junction | Planned | 2026-08-14 | — | 15 | Lahu Navsupe | Major | Open Overdue | Medium |
| MAPEX-9915 | MDA - Community outreach and insights | In Progress | 2026-08-14 | — | 15 | Szabolcs Szász | Major | Open Overdue | Medium |
| MAPEX-12113 | Source Validation MLT postal Q3 | Backlog | 2026-08-17 | — | 12 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12359 | SAU Orbis Admin Area Maintenance:  Conformation about the Orbis Admin structure and geometry alignment | Open | 2026-08-21 | — | 8 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12221 | Source Validation Support IM-71559 DNK | Backlog | 2026-08-21 | — | 8 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12184 | XAM, XAN, XES, XHT, XKX, XLX, XPX, XSX, XXB, XXS Orbis Admin Area Maintenance: CM-Geopol Countries Source Validation Q3 | Open | 2026-08-21 | — | 8 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12156 | Count of Sub Addresses in Product stats - Orbis and Genesis | In Progress | 2026-08-21 | — | 8 | Sopan Kajale | Major | Open Overdue | Medium |
| MAPEX-11614 | CC rule Analysis Traffic light at connector Toyota delivery (August) | Planned | 2026-08-25 | — | 4 | Anil Kasar | Major | Open Overdue | Medium |
| MAPEX-12525 | APA_North East Asia_Exonyms | Backlog | 2026-08-26 | — | 3 | Sunny Ji | Critical | Open Overdue | Medium |
| MAPEX-12481 | NLD-C W34 - analysis of new repartitioning vs and old one | In Progress | 2026-08-26 | — | 3 | Dorota Stanczak | Major | Open Overdue | Medium |
| MAPEX-12552 | NLD-C W34 - changes in RM/LM CCs | In Progress | 2026-08-27 | — | 2 | Łukasz Kurzysz | Major | Open Overdue | Medium |
| MAPEX-12551 | NLD-C W34 - situation in LM before/after conflation | In Progress | 2026-08-27 | — | 2 | Dorota Stanczak | Major | Open Overdue | Medium |
| MAPEX-12363 | TomTom-SMARTY Quality Check | In Progress | 2026-08-27 | — | 2 | Sneha Deshpande | Major | Open Overdue | Medium |
| MAPEX-12665 | GBL TZ source validation Q3 | Backlog | 2026-08-28 | — | 1 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12589 | ACI B2B: Geometry update, USA country | In Progress | 2026-08-28 | — | 1 | Tim Bethke | Major | Open Overdue | Medium |
| MAPEX-12418 | Serbia – Full RNR update required: New M-road category (M1–M20) and expanded A-road network (up to A12) | In Progress | 2026-08-28 | — | 1 | Mile Milkovski | Major | Open Overdue | Medium |
| MAPEX-12404 | Review ARC1 degradation for Basemap using CA changes | Backlog | 2026-08-28 | — | 1 | Kalyan Dhaytonde | Major | Open Overdue | Medium |
| MAPEX-12386 | Source Validation Support IM-66555 USA | Planned | 2026-08-28 | — | 1 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12367 | [OA33] update existing ADE query for new gradient tags | Backlog | 2026-08-28 | — | 1 | Ted Yates | Major | Open Overdue | Medium |
| MAPEX-12362 | scope navigability=prohibited at aerodromes | Backlog | 2026-08-28 | — | 1 | Kalyan Dhaytonde | Major | Open Overdue | Medium |
| MAPEX-12333 | Need support on IM-68280 (CLONE - [CXPV-160886] Although 'Avoid Tollgate' is toggled ON, the route is still set to pass through a tollgate) | In Progress | 2026-08-28 | — | 1 | Seunghee Cho | Critical | Open Overdue | Medium |
| MAPEX-12295 | 60892 - Invalid Traffic Calming On Structure | In Progress | 2026-08-28 | — | 1 | Lahu Navsupe | Major | Open Overdue | Medium |
| MAPEX-11909 | update LEZ ADE query to include emission_regulation = 'no' | Backlog | 2026-08-28 | — | 1 | Daniel Roy | Major | Open Overdue | Medium |
| MAPEX-11784 | Improve visibility of feature eph to overall TBT eph | Backlog | 2026-08-28 | — | 1 | Erik Follensbee | Major | Open Overdue | Medium |
| MAPEX-9825 | check LEZ polys and alignment with roads in Genesis | In Progress | 2026-08-28 | — | 1 | Daniel Roy | Critical | Open Overdue | Medium |
| MAPEX-9795 | [CC] [LEZ] LEZ CC rule development | Backlog | 2026-08-28 | — | 1 | Daniel Roy | Critical | Open Overdue | Medium |
| MAPEX-12737 | Required Exonyms for "Naoero" | Backlog | 2026-09-04 | — | n/a | Paulina Olszak | Major | Due Soon – Not Started | Medium |
| MAPEX-12705 | Support for a highway rest area POI | Backlog | 2026-08-31 | — | n/a | Bernhard Braun | Major | Due Soon – Not Started | Medium |
| MAPEX-12703 | New geometry changes at YUL Terminal|Montréal-CAN | Open | 2026-08-31 | — | n/a | Rima Ouferoukh | Major | Due Soon – Not Started | Medium |
| MAPEX-12702 | POI IM-74648 ISR - Request to provide Transliterated name | Backlog | 2026-08-31 | — | n/a | Massimo Vallainc | Major | Due Soon – Not Started | Medium |
| MAPEX-12701 | HRV SCaaS: Street Name Pair Validation by Native Croatian Speakers — HRV | Planned | 2026-09-04 | — | n/a | Paulina Olszak | Major | Due Soon – Not Started | Medium |
| MAPEX-12696 | [CS0013523] [Nissan Motor Co., LTD] - ST2.1 2026.06 SAM-ARG QLU Items | Open | 2026-08-31 | — | n/a | Leticia Borges | Major | Due Soon – Not Started | Medium |
| MAPEX-12687 | POI IM-74643 & IM-74644 TUR - Request to verify and confirm existence | Backlog | 2026-08-31 | — | n/a | Dario Spinazzola | Major | Due Soon – Not Started | Medium |
| MAPEX-12671 | KOR : Prepare scope for highway=service missing navigability=no_through | Backlog | 2026-08-31 | — | n/a | Kalyan Dhaytonde | Critical | Due Soon – Not Started | Medium |
| MAPEX-12590 | determine how to find LEZ yes/no gaps / unwanted changes along a road | Backlog | 2026-09-04 | — | n/a | Daniel Roy | Major | Due Soon – Not Started | Medium |
| MAPEX-12584 | Create North Carolina DOT Source for Truck Weight Restrictions | Planned | 2026-09-10 | — | n/a | Matthew Rinaldi | Major | Due Soon – Not Started | Medium |
| MAPEX-12566 | Area Process fme-migration-javaService_VS_Support | Backlog | 2026-09-11 | — | n/a | Vijay Bhujbal | Major | Due Soon – Not Started | Medium |
| MAPEX-12557 | [QF] populate Routing QF for Aug 2026 | Backlog | 2026-09-04 | — | n/a | Daniel Roy | Major | Due Soon – Not Started | Medium |
| MAPEX-12556 | TTI - QC September-October 2026 - Global Events - APA | Backlog | 2026-09-07 | — | n/a | Daniel Jooste | Major | Due Soon – Not Started | Medium |
| MAPEX-12546 | KOR SCaaS: Street Name Pair Validation by Native Korean Speakers — KOR | Backlog | 2026-09-01 | — | n/a | Sunny Ji | Major | Due Soon – Not Started | Medium |
| MAPEX-12530 | Need to support OM-375114 (MLT- Orbis Street Name Source prep in mt_Latn and en_Latn) | Backlog | 2026-09-01 | — | n/a | Alberto Saini | Critical | Due Soon – Not Started | Medium |
| MAPEX-12509 | get km coverage for taxi restrictions | Backlog | 2026-09-04 | — | n/a | Daniel Roy | Major | Due Soon – Not Started | Medium |
| MAPEX-12508 | [Bifrost] compare Genesis and Orbis TBT Oneway errors | Backlog | 2026-09-04 | — | n/a | Erik Follensbee | Critical | Due Soon – Not Started | Medium |
| MAPEX-11830 | [Bifrost] compare Genesis and Orbis TBT TR errors | Backlog | 2026-09-04 | — | n/a | Erik Follensbee | Critical | Due Soon – Not Started | Medium |
| MAPEX-11827 | P1: Superflous APTs validation | Backlog | 2026-08-31 | — | n/a | Rajendra Nirgude | Major | Due Soon – Not Started | Medium |
| MAPEX-11826 | P1: Stacked APTs validation | Planned | 2026-08-31 | — | n/a | Rajendra Nirgude | Major | Due Soon – Not Started | Medium |
| MAPEX-11290 | Mexico – Follow-up and Activity Planning with YouthMappers UAEMEX | Planned | 2026-08-31 | — | n/a | Rita Garcia | Major | Due Soon – Not Started | Medium |
| MAPEX-10962 | SO_TMC Source 2026 LT 1 – Belgium version 3.9 | Verkeerscentrum | Open | 2026-08-30 | — | n/a | Kristian Georg Klem | Major | Due Soon – Not Started | Medium |
| MAPEX-10750 | ARG - Add Multiple Missing Schemas to Support Source Ingestion | Backlog | 2026-08-31 | — | n/a | Sneha Deshpande | Minor | Due Soon – Not Started | Medium |
| MAPEX-10748 | Action Plan: Sub-Address Addition for AUT, EST, IRL, SAU, SVN, NOR | Backlog | 2026-08-29 | — | n/a | Sneha Deshpande | Major | Due Soon – Not Started | Medium |
| MAPEX-10737 | SWE: Building Names Handling in Auto Source Process – Proposal & Data Normalization | Open | 2026-08-31 | — | n/a | Sneha Deshpande | Major | Due Soon – Not Started | Medium |
| MAPEX-10165 | Toll GTD - Local Expert checks for MEX (prio 10) | Planned | 2026-08-31 | — | n/a | Vicente Perez Nunez | Critical | Due Soon – Not Started | Medium |
| MAPEX-10025 | DEU Source Prep Activity Automation - Fine-Tuning Based on LE Feedback (OM-334770) | Planned | 2026-08-31 | — | n/a | Sneha Deshpande | Major | Due Soon – Not Started | Medium |
| MAPEX-10024 | COL: Scan existing data to identify sub-address scope and normalization needs | Planned | 2026-08-31 | — | n/a | Sneha Deshpande | Major | Due Soon – Not Started | Medium |
| MAPEX-9382 | SO_TMC Source 2026 ARE HERE 11 | Open | 2026-08-31 | — | n/a | Devidas Thite | Major | Due Soon – Not Started | Medium |
| MAPEX-10727 | Scale spot-check validation of genuinely-missing POIs with Ops | In Progress | — | — | n/a | Vincent Penalba | Major | Stale | Low |
| MAPEX-10726 | Run same unmatched analysis on SERP API for side-by-side PAV comparison | In Progress | — | — | n/a | Vincent Penalba | Major | Stale | Low |
| MAPEX-10008 | TTI - TTI Support Q2-Q3-Q4 2026 - SWE | Planned | — | — | n/a | Massimo Vallainc | Major | Stale | Low |
| MAPEX-9989 | TTI - TTI Support Q2-Q3-Q4 2026 - NCE | In Progress | — | — | n/a | Bernhard Braun | Major | Stale | Low |


## 4. Follow-up

The table below lists all flagged tickets (excluding _Due Soon – Not Started_ and _Closed Late_ categories) that require follow-up action. Assignees are asked to review their tickets, provide a status update in the **Follow-up Status** column, and propose a recommendation in the **User Recommendation** column.

**Why follow-up matters:** Timely follow-up on flagged tickets prevents recurring issues, supports continuous improvement, and ensures the project maintains healthy delivery rhythms. For the **User Recommendation** column, consider actions such as: adjusting the process that led to the delay, updating documentation, re-scoping the ticket, or escalating blockers.

| Key | Assignee | Follow-up Status | Reason for Flagging | User Recommendation |
|-----|----------|-----------------|---------------------|---------------------|
| MAPEX-9377 | Berk Ulupinar | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-9922 | Tim Bethke | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10123 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10042 | Chiara Angiolini | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10706 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10707 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10704 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10263 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10262 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10881 | Daniel Jooste | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10880 | Daniel Jooste | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10879 | Daniel Jooste | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-11045 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10387 | Szabolcs Szász | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11441 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11452 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11503 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-9985 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11751 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11872 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12117 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11666 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11626 | Lahu Navsupe | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-9915 | Szabolcs Szász | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12113 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12359 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12221 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12184 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12156 | Sopan Kajale | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11614 | Anil Kasar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12525 | Sunny Ji | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12481 | Dorota Stanczak | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12552 | Łukasz Kurzysz | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12551 | Dorota Stanczak | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12363 | Sneha Deshpande | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12665 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12589 | Tim Bethke | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12418 | Mile Milkovski | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12404 | Kalyan Dhaytonde | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12386 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12367 | Ted Yates | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12362 | Kalyan Dhaytonde | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12333 | Seunghee Cho | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12295 | Lahu Navsupe | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11909 | Daniel Roy | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11784 | Erik Follensbee | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-9825 | Daniel Roy | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-9795 | Daniel Roy | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10727 | Vincent Penalba | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-10726 | Vincent Penalba | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-10008 | Massimo Vallainc | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-9989 | Bernhard Braun | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
