from bottle import Bottle, request, template, static_file, run
import random
import os

application = Bottle()

# List of ice cream flavors (name, image file, description)
flavors = [
    ("Vanilla", "vanilla.jpg", "Classic and creamy, loved by everyone."),
    ("Chocolate", "chocolate.jpg", "Rich, sweet, and a little indulgent."),
    ("Strawberry", "strawberry.jpg", "Fruity and fresh with a pink twist."),
    ("Blueberry", "blueberry.jpg", "Sweet and tangy with a deep purple color."),
    ("Pistachio", "pistachio.jpg", "Nutty, smooth, and a little fancy."),
    ("Hazelnut", "hazelnut.jpg", "Nutty, creamy, and melt-in-your-mouth."),
    ("Chocolate Chip", "chocolate_chip.jpg", "Vanilla base dotted with chocolate chunks."),
    ("Mint", "mint.jpg", "Cool and refreshing with a hint of sweetness."),
    ("Peach", "peach.jpg", "Soft, sweet, and summery fresh."),
    ("Raspberry Ripple", "raspberry_ripple.jpg", "Velvety cream with swirls of tangy raspberry."),
    ("Watermelon", "watermelon.jpg", "Juicy and sweet with a bright pink smile."),
    ("Cookies & Cream", "cookies_cream.jpg", "Crunchy cookie bits in creamy vanilla."),
    ("Mango", "mango.jpg", "Tropical and juicy, perfect for summer days.")
]

@application.route("/", method=["GET", "POST"])
def home():
    if request.method == "POST":
        # Pick a random flavor
        flavor = random.choice(flavors)
        return template(
            "flavor", 
            name=flavor[0], 
            img="/static/" + flavor[1],  # ✅ Fixed path for Render
            desc=flavor[2], 
            btn_text="One More Scoop!😋"
        )
    else:
        # First page load
        return template(
            "flavor", 
            name="", 
            img="", 
            desc="Click the button to find your sweet treat!", 
            btn_text="Find the Sweet Treat🍦"
        )

@application.route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./static")

# ✅ Entry point for Render
if __name__ == "__main__":
    run(application, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
