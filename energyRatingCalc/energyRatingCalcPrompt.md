Src: https://www.101computing.net/light-bulb-energy-rating-calculator/

Goal: Write a Python program that will determine the energy rating of
  a lightbulb based on user inputs. If the rating is G or A, throw an
  error.

Relevant Information:
  * Efficiency ratio = (luminous flux) / (power consumption)
  * Luminous flux is in lumens (lm), power consumption is in kilowatts
    per 1,000 hours (kW/1000hr)
  * The energy rating is a letter grade based on the ratio
  * A: ≥210, B: ≥185, C: ≥160, D: ≥135, E: ≥110, F: ≥85, G: <85
  * If the rating is A, throw an exception with the text "The rating
    is too high"
  * If the rating is G, throw an excpetion with the text "The rating
    is too low"
  * Ex:
    * 1600 lm, 8 kW/1000hr: B
    * 1800 lm, 5 kW/1000hr: A
    * 1100 lm, 12 kw/1000hr: F
    * 84 lm, 1 kw/1000hr: G
