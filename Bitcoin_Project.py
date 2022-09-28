"""
    In this project, a program was created that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000 print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) function to calculate bitcoin to usd.
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  usd_value = 1.2 * 4000
  return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if investment_in_usd <= 30001:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")


# 2) use function to calculate if its below $X amount.