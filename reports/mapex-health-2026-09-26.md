# Jira MapEx Project Health Check Report - 2026-09-26

_Generated on 2026-09-26 by automated GitHub Actions workflow._


## 1. Executive Summary

**Overall Health:** 🔴

**Scope:** 1504 tickets analyzed | 2026-06-28 → 2026-09-26 <span style="color:red"><strong>**Remark: only tickets created by Non-Map Experts are considered here*</strong></span>

**Rejection Rate:** 20 disputed/flagged vs 1019 total closed tickets in the last 90 days

**Schedule Health:**

- 67 overdue (1 critical, 9 high)
- 7 blocked tickets with due dates
- 68 due within 14 days, not started
- 21 stale (no update 30+ days)

**Top 5 Urgent Tickets:**

- **MAPEX-13209** (Critical) — report for child tickets of PT-Routing ON34 failure IM's [11d overdue]
- **MAPEX-10706** (High) — COL orbis admin area source validation Q3 [78d overdue]
- **MAPEX-10707** (High) — SRB orbis admin area source validation Q3 [75d overdue]
- **MAPEX-10263** (High) — Scoping inconsistency of PlaceChain members [70d overdue]
- **MAPEX-10881** (High) — GEN source -EGY Postal source delivery [67d overdue]

**Assignee Overload (3+ flagged tickets):**

- Angelique Corion: 21 flagged tickets
- Nikki Royce: 18 flagged tickets
- Lahu Navsupe: 11 flagged tickets
- Seunghee Cho: 9 flagged tickets
- Kalyan Dhaytonde: 9 flagged tickets
- HC Yen: 8 flagged tickets
- Ted Yates: 7 flagged tickets
- Berk Ulupinar: 7 flagged tickets
- Zorka Marinovic: 6 flagged tickets
- Szabolcs Szász: 4 flagged tickets
- Natasha Klinghardt: 4 flagged tickets
- Daniel Roy: 3 flagged tickets
- Amar Firdaus Bin Abdullah: 3 flagged tickets
- Erik Follensbee: 3 flagged tickets
- Massimo Vallainc: 3 flagged tickets
- Kristian Georg Klem: 3 flagged tickets
- Rita Garcia: 3 flagged tickets

**Recommendations:**

1. 🔴 Immediately review and address 1 critical overdue ticket(s) — these are >90 days late or blocker priority.
2. 🟡 Unblock 7 ticket(s) that are blocked and have due dates to prevent further schedule slippage.
3. 🟡 Triage 21 stale ticket(s) with no updates for 30+ days — close if obsolete or reassign/re-prioritize.


## 2. Rejected / Disputed Tickets

Tickets where work was potentially rejected or challenged, identified through resolution status, reopening history, comment keywords, or reporter post-closure activity.

