## Key Ideas
Betting Odds: 
- Betting odds work by reflecting the implied chance of an outcome in monetary terms inclusive of the operator's margin.
![[Pasted image 20230530142009.png]]
- 

## Example: Two-Horse Race
- One horse has 20% chance to win, another has 80% chance (but assume bookie actually knows this)
- $10000 is put on the first one and $50000 on the second
If odds are set 4-1:
- Bookie may gain $10000 (if first horse wins). He would have to pay back 10k and 4 times more, so 50000 altogether. But he received $60000 so he keeps $10000
- If the second horse wins, he would have to pay $50000 and 1/4 of it, so $62500. Which means he would lose $2500.
- The expectation of the bookie's returns is 0.2 * 10000 + 0.8 * -2500 = 0.
If the odds are set 5-1:
- Bookie will not lose or gain money no matter which horse wins

## Risk Neutral Valuation: Introduction
Interested in finding prices of various derivatives.
- Mostly derivatives on stocks, but more complicated derivatives exist whose underlying could be interest rates, bonds, swaps, commodities, etc
- Usually the underlying is liquid and traded on exchanges
### Main Points
- Given the current price of the stock and assumptions on the dynamics of stock price, there is no uncertainty about the price of a derivative.
- The price is defined only by the price of the stock and not by the risk preferences of the market participants. Risk neutrality. Only depends on dynamics / volatility of the stock.
- Mathematical apparatus allows to compute current price of a derivative and its risks, given certain assumptions about the market.
