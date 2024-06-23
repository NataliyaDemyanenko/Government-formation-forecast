Government Formation Forecast App//
Overview
The Government Formation Forecast App is a tool designed to predict government coalition structure and power distribution within a government coalition based on the results of parliamentary elections or public opinion polls. 
It utilizes a cooperative game theory approach to provide empirically accurate forecasts of two aspects of the government formation process: which political parties will form a government coalition and the distribution of power within that coalition.

Features
Input Data: Accepts shares of votes received in parliamentary elections or levels of support in public opinion polls.
Constraints Handling: Considers credible commitments between each pair of political parties that preclude cooperation in the government formation process.
Output: Predicts the government formation process, in particular, which parties will form a coalition and how the power will be distributed.

Methodology
The algorithm utilizes the conditional Shapley value.
For empirical accuracy of the methodology see Demyanenko, N., & La Mura, P. (2023). Gamson–Shapley Laws: A formal approach to parliamentary coalition formation. Humanities and Social Sciences Communications, 10(1), 1-10.
For more details on methodology see Casajus, A., & La Mura, P. (2024). Null players, outside options, and stability: The conditional Shapley value. Journal of Mathematical Economics, 110, 102931.

Installation
To install and run the Government Formation Forecast App, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/government-formation-forecast.git
cd government-formation-forecast

Run the application:
bash
Copy code
python Gamson-Shapley.py

Usage
Prepare Input Data: Format your input data to include the shares of votes received or levels of support in public opinion polls and the bilateral constraints between political parties.
Run the Forecast: Use the app to input your data and generate a prediction of the government structure and power distribution.
Review Output: Analyze the predicted government coalition and the distribution of ministry posts among the participating parties.

Example
python
Copy code
from forecast_app import forecast_government

# Example input
vote_shares = {
    'Party A': 30,
    'Party B': 25,
    'Party C': 20,
    'Party D': 15,
    'Party E': 10
}

constraints = [
    ('Party A', 'Party D'),
    ('Party B', 'Party E')
]


Contributing
Contributions to the Government Formation Forecast App are welcome! Please follow these steps:
Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/your-feature-name.
Submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or feedback, please contact the project maintainers at nataliya.demyanenko@gmail.com.
