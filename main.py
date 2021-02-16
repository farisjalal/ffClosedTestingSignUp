from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']+'\n'
    with open('emailIDs.txt') as fin:
      existingEmails = fin.readlines()
    if email not in existingEmails:
      with open('emailIDs.txt','a') as fout:
        fout.write(email)
      return render_template('thanks.html')
    else:
      return render_template('already_registered.html')
  else:
    return render_template('index.html')


if __name__ == '__main__':
  print("Server running!")
  app.run(host='0.0.0.0', port=8080)
