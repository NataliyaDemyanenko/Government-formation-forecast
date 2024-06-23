Government Formation Forecast App<br />
Overview<br />
The Government Formation Forecast App is a tool designed to predict government coalition structure and power distribution within a government coalition based on the results of parliamentary elections or public opinion polls. <br />
It utilizes a cooperative game theory approach to provide empirically accurate forecasts of two aspects of the government formation process: which political parties will form a government coalition and the distribution of power within that coalition.<br />

Features<br />
Input Data: Accepts shares of votes received in parliamentary elections or levels of support in public opinion polls.<br />
Constraints Handling: Considers credible commitments between each pair of political parties that preclude cooperation in the government formation process.<br />
Output: Predicts the government formation process, in particular, which parties will form a coalition and how the power will be distributed.<br />

Methodology<br />
The algorithm utilizes the conditional Shapley value.<br />
For empirical accuracy of the methodology see Demyanenko, N., & La Mura, P. (2023). Gamson–Shapley Laws: A formal approach to parliamentary coalition formation. Humanities and Social Sciences Communications, 10(1), 1-10.<br />
For more details on methodology see Casajus, A., & La Mura, P. (2024). Null players, outside options, and stability: The conditional Shapley value. Journal of Mathematical Economics, 110, 102931.<br />

Installation<br />
To install and run the Government Formation Forecast App, follow these steps:<br />

Clone the repository:<br />
bash<br />
Copy code
git clone https://github.com/your-username/government-formation-forecast.git<br />
cd government-formation-forecast<br />

Run the application:<br />
bash<br />
Copy code<br />
python Gamson-Shapley.py<br />

Usage<br />
Prepare Input Data: Format your input data to include the shares of votes received or levels of support in public opinion polls and the bilateral constraints between political parties.<br />
Run the Forecast: Use the app to input your data and generate a prediction of the government structure and power distribution.<br />
Review Output: Analyze the predicted government coalition and the distribution of ministry posts among the participating parties.<br />

Example<br />

# Example input<br />
vote_shares = {<br />
    'Party A': 30,<br />
    'Party B': 25,<br />
    'Party C': 20,<br />
    'Party D': 15,<br />
    'Party E': 10<br />
}

constraints = [<br />
    ('Party A', 'Party D'),<br />
    ('Party B', 'Party E')<br />
]<br />


Contributing<br />
Contributions to the Government Formation Forecast App are welcome! Please follow these steps:<br />
Fork the repository.<br />
Create a new branch: git checkout -b feature/your-feature-name.<br />
Commit your changes: git commit -m 'Add some feature'.<br />
Push to the branch: git push origin feature/your-feature-name.<br />
Submit a pull request.<br />

License<br />
This project is licensed under the MIT License. See the LICENSE file for details.<br />

Contact<br />
For any questions or feedback, please contact the project maintainers at nataliya.demyanenko@gmail.com.<br />
