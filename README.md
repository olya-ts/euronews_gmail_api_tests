# Steps to take to before running the tests

## Instructions for obtaining the client_secrets.json file:
1. Follow the link - https://console.cloud.google.com/
2. Sing in with a test account
3. In the upper panel select "Select a project" -> "New project"
4. After the project is created, select "APIs & Services" -> "OAuth consent screen" on the left menu
5. Select User Type - External, click "Create"
6. On the "OAuth consent screen" tab fill only necessary fields (the "App name" field should be different from the existing ones) - leave all other tabs as default.
7. After creation click "Publish App"
8. On the left menu select "APIs & Services" -> "Library" -> enter "Gmail API" in the search box -> choose "Gmail API" from the list-> click "Enable"
9. On the left menu select "APIs & Services" -> "Credentials" -> click "+ Create Credentials" on the top of the page-> "OAuth Client ID" -> choose application type "Web app" -> save the file with the received credits locally
10. Rename the saved file to "client_secrets.json" and store it in the project in the directory "tests/config": tests-config-client-secrets.json

## Instructions for storing credentials:
1. In the project's file "tests/config/oauth.py" replace the empty strings with your test credentials:
   * APP_NAME - use the App name field you created on step 6 of the previous instructions
   * EMAIL - use your test gmail 
   * PASSWORD - use the password for your test google account