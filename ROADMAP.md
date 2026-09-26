# Data Analyst Skill-Up Roadmap

> A practical-first path from "finished a course" to a job-ready analyst working at intermediate and then advanced level. **Every tool and resource here is free.**
> Item IDs (`1.2`, `P3`, …) are tracked in `PROGRESS.md`.

## How this roadmap works

- **Pace:** 3 hrs/day, 7 days a week (~21 hrs/week), for about **19 weeks (2026-09-27 → ~2027-02-07)**. The dates are targets, not deadlines. The teacher re-plans at each phase gate based on actual progress.
- **Split:** ~30% learning and ~70% doing. Modules are short, and **projects are the core**.
- **Structure:** each phase is a set of skill modules (learn + drills), then projects framed as business problems, then a **level gate** (a practical check with the teacher) before moving on.
- **Why this order:** SQL and pandas fluency → business analysis and communication → analytics engineering, forecasting, and ML. Each step builds on the one before, and each project reuses earlier skills.

## Schedule (3 hrs/day)

| Phase | Dates | Length |
|---|---|---|
| 0: Setup & Baseline | 2026-09-27 → 09-30 | 4 days |
| 1: Solid Foundations | 2026-10-01 → 10-25 | ~3.5 weeks |
| 2: Intermediate | 2026-10-26 → 12-06 | 6 weeks |
| 3: Advanced | 2026-12-07 → 2027-01-24 | 7 weeks (includes a holiday buffer) |
| 4: Job-Ready Sprint | 2027-01-25 → 02-07 | 2 weeks |

### Daily 3-hour session

| Block | Time | What |
|---|---|---|
| Warm-up | 20 min | 2–3 SQL problems, or recall questions from *Weak spots* |
| Main block | 2 hrs | The module task or project milestone, worked on with the teacher |
| Learn block | 30 min | Reading or video from the resource list, to prepare for tomorrow |
| Wrap-up | 10 min | Learning-log entry, then say **"wrap up"** so the teacher updates `PROGRESS.md` |

### Weekly rhythm
- **Days 1–6:** normal sessions.
- **Day 7 is review day:** a weekly quiz on that week's topics, a weak-spot review, catch-up on anything that slipped, and one TidyTuesday or Makeover Monday chart. Spreadsheet practice (1.5) goes here during Phase 1. Keep it lighter if you need rest; this day is the buffer.

### Phase 1 week-by-week (later phases are detailed when we reach them)
| Week | Dates | Focus |
|---|---|---|
| 1 | 10-01 → 10-07 | 1.1 SQL (through window functions) + 1.2 pandas cleaning drills |
| 2 | 10-08 → 10-14 | 1.3 EDA/viz + 1.4 stats, then start **P1** (audit + cleaning) |
| 3 | 10-15 → 10-21 | Finish **P1** (EDA + recommendation), start **P2** (schema, load, DQ checks) |
| 4 | 10-22 → 10-25 | Finish **P2** (20 questions + memo), then the **Phase 1 gate** |

## Free toolkit (installed in Phase 0 unless noted)

| Tool | Purpose | Notes |
|---|---|---|
| Miniforge (conda) | Python environments | Fully free conda distribution (conda-forge) |
| VS Code + Python/Jupyter extensions | Editor and notebooks | |
| Git + GitHub | Version control and portfolio | |
| PostgreSQL + DBeaver Community | Relational DB and SQL client | |
| DuckDB | Fast local SQL on CSV/Parquet | `pip`/`conda` install |
| Power BI Desktop | BI dashboards | Free on Windows (Microsoft Store) |
| Google Sheets / Excel for the web | Spreadsheets | Free with a Google/Microsoft account |
| Kaggle account | Datasets and free cloud notebooks | |
| BigQuery Sandbox + Looker Studio | Cloud warehouse and BI | Phase 3; no credit card needed |
| dbt-core (+ dbt-duckdb) | Analytics engineering | Phase 3 |
| Streamlit + Community Cloud | Data apps | Phase 3 |

---

## Phase 0: Setup & Baseline (2026-09-27 → 09-30)

**Goal:** a working environment and an honest baseline.

