# Big Data Privacy Audit Pipeline

A distributed data pipeline using **PySpark** and **AWS S3** to scan massive datasets for **Personally Identifiable Information (PII)**.

> Designed to showcase enterprise-grade big data and privacy engineering skills for roles at top-tier tech companies.

---

## Project Structure

```
big-data-privacy-audit/
├── scripts/
│   └── scan_reviews.py        # Spark job to scan for PII
├── tests/
│   └── test_scanner_logic.py # Pytest unit tests
├── requirements.txt           # All dependencies
└── README.md                  # Documentation you're reading
```

---

## Usage

### Prerequisites

- Python 3.8+
- Java 8 or 11
- AWS CLI configured (`~/.aws/credentials`)
- Spark installed locally or running on a cluster

---

### Run the Application

```bash
# Clone the repository
git clone https://github.com/mehreenkabir/big-data-privacy-audit.git
cd big-data-privacy-audit

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the PII scanner
python scripts/scan_reviews.py
```

---

## Run the Tests

To validate the `find_pii` detection logic:

```bash
pytest
```

**Expected output:**

```
========== test session starts ==========
...
tests/test_scanner_logic.py ........                          [100%]
========== 8 passed in X.XXs ==========
```

---

## Project Highlights

- Distributed PII Scanning (emails, IPs) at scale
- Reads directly from Amazon S3 (Parquet format)
- Optimized for Big Data (PySpark UDFs, columnar formats)
- Unit-tested core logic using `pytest`

---

## License

MIT License © [Mehreen Kabir](https://github.com/mehreenkabir)

---
