--- Output: raw/invoices.csv
SELECT 
    invoice_id,
    customer_id,
    invoice_date,
    due_date,
    invoice_amount,
    currency,
    payment_status
FROM dbo.invoices;