| Key | Summary | Status | Resolution | Reporter | Assignee | Signal | Evidence | Severity |
|-----|---------|--------|------------|----------|----------|--------|----------|----------|
| MAPEX-13331 | KOR : Investigate low coverage of RPs | In Progress | — | Akshay Borawake | Swarup Jadhav | Dissatisfaction keyword in comment | Comment by Akshay Borawake: "Seems like numbers shared in the doc were wrong:…" | High |
| MAPEX-12548 | Required exonyms in multiple languages (EGY Country) | Closed | Done | Gautam Pradhan | Massimo Vallainc | Dissatisfaction keyword in comment; Reporter commented after closure | Comment by Mangesh Kumbhar: "Hi Team, While working on GEN-AdminAreas_UPDATE_AA_OM_351865_EGY_REG-Fallouts project. We have logged the RID 54033, 538…" | Reporter comment after resolution: "Hello   ,    Please check Mangesh comment regarding Greek.Greek & Hebrew.Latin name RID and provide your feedback Regard…" | High |
| MAPEX-13087 | TTI - Perform a test of the enhanced GLS version - CAN&USA | In Progress | — | Andrea De Meo | Luca Comi | Dissatisfaction keyword in comment | Comment by André Bolt: "Luca, four of your five points are live on   since this evening (22 September). Numbers as in your list: Point 1, Region…" | High |
| MAPEX-13063 | [SchoolZone] [Cariad] [KOR] Structural fixes | On Hold | — | Anna Krzyzanowska | Erik Follensbee | Dissatisfaction keyword in comment | Comment by Erik Follensbee: "Status update (21-Sep-2026) — analysis started, structural pattern identified Reviewed the 8 KOR IMs on  KOR IM's Analys…" | High |
| MAPEX-10472 | Toll GTD - Local Expert checks for SWE | Closed | Done | Liesbeth De Groote | Ron Bos | Dissatisfaction keyword in comment | Comment by Tomasz Kozlowski: "one of the Adds has coordinates that points us to RUS - longitude is incorrect, same as latitude: 59.3225731, 59.322573…" | High |
| MAPEX-13419 | ESP - missing sources | Closed | Done | Michal Wlodarczyk | Diego Carreira Fernández | Dissatisfaction keyword in comment | Comment by Michal Wlodarczyk: "Hi   thank you very much for the analysis. I will share your feedback in the IM ticket.  BTW, Can you raise Vertex Sugge…" | High |
| MAPEX-12816 | CYP - 2026 APT from ULAB Queries | Closed | Done | Supriya Mannepalli | Alberto Saini | Dissatisfaction keyword in comment | Comment by Alberto Saini: "Hi    cc    please find my feedback in    please note some errors are due to suppliers Ulab source, some other ( like wr…" | High |
| MAPEX-11291 | Mexico – Pre-State of the Map Mapping Activity | In Progress | — | María José Labarca | Rita Garcia | Dissatisfaction keyword in comment | Comment by María José Labarca: "Hello   and    I would like to document an important point regarding the analysis of this request. The information initi…" | High |
| MAPEX-13132 | MYS Admin Area Maintenance 2026 Q3 - SEAO - Source Query | Open | — | Hiraman Chorghade | Amar Firdaus Bin Abdullah | Reopened after closure | Status WAS Closed, now reopened | Medium |
| MAPEX-13421 | SWE: Clarification needed on ICL\BuiltUpArea\implicit speed limit definition — SWE | Open | — | Michal Kazmierski | Kristian Georg Klem | Reopened after closure | Status WAS Closed, now reopened | Medium |
| MAPEX-13466 | POI IM-75996 GBR - Request to verify and confirm existence of POIs | Closed | Done | Amrapali Shirsat | Ron Bos | Reporter commented after closure | Reporter comment after resolution: "Thanks for the feedback…" | Low |
| MAPEX-13343 | 2026 Q3 APT from Visicom – SM Delivery for MKD | Closed | Done | Supriya Mannepalli | Paulina Olszak | Reporter commented after closure | Reporter comment after resolution: "Hi  , Thank you for providing feedback ! Could you please provide feedback on below more 2 queries Observed suspicious H…" | Low |
| MAPEX-13183 | Need support on IM-75532 ([CS0014243] [Sygic a. s.] - Closed border crossing between Ukraine and Moldova (Transnitria)) | Closed | Done | BalaMurali Tata | Mile Milkovski | Reporter commented after closure | Reporter comment after resolution: "Thank you for feedback,  Could you please confirm whether vehicles are allowed to travel through the locations listed…" | Low |
| MAPEX-13023 | Community feedback | ALB & SRB - Brand verification | Closed | Done | Priscilla Zachee | Mile Milkovski | Reporter commented after closure | Reporter comment after resolution: "Thanks  . FYI we had some clarification in the tasks description of the challenge following the local community feedback…" | Low |
| MAPEX-12536 | Required exonyms in multiple languages (EGY Country) | Closed | Done | Gautam Pradhan | Natasha Klinghardt | Reporter commented after closure | Reporter comment after resolution: "Hello      Please check Mangesh comment regarding Tha.Latin name RID and provide your feedback Regards, Gautam.…" | Low |
| MAPEX-12369 | Need more source support to create Public bus road (Country AUS) | Closed | Done | Amol Dhage | Peter LeGras | Reporter commented after closure | Reporter comment after resolution: "Hello  . Please check below image can we remove signpost [ID: 0000514c-4400-4600-0000-0000343e891e] here at -27.6120027,…" | Low |
| MAPEX-10468 | Toll GTD - Local Expert checks for DNK | Closed | Done | Liesbeth De Groote | Ron Bos | Reporter commented after closure | Reporter comment after resolution: "this is probably usefull feedback for you:    thanks.…" | Low |
| MAPEX-13182 | Challenge Notification | North Macedonia - POIs on Highways | Closed | Done | Priscilla Zachee | Mile Milkovski | Reporter commented after closure | Reporter comment after resolution: "Close/done is fine. Thanks.…" | Low |
| MAPEX-13229 | DEU Name Library - Prefix and Suffix component feedback (LE) | Closed | Done | Santosh Gaikar | Matthias Mersch | Reporter commented after closure | Reporter comment after resolution: "Thanks for the feedback. The names have been updated accordingly in the Name Library.…" | Low |
| MAPEX-12776 | CYP SCaaS: Street Name Pair Validation by Native Greek Speakers — CYP | Closed | Done | Anjali Mudawadkar | Alberto Saini | Reporter commented after closure | Reporter comment after resolution: "Hi   , thanks for the feedback. Actually this file contains machine generated distinct pairs which get verified from LE.…" | Low |


## 3. At-Risk / Late Tickets

Tickets that are overdue, blocked, stale, or at risk of missing their deadline. Tickets with status _On Hold_, _Blocked_, or _Closed_ are excluded from this table (though relevant metrics appear in the Executive Summary).