- **0.1 Environment setup.** Install the toolkit. Create the `analyst` conda env with: `pandas numpy matplotlib seaborn plotly scipy statsmodels scikit-learn jupyterlab duckdb sqlalchemy psycopg requests python-dotenv pyarrow openpyxl`.
- **0.2 Git and GitHub essentials.** Cover `init/add/commit/push/branch`, `.gitignore`, writing a README, and turning this workspace into a repo. *Resources:* GitHub Skills "Introduction to GitHub", *Pro Git* chapters 1–3.
- **0.3 Diagnostic with the teacher** (60–90 min): 10 SQL questions, 5 pandas tasks, 8 stats concept questions, and 1 mini business case. The results set the baseline skill matrix and decide which Phase 1 modules to compress.

**Done when:** `python -c "import pandas, duckdb, sklearn"` runs, DBeaver connects to Postgres, the first commit is pushed to GitHub, and the diagnostic is recorded in `PROGRESS.md`.

---

## Phase 1: Solid Foundations Through Practice (2026-10-01 → 10-25)

**Goal:** move from "I've seen it" to "I can do it without a tutorial."

### Modules

**1.1 SQL: querying fluently**
- Topics: a fast review of SELECT/WHERE/GROUP BY/HAVING; all JOIN types and **join pitfalls** (fan-out, duplicate rows); CASE WHEN and conditional aggregation; subqueries vs CTEs; date functions; NULL handling; **window functions** (ROW_NUMBER, RANK, LAG/LEAD, running totals, moving averages, NTILE).
- Practice: SQLBolt (refresher), Select Star SQL, PostgreSQL Exercises, LeetCode *SQL 50*, DataLemur (free questions).
- Target: 40 problems solved, at least 15 of them medium.

**1.2 Python: pandas wrangling and cleaning**
- Topics: reading CSV/Excel/JSON/Parquet; dtypes; strategies for missing values; duplicates; string cleaning (`.str`); dates (`to_datetime`, `.dt`); `groupby` + `agg`/`transform`; `merge` with `validate=`; `pivot_table`/`melt`; vectorisation vs `apply`; method chaining; writing reusable cleaning functions.
- Resources: Kaggle Learn *Pandas* + *Data Cleaning*; *Python for Data Analysis, 3e* (free online), chapters 5–10.

**1.3 EDA and visualisation**
- Topics: an EDA checklist; univariate and bivariate analysis; distributions and outliers; choosing the right chart; matplotlib/seaborn/plotly; titles and annotations written for humans.
- Resources: Kaggle Learn *Data Visualization*; *Fundamentals of Data Visualization* (Claus Wilke, free online); the FT *Visual Vocabulary*.

**1.4 Practical statistics I**
- Topics: central tendency and spread; percentiles; skew; normal and binomial distributions; sampling and the CLT; confidence intervals; correlation vs causation; Simpson's paradox.
- Resources: StatQuest (YouTube); Khan Academy *Statistics & Probability*; *OpenIntro Statistics* (free PDF), chapters 1–5.

**1.5 Spreadsheet fluency (light, because every analyst job uses spreadsheets)**
- Topics: XLOOKUP / INDEX-MATCH, pivot tables, conditional formatting, data validation, quick charts.
- Resources: Exceljet; Google Sheets help centre.

### Projects

**P1: Airbnb market analysis (data cleaning + EDA)**
- *Scenario:* "You're an analyst at a short-term-rental investment firm. Which neighbourhoods in <city> should we buy in, and what type of property?"
- *Data:* Inside Airbnb, specifically `listings`, `calendar`, and `reviews` for one city of your choice.
- *Milestones:*
  1. Data audit report: shape, dtypes, missingness, duplicates, and odd values (prices stored as `"$1,200.00"`, amenities stored as list-strings).
  2. A cleaning pipeline written as reusable functions in `src/clean.py`, not just notebook cells.
  3. EDA that answers: what drives price (neighbourhood, room type, capacity); an occupancy proxy; multi-listing hosts; seasonality.
  4. A recommendation of the top 3 neighbourhoods, with evidence and caveats.
