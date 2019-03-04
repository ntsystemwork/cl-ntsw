-- Make unique number

update account_invoice
  set number = number || cast(id as varchar);
