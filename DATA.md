# Data Documentation: UW-Madison Simulation

This document describes the scope, schema, boundaries, and generation logic of the datasets compiled for the University of Wisconsin–Madison IPU population simulation. All data in this databank corresponds to the **First Semester (Fall) 2025–2026** academic term.

---

## 1. Datasets & Sources Directory

All local file links below are relative to the repository root.

### A. Student GPA Statistics
* **Web Source (PDF download link)**: [Undergraduate Semester Grade-Point Average Report](https://uwmadison.box.com/s/km8bc2cvvouugo1e6b54m51ed5mq3i5o)
* **Local Raw File**: [data/gpa_report_recent.pdf](data/gpa_report_recent.pdf)
* **Local Parsed Output**: [data/gpa_parsed.csv](data/gpa_parsed.csv)
* **Creation Principle / Logic**: 
  Lines are grouped horizontally by clustering text coordinates within close vertical range ($\Delta y < 3$). Numbers are mapped to their respective columns (Freshmen, Sophomores, Juniors, Seniors, and Totals) using horizontal coordinate bins ($x_0$ ranges). Duplicate major-to-school name matches (e.g., the *Human Ecology* major within the *Human Ecology* school) are statefully resolved by maintaining a running school block context across page sequences, preventing double-counting.

### B. Course Grade Distributions
* **Web Source (PDF download link)**: [Course Grade Distribution Report](https://uwmadison.box.com/s/h17p8z5rcqlrbkg0k2digdqz9q10o5ta)
* **Local Raw File**: [data/grade_distribution_recent.pdf](data/grade_distribution_recent.pdf)
* **Local Parsed Output**: [data/grade_distribution_parsed.csv](data/grade_distribution_parsed.csv)
* **Creation Principle / Logic**: 
  Horizontal lines are reconstructed using vertical coordinate proximity. A stateful parser categorizes lines into subject headers, section rows, and course totals. For multi-section courses, section details (which lack titles/course numbers) are temporarily buffered. Once the Course Total row (which contains the title) is encountered, the title and catalog number are back-propagated to all buffered sections. Subject code context is persisted across page boundaries to avoid clearing the buffer prematurely on multi-page courses.

### C. Tableau Dashboard Extracts
* **Web Source**: [UW–Madison Enrollment Report (Interactive Tableau Dashboard)](https://viz.wisc.edu/views/UW-MadisonEnrollmentReport/HomePage)
* **Local CSV Files (56 total)**:
  * [country_academicLevel.csv](data/country_academicLevel.csv)
  * [country_admitType.csv](data/country_admitType.csv)
  * [country_residency.csv](data/country_residency.csv)
  * [credits_academicLevel.csv](data/credits_academicLevel.csv)
  * [credits_residency.csv](data/credits_residency.csv)
  * [credits_termAdmitType.csv](data/credits_termAdmitType.csv)
  * [degreeLevel_age.csv](data/degreeLevel_age.csv)
  * [degreeLevel_citizenship.csv](data/degreeLevel_citizenship.csv)
  * [degreeLevel_legalSex.csv](data/degreeLevel_legalSex.csv)
  * [degreeLevel_race.csv](data/degreeLevel_race.csv)
  * [degreeLevel_residency.csv](data/degreeLevel_residency.csv)
  * [degreeLevel_termAdmitType.csv](data/degreeLevel_termAdmitType.csv)
  * [fullTimePartTime_age.csv](data/fullTimePartTime_age.csv)
  * [fullTimePartTime_citizenship.csv](data/fullTimePartTime_citizenship.csv)
  * [fullTimePartTime_legalSex.csv](data/fullTimePartTime_legalSex.csv)
  * [fullTimePartTime_race.csv](data/fullTimePartTime_race.csv)
  * [fullTimePartTime_residency.csv](data/fullTimePartTime_residency.csv)
  * [fullTimePartTime_termAdmitType.csv](data/fullTimePartTime_termAdmitType.csv)
  * [highSchoolName_fullTimePartTime.csv](data/highSchoolName_fullTimePartTime.csv)
  * [highSchoolName_legalSex.csv](data/highSchoolName_legalSex.csv)
  * [highSchoolName_residency.csv](data/highSchoolName_residency.csv)
  * [internationalCountry_academicGroup.csv](data/internationalCountry_academicGroup.csv)
  * [internationalCountry_academicLevel.csv](data/internationalCountry_academicLevel.csv)
  * [internationalCountry_admit.csv](data/internationalCountry_admit.csv)
  * [internationalWorldMap.csv](data/internationalWorldMap.csv)
  * [level_age.csv](data/level_age.csv)
  * [level_citizenship.csv](data/level_citizenship.csv)
  * [level_legalSex.csv](data/level_legalSex.csv)
  * [level_race.csv](data/level_race.csv)
  * [level_residency.csv](data/level_residency.csv)
  * [level_termAdmitType.csv](data/level_termAdmitType.csv)
  * [plan_academicLevel.csv](data/plan_academicLevel.csv)
  * [plan_citizenship.csv](data/plan_citizenship.csv)
  * [plan_fullTimePartTime.csv](data/plan_fullTimePartTime.csv)
  * [plan_legalSex.csv](data/plan_legalSex.csv)
  * [plan_race.csv](data/plan_race.csv)
  * [plan_residency.csv](data/plan_residency.csv)
  * [plan_termAdmitType.csv](data/plan_termAdmitType.csv)
  * [school_age.csv](data/school_age.csv)
  * [school_citizenship.csv](data/school_citizenship.csv)
  * [school_legalSex.csv](data/school_legalSex.csv)
  * [school_race.csv](data/school_race.csv)
  * [school_residency.csv](data/school_residency.csv)
  * [school_termAdmitType.csv](data/school_termAdmitType.csv)
  * [transfer_fullTimePartTime.csv](data/transfer_fullTimePartTime.csv)
  * [transfer_legalSex.csv](data/transfer_legalSex.csv)
  * [transfer_residency.csv](data/transfer_residency.csv)
  * [usMap.csv](data/usMap.csv)
  * [usState_academicLevel.csv](data/usState_academicLevel.csv)
  * [usState_residency.csv](data/usState_residency.csv)
  * [usState_termAdmitType.csv](data/usState_termAdmitType.csv)
  * [wisconsinCounty_academicLevel.csv](data/wisconsinCounty_academicLevel.csv)
  * [wisconsinCounty_map.csv](data/wisconsinCounty_map.csv)
  * [wisconsinCounty_residency.csv](data/wisconsinCounty_residency.csv)
  * [wisconsinCounty_termAdmitType.csv](data/wisconsinCounty_termAdmitType.csv)
  * [worldMap.csv](data/worldMap.csv)
* **Creation Principle / Logic**: 
  Downloaded in CSV format from the interactive Tableau dashboard.

---

## 2. Scope & Boundaries

* **Institution**: University of Wisconsin–Madison (UW–Madison).
* **Temporal Scope**: **First Semester (Fall) 2025–2026** (Registrar Term Code `1262`).
* **Academic Level**:
  * **GPA Data**: Undergraduate level only.
  * **Grade Data**: All active course levels (Undergraduate, Graduate, Professional).
  * **Age & Enrollment Data**: All active enrollment levels (Undergraduate, Graduate, Clinical Doctorate, Special/Non-Degree).
* **Privacy Redactions**: Enrollment and grade figures for cohorts of **5 or fewer students** are redacted by the Registrar (represented as `***` or `NaN`).
* **Term Exclusions**: Summer terms are excluded.

### School / College Coverage

The dataset spans the following academic divisions (referred to as schools, colleges, or faculties):

| School/College Grouping | GPA Data (Undergrad) | Course Grade Data | Abbreviation |
| :--- | :--- | :--- | :--- |
| **Agricultural and Life Sciences** | Yes | Yes | `ALS` |
| **Business** | Yes | Yes | `BUS` |
| **Education** | Yes | Yes | `EDU` |
| **Engineering** | Yes | Yes | `EGR` |
| **Human Ecology** | Yes | Yes | `HEC` |
| **Letters and Science** | Yes | Yes | `L&S` |
| **Nursing** | Yes | Yes | `NUR` |
| **Pharmacy** | Yes | Yes | `PHM` |
| **Law School** | No | Yes | `LAW` |
| **Medicine & Public Health** | No | Yes | `MED` |
| **Veterinary Medicine** | No | Yes | `VET` |
| **Environmental Studies** | No | Yes | `IES` |
| **Academic Affairs / Misc.** | No | Yes | `AMN` |

---

## 3. Variable Dictionary (Schemas)

### A. GPA Data Schema (`gpa_parsed.csv`)

| Variable | Type | Description |
| :--- | :--- | :--- |
| `gender` | Text | Cohort gender split (`Men`, `Women`, or `Total`). |
| `school` | Text | Name of the hosting School or College. |
| `program` | Text | Name of the specific Undergraduate Major Program (e.g. `Mechanical Engineering`). |
| `is_school_total` | Boolean | True if the row represents the aggregated total of the entire school/faculty. |
| `freshman_count` | Numeric/String | Total count of enrolled freshmen in the program (can be `***` if redacted). |
| `freshman_gpa` | Numeric/String | Average cumulative GPA for freshmen (can be `***` or empty). |
| `sophomore_count` | Numeric/String | Count of sophomores. |
| `sophomore_gpa` | Numeric/String | Average cumulative GPA for sophomores. |
| `junior_count` | Numeric/String | Count of juniors. |
| `junior_gpa` | Numeric/String | Average cumulative GPA for juniors. |
| `senior_count` | Numeric/String | Count of seniors. |
| `senior_gpa` | Numeric/String | Average cumulative GPA for seniors. |
| `total_count` | Numeric/String | Total undergraduate enrollment count for the cohort. |
| `total_gpa` | Numeric/String | Total average cumulative GPA for the cohort. |

### B. Grade Distribution Schema (`grade_distribution_parsed.csv`)

| Variable | Type | Description |
| :--- | :--- | :--- |
| `page` | Numeric | Source PDF page number. |
| `school` | Text | School abbreviation (e.g., `ALS`, `L&S`). |
| `subject` | Text | Subject number and abbreviation (e.g., `108 AAE`). |
| `course_title` | Text | Name of the course (e.g., `Intro to Ag & Applied Econ`). |
| `course_num` | Numeric | Department course catalog number (e.g., `101`). |
| `section_num` | Numeric/String | Section code (e.g. `001`) or `"Course"` if it represents a total row. |
| `grades_count` | Numeric/String | Total count of grades recorded for the course/section (can be `***`). |
| `avg_gpa` | Numeric/String | Section average GPA (can be `***` or empty). |
| `A_pct` to `F_pct` | Numeric/String | Grade percentage distributions (A, AB, B, BC, C, D, F). |
| `S_pct` to `other_pct` | Numeric/String | Distribution of non-GPA marks (S, U, CR, N, P, I, NW, NR, Other). |
| `is_course_total` | Boolean | True if the row represents the aggregated totals of all sections for a single course. |

### C. Tableau Dashboard Extracts (56 CSV Files)

| File | Column Headers |
| :--- | :--- |
| [country_academicLevel.csv](data/country_academicLevel.csv) | `Home Country`, `Student Level`, `Academic Level`, `Count of Students` |
| [country_admitType.csv](data/country_admitType.csv) | `Home Country`, `Term Admit Type`, `Count of Students` |
| [country_residency.csv](data/country_residency.csv) | `Home Country`, `WI Residency Status`, `Count of Students` |
| [credits_academicLevel.csv](data/credits_academicLevel.csv) | `Credits Enrolled`, `Student Level`, `Academic Level`, `Count of Students` |
| [credits_residency.csv](data/credits_residency.csv) | `Credits Enrolled`, `WI Residency Status`, `Count of Students` |
| [credits_termAdmitType.csv](data/credits_termAdmitType.csv) | `Credits Enrolled`, `Term Admit Type`, `Count of Students` |
| [degreeLevel_age.csv](data/degreeLevel_age.csv) | `Student Level`, `Age Group`, `Count of Students` |
| [degreeLevel_citizenship.csv](data/degreeLevel_citizenship.csv) | `Student Level`, `U.S. Citizen`, `Count of Students` |
| [degreeLevel_legalSex.csv](data/degreeLevel_legalSex.csv) | `Student Level`, `Legal Sex `, `Count of Students` |
| [degreeLevel_race.csv](data/degreeLevel_race.csv) | `Student Level`, `Race/Ethnicity`, `Count of Students` |
| [degreeLevel_residency.csv](data/degreeLevel_residency.csv) | `Student Level`, `WI Residency Status`, `Count of Students` |
| [degreeLevel_termAdmitType.csv](data/degreeLevel_termAdmitType.csv) | `Student Level`, `Term Admit Type`, `Count of Students` |
| [fullTimePartTime_age.csv](data/fullTimePartTime_age.csv) | `Full Time/Part Time`, `Age Group`, `Count of Students` |
| [fullTimePartTime_citizenship.csv](data/fullTimePartTime_citizenship.csv) | `Full Time/Part Time`, `U.S. Citizen`, `Count of Students` |
| [fullTimePartTime_legalSex.csv](data/fullTimePartTime_legalSex.csv) | `Full Time/Part Time`, `Legal Sex `, `Count of Students` |
| [fullTimePartTime_race.csv](data/fullTimePartTime_race.csv) | `Full Time/Part Time`, `Race/Ethnicity`, `Count of Students` |
| [fullTimePartTime_residency.csv](data/fullTimePartTime_residency.csv) | `Full Time/Part Time`, `WI Residency Status`, `Count of Students` |
| [fullTimePartTime_termAdmitType.csv](data/fullTimePartTime_termAdmitType.csv) | `Full Time/Part Time`, `Term Admit Type`, `Count of Students` |
| [highSchoolName_fullTimePartTime.csv](data/highSchoolName_fullTimePartTime.csv) | `High School Name`, `HS Code`, `High School Name.1`, `High School State`, `High School City`, `Full Time/Part Time`, `Count of Students` |
| [highSchoolName_legalSex.csv](data/highSchoolName_legalSex.csv) | `High School Name`, `HS Code`, `High School Name.1`, `High School State`, `High School City`, `Legal Sex `, `Count of Students` |
| [highSchoolName_residency.csv](data/highSchoolName_residency.csv) | `High School Name`, `HS Code`, `High School Name.1`, `High School State`, `High School City`, `WI Residency Status`, `Count of Students` |
| [internationalCountry_academicGroup.csv](data/internationalCountry_academicGroup.csv) | `Country Of Citizenship`, `School/College (abbreviated)`, `Count of Students`, `School/College` |
| [internationalCountry_academicLevel.csv](data/internationalCountry_academicLevel.csv) | `Country Of Citizenship`, `Student Level`, `Academic Level`, `Count of Students` |
| [internationalCountry_admit.csv](data/internationalCountry_admit.csv) | `Country Of Citizenship`, `Term Admit Type`, `Count of Students`, `School/College` |
| [internationalWorldMap.csv](data/internationalWorldMap.csv) | `Country Of Citizenship`, `Count of Students`, `Latitude (generated)`, `Longitude (generated)` |
| [level_age.csv](data/level_age.csv) | `Student Level`, `Academic Level`, `Age Group`, `Count of Students` |
| [level_citizenship.csv](data/level_citizenship.csv) | `Student Level`, `Academic Level`, `U.S. Citizen`, `Count of Students` |
| [level_legalSex.csv](data/level_legalSex.csv) | `Student Level`, `Academic Level`, `Legal Sex `, `Count of Students` |
| [level_race.csv](data/level_race.csv) | `Student Level`, `Academic Level`, `Race/Ethnicity`, `Count of Students` |
| [level_residency.csv](data/level_residency.csv) | `Student Level`, `Academic Level`, `WI Residency Status`, `Count of Students` |
| [level_termAdmitType.csv](data/level_termAdmitType.csv) | `Student Level`, `Academic Level`, `Term Admit Type`, `Count of Students` |
| [plan_academicLevel.csv](data/plan_academicLevel.csv) | `Plan School/College`, `Academic Plan`, `Student Level`, `Academic Level`, `Count of Students` |
| [plan_citizenship.csv](data/plan_citizenship.csv) | `Plan School/College`, `Academic Plan`, `U.S. Citizen`, `Count of Students` |
| [plan_fullTimePartTime.csv](data/plan_fullTimePartTime.csv) | `Plan School/College`, `Academic Plan`, `Full Time/Part Time`, `Count of Students` |
| [plan_legalSex.csv](data/plan_legalSex.csv) | `Plan School/College`, `Academic Plan`, `Legal Sex `, `Count of Students` |
| [plan_race.csv](data/plan_race.csv) | `Plan School/College`, `Academic Plan`, `Race/Ethnicity`, `Count of Students` |
| [plan_residency.csv](data/plan_residency.csv) | `Plan School/College`, `Academic Plan`, `WI Residency Status`, `Term Descr (Stdnt Term Codes)`, `Count of Students` |
| [plan_termAdmitType.csv](data/plan_termAdmitType.csv) | `Plan School/College`, `Academic Plan`, `Term Admit Type`, `Count of Students` |
| [school_age.csv](data/school_age.csv) | `School/College`, `Age Group`, `Count of Students` |
| [school_citizenship.csv](data/school_citizenship.csv) | `School/College`, `U.S. Citizen`, `Count of Students` |
| [school_legalSex.csv](data/school_legalSex.csv) | `School/College`, `Legal Sex `, `Count of Students` |
| [school_race.csv](data/school_race.csv) | `School/College`, `Race/Ethnicity`, `Count of Students` |
| [school_residency.csv](data/school_residency.csv) | `School/College`, `WI Residency Status`, `Count of Students` |
| [school_termAdmitType.csv](data/school_termAdmitType.csv) | `School/College`, `Term Admit Type`, `Count of Students` |
| [transfer_fullTimePartTime.csv](data/transfer_fullTimePartTime.csv) | `College Admitted From`, `Full Time/Part Time`, `Count of Students` |
| [transfer_legalSex.csv](data/transfer_legalSex.csv) | `College Admitted From`, `Legal Sex `, `Count of Students` |
| [transfer_residency.csv](data/transfer_residency.csv) | `College Admitted From`, `WI Residency Status`, `Count of Students` |
| [usMap.csv](data/usMap.csv) | `Home State`, `USA`, `Count of Students`, `Latitude (generated)`, `Longitude (generated)` |
| [usState_academicLevel.csv](data/usState_academicLevel.csv) | `Home State`, `Student Level`, `Academic Level`, `Count of Students` |
| [usState_residency.csv](data/usState_residency.csv) | `Home State`, `WI Residency Status`, `Count of Students` |
| [usState_termAdmitType.csv](data/usState_termAdmitType.csv) | `Home State`, `Term Admit Type`, `Count of Students` |
| [wisconsinCounty_academicLevel.csv](data/wisconsinCounty_academicLevel.csv) | `Home Address Location`, `Student Level`, `Academic Level`, `Count of Students` |
| [wisconsinCounty_map.csv](data/wisconsinCounty_map.csv) | `WI`, `WI County`, `Count of Students`, `Latitude (generated)`, `Longitude (generated)` |
| [wisconsinCounty_residency.csv](data/wisconsinCounty_residency.csv) | `Home Address Location`, `WI Residency Status`, `Count of Students` |
| [wisconsinCounty_termAdmitType.csv](data/wisconsinCounty_termAdmitType.csv) | `Home Address Location`, `Term Admit Type`, `Count of Students` |
| [worldMap.csv](data/worldMap.csv) | `Home Country`, `Count of Students`, `Latitude (generated)`, `Longitude (generated)` |

### D. Geographic Origin Coordinates

To support geographical analysis of student origins without compromising student privacy, the databank includes approximate coordinate centroids under the `home_latitude` and `home_longitude` fields:
* **WI County Centroids**: Wisconsin resident coordinates are mapped from `data/wisconsinCounty_map.csv` representing the geographical center (centroid) of their respective home Wisconsin county (e.g., Dane, Milwaukee).
* **US State Centroids**: Non-resident U.S. citizen coordinates are mapped from `data/usMap.csv` representing the geographical center (centroid) of their home state (e.g., Illinois, California).
* **International Country Centroids**: Non-citizen coordinates are mapped from `data/worldMap.csv` representing the geographical center (centroid) of their country of citizenship (e.g., China, India, South Korea).

These coordinates are statistical county/state/country centroids rather than exact residential addresses.

---

## 4. Hierarchical Nesting & Redundancy Relations

This section documents all mathematically verified nesting hierarchies and identifies the redundant tables that can be completely derived from other datasets in the databank.

### A. Verified Nesting Relationships

Every relationship below has been strictly validated across the data:

1. **`Academic Level` $\rightarrow$ `Student Level`**:
   * *Nesting*: Every unique value of `Academic Level` maps to exactly one `Student Level` (e.g. `Freshman` is strictly `Undergraduate`, `PhD` is strictly `Graduate`, `Guest Student` is strictly `Special (Non-Degree)`).
2. **`Academic Plan` $\rightarrow$ `Plan School/College`**:
   * *Nesting*: Every unique academic plan (major) belongs to exactly one school/college (e.g., `Entomology PHD` is strictly within `Agricultural and Life Sciences`).
3. **`HS Code` $\rightarrow$ `High School Name`, `High School City`, `High School State`**:
   * *Nesting*: The unique high school code maps to exactly one name, city, and state.
4. **`High School Name` $\leftrightarrow$ `High School Name.1`**:
   * *Nesting*: Mapped 1-to-1 identically.
5. **`School/College` $\leftrightarrow$ `School/College (abbreviated)`**:
   * *Nesting*: Mapped 1-to-1.
6. **`page` $\rightarrow$ `subject`, `school`** (in `grade_distribution_parsed.csv`):
   * *Nesting*: The page number maps to exactly one subject and school context.
7. **`section_num` $\rightarrow$ `is_course_total`**:
   * *Nesting*: Mapped uniquely (value `"Course"` maps to `True`, otherwise `False`).
8. **Constant / Term Descr Nesting**:
   * `Plan School/College` $\rightarrow$ `Term Descr (Stdnt Term Codes)` (which is always the Fall 2025-2026 constant).
   * `Academic Plan` $\rightarrow$ `Term Descr (Stdnt Term Codes)`.

### B. Redundant Tables (Schema Subsets)

The following **20 tables** are mathematically redundant because their key column schemas are strict subsets of other tables in the databank. Their student counts can be derived by grouping and aggregating the corresponding superset tables:

1. **Degree Level Redundancies** (Derivable from `level_*.csv` tables):
   * **`degreeLevel_age.csv`** (keys: `['Student Level', 'Age Group']`) $\rightarrow$ subset of **`level_age.csv`** (`['Student Level', 'Academic Level', 'Age Group']`).
   * **`degreeLevel_citizenship.csv`** (keys: `['Student Level', 'U.S. Citizen']`) $\rightarrow$ subset of **`level_citizenship.csv`**.
   * **`degreeLevel_legalSex.csv`** (keys: `['Student Level', 'Legal Sex ']`) $\rightarrow$ subset of **`level_legalSex.csv`**.
   * **`degreeLevel_race.csv`** (keys: `['Student Level', 'Race/Ethnicity']`) $\rightarrow$ subset of **`level_race.csv`**.
   * **`degreeLevel_residency.csv`** (keys: `['WI Residency Status', 'Student Level']`) $\rightarrow$ subset of **`level_residency.csv`**.
   * **`degreeLevel_termAdmitType.csv`** (keys: `['Student Level', 'Term Admit Type']`) $\rightarrow$ subset of **`level_termAdmitType.csv`**.

2. **Geographical Redundancies** (Derivable from detailed state/county tables):
   * **`usState_residency.csv`** (keys: `['Home State', 'WI Residency Status']`) $\rightarrow$ subset of **`usState_academicLevel.csv`** or **`usState_termAdmitType.csv`**.
   * **`usMap.csv`** (keys: `['Home State']`) $\rightarrow$ subset of any of the state-level tables (e.g., **`usState_residency.csv`**).
   * **`wisconsinCounty_residency.csv`** (keys: `['Home Address Location', 'WI Residency Status']`) $\rightarrow$ subset of **`wisconsinCounty_academicLevel.csv`** or **`wisconsinCounty_termAdmitType.csv`**.

3. **Origin & Transfer Redundancies**:
   * **`highSchoolName_residency.csv`** (keys: `['High School Name', 'HS Code', 'High School City', 'High School State']`) $\rightarrow$ subset of **`highSchoolName_fullTimePartTime.csv`** or **`highSchoolName_legalSex.csv`**.
   * **`transfer_residency.csv`** (keys: `['College Admitted From']`) $\rightarrow$ subset of **`transfer_fullTimePartTime.csv`** or **`transfer_legalSex.csv`**.

4. **Aggregate Demographics / Academic Redundancies**:
   * **`school_residency.csv`** (keys: `['School/College']`) $\rightarrow$ subset of any `school_*.csv` file (e.g., **`school_age.csv`**).
   * **`school_termAdmitType.csv`** (keys: `['School/College', 'Term Admit Type']`) $\rightarrow$ subset of **`internationalCountry_admit.csv`**.
   * **`credits_residency.csv`** (keys: `['Credits Enrolled']`) $\rightarrow$ subset of **`credits_academicLevel.csv`** or **`credits_termAdmitType.csv`**.
   * **`country_academicLevel.csv`** (keys: `['Student Level', 'Academic Level']`) $\rightarrow$ subset of **`credits_academicLevel.csv`**, **`level_age.csv`**, or any other `level_*.csv` table.
   * **`internationalCountry_academicLevel.csv`** (keys: `['Student Level', 'Academic Level']`) $\rightarrow$ subset of same.
   * **`country_admitType.csv`** (keys: `['Term Admit Type']`) $\rightarrow$ subset of any of the term admit type tables (e.g., **`level_termAdmitType.csv`**).
   * **`country_residency.csv`** (keys: `['WI Residency Status']`) $\rightarrow$ subset of any residency table.
   * **`fullTimePartTime_residency.csv`** (keys: `['Full Time/Part Time']`) $\rightarrow$ subset of any `fullTimePartTime_*.csv` table.
   * **`internationalCountry_admit.csv`** (keys: `['School/College', 'Term Admit Type']`) $\rightarrow$ subset of **`school_termAdmitType.csv`**.
   * **`level_residency.csv`** (keys: `['Student Level', 'Academic Level']`) $\rightarrow$ subset of any `level_*.csv` table.

### C. Redundancy Summary

* **Total CSV Tables in Databank**: 58 tables
  * **Parsed PDF Reports (A & B)**: 2 tables
  * **Tableau Extracts (C)**: 56 tables
* **Redundant Tables**: 20 tables
* **Representative Tables (Required for IPU / validation)**: 38 tables

