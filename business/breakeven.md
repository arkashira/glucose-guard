# breakeven.md
## Unit Economics
### Cost per Active User
Based on the glucose-guard system's architecture, we estimate the following costs:
* Compute: $0.05 per user per month (assuming 10% average utilization of a $5/month server)
* Storage: $0.01 per user per month (assuming 1GB storage per user at $0.10/GB-month)
* Bandwidth: $0.02 per user per month (assuming 100MB/month bandwidth at $0.20/GB)
Total cost per active user: $0.08 per month

## Pricing Tiers
We propose the following pricing tiers:
1. **Basic**: $9.99/month - limited to 100 readings per month, basic analytics, and email support
2. **Premium**: $19.99/month - unlimited readings, advanced analytics, priority support, and integration with popular health apps
3. **Pro**: $49.99/month - all premium features, plus personalized coaching, dedicated support, and advanced data export options

## Customer Acquisition Cost (CAC) Range
Based on industry benchmarks, we estimate the CAC to be between $15 and $30 per user.

## Lifetime Value (LTV) Estimate
Assuming an average user retention rate of 75% per annum, and an average revenue per user (ARPU) of $19.99 (weighted average of the pricing tiers), we estimate the LTV to be:
LTV = ARPU / (1 - retention rate) = $19.99 / (1 - 0.75) = $79.96

## Break-even Analysis
Break-even point (BEP) = CAC / (LTV - CAC)
Using the estimated CAC range and LTV, we calculate the BEP:
* Best case (CAC = $15): BEP = 15 / (79.96 - 15) = 0.23 years or approximately 2.7 months
* Worst case (CAC = $30): BEP = 30 / (79.96 - 30) = 0.61 years or approximately 7.3 months

## Break-even Users Count
To calculate the break-even users count, we need to consider the monthly costs and revenue:
Monthly costs = $0.08 per user (as estimated earlier)
Monthly revenue per user = $19.99 (weighted average of the pricing tiers)
Break-even users count = Total monthly costs / (Monthly revenue per user - Monthly costs)
Assuming 1,000 users, the total monthly costs would be $80 (1,000 users \* $0.08). The total monthly revenue would be $19,990 (1,000 users \* $19.99).
Break-even users count = $80 / ($19.99 - $0.08) ≈ 4 users (this calculation is not meaningful, as the costs are negligible compared to the revenue. A more realistic approach would be to consider the fixed costs, such as server and personnel costs, and calculate the break-even point based on those.)

## Path to $10K MRR
To reach $10,000 MRR, we would need:
* 500 users on the **Premium** tier ($19.99/month)
* Alternatively, a combination of users across the different tiers, such as:
	+ 200 users on the **Pro** tier ($49.99/month) = $9,998/month (close to the target)
	+ 100 users on the **Pro** tier ($49.99/month) = $4,999/month + 250 users on the **Premium** tier ($19.99/month) = $4,997.50/month (total: $9,996.50/month)

Note that these calculations are simplified and do not take into account various factors that can affect the actual revenue and user growth.