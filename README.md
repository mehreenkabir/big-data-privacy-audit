# Big Data Privacy Audit Pipeline

A distributed data pipeline using PySpark and AWS S3 to scan massive datasets for Personally Identifiable Information (PII).

---

## Project Structure
Use code with caution.
Markdown
big-data-privacy-audit/
├── scripts/
│ └── scan_reviews.py
├── tests/
│ └── test_scanner_logic.py
├── requirements.txt
└── README.md
Generated code
---

## Usage

### Prerequisites
-   Python 3.8+
-   Java 8 or 11
-   Configured AWS Credentials

### Instructions

1.  Clone the repository:
    ```bash
    git clone https://github.com/mehreenkabir/big-data-privacy-audit.git
    cd big-data-privacy-audit
    ```

2.  Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the application:
    ```bash
    python scripts/scan_reviews.py
    ```

---

## Run the Tests

To validate the PII detection logic, run the test suite:

```bash
pytest
Use code with caution.
Expected output:
Generated code
========== test session starts ==========
...
tests/test_scanner_logic.py ........                                     [100%]
========== 8 passed in X.XXs ==========
Use code with caution.
License
MIT License © Mehreen Kabir