- *Crucial learnings:* auditing before analysing, documenting cleaning decisions, handling outliers, reproducibility, answering a question instead of just describing the data.
- *Deliverables:* the notebook, `src/clean.py`, and a README with a one-page findings summary and 4–5 charts.
- *Stretch:* an interactive map (plotly or folium).

**P2: E-commerce business deep-dive in SQL**
- *Scenario:* "Olist's Head of Operations asks: where are we losing money and customers?"
- *Data:* the Brazilian E-Commerce Public Dataset by Olist (Kaggle; 9 related tables).
- *Milestones:*
  1. Load the data into PostgreSQL with a proper schema (types, primary and foreign keys), and draw an ER diagram.
  2. Data-quality checks in SQL: orphan rows, duplicates, impossible dates.
  3. Answer 20 business questions in pure SQL, getting harder as you go. They include revenue and MoM growth, AOV, top categories, repeat-purchase rate, delivery delay vs review score, seller ranking per state, running totals, first-order cohorts, and a Pareto (80/20) analysis of sellers.
  4. A memo with 5 insights and 3 recommendations.
- *Crucial learnings:* relational modelling, join fan-out traps, window functions on real data, turning vague questions into SQL, writing readable SQL.
- *Deliverables:* `sql/schema.sql`, numbered and commented query files, and a README memo.
- *Stretch:* run the same queries in DuckDB directly on the CSVs and compare the experience.

### Phase 1 gate
- [ ] Solve 4 unseen medium SQL problems (including windows) in about 45 min, with no help.
- [ ] Given a new messy CSV, produce an audit and cleaning plan in 30 min.
- [ ] Explain a confidence interval, when to use the median over the mean, and correlation vs causation, each with an example.
- [ ] P1 and P2 pass review and are pushed to GitHub.

---

## Phase 2: Intermediate: Business Analysis, BI & Experiments (2026-10-26 → 12-06)

**Goal:** think and work like a business analyst using metrics, segments, experiments, dashboards, and stories.

### Modules

**2.1 Business metrics and analytical frameworks**
- Topics: KPI trees and metric decomposition (revenue = users × conversion × AOV); funnels; cohorts and retention curves; RFM; simple CLV; churn definitions; unit economics; leading vs lagging metrics; root-cause analysis for "why did metric X drop?".
- Resources: teacher-led mini-cases (primary), plus the free guides from Amplitude and Mixpanel on funnels, retention, and cohorts.

**2.2 Power BI**
- Topics: Power Query cleaning; star schema and relationships; DAX (measures vs calculated columns, `CALCULATE`, filter context, time intelligence); visual design; drill-through; tooltips; bookmarks.
- Note: publishing online needs a work account, so the portfolio will use the `.pbix` file, a PDF export, and screenshots or a GIF.
- Resources: the free Microsoft Learn *PL-300 (Power BI Data Analyst)* learning paths; DAX Guide (dax.guide); SQLBI free articles; Guy in a Cube (YouTube).

**2.3 Statistics II: inference and experimentation**
- Topics: the hypothesis-testing framework; t-tests, chi-square, and proportion z-tests; p-values and how they're misused; effect size; power and sample size; A/B test design (randomisation unit, guardrail metrics, sample-ratio mismatch, peeking, novelty effects); bootstrap confidence intervals.
- Resources: StatQuest; *OpenIntro Statistics* chapters 5–7; Evan Miller's A/B testing articles and calculators; `scipy.stats` docs.

**2.4 Acquiring data: APIs, JSON, scraping, automation**
- Topics: `requests` and REST APIs; pagination; `pd.json_normalize`; rate limits; keeping secrets in `.env`; ethical scraping (robots.txt) with BeautifulSoup; logging; scheduling scripts.
- Resources: Real Python's free articles; the Beautiful Soup docs; the World Bank API docs.

**2.5 Communicating insights**
- Topics: answer-first writing (pyramid principle); the one-page analysis memo; chart annotation; slide storytelling; tailoring to executive vs technical audiences; presenting uncertainty.
- Resources: *Fundamentals of Data Visualization* (storytelling chapters); the Storytelling with Data blog (free); teacher reviews of every memo.

### Projects

