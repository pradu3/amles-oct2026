# Challenge #2: ClinicalTrials.gov Data Product Prototype on SAP HANA
> Presentation Date: Thursday, November 26, 2026
 
## Objective
Design, build, and pitch an initial working prototype (first-step proof of concept) for a data product built on top of the ClinicalTrials.gov dataset using SAP HANA and its native machine learning capabilities.
 
> Scope Note: You are not expected to build a polished application, custom frontend, or production-ready system. This challenge is strictly about taking the first technical step: testing feasibility on real data, implementing a minimal baseline pipeline in SAP HANA, and showing early directional results.
 
## Prerequisites
Before starting this challenge, ensure the following setup steps are complete:
 
- **Database Setup**: ClinicalTrials.gov data is loaded into your SAP HANA instance.
- **ML Engine**: SAP HANA Predictive Analysis Library (PAL) is activated and ready for use.
- **Prior Tasks**: All requirements from Round 2 (amles-oct2026/round-2) are completed.

## Deliverables

1. Data Product Concept (First-Step Scope)
Define a concrete, practical data product use case leveraging the ClinicalTrials.gov dataset.
Identify the target audience.
Specify the exact decision or workflow your solution improves.
Define the minimal scope selected for this initial proof of concept.

2. The 1-Minute Pitch
Prepare a strict 1-minute pitch aimed at stakeholders covering:
Problem Statement: What pain point or gap exists in clinical trial analysis?
Proposed Solution: What will your data product do, and what does this first prototype demonstrate?
Value Proposition: Why is this useful, and what impact could it create if scaled?

3. The 5-Minute Technical Walkthrough & Live Prototype Demo
Prepare a 5-minute technical explanation and live demo showing how you implemented your first-step prototype.
 
### Acceptable Prototype Artifacts (What Your Demo Might Show):
Your demo should be grounded in working code and database execution rather than mockups. Depending on your architecture, a valid prototype demo might include:
- Exploratory and scoring SQL SELECT queries run directly against your HANA tables or views
- One or more SAP HANA SQLScript stored procedures encapsulating data preparation and PAL model execution
- Python scripts or notebooks (e.g., using hana-ml or hdbcli) orchestrating training, inference, or evaluation
- A lightweight AI agent or tool-calling script that queries your HANA views or procedures to answer domain questions
- Raw output tables, terminal logs, or simple charts demonstrating that the pipeline runs end-to-end

## Required Technical Discussion Points
During your walkthrough, explicitly address:
 
#### Data Size & Quality: 
- State how many rows and features are available in your HANA tables for your specific use case.
- Detail the data quality issues encountered (e.g., missing values, inconsistent status labels, unstructured free-text fields, class imbalance).
- Assess whether the current dataset is sufficient to move forward, or what additional data and cleaning would be needed in a second iteration.

#### Algorithm Selection:
- Specify which SAP HANA PAL algorithm(s) you selected for your baseline model.
- Explain why this algorithm is an appropriate starting point given your data structure and target objective.

#### Preliminary Results:
- Present concrete outputs, baseline evaluation metrics, or sample predictions directly from your HANA execution.
- Outline the main limitations observed in this first pass and what you would improve next.
- Presentation Format & Schedule


Total Time per Individual: 6 minutes
Part 1 (Pitch): 1 minute
Part 2 (Prototype Walkthrough & Demo): 5 minutes
