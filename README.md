# WebScan

> Built as a couter-part for [PortScan](https://github.com/AlanJoji/PortScan) reconnaisance and pen-testing

1. The SSL certificate for the specified URL, or hostname
	- Creates a *socket* and an *SSL context* which is placed over the socket; *2nd Phase of (4 Phase) TLS-SSL Handshake*
	- Checks the domain’s SSL Certificate, this *can be configured to make sure a set of CA’s trusted by the User*
2. Performs a Check for R-XSS attack
	- Runs a script to check if the page is vulnerable to XSS
3. Performs a SQL Injection Check
	- Finds all the forms on the webpage
	- Checks if the form is vulnerable to SQL vulnerability by checking it against a set of characters.

## Tech Stack

**Languages:** python, markdown, javascript, sql

**LocalHost:** streamlit


## Run Locally

**Clone the project**

```bash
  git clone https://github.com/AlanJoji/WebScan.git
```

**Go to the project directory**

```bash
  cd WebScan
```

**Install dependencies**

1. For SSL
```bash
  pip install ssl 
```

2. For making requests to websites
```bash
  pip install requests
```

3. For streamlit 
```bash
  pip install streamlit
```

**Run the Program**
```bash
    streamlit run main.py
```

## Author

- [Alan Joji](https://github.com/AlanJoji)

**DISCLAIMER**

THIS SOFTWARE WAS CREATED FOR AUTOMATED PENETRATION TESTING AND INFORMATION GATHERING. CONTRIBUTOR WILL NOT BE RESPONSIBLE FOR ANY ILLEGAL USAGE.
