from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def simulate_exposure(user_data):
    # Random simulated results
    leak_count = random.randint(3, 25)
    risk_score = random.randint(40, 95)

    sample_sites = [
        "BlackBazaar Forums",
        "ShadowLeak DB",
        "NightMarket Dumps",
        "Phantom Breach Archives"
    ]
    found_on = random.sample(sample_sites, random.randint(1, 3))

    return leak_count, risk_score, found_on


def generate_decoys(real_data, amount=1000):
    decoys = []

    for _ in range(amount):
        fake_name = real_data["name"][0] + ''.join(random.choices(string.ascii_letters, k=6))
        fake_mail = ''.join(random.choices(string.ascii_lowercase, k=7)) + "@fakemail.com"
        fake_phone = "+1 " + "".join(random.choices("0123456789", k=10))

        decoys.append({
            "name": fake_name,
            "email": fake_mail,
            "phone": fake_phone
        })

    return decoys


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")

    user_data = {"name": name, "email": email, "phone": phone}

    leak_count, risk_score, found_on = simulate_exposure(user_data)
    decoys = generate_decoys(user_data)

    return render_template(
        "result.html",
        name=name,
        email=email,
        phone=phone,
        leak_count=leak_count,
        risk_score=risk_score,
        found_on=found_on,
        decoy_count=len(decoys)
    )


@app.route("/decoys")
def show_decoys():
    name = "Example"
    fake_user = {"name": name}
    decoys = generate_decoys(fake_user)
    return render_template("decoys.html", decoys=decoys)


if __name__ == "__main__":
    app.run(debug=True)
