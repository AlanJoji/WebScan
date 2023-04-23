# SQL Injection Checking
# By: Alan Joji
# Created: 19.04.2023

from requests import *
from bs4 import BeautifulSoup
from sys import *
from urllib.parse import urljoin
import streamlit as st

# Function
# Debugging Scripts are placed where required

def get_forms (url, session) :
    """
    Input:  
        URL for the website
        Session eastablished using a browser user agent
    Action: 
        Reads all the forms that are present on the website
    Output:     
        Returns all the forms on the website
    """
    soup = BeautifulSoup(session.get(url).content, "html.parser")
    form = soup.find_all("form")

    return form


def get_form_details (form) :
    """
    Input:  
        One Form from the website
    Action: 
        Produces the dictionary of details for that One Form 
        - Action -> Action for the form
        - Method -> Method used by the form
        - Inputs -> Inputs & Submit as a List of Dictionaries(contains type, name, value)
    Output:     
        Returns Form Details for One Form
    """
    form_details = {}

    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")

    inputs = []

    for input_tag in form.find_all("input") :
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")

        inputs.append({
            "type": input_type,
            "name": input_name,
            "value": input_value
        })
    
    form_details["action"] = action
    form_details["method"] = method
    form_details["inputs"] = inputs

    return form_details


def is_sql_vulnerable (response) :
    """
    Input:  
        Response from the Server
    Action: 
        Checks response against a common set of errors produced at during SQL injection
    Output:     
        Returns 
        - True -> Vulnerability Found
        - False -> Vulnerability Not Found
    """
    errors = {"quoted string not properly terminated",
              "unclosed quoatation mark after the character string",
              "you have an error in your sql syntax"}
    
    for error in errors :
        if (error in response.content.decode().lower()) :
            return True
        else :
            return False
            
        
def sql_is_safe (url, session) :
    """
    Input:  
        URL for the website
        Session eastablished with the website
    Action: 
        Driver function for all SQL injection
    Output:     
        None
    """
    forms = get_forms(url, session)

    # From: Number of Forms 
    st.write("**Number of forms detected:** ", len(forms), "@", url)
    # Till

    print("Number of forms detected: ", len(forms))   

    malicious_characters = "\"'"

    for form in forms :
        details = get_form_details(form)
        # print("Details:", details["inputs"])

        for character in malicious_characters :
            data = {}
            
            for input_tag in details["inputs"] :
                if (input_tag["type"] == "hidden" or input_tag["value"]) :
                    data[input_tag['name']] = input_tag["value"] + character
                
                elif (input_tag["type"] != "submit") :
                    data[input_tag['name']] = f"test{character}"

            print(url)
            # get_form_details(form)
            # print("Data:", data)

            if (details["method"].lower() == "post") :
                response = session.post(url, data = data)

            elif (details["method"].lower() == "get") :
                response = session.get(url, params = data)

            else :
                continue

            # print("Response:", response)

            if is_sql_vulnerable(response) == True :
                print("SQL Injection Attack Possible @", url)
                return True
                print()

            else :
                print("No SQL Injection Attack Possible @", url)
                print()
                break
    return False   

def tester () :
    session = Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    url = "https://cnn.com"
    sql_is_safe(url, session)

# Main
if __name__ == "__main__" :
    tester()