# Custom Kali Linux Nmap Scanner Web App

A Flask-based web app that allows authenticated users to run Nmap scans against target hosts and store the results in a Database.

## Overview
Nmap is one of the most widely used scanning tools in entry-level Information Security. When completeing "Capture the Flag" modules on platforms like TryHackMe, one of the first steps is almost always to perform an Nmap scan against the target machine.

This project was created as part of a Web Development final project with the goal of using web development concepts like CRUD operations, authentication, and databases to create a practical tool for future Information Secuirty classes. 

The core idea was to a build a we interface that:
  * requires some user authentication
  * allows a user to run an Nmap Scan against a target machine
  * automatically saves the result to a database
  * allows authenticated users to revist previous scans instead of rerunning them.

![Nmap Scan Form](images/nmap_scan.png)

## Technologies Used
  * Python Flask
  * Flask-Login
  * Flask-SQLAlchemy
  * SQLite
  * HTML w/ Jinja Templates
  * CSS
  * Javascript
  * Nmap
  * Kali/Linux

## What Worked Well
  * The authenitcation correctly restricts users to only viewing and managing their own scans
  * The scan results are saved and persist through sessions
  * The application demonstrates CRUD operations using a relational database
  * File cleanup is handled when scans are deleted

![Scan Results](scans_database.png)

## Limitaions and Challenges
While the application functions at a basic level, several limitaiotns were discovered
  * Performance Issues of nmap scans
      - Running Nmap scans through Flask is significantly slower than running it directly in a terminal.
      - Longer and more aggressive scans can block the web server while executing or time out completely.
  * Security Concerns
      - Executing system command straight from user input is inherently dangerous. Strict input validation would be required
      - User authentication is not encrypted whatsoever.
   
## Possible Improvements
  * Find a way to asynchronously run scans
  * Hash user passwords securely
  * Create a robust user input validation system
  * Consider adding additional tools that can be run in series (Gobuster, Hydra, WHOIS)

## Disclaimer
This application is intended for educational purposes only. Running network scans against systems you do not own or have permission to test may be illegal.
