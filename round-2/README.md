# Applied Machine Learning for Engineering Systems @Faculty of Engineering in Foreign Languages, National University of Science and Technology POLITEHNICA Bucharest



---

## 1. Get Your SAP HANA Cloud Trial Instance

### Step 1 — Sign up for the trial

1. Go to: **https://www.sap.com/products/data-cloud/hana/trial.html**
2. Click **"Try now"** and register with your university email
3. You will receive a link to a guided workbook:
   **Basic Trial — Introduction to SAP HANA Cloud**

> If there are issues with environment being accessed, also try this link as an alternative: [trial](https://cockpit.hanatrial.ondemand.com/trial/)

### Step 2 — Log in to Database Explorer

Inside the workbook, navigate to:
**Getting Started and Introduction → Getting Started → Logging into Database Explorer (DBX)**

Your login credentials (username and password) are shown on screen and were also sent to your email.

> These are **not** DBADMIN credentials — use exactly the username and password shown in the workbook / your email.

### Step 3 — Find your connection host

Once logged in to Database Explorer:

1. In the left panel, locate your database instance
2. **Right-click** the instance → choose **Properties**
3. Copy the **Host** value — it looks like:
   ```
   abc123.hanacloud.ondemand.com
   ```

You now have everything you need:

| Variable | Where to find it |
|----------|-----------------|
| `HANA_HOST` | Host from Properties (step above) |
| `HANA_PORT` | `443` |
| `HANA_USER` | Username shown in workbook / email |
| `HANA_PASSWORD` | Password shown in workbook / email |

---

## 2. Set Up the Python Environment

### Requirements

- Python 3.9 or later
- `pip`

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create your `.env` file

Create a file named `.env` in the project root:

```
HANA_HOST=abc123.hanacloud.ondemand.com
HANA_PORT=443
HANA_USER=your-username-from-email
HANA_PASSWORD=your-password-from-email
```

> **Never commit `.env` to Git** — it is already listed in `.gitignore`.

### Verify the connection

```bash
python exercises/verify_connection.py
```

Expected output:
```
Connected — SAP HANA Cloud 4.x.x
PAL: available ✓
Vector embeddings: available ✓

Available embedding models:
  SAP_GXY  (version: 20250407 | dims: 768)
```

---

## 3. Verify PAL and Vector Embeddings Are Available

You can also confirm directly in Database Explorer:

```sql
-- PAL available? (should return a row with AREA_NAME = 'AFLPAL')
SELECT * FROM SYS.AFL_AREAS WHERE AREA_NAME = 'AFLPAL';

-- Vector embedding test
SELECT VECTOR_EMBEDDING('hello world', 'DOCUMENT', 'SAP_GXY.20250407') FROM DUMMY;

-- List all available embedding models
SELECT * FROM NLP_VECTOR_EMBEDDING_MODELS;
```

---



## 4. Known Limitations of the Free Tier

| Capability | Free Tier Limit | Notes |
|-----------|-----------------|-------|
| Memory | 30 GB | Sufficient for this workshop |
| Storage | 120 GB | Sufficient |
| PAL | ✅ Fully included | Pre-enabled in the trial instance |
| Vector embeddings | ✅ Fully included | Pre-enabled in the trial instance |
| Concurrent users | 1 per instance | Each student has their own instance |
| Auto-stop | After 30 days of inactivity | Restart from the trial workbook |

---

## 6. HANA Quick Reference

| Topic | URL |
|-------|-----|
| HANA Cloud Trial | https://www.sap.com/products/data-cloud/hana/trial.html |
| PAL Documentation | https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-predictive-analysis-library-pal/predictive-analysis-library-pal |
| Vector Engine Guide | https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-vector-engine-guide |
| hana-ml on PyPI | https://pypi.org/project/hana-ml/ |

---

## 7. Repository Structure

```
summer_school_upb_2026/
├── slides/
│   └── index.html              ← Reveal.js presentation (open in browser)
├── exercises/
│   ├── verify_connection.py    ← Run this first to check your setup
├── outputs/                    ← Generated charts (git-ignored)
├── .env                        ← YOUR credentials (git-ignored)
├── requirements.txt
└── README.md
```

---

## 8. ClinicalTrials.gov Quick Reference

| Topic | URL |
|-------|-----|
| ClinicalTrials.gov Home | https://clinicaltrials.gov/ |
| Study Data API (v2) | https://clinicaltrials.gov/data-api/about-api |
| API Migration Guide | https://clinicaltrials.gov/data-api/about-api-migration |
| Study Fields / Data Structure | https://clinicaltrials.gov/data-api/about-study-data-structure |
| API Reference (OpenAPI/Swagger) | https://clinicaltrials.gov/data-api/api |
