
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~    INSTRUCTIONS    ~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clone repository
2. Use pip to install requirements.txt (i.e. `> pip install requirements.txt`)
3. Update `template example.xlsx` with new tenants, and fill out details
   (See description below for further explanation of the template)
4. Run main script (i.e. `python main.py`)
5. Results will be in the newly created `output.xlsx`


Note:  Be sure to close the `output.xlsx` file before running again.  The template
       can remain open, but be sure to save for changes to be included.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~     TEMPLATE     ~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

** SHEET 1 **

New rows (i.e. additional tenants) can be added by just filling out a new row.

<prorate_factor> is used to quantify relative payment amounts.
Rather than implement fractions, which are dependent on the amount of active tenant for a given month,
the <prorate_factor> is expressed as a multiple of the average rent.  These amounts are then normalized
based on how many people are present, allowing prorated rent amounts to be calculated in an automated manner.


To change the renting schedule, adjust the TRUE/FALSE values for each month.


** SHEET 2 **

<monthly_rent> is the gross monthly rate requested by the leasing company

<credit> is a sum total of credit/discount granted by the leasing company.
ex. one month free ($9365) + $2000 credit = $11365

<credit_month_applied> is the month to which the total <credit> is applied.
The credit amount is distributed in a prorated fashion to tenants present at the house that month.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~      OUTPUT      ~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"(present average)" is calculated as the average per-person rent paid by tenants currently living at the house.
"(active average)" is caluclated as the average per-month rent paid by tenants across months they were active at the house.
