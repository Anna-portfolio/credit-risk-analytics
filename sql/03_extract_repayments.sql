--- Output: raw/repayments.csv
SELECT 
    repayment_id,
    invoice_id,
    repayment_date,
    repayment_amount,
    payment_method
FROM dbo.repayments;