**P3: Customer retention and segmentation for an online retailer**
- *Scenario:* "A UK gift retailer's CMO asks: who are our valuable customers, and when and why do customers stop buying?"
- *Data:* Online Retail II (UCI Machine Learning Repository).
- *Milestones:* cleaning (cancellations/returns, negative quantities, missing CustomerIDs, wholesale outliers) → a monthly cohort retention matrix and heatmap → RFM scoring and named segments → simple CLV → an action plan for each segment.
- *Crucial learnings:* how cohort analysis works, RFM, turning segments into actions, handling returns properly.
- *Deliverables:* the notebook, **an SQL version of the cohort query** (build it both ways), and a README memo.
- *Stretch:* compare K-means clustering with rule-based RFM.

**P4: Executive sales dashboard in Power BI**
- *Scenario:* "Build the performance dashboard the Sales VP opens every Monday."
- *Data:* your Olist PostgreSQL database from P2. This is realistic, because in real jobs BI tools sit on top of a database. *Alternative:* a multi-table dataset from the Maven Analytics Data Playground.
- *Milestones:* a requirements doc (users, questions, KPIs) → a star-schema model → DAX measures (YoY, YTD, MoM %, rolling 3-month, % of total, target vs actual) → 3 pages (executive overview, product/region drill-down, customer) → UX polish → a short user guide.
- *Crucial learnings:* data modelling for BI, DAX filter context, designing a dashboard for decisions, gathering requirements.
- *Deliverables:* the `.pbix` file, a PDF export, screenshots or a GIF in the README, and a measure dictionary.
- *Stretch:* rebuild one page in Looker Studio or Tableau Public to compare the tools.

**P5: A/B test analysis and decision**
- *Scenario:* "Should the mobile game move its first gate from level 30 to level 40?"
- *Data:* the Kaggle dataset *Mobile Games A/B Testing – Cookie Cats*.
- *Milestones:* sanity checks (sample-ratio mismatch, balance) → metric definitions (1-day and 7-day retention, engagement) → hypothesis tests and bootstrap CIs → a discussion of power and minimum detectable effect → a recommendation with risks.
- *Crucial learnings:* experimental rigour, statistics in a decision context, communicating uncertainty.
- *Deliverables:* the notebook and a one-page decision memo.
- *Stretch:* design the follow-up experiment (sample-size calculation and guardrail metrics).

**P6: Build your own dataset from an API**
- *Scenario:* "An NGO wants a refreshable dataset and analysis of development indicators (GDP, inflation, health, education) for a group of countries."
- *Data:* the World Bank Indicators API (no key needed), or another free public API that interests you.
- *Milestones:* explore the API and read its docs → an extraction script with pagination, retries, and logging → a tidy data model saved to Parquet/DuckDB → incremental refresh → analysis and charts → scheduling via Windows Task Scheduler or GitHub Actions (free).
- *Crucial learnings:* data acquisition, script engineering (functions, config, error handling), reproducible pipelines.
- *Deliverables:* a `src/` package, a README explaining how to run it, and an analysis notebook.
- *Stretch:* a small Streamlit app on top of the data.

### Phase 2 gate
- [ ] Live case with the teacher: "Weekly active users dropped 12%. Investigate." Structure your approach in 20 min.
- [ ] Explain p-value, statistical power, and SRM to a non-technical product manager.
- [ ] Build a YoY DAX measure and explain the filter context behind it.
- [ ] P3–P6 pass review and are published.

---

## Phase 3: Advanced: Analytics Engineering, Modelling & Impact (2026-12-07 → 2027-01-24)

**Goal:** operate like a senior analyst. That means building trustworthy data layers, forecasting, using ML as decision support, reasoning causally, and shipping tools.

### Modules

**3.1 Advanced SQL and performance.** `EXPLAIN ANALYZE`, indexes, sargable predicates, gaps-and-islands, sessionisation, funnels in SQL, recursive CTEs, dedup patterns, `QUALIFY`, JSON in SQL.
*Resources:* Use The Index, Luke; the PostgreSQL docs; hard DataLemur problems; Kaggle *Advanced SQL* (BigQuery).

