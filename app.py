from flask import Flask, render_template, request, url_for, redirect
import  RPi.GPIO as GPIO

app = Flask(__name__)

def gpio_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    print('Web Server starts')

def controller(status):
    print(status)
    GPIO.output(14, status)

@app.route('/')
def index():
    return redirect(url_for('off'))

@app.route('/OFF')
def off():
    status = 0
    controller(status)
    return render_template('OFF.html', status=status)

@app.route('/ON')
def on():
    status = 1
    controller(status)
    return render_template('ON.html', status=status)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    gpio_init()
    app.run(debug = True)

GPIO.cleanup()
print('Program End')