| Key | Summary | Status | Due Date | Closed Date | Days Overdue | Assignee | Priority | Risk Category | Risk Level |
|-----|---------|--------|----------|-------------|--------------|----------|----------|---------------|------------|
| MAPEX-13209 | report for child tickets of PT-Routing ON34 failure IM's | Open | 2026-09-15 | — | 11 | Daniel Roy | Blocker | Open Overdue | Critical |
| MAPEX-10706 | COL orbis admin area source validation Q3 | Backlog | 2026-07-10 | — | 78 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-10707 | SRB orbis admin area source validation Q3 | Backlog | 2026-07-13 | — | 75 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-10263 | Scoping inconsistency of PlaceChain members | Backlog | 2026-07-18 | — | 70 | Nikki Royce | Critical | Open Overdue | High |
| MAPEX-10881 | GEN source -EGY Postal source delivery | Backlog | 2026-07-21 | — | 67 | Daniel Jooste | Major | Open Overdue | High |
| MAPEX-11045 | DZA Orbis admin source validation Q3 | Backlog | 2026-07-24 | — | 64 | Nikki Royce | Critical | Open Overdue | High |
| MAPEX-11452 | Source Validation Support - Q3Postal - NOR | Backlog | 2026-08-04 | — | 53 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-11503 | LTU Orbis Admin area source validation Q3 | Backlog | 2026-08-06 | — | 51 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-12113 | Source Validation MLT postal Q3 | Backlog | 2026-08-17 | — | 40 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-12221 | Source Validation Support IM-71559 DNK | Backlog | 2026-08-21 | — | 36 | Nikki Royce | Major | Open Overdue | High |
| MAPEX-12386 | Source Validation Support IM-66555 USA | Planned | 2026-08-28 | — | 29 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12333 | Need support on IM-68280 (CLONE - [CXPV-160886] Although 'Avoid Tollgate' is toggled ON, the route is still set to pass through a tollgate) | In Progress | 2026-08-28 | — | 29 | Seunghee Cho | Critical | Open Overdue | Medium |
| MAPEX-10690 | Investigate Additional Countries with Secondary Addresses | In Progress | 2026-08-31 | — | 26 | Paulina Olszak | Major | Open Overdue | Medium |
| MAPEX-12751 | NGA source validation Q3 | Backlog | 2026-09-04 | — | 22 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12474 | Source Validation Support IRL IM-72509 | Planned | 2026-09-04 | — | 22 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12556 | TTI - QC September-October 2026 - Global Events - APA | Backlog | 2026-09-07 | — | 19 | Daniel Jooste | Major | Open Overdue | Medium |
| MAPEX-13032 | IND_Batch 5 source validation Q3 | Backlog | 2026-09-10 | — | 16 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-12882 | The bridge has restrictions due to structural integrity concerns. Vehicles exceeding 15 tons gross weight or 7.3 tons axle weight | In Progress | 2026-09-11 | — | 15 | Bert van den Munckhof | Major | Open Overdue | Medium |
| MAPEX-13306 | RM Orbis Lane information USA Lane Direction - Lane connectivity rules | In Progress | 2026-09-17 | — | 9 | Ted Yates | Major | Open Overdue | Medium |
| MAPEX-13237 | IND_Batch 1 source validation Q3 | Backlog | 2026-09-17 | — | 9 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-13132 | MYS Admin Area Maintenance 2026 Q3 - SEAO - Source Query | Open | 2026-09-18 | — | 8 | Amar Firdaus Bin Abdullah | Major | Open Overdue | Medium |
| MAPEX-12899 | Barrier / non-passable analysis for NDS | In Progress | 2026-09-18 | — | 8 | Daniel Roy | Major | Open Overdue | Medium |
| MAPEX-12310 | VS Exp Validation - RM Overtaking Prohibition | In Progress | 2026-09-18 | — | 8 | Lahu Navsupe | Major | Open Overdue | Medium |
| MAPEX-11830 | [Bifrost] compare Genesis and Orbis TBT TR errors | Backlog | 2026-09-18 | — | 8 | Erik Follensbee | Critical | Open Overdue | Medium |
| MAPEX-11626 | PLJ RID : 60716 Analysis – suspicious gap in Plural Junction | In Progress | 2026-09-19 | — | 7 | Lahu Navsupe | Major | Open Overdue | Medium |
| MAPEX-13087 | TTI - Perform a test of the enhanced GLS version - CAN&USA | In Progress | 2026-09-21 | — | 5 | Luca Comi | Major | Open Overdue | Medium |
| MAPEX-13379 | Source Validation Support- GRC-IM-73614 | Backlog | 2026-09-22 | — | 4 | Nikki Royce | Critical | Open Overdue | Medium |
| MAPEX-13321 | detect old and outdated Construction cases in OSM/Orbis | In Progress | 2026-09-23 | — | 3 | Ted Yates | Critical | Open Overdue | Medium |
| MAPEX-12168 | Need support on IM-73878 (Need update "residents only" restriction on bunch of road geometry (country SVN)) | In Progress | 2026-09-23 | — | 3 | Szabolcs Szász | Critical | Open Overdue | Medium |
| MAPEX-13547 | Support requires to fix IM-76049 and IM-76044 | USA-MD | Backlog | 2026-09-24 | — | 2 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-13377 | LE Feedback-[Korea] All Korea Expressway IMs | In Progress | 2026-09-24 | — | 2 | Seunghee Cho | Critical | Open Overdue | Medium |
| MAPEX-13371 | [Walle] please update H2 targets | In Progress | 2026-09-24 | — | 2 | Erik Follensbee | Major | Open Overdue | Medium |
| MAPEX-13590 | GRC Postal Multipart in Island area | Backlog | 2026-09-25 | — | 1 | Massimo Vallainc | Major | Open Overdue | Medium |
| MAPEX-13577 | RM Orbis Lane information USA_Clarification on crossing Solid lines when entering traffic | In Progress | 2026-09-25 | — | 1 | Ted Yates | Major | Open Overdue | Medium |
| MAPEX-13551 | OMN source validation Q3 | Backlog | 2026-09-25 | — | 1 | Nikki Royce | Major | Open Overdue | Medium |
| MAPEX-13549 | Volvo Expedition Routes - LM Data & CC Rules Quality Analysis (Week 39, OLM) | In Progress | 2026-09-25 | — | 1 | Łukasz Kurzysz | Major | Open Overdue | Medium |
| MAPEX-13548 | POI IM-75538 ESP - Request to verify and confirm existence of POIs with EP | Backlog | 2026-09-25 | — | 1 | Massimo Vallainc | Major | Open Overdue | Medium |
| MAPEX-13546 | Need support on IM-75992 ([CS0014715] [Aspiegel SE] - Network and road attribute errors. HW ROAD test) | Backlog | 2026-09-25 | — | 1 | Massimo Vallainc | Critical | Open Overdue | Medium |
| MAPEX-13369 | [BicycleZone] support scoping feature country list | Backlog | 2026-09-25 | — | 1 | Erik Follensbee | Major | Open Overdue | Medium |
| MAPEX-13331 | KOR : Investigate low coverage of RPs | In Progress | 2026-09-25 | — | 1 | Swarup Jadhav | Major | Open Overdue | Medium |
| MAPEX-13210 | TTI - Perform a test of the enhanced RoadLens version - CAN&USA | In Progress | 2026-09-25 | — | 1 | Luca Comi | Major | Open Overdue | Medium |
| MAPEX-13044 | Migrate FME Workbench to Python: Driveway Attribute Update Rule ID 54291 fixing | Backlog | 2026-09-25 | — | 1 | Atish Pawar | Major | Open Overdue | Medium |
| MAPEX-12976 | Prepare Ground Truth input locations for Bridges & Tunnels metrics | In Progress | 2026-09-25 | — | 1 | Martyna Dziedzinska | Major | Open Overdue | Medium |
| MAPEX-12161 | BEL: Sub address pending cases | In Progress | 2026-09-25 | — | 1 | Sneha Deshpande | Major | Open Overdue | Medium |
| MAPEX-11826 | P1: Stacked APTs validation | Planned | 2026-09-25 | — | 1 | Rajendra Nirgude | Major | Open Overdue | Medium |
| MAPEX-11499 | TUR - Q3 retention check | In Progress | 2026-09-25 | — | 1 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-11498 | TUR - Mapillary-oriented MapRoulette challenge promotion with Burak | In Progress | 2026-09-25 | — | 1 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-11497 | TUR - Organic engagement: "What to map today" | In Progress | 2026-09-25 | — | 1 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-11495 | TUR - Online outreach to remote active editors + targeted thematic challenges | In Progress | 2026-09-25 | — | 1 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-11494 | TUR - New partner development | In Progress | 2026-09-25 | — | 1 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-11493 | TUR - In-person meet-up, Istanbul | In Progress | 2026-09-25 | — | 1 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-11492 | TUR - TBT-oriented online campaign with OSM-TR | In Progress | 2026-09-25 | — | 1 | Berk Ulupinar | Major | Open Overdue | Medium |
| MAPEX-11491 | TWN - Organic Engagement - regular casual "What to map today" check-ins | Open | 2026-09-25 | — | 1 | HC Yen | Major | Open Overdue | Medium |
| MAPEX-11490 | TWN - Q3 Retention Check across online + in-person events | Backlog | 2026-09-25 | — | 1 | HC Yen | Major | Open Overdue | Medium |
| MAPEX-11485 | TWN - Community Events for Mapillary-Oriented MapRoulette challenges | Backlog | 2026-09-25 | — | 1 | HC Yen | Major | Open Overdue | Medium |
| MAPEX-11484 | TWN - Mapillary community development (core anchor) | Backlog | 2026-09-25 | — | 1 | HC Yen | Major | Open Overdue | Medium |
| MAPEX-11483 | KOR - Q3 retention check across online + in-person events | Backlog | 2026-09-25 | — | 1 | Seunghee Cho | Major | Open Overdue | Medium |
| MAPEX-11482 | KOR - Organic Engagement - regular casual "What to map today" check-ins | Backlog | 2026-09-25 | — | 1 | Seunghee Cho | Major | Open Overdue | Medium |
| MAPEX-11480 | KOR - Online outreach to remote & active editors → Online meet-up event | Backlog | 2026-09-25 | — | 1 | Seunghee Cho | Major | Open Overdue | Medium |
| MAPEX-11479 | KOR - Formalise Hong-ik University connection & co-host/sponsor community-led f2f mapathon | Backlog | 2026-09-25 | — | 1 | Seunghee Cho | Major | Open Overdue | Medium |
| MAPEX-11476 | KOR - Maintain casual local "Maek-pping" Party socials (Seoul) | Planned | 2026-09-25 | — | 1 | Seunghee Cho | Major | Open Overdue | Medium |
| MAPEX-11058 | Mapillary Visibility & Field Collection – ITA, MLT, GRC – Gennaro Pesce | Backlog | 2026-09-25 | — | 1 | Gennaro Pesce | Major | Open Overdue | Medium |
| MAPEX-11052 | Mapillary Visibility & Field Collection – ROU, HUN – Szabolcs Szász | Backlog | 2026-09-25 | — | 1 | Szabolcs Szász | Major | Open Overdue | Medium |
| MAPEX-11051 | Local Expert–Led Mapathons & Mapping Events – ROU, HUN – Szabolcs Szász | Backlog | 2026-09-25 | — | 1 | Szabolcs Szász | Major | Open Overdue | Medium |
| MAPEX-11047 | University Outreach & Mapper Recruitment – ROU, HUN – Szabolcs Szász | Backlog | 2026-09-25 | — | 1 | Szabolcs Szász | Major | Open Overdue | Medium |
| MAPEX-11036 | Local Expert–Led Mapathons & Mapping Events – ALB, SRB, BIH, MKD, XKX, HRV, SLV, MNE – Mile Milkovski | In Progress | 2026-09-25 | — | 1 | Mile Milkovski | Major | Open Overdue | Medium |
| MAPEX-11034 | Mapillary Field Collection – ALB Camera Grant Revival & Balkans Onboarding – Mile Milkovski | In Progress | 2026-09-25 | — | 1 | Mile Milkovski | Major | Open Overdue | Medium |
| MAPEX-13623 | 2026 APT from ULAB – SM Delivery for ROU - Queries | Backlog | 2026-09-28 | — | n/a | Dario Spinazzola | Major | Due Soon – Not Started | Medium |
| MAPEX-13619 | Q3 APT Maintenance - Open data — COL- Queries | Backlog | 2026-09-28 | — | n/a | Zorka Marinovic | Major | Due Soon – Not Started | Medium |
| MAPEX-13615 | India- Missing Airport Grounds IM-76403 | Backlog | 2026-09-29 | — | n/a | Devidas Thite | Critical | Due Soon – Not Started | Medium |
| MAPEX-13578 | PHL SCaaS: Street Name Pair Validation by Native Filipino Speakers — PHL | Backlog | 2026-10-01 | — | n/a | Natasha Klinghardt | Major | Due Soon – Not Started | Medium |
| MAPEX-13566 | Source Validation DEU Postal- Country Crossing | Backlog | 2026-09-28 | — | n/a | Nikki Royce | Critical | Due Soon – Not Started | Medium |
| MAPEX-13561 | Request for BEL Country NBR Source to Resolve CCRID : 60632 | Backlog | 2026-09-28 | — | n/a | Bert van den Munckhof | Major | Due Soon – Not Started | Medium |
| MAPEX-13552 | BHR SCaaS: Street Name Pair Validation by Native Arabic Speakers — BHR | Backlog | 2026-10-01 | — | n/a | Devidas Thite | Major | Due Soon – Not Started | Medium |
| MAPEX-13545 | USA National Parks Data Update - Validation and Feedback Required | Backlog | 2026-09-28 | — | n/a | Nikki Royce | Critical | Due Soon – Not Started | Medium |
| MAPEX-13451 | LE Feedback-[Korea][WK2635][ANA] It is displayed as the Guri-Pocheon Expressway. | Backlog | 2026-09-29 | — | n/a | Seunghee Cho | Critical | Due Soon – Not Started | Medium |
| MAPEX-13446 | LE Feedback-IM-75105 [Korea][WK2635][ANA] The road name is not displayed. | Backlog | 2026-09-29 | — | n/a | Seunghee Cho | Critical | Due Soon – Not Started | Medium |
| MAPEX-13421 | SWE: Clarification needed on ICL\BuiltUpArea\implicit speed limit definition — SWE | Open | 2026-09-28 | — | n/a | Kristian Georg Klem | Critical | Due Soon – Not Started | Medium |
| MAPEX-13374 | modify access query to include a flavor for vehicle type | Backlog | 2026-09-30 | — | n/a | Ted Yates | Major | Due Soon – Not Started | Medium |
| MAPEX-13372 | Validate auto-fix rules for navigability and access related RAI | Backlog | 2026-10-09 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-13360 | SGP - Top Contributors - Outreach | Open | 2026-09-30 | — | n/a | Zuraimi Bin Idris | Major | Due Soon – Not Started | Medium |
| MAPEX-13359 | THA - Top Contributors - Outreach | Open | 2026-09-30 | — | n/a | Kuntida Uampranee | Major | Due Soon – Not Started | Medium |
| MAPEX-13358 | IDN - Top Contributors - Outreach | Open | 2026-09-30 | — | n/a | Happy Siagian | Major | Due Soon – Not Started | Medium |
| MAPEX-13347 | AUS - OSM Support - Q3 - Asia Pacific - Host Q3 Mapping Event | Open | 2026-09-30 | — | n/a | Natasha Klinghardt | Major | Due Soon – Not Started | Medium |
| MAPEX-13345 | OSM Support - Q3 - Asia Pacific | Backlog | 2026-09-30 | — | n/a | Natasha Klinghardt | Major | Due Soon – Not Started | Medium |
| MAPEX-13290 | Geolytica APTs – validate S2S delta for GBR - Queries | Backlog | 2026-10-09 | — | n/a | Dana Stepitova | Major | Due Soon – Not Started | Medium |
| MAPEX-13081 | Create Georgia DOT Source for Truck Weight Restrictions | Planned | 2026-10-09 | — | n/a | Matthew Rinaldi | Major | Due Soon – Not Started | Medium |
| MAPEX-12842 | Taxi Restriction evaluation Genesis vs Orbis | Backlog | 2026-10-01 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-12590 | refine / evaluate LEZ gap leads proposed by VS | Backlog | 2026-09-30 | — | n/a | Daniel Roy | Major | Due Soon – Not Started | Medium |
| MAPEX-12404 | Review ARC1 degradation for Basemap using CA changes | Backlog | 2026-09-30 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-12362 | scope navigability=prohibited at aerodromes | Backlog | 2026-10-01 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-12332 | Geopol Orbis 2026.Q4 TUR - DB Update | Planned | 2026-09-30 | — | n/a | Katrien Wouters | Major | Due Soon – Not Started | Medium |
| MAPEX-11894 | CC rule Calcification/Analysis [Railway Crossing] Q3 | Backlog | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-11836 | [LAM] Q3 2026 LE Activities for Speed limits based on change detection sources | Open | 2026-09-30 | — | n/a | Maximiliano Jaida Santander | Major | Due Soon – Not Started | Medium |
| MAPEX-11834 | [LAM] Q3 2026 LE Activities for Speed limits based on change detection sources | Planned | 2026-09-30 | — | n/a | Vicente Perez Nunez | Major | Due Soon – Not Started | Medium |
| MAPEX-11827 | P1: Superflous APTs validation | Planned | 2026-09-30 | — | n/a | Rajendra Nirgude | Major | Due Soon – Not Started | Medium |
| MAPEX-11792 | investigate additional sources for Toll roads | Backlog | 2026-10-01 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-11791 | Evaluate Toll CC checks | Backlog | 2026-10-01 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-11790 | investigate new sources for CA attribution | Backlog | 2026-10-01 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-11789 | support new CC rules for new CA length spec | Backlog | 2026-10-01 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-11788 | work with VS to support implementation of Under Construction CC rules | Open | 2026-10-01 | — | n/a | Ted Yates | Major | Due Soon – Not Started | Medium |
| MAPEX-11786 | Evaluate current CC rules for Routing Class | Open | 2026-10-01 | — | n/a | Ted Yates | Major | Due Soon – Not Started | Medium |
| MAPEX-11785 | Support the development of new metrics and CC for Routing Class | Open | 2026-10-01 | — | n/a | Ted Yates | Major | Due Soon – Not Started | Medium |
| MAPEX-11769 | Geopol Orbis 2026.Q4 CHN - Kit Review | Backlog | 2026-10-02 | — | n/a | HC Yen | Major | Due Soon – Not Started | Medium |
| MAPEX-11765 | Geopol Genesis 2026.12.000 CHN - Kit Review | Backlog | 2026-10-02 | — | n/a | HC Yen | Major | Due Soon – Not Started | Medium |
| MAPEX-11612 | Analysis CC rule Traffic Signals {traffic_light} [Not Committed] Toyota August Delivery | Backlog | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-11610 | Analysis CC rule Traffic signs [Not Committed] Toyota Delivery | Backlog | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-11599 | Geopol Genesis 2026.12.000 Review Geogrify file | Planned | 2026-10-07 | — | n/a | Zorka Marinovic | Major | Due Soon – Not Started | Medium |
| MAPEX-11597 | PLJ Rule Analysis Not Committed  to Toyota august Delivery | Backlog | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-11595 | Geopol Genesis 2026.12.000 VNM - Kit Review | Backlog | 2026-10-02 | — | n/a | Natasha Klinghardt | Major | Due Soon – Not Started | Medium |
| MAPEX-11594 | Geopol Genesis 2026.12.000 TWN - Kit Review | Backlog | 2026-10-02 | — | n/a | HC Yen | Major | Due Soon – Not Started | Medium |
| MAPEX-11586 | Geopol Orbis 2026.Q4 TWN - Kit Review | Backlog | 2026-10-02 | — | n/a | HC Yen | Major | Due Soon – Not Started | Medium |
| MAPEX-11549 | Geopol Orbis 2026.Q4 MYS - Kit Review | Planned | 2026-10-09 | — | n/a | Amar Firdaus Bin Abdullah | Major | Due Soon – Not Started | Medium |
| MAPEX-11547 | Geopol Genesis 2026.12.000 MYS - Kit Review | Planned | 2026-10-09 | — | n/a | Amar Firdaus Bin Abdullah | Major | Due Soon – Not Started | Medium |
| MAPEX-11545 | Geopol Orbis 2026.Q4 PER - Kit Review | Planned | 2026-10-02 | — | n/a | Zorka Marinovic | Major | Due Soon – Not Started | Medium |
| MAPEX-11544 | Geopol Genesis 2026.12.000 PER - Kit Review | Planned | 2026-10-02 | — | n/a | Zorka Marinovic | Major | Due Soon – Not Started | Medium |
| MAPEX-11543 | Geopol Orbis 2026.Q4 CHL - Kit Review | Planned | 2026-10-02 | — | n/a | Zorka Marinovic | Major | Due Soon – Not Started | Medium |
| MAPEX-11542 | Geopol Genesis 2026.12.000 CHL - Kit Review | Planned | 2026-10-02 | — | n/a | Zorka Marinovic | Major | Due Soon – Not Started | Medium |
| MAPEX-11541 | CC rule Calcification/Analysis [Speed bumps] Q3 | Backlog | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-11540 | Geopol Orbis 2026.Q4 ARG - Kit Review | Planned | 2026-10-02 | — | n/a | Pablo Schweitzer | Major | Due Soon – Not Started | Medium |
| MAPEX-11539 | Geopol Genesis 2026.12.000 ARG - Kit Review | Planned | 2026-10-02 | — | n/a | Pablo Schweitzer | Major | Due Soon – Not Started | Medium |
| MAPEX-11308 | [Q3 2026] Access + Navigability | Open | 2026-09-30 | — | n/a | Kalyan Dhaytonde | Major | Due Soon – Not Started | Medium |
| MAPEX-11290 | Mexico – Follow-up and Activity Planning with YouthMappers UAEMEX | Planned | 2026-09-30 | — | n/a | Rita Garcia | Major | Due Soon – Not Started | Medium |
| MAPEX-11289 | Mexico – Follow-up and Activity Planning with UAMAPS | Planned | 2026-09-30 | — | n/a | Rita Garcia | Major | Due Soon – Not Started | Medium |
| MAPEX-11288 | Mexico – Follow-up and Activity Planning with Iztapamapas | Planned | 2026-09-30 | — | n/a | Rita Garcia | Major | Due Soon – Not Started | Medium |
| MAPEX-11158 | Pre-event planning and Preparation - ESP - State of the Map Spain 2026 | Open | 2026-09-30 | — | n/a | Africa Dumas | Major | Due Soon – Not Started | Medium |
| MAPEX-11059 | University Outreach & Mapper Recruitment – NOR, SWE, FIN, DNK – Kristian Georg Klem | Open | 2026-09-30 | — | n/a | Kristian Georg Klem | Major | Due Soon – Not Started | Medium |
| MAPEX-11057 | Local Expert–Led Mapathons & Mapping Events – ITA, MLT, GRC – Gennaro Pesce | Backlog | 2026-09-30 | — | n/a | Gennaro Pesce | Major | Due Soon – Not Started | Medium |
| MAPEX-11054 | Local Expert–Led Mapathons & Mapping Events – AND, ESP – Africa Dumas | Open | 2026-09-30 | — | n/a | Africa Dumas | Major | Due Soon – Not Started | Medium |
| MAPEX-10962 | SO_TMC Source 2026 LT 1 – Belgium version 3.9 | Verkeerscentrum | Open | 2026-09-28 | — | n/a | Kristian Georg Klem | Major | Due Soon – Not Started | Medium |
| MAPEX-10737 | SWE: Building Names Handling in Auto Source Process – Proposal & Data Normalization | Planned | 2026-09-30 | — | n/a | Sneha Deshpande | Minor | Due Soon – Not Started | Medium |
| MAPEX-10594 | Traffic light and Traffic sign MapExpert Support [Q3] | Backlog | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-10408 | CC rule Calification/Analysis [PLJ] Q3 | Open | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-10406 | Guidence | M-Map (LM/HD) ADE Stats Query [Q3] | Backlog | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-10405 | Guidance | S-Map (RM/SD) ADE Stats Query [Q3] | Backlog | 2026-09-30 | — | n/a | Lahu Navsupe | Major | Due Soon – Not Started | Medium |
| MAPEX-12327 | 60835 - Road Median also has Road Boundary | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12286 | VS Exp Validation - Road Median | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12103 | 60609 v2 - Invalid length of Exit Or Entrance Lane (lane count change) | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12102 | 60608 v2 - Invalid length of Exit Or Entrance Lane (no lane count change) | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12094 | 60362 v2 - Discontinued Exit Or Entrance Lane for road | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12074 | 60211 v2 - Invalid syntax for connectivity Property on Lane Connectivity | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12073 | 60201 v4 - Missing Lane Connectivity at two-valent nodes | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12072 | 60844 v1 - Invalid conditional for lanes | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12071 | 60843 - Overlapping #Conditional for HOV | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12070 | 60842 v1 - Superfluous HOV Lane | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12067 | 60405 v2 - Invalid Segment Definition in Linear Reference of Lane Properties or Lane Connectivity Members | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12063 | 60838 v1 - Superfluous Property tag | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12059 | 60354 v2 - Lane Payment Method ‘cash' and 'coins' can not occur together | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12058 | 60251 v2 Missing or incorrect “toll_booth” Divider Type | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12057 | 60646 v2 - Contradicting Lane Payment Method and Toll Method | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12056 | 60645 v2 - Contradicting Lane Payment Method and Toll Method | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12055 | 60644 v2 - Missing Toll Info at Road Line with Lane level toll info | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12054 | 60447 v2 - Invalid Toll Lane position | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12053 | 60232 v2  - Toll Lane cannot be captured for all Lanes | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12047 | 60238 v2 - HOV toll payment exception must have HOV and Toll Lane | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-12035 | VS Exp Validation - Lanes (spec change) | Open | — | — | n/a | Angelique Corion | Major | Stale | Low |
| MAPEX-11053 | University Outreach & Mapper Recruitment – AND, ESP – Africa Dumas | In Progress | 2026-09-30 | — | n/a | — | Major | Unassigned At-Risk | Low |


