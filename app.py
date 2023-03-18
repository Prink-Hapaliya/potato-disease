from flask import Flask, render_template

app = Flask(__name__,)

a="hello how are you?";
@app.route("/")
def hello_world():
  return render_template('home.html',
                        image_name='good',name=a)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
