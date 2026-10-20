"""
verify_connection.py — run this first to confirm your setup is correct.

Usage:
    python exercises/verify_connection.py

Expected output:
    Connected — SAP HANA Cloud 4.x.x
    PAL: available ✓
    Vector embeddings: available ✓
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

HANA_HOST     = os.getenv("HANA_HOST")
HANA_PORT     = int(os.getenv("HANA_PORT", 443))
HANA_USER     = os.getenv("HANA_USER", "DBADMIN")
HANA_PASSWORD = os.getenv("HANA_PASSWORD")

if not HANA_HOST or not HANA_PASSWORD:
    print("ERROR: HANA_HOST or HANA_PASSWORD not set in .env")
    print("Create a .env file in the project root — see setup_guide.md")
    sys.exit(1)

try:
    from hana_ml.dataframe import ConnectionContext
except ImportError:
    print("ERROR: hana-ml is not installed.")
    print("Run:  pip install -r requirements.txt")
    sys.exit(1)

print(f"Connecting to {HANA_HOST}:{HANA_PORT} ...")
try:
    cc = ConnectionContext(
        address=HANA_HOST, port=HANA_PORT,
        user=HANA_USER, password=HANA_PASSWORD, encrypt=True,
    )
except Exception as e:
    print(f"ERROR: Could not connect — {e}")
    print("Check your HANA_HOST, HANA_USER, and HANA_PASSWORD in .env")
    sys.exit(1)

print(f"Connected — SAP HANA Cloud {cc.hana_version()}")

# Check PAL — the trial instance registers it as 'AFLPAL'
cursor = cc.connection.cursor()
cursor.execute("SELECT COUNT(*) FROM SYS.AFL_AREAS WHERE AREA_NAME = 'AFLPAL'")
pal_ok = cursor.fetchone()[0] > 0
print(f"PAL: {'available ✓' if pal_ok else 'NOT available ✗ — contact your instructor'}")

# Check vector embeddings and list available models
try:
    cursor.execute("SELECT VECTOR_EMBEDDING('test', 'DOCUMENT', 'SAP_GXY.20250407') FROM DUMMY")
    cursor.fetchone()
    emb_ok = True
except Exception:
    emb_ok = False
print(f"Vector embeddings: {'available ✓' if emb_ok else 'NOT available ✗ — contact your instructor'}")

# List available embedding models
try:
    cursor.execute("SELECT * FROM NLP_VECTOR_EMBEDDING_MODELS")
    rows = cursor.fetchall()
    cols = [d[0] for d in cursor.description]
    if rows:
        print("\nAvailable embedding models:")
        for row in rows:
            print("  " + "  |  ".join(f"{c}: {v}" for c, v in zip(cols, row)))
    else:
        print("\nNo embedding models found.")
except Exception as e:
    print(f"\n(Could not retrieve model list: {e})")

cursor.close()
cc.close()

if not pal_ok or not emb_ok:
    print("\nSee setup_guide.md § 2 for how to enable Script Server.")
    sys.exit(1)

print("\nAll checks passed — you are ready to start Exercise 1!")
