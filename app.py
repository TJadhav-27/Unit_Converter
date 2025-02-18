from flask import Flask, render_template, request

app = Flask(__name__)

def convert_length(value, from_unit, to_unit):
    units = {"meters": 1, "kilometers": 0.001, "centimeters": 100, "millimeters": 1000}
    return value * (units[to_unit] / units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

def convert_weight(value, from_unit, to_unit):
    units = {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274}
    return value * (units[to_unit] / units[from_unit])

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        category = request.form["category"]
        
        if category == "length":
            result = convert_length(value, from_unit, to_unit)
        elif category == "temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif category == "weight":
            result = convert_weight(value, from_unit, to_unit)
        
        result = round(result, 2)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