**3.2 Data modelling and dbt.** Dimensional modelling (facts, dimensions, **grain**, SCD basics); staging → intermediate → marts layers; dbt models, sources, tests, docs, seeds, Jinja/macros basics, and incremental models.
*Resources:* dbt Learn *dbt Fundamentals* (free); dbt's guide "How we structure our dbt projects"; the dbt-duckdb adapter.

**3.3 Cloud warehouse basics.** BigQuery Sandbox (free, no card), public datasets, partitioning, and query-cost awareness; connecting Looker Studio.
*Resources:* the BigQuery sandbox docs and quickstarts; Kaggle *Intro to SQL* (runs on BigQuery).

**3.4 Time series and forecasting.** Decomposition; stationarity; **baselines first** (naive, seasonal naive); ETS and ARIMA intuition; regression and gradient boosting with lag features; time-based backtesting; MAE/MAPE/WAPE; forecasting for planning.
*Resources:* *Forecasting: Principles and Practice* (Hyndman & Athanasopoulos; free online, with a Python edition on OTexts); Kaggle Learn *Time Series*; the statsmodels docs.

**3.5 Machine learning for analysts.** Linear and logistic regression **with interpretation** (statsmodels); train/test splits and cross-validation; leakage; class imbalance; tree ensembles; precision/recall, ROC-AUC/PR-AUC, calibration; **choosing thresholds from business costs**; explainability (permutation importance, SHAP); when *not* to use ML.
*Resources:* Kaggle Learn *Intro* and *Intermediate ML*; the scikit-learn user guide; the StatQuest ML playlist; *An Introduction to Statistical Learning with Python* (ISLP, free PDF).

**3.6 Causal thinking for analysts.** Confounding, selection bias, regression adjustment, difference-in-differences, propensity-score basics, natural experiments, and when you can and can't claim impact.
*Resources:* *Causal Inference for the Brave and True* (free online); *The Effect* by Nick Huntington-Klein (free online).

**3.7 Data apps and automation.** Streamlit apps, parameterised reports, pipelines scheduled with GitHub Actions, config management, `pytest` for data code, and data-quality checks.
*Resources:* the Streamlit docs and Community Cloud; the GitHub Actions docs.

### Projects

**P7: A modern analytics pipeline with dbt**
- *Scenario:* "Our dashboards disagree on revenue. Build a trustworthy metrics layer from the raw tables."
- *Data:* the BigQuery public dataset `thelook_ecommerce` (orders, users, web events) via the sandbox. *Fully local alternative:* Olist in DuckDB.
- *Milestones:* source audit → a dbt project with staging, intermediate, and marts layers (`fct_orders`, `dim_customers`, `fct_sessions` built from events) → tests (unique, not_null, relationships, accepted_values, plus one custom test) → a docs site and lineage graph → a conversion funnel, retention, and revenue marts → a dashboard in Looker Studio or Power BI.
- *Crucial learnings:* analytics engineering, grain, data testing, documentation, sessionisation and funnel SQL.
- *Deliverables:* the dbt repo, a lineage screenshot, the dashboard, and a README with an architecture diagram.

**P8: Demand forecasting for inventory planning**
- *Scenario:* "Forecast the next 4 weeks of sales by store and product family to reduce stock-outs."
- *Data:* Kaggle *Store Sales – Time Series Forecasting* (Favorita).
- *Milestones:* EDA of seasonality, holidays, and promotions → baseline models → ETS/ARIMA or gradient boosting with lag features → proper backtesting → error broken down by segment → forecast error translated into business terms (safety stock) → a presentation of scenarios.
- *Crucial learnings:* time-based validation, the discipline of beating the baseline, communicating forecasts.

**P9: Churn prediction → retention campaign ROI**
- *Scenario:* "The retention team can call 500 customers a month. Who should they call, and is the campaign worth it?"
- *Data:* IBM *Telco Customer Churn* (Kaggle).
- *Milestones:* EDA and churn drivers → interpretable logistic regression vs gradient boosting → evaluation with PR-AUC and lift/gains charts → a cost-based decision threshold → SHAP explanations → an ROI simulation for the campaign → a stakeholder deck.
- *Crucial learnings:* ML as decision support, evaluation beyond accuracy, explainability, building a business case.
- *Stretch:* a "who to call" Streamlit app.

