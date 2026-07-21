---sample quality checks for customers, invoices, and repayments


---check #1: missing data (expected result: 0 rows)
SELECT *
FROM customers
WHERE customer_id IS NULL
   OR company_name IS NULL
   OR industry IS NULL
   OR segment IS NULL
   OR country IS NULL
   OR registration_date IS NULL
   OR annual_turnover IS NULL;

SELECT *
FROM invoices
WHERE invoice_id IS NULL
   OR customer_id IS NULL
   OR invoice_amount IS NULL
   OR invoice_date IS NULL
   OR due_date IS NULL;

SELECT *
FROM repayments
WHERE repayment_id IS NULL
   OR invoice_id IS NULL
   OR repayment_date IS NULL
   OR repayment_amount IS NULL;


---check: duplicates (expected result: 0 rows)
SELECT
    customer_id,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT
    invoice_id,
    COUNT(*) AS duplicate_count
FROM invoices
GROUP BY invoice_id
HAVING COUNT(*) > 1;

SELECT
    repayment_id,
    COUNT(*) AS duplicate_count
FROM repayments
GROUP BY repayment_id
HAVING COUNT(*) > 1;

---check: Referential integrity checks
---invoice without customer
SELECT
    i.invoice_id,
    i.customer_id
FROM invoices i
LEFT JOIN customers c
    ON i.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

---payment without invoce
SELECT
    r.repayment_id,
    r.invoice_id
FROM repayments r
LEFT JOIN invoices i
    ON r.invoice_id = i.invoice_id
WHERE i.invoice_id IS NULL;

---check: Business rules checks
---invoice amounts need to be higher than 0 (expected result: 0 rows)
SELECT *
FROM invoices
WHERE invoice_amount <= 0;

---repayment data needs to be after invoice date (expected result: 0 rows)
SELECT
    r.repayment_id,
    r.repayment_date,
    i.invoice_date
FROM repayments r
JOIN invoices i
    ON r.invoice_id = i.invoice_id
WHERE r.repayment_date < i.invoice_date;


---check: Financial consistency check
--- check if customer did not pay more than the invoice amount (expected result: 0 rows)
SELECT
    i.invoice_id,
    i.invoice_amount,
    SUM(r.repayment_amount) AS total_repaid

FROM invoices i

LEFT JOIN repayments r
    ON i.invoice_id = r.invoice_id

GROUP BY
    i.invoice_id,
    i.invoice_amount

HAVING SUM(r.repayment_amount) > i.invoice_amount;