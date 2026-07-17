# UI.md

## UI Redesign Requirements & Decisions

### 1. Visual Style & Brand Identity
* **Theme**: Light Mode (pure white background `#ffffff` replacing the dark theme).
* **Primary Accent Color**: Official UW-Madison Badger Red (`#c5050c`) for borders, buttons, and highlights.
* **Typography**: Sleek, modern sans-serif (official UW-Madison web fonts Red Hat Display for headings, Red Hat Text for body copy) with soft drop shadows and rounded corner cards.
* **Header Changes**:
  * Remove semester subtext "Fall 2025-2026" entirely.
  * Remove "Academic Trajectory" wording.

---

### 2. Landing Splash Page (Immersive Welcome)
* **Behavior**: Displayed immediately on page load, blocking the explorer.
* **Subtitle**: "Interactive Campus Explorer".
* **Message**:
  > *"All student profiles and transcripts displayed herein are synthetically generated and do not represent any actual individuals. This environment is created solely for research and analysis. The underlying statistical distributions of the source registrar records have been preserved with 100% mathematical fidelity."*
* **Action**: A prominent "Enter Campus Explorer" button with smooth fade-out transition to immerse the user into the database.

---

### 3. Navigation & Hierarchy
* **Breadcrumb Order**:
  * The root link is always **`University`** (never flips to other names).
  * Navigation path: **`University`** $\rightarrow$ **`<name of school or college>`** $\rightarrow$ **`<name of major>`**.
  * The left-side navigation elements have fixed coordinates and layouts to prevent shifting/jumping when loading data.
* **Unified Page Header**:
  * A shared header with fixed height and matching font size across all levels to prevent visual jumping/flakiness.
  * All "Back" operations are delegated to the breadcrumb navigation.
* **Contextual Level Subtexts** (Styled with enlarged `text-sm` font size):
  * **University**: `"Select an academic school or college block to explore departments and majors."`
  * **School**: `"Select a major program block to explore departments and majors."`
  * **Major**: `"Hover over a seat to inspect, click to view profile. Drag to pan, wheel/buttons to zoom."`

---

### 4. Campus Hierarchical Mapping

#### A. University Level (Campus Overview)
* Displays **Schools & Colleges** as cards arranged in a clean visual campus grid.
* Custom sorting applied: alphabetical, with **Graduate School** placed second to last and **Continuing Studies** placed last.
* Card badge displays **`X% of University`** (replacing "Univ").
* No explanatory subtext inside individual school blocks.

#### B. School Level (Department Map)
* Displays **Majors** within the selected school as cards.
* Each card displays the Major Name and Student Count.
* Student Count is styled as a neutral grey badge (`bg-slate-50 text-slate-400`), mirroring the university percentage badge, with no red accent.
* No explanatory subtext inside individual major blocks.
* No demographic splits previews on major cards.

---

### 5. Major Level (The Lecture Hall Visualizer)
* **Seating Grid Visuals**: Seating is organized in desks/rows, styled to look like long physical desks without text labels (no "Row 1", "Row 2" subscripts).
* **Student Representation**: Each student is a simple colored circle (no text inside). Circle color indicates legal sex (Male: Sky Blue | Female: Pink).
* **Grid Sizing & Scaling**:
  * Circle absolute size is constant (`22px` width/height).
  * Computes rows, columns, and dimensions mathematically on load.
  * Applies the fit scale factor so the entire cohort fills the screen bounds with a safe margin and no vertical scrollbars.
  * Captures browser focus prevention (`tabindex="-1"`) to block automatic scrolling shifts when reloading.
* **Zoom & Pan Controls**:
  * Native mouse-drag panning and wheel-based zooming with moderated sensitivity steps.
  * UI toggle buttons (`+` Zoom In, `-` Zoom Out, `Reset` View) for resetting scale and panning coordinates.
* **Interactive Tooltips**:
  * Hovering over a seat circle displays a quick tooltip preview containing the pupil's name (`Pupil #ID`) and GPA.
* **Profile Inspector Popup**:
  * Clicking a seat circle opens a modal/popup containing the pupil's full 27-feature academic, demographic, geographic, prior institution, and term grade details.
  * Designed in three clear categories: Academics, Demographics, and Prior School.
  * **Academics**: School/College, Academic Plan, Student Level, and Admit Type.
  * **Demographics**: Legal Sex, Age Group, Race/Ethnicity (international expanded), Citizenship, Wisconsin Residency, Home Region, and Home Location.
  * **Prior School**: Prior School Code, Prior School name (wrapping enabled), and Prior Location.
  * *Note*: The `Coordinates` (latitude/longitude) feature has been completely dropped from the UI modal inspector.

---

### 6. Bottom Footer & Licensing
* **Visual**: A clean, fixed bottom footer (`h-8`, bg-white, border-t) to ground copyright ownership and link back to development records.
* **Footnote**: `© 2026 chep0k | MIT License`
* **Links**: Clickable link to the project's source GitHub repository.
* **Web Icon (Favicon)**:
  * Linked in all HTML pages via `data/favicon.jpg`.
  * Designed as a single, thick, full-size red outline of the letter "W" with a digital pixelated/dissolving top-right edge, matching the official color palette.