## 4. Follow-up

The table below lists all flagged tickets (excluding _Due Soon – Not Started_ and _Closed Late_ categories) that require follow-up action. Assignees are asked to review their tickets, provide a status update in the **Follow-up Status** column, and propose a recommendation in the **User Recommendation** column.

**Why follow-up matters:** Timely follow-up on flagged tickets prevents recurring issues, supports continuous improvement, and ensures the project maintains healthy delivery rhythms. For the **User Recommendation** column, consider actions such as: adjusting the process that led to the delay, updating documentation, re-scoping the ticket, or escalating blockers.

| Key | Assignee | Follow-up Status | Reason for Flagging | User Recommendation |
|-----|----------|-----------------|---------------------|---------------------|
| MAPEX-13209 | Daniel Roy | _(to be filled)_ | Open Overdue — Critical risk | _(to be filled)_ |
| MAPEX-10706 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10707 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10263 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-10881 | Daniel Jooste | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-11045 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-11452 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-11503 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-12113 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-12221 | Nikki Royce | _(to be filled)_ | Open Overdue — High risk | _(to be filled)_ |
| MAPEX-12386 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12333 | Seunghee Cho | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-10690 | Paulina Olszak | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12751 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12474 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12556 | Daniel Jooste | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13032 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12882 | Bert van den Munckhof | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13306 | Ted Yates | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13237 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13132 | Amar Firdaus Bin Abdullah | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12899 | Daniel Roy | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12310 | Lahu Navsupe | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11830 | Erik Follensbee | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11626 | Lahu Navsupe | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13087 | Luca Comi | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13379 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13321 | Ted Yates | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12168 | Szabolcs Szász | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13547 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13377 | Seunghee Cho | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13371 | Erik Follensbee | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13590 | Massimo Vallainc | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13577 | Ted Yates | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13551 | Nikki Royce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13549 | Łukasz Kurzysz | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13548 | Massimo Vallainc | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13546 | Massimo Vallainc | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13369 | Erik Follensbee | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13331 | Swarup Jadhav | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13210 | Luca Comi | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-13044 | Atish Pawar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12976 | Martyna Dziedzinska | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12161 | Sneha Deshpande | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11826 | Rajendra Nirgude | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11499 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11498 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11497 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11495 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11494 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11493 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11492 | Berk Ulupinar | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11491 | HC Yen | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11490 | HC Yen | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11485 | HC Yen | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11484 | HC Yen | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11483 | Seunghee Cho | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11482 | Seunghee Cho | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11480 | Seunghee Cho | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11479 | Seunghee Cho | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11476 | Seunghee Cho | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11058 | Gennaro Pesce | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11052 | Szabolcs Szász | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11051 | Szabolcs Szász | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11047 | Szabolcs Szász | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11036 | Mile Milkovski | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-11034 | Mile Milkovski | _(to be filled)_ | Open Overdue — Medium risk | _(to be filled)_ |
| MAPEX-12327 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12286 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12103 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12102 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12094 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12074 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12073 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12072 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12071 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12070 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12067 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12063 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12059 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12058 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12057 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12056 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12055 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12054 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12053 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12047 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-12035 | Angelique Corion | _(to be filled)_ | Stale — Low risk | _(to be filled)_ |
| MAPEX-11053 | — | _(to be filled)_ | Unassigned At-Risk — Low risk | _(to be filled)_ |