**P10: Capstone (your own question, end to end)**
- Pick a domain you want to work in (for example fintech, healthcare, retail, sports, or public policy).
- *Must include:* your own data acquisition (an API, scraping, or multiple sources); an SQL layer; at least one advanced method (a forecast, an experiment, causal analysis, or ML); a dashboard or app; a written report; and a recorded 10-minute presentation.
- The teacher plays the stakeholder across three reviews: proposal, mid-point, and final.

### Phase 3 gate
- [ ] Timed take-home simulation (4 hrs): raw data → insights → a short deck, graded against the rubric.
- [ ] Hard SQL set (sessionisation, gaps-and-islands) in 60 min.
- [ ] Explain a model's output and its limits to a non-technical executive.
- [ ] P7–P10 pass review and are published.

---

## Phase 4: Job-Ready Sprint (2027-01-25 → 02-07; start pieces from Phase 2 onward)

- **4.1 Portfolio.** Pin your best 4–6 projects. Polish each README into problem → approach → result → impact. Build a portfolio site with GitHub Pages (free).
- **4.2 Resume and LinkedIn.** Write impact-style project bullets and an ATS-friendly resume.
- **4.3 Interview prep.** Practise SQL live coding (DataLemur, StrataScratch free tier), product and metric case questions, stats questions, take-home strategy, and STAR behavioural stories. **The teacher runs mock interviews.**
- **4.4 Visibility.** Publish Kaggle notebooks, write LinkedIn posts about your projects, and take part in TidyTuesday or Makeover Monday.

---

## Continuous habits (every phase)

| Habit | Cadence |
|---|---|
| SQL drill: 2–3 problems (daily warm-up) | Daily |
| One chart from TidyTuesday or Makeover Monday | Weekly, on review day |
| Learning log entry (`notes/learning-log.md`) | After every session |
| Weekly quiz + weak-spot review | Weekly, on review day |
| Skill matrix update with the teacher | At each phase gate |

---

## Resource index (all free)

> Links can move. If one breaks, tell the teacher, who will find a free replacement and update this file.

**SQL:** SQLBolt (sqlbolt.com) · Select Star SQL (selectstarsql.com) · PostgreSQL Exercises (pgexercises.com) · LeetCode SQL 50 (leetcode.com/studyplan/top-sql-50) · DataLemur (datalemur.com) · StrataScratch (stratascratch.com) · Use The Index, Luke (use-the-index-luke.com)

**Python / pandas:** Kaggle Learn (kaggle.com/learn) · *Python for Data Analysis 3e* (wesmckinney.com/book) · pandas docs (pandas.pydata.org)

**Visualisation:** *Fundamentals of Data Visualization* (clauswilke.com/dataviz) · FT Visual Vocabulary (github.com/Financial-Times/chart-doctor) · Storytelling with Data blog

**Statistics:** StatQuest (youtube.com/@statquest) · Khan Academy Statistics · *OpenIntro Statistics* (openintro.org) · Evan Miller A/B tools (evanmiller.org/ab-testing)

**BI:** Microsoft Learn PL-300 paths (learn.microsoft.com) · DAX Guide (dax.guide) · SQLBI articles (sqlbi.com) · Guy in a Cube (YouTube) · Looker Studio

**Engineering:** dbt Learn (learn.getdbt.com) · dbt docs (docs.getdbt.com) · BigQuery Sandbox (cloud.google.com/bigquery/docs/sandbox) · Streamlit docs (docs.streamlit.io) · *Pro Git* (git-scm.com/book) · GitHub Skills (skills.github.com)

**Forecasting / ML / causal:** *Forecasting: Principles and Practice* (otexts.com) · ISLP (statlearning.com) · scikit-learn user guide · *Causal Inference for the Brave and True* (matheusfacure.github.io/python-causality-handbook) · *The Effect* (theeffectbook.net)

**Datasets:** Kaggle Datasets · UCI ML Repository (archive.ics.uci.edu) · Inside Airbnb (insideairbnb.com) · Our World in Data · World Bank Open Data / API · data.gov.in · BigQuery public datasets · TidyTuesday (github.com/rfordatascience/tidytuesday) · Makeover Monday · Maven Analytics Data Playground
