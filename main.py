# Main
# By: Alan Joji
# Created: 22.04.2023

# Libraries
import streamlit as st
from certificate import *
from python_xss import *
from sql_injection import *

# Main
st.title("Security Operations Center - Web Vulnerability Scanner Application")


st.markdown( """ 
# SSL Certificate Verification 
## Features
- Checks the whether the 4-Way TLS-SSL Handshake is completed
- **Method 1:** Allows the user to Request a URL with verify set to True, Option the user to set their own Verified/Trusted CA Directory
- **Method 2:** Allows the user to Request a Hostname, Creates an SSL Context and Verifies the Certificates
"""
, True)

hostname =  st.text_input("Domain")
if not hostname :
    pass
else :
    hostname_result = hostname_is_safe(hostname)
    if hostname_result == True :
        st.write(hostname, " **has a valid SSL Certificate**")
    elif hostname_result == False :
        st.write(hostname, " **has a invalid/no SSL Certificate**")

url =  st.text_input("URL")
if not url :
    pass
else :
    url_result = url_is_safe(url)

    if url_result == True :
        st.write(url, " **has a valid SSL Certificate**")
    elif url_result == False :
        st.write(url, " **has a invalid/no SSL Certificate**")

st.markdown( """ 
> _Check Terminal for Information about Certificate and 2nd Part of 4 Way TLS Handshake_
"""
, True)


st.markdown( """ 
# Reflective Cross Site Scripting 
## Features
- Checks for Reflective XSS 
- Code is Injected into the URL, the result of the Penetration is used to Test if a URL is XSS Vulnerable
> This method can allow **redirection** or **access to cookies** local cookies through JS
"""
, True)

if not url :
    pass
else :
    url_result = is_python_xss_vulnerable(url)

    if url_result == True :
        st.write(url, " **is Vulnerable to R-XSS**")
    elif url_result == False :
        st.write(url, " **is not Vulnerable to R-XSS**")

st.markdown( """ 
# SQL Injection
## Features
- Checks for Common SQL Injection Vulnerabilites that Result in Condition = True
- Scrapes all Forms on a URL, checks whether the site is vulnerable SQL Injection
"""
, True)

if not url :
    pass
else :
    session = Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    url_result = sql_is_safe(url, session)

    if url_result == True :
        st.write(url, " **@ SQL Injection Vulnerability**")
    elif url_result == False :
        st.write(url, " **@ No SQL Injection Vulnerability**")


st.markdown( """ 
> _Check Terminal for Information about the Forms on the Website and the Analysis and Debugging for each Form_
"""
, True)