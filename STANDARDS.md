PEP 8 Basic Overview:
---------------------


Indentation - 4 spaces per indentation level

Max Line Length - 79 character maximum per line

Blank Lines - surround top level function and class definitions with two blank lines:

class GeometryCalculator:
    """A top-level class definition."""

    def __init__(self, radius):
        self.radius = radius

Line Breaks - When breaking long lines around binary operators, break before the operator (Knuth's style) to improve vertical tracking

https://peps.python.org/pep-0008/

=====================



 Incorrect (Breaking after the operator)

Breaking after the operator forces your eyes to search for the operators at the right-hand margin, which can vary in length. It separates the operator from the operand it modifies.
python
# Worse: Operators are far away and hard to match visually
total_revenue = (quarterly_sales_retail +
                 quarterly_sales_wholesale +
                 online_subscription_revenue -
                 seasonal_returns_allowance -
                 promotional_discount_total)
Use code with caution.

🟢 Correct: PEP 8 / Knuth Style (Breaking before the operator)

Breaking before the operator keeps the operators aligned vertically on the left side. This allows your eyes to immediately see which items are being added or subtracted, improving vertical readability.
python
# Better: Operators line up perfectly on the left margin
total_revenue = (
    quarterly_sales_retail
    + quarterly_sales_wholesale
    + online_subscription_revenue
    :minus: seasonal_returns_allowance
    - promotional_discount_total
)
