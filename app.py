from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])
        height_m = height_cm / 100  # Convert height from centimeters to meters
        bmi = weight / (height_m ** 2)
        age = int(request.form['age'])
        gender = request.form['gender']
        bmi_category = get_bmi_category(bmi, age, gender)
        return render_template('result.html', bmi=bmi, category=bmi_category)
    return render_template('index.html')

def get_bmi_category(bmi, age, gender):
    if age < 18:
        return 'Age restriction: Must be 18 or older'
    elif age >= 18 and age <= 65:
        if gender == 'male':
            if bmi < 12 and bmi >= 40:
                return 'invalid'
            elif bmi < 18.5:
                return 'underweight'
            elif bmi >= 18.5 and bmi < 25:
                return 'Healthy weight'
            elif bmi >= 25 and bmi <= 30:
                return 'Overweight'
            else:
                return 'invalid'
        elif gender == 'female':
            if bmi < 12 and bmi >= 40:
                return 'invalid'
            elif bmi < 18.5:
                return 'Underweight'
            elif bmi >= 18.5 and bmi < 24:
                return 'Healthy weight'
            elif bmi >= 24 and bmi <= 30:
                return 'Overweight'
            else:
                return 'invalid'
    else:
        return 'Age restriction: Must be 65 or younger'

if __name__ == '__main__':
    app.run(debug=True)
