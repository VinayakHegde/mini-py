![Star Badge](https://img.shields.io/static/v1?style=flat&color=green&logo=python&label=MiniPy&message=%F0%9F%8C%9F%20If%20you%20found%20it%20useful) <a href="https://github.com/VinayakHegde">![Star Author](https://img.shields.io/static/v1?&style=flat&color=green&logo=github&label=Author&message=Vinayak%20Hegde)</a>

# Email Marketing Automation

## 🛠️ Description

This python programe helps to automate the process of sending mail to larger recipients. 

**Input**: It takes csv as input file where recipients details stored in the following format.
```csv
name,email
recipient1,recipient1@email.com
```

## ⚙️ Modules Used

Program used modules comes with python3 
`smtplib`
`csv`
`json`
`email`

 
## 🤖 How to run
- Update email subject and template dir and csv file name in the `app.config.json`
- Create `.env` at the root and update the credentials (have a look at `.env.example` file) 
- Run the program using `python3 main.py`

**Note for gmail users**: your gmail id and app password as mentioned [here](https://support.google.com/mail/answer/185833?hl=en-GB). Use `smtp.gmail.com` as host and port `465`.
