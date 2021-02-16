# ffClosedTestingSignUp
This project is a basic flask server being hosted on repl.it to serve static webpages(HTML, CSS).

## Features:
1. Main page has a form that accepts only valid email ID formats(using regex validation).
2. Aforementioned form is submittable only if user passes reCaptcha check.
3. Submitted email IDs are added to a .txt file.

## Note:
This was quickly whipped up meet a small need for another Private project, not intended to be a full-fledged project.

## How to use:
Register your domains with reCaptcha and replace the reCaptcha key in templates/index.html.

Finally, run main.py.


## Packages used
1. flask - to deploy a flask server
