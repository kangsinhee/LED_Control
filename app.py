from flask import Flask, render_template, request
import  RPi.GPIO as GPIO

app = Flask(__name__)

status = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)


@app.route('/OFF')
def off():
    status = 0
    print(status)
    GPIO.output(14, 1)
    return render_template('OFF.html', status= status)

@app.route('/ON')
def on():
    status = 1
    print(status)
    GPIO.output(14, 0)
    return render_template('ON.html', status=status)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    print('Web Server starts')
    app.run(debug = True, host="127.0.0.3", port="8888")

GPIO.cleanup()
print('Program End')