few_shots = [
    {'Question' : "how much claim payment was made in year 2021?",
     'SQLQuery' : "SELECT sum(payment) FROM financial WHERE claimnum IN (SELECT claimnum FROM claims WHERE claim_date BETWEEN '2021-01-01' AND '2021-12-31')",
     'SQLResult': "Result of the SQL query",
     'Answer' :"10000.0"},
    {'Question': "how much claim reserves was made in year 2022?",
     'SQLQuery':"SELECT sum(reserves) FROM financial WHERE claimnum IN (SELECT claimnum FROM claims WHERE claim_date BETWEEN '2022-01-01' AND '2022-12-31')",
     'SQLResult': "Result of the SQL query",
     'Answer': "62400.0"},
    {'Question': "how much claim payment was made in year 2021 and 2022?" ,
     'SQLQuery' : "SELECT sum(payment) FROM financial WHERE claimnum IN (SELECT claimnum FROM claims WHERE claim_date BETWEEN '2021-01-01' AND '2022-12-31')",
     'SQLResult': "Result of the SQL query",
     'Answer': "36200.0" 
     }
]