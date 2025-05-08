from flask import Flask, render_template, request

app = Flask(__name__)

# Sample room data
rooms = [
    {
        'id': 1,
        'name': 'Deluxe Room',
        'price': 120,
        'facilities': ['Wi-Fi', 'AC', 'TV'],
        'image': 'https://source.unsplash.com/600x400/?hotel,room,1'
    },
    {
        'id': 2,
        'name': 'Executive Suite',
        'price': 200,
        'facilities': ['Wi-Fi', 'AC', 'TV', 'Mini Bar'],
        'image': 'https://source.unsplash.com/600x400/?hotel,room,2'
    },
    {
        'id': 3,
        'name': 'Budget Room',
        'price': 80,
        'facilities': ['Wi-Fi', 'Fan'],
        'image': 'https://source.unsplash.com/600x400/?hotel,room,3'
    }
]

@app.route('/')
def index():
    return render_template('index.html', rooms=rooms)

@app.route('/room/<int:room_id>')
def room_detail(room_id):
    room = next((room for room in rooms if room['id'] == room_id), None)
    if not room:
        return "Room not found", 404
    return render_template('room_detail.html', room=room)

@app.route('/book/<int:room_id>', methods=['GET', 'POST'])
def book(room_id):
    room = next((room for room in rooms if room['id'] == room_id), None)
    if not room:
        return "Room not found", 404

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        checkin = request.form['checkin']
        checkout = request.form['checkout']

        # Save booking to a text file (optional)
        with open('bookings.txt', 'a') as file:
            file.write(f"{name}, {email}, {phone}, Room: {room['name']}, {checkin} to {checkout}\n")

        message = f"Thank you {name}, your booking for {room['name']} from {checkin} to {checkout} is confirmed!"
        return render_template('book.html', room=room, message=message)

    return render_template('book.html', room=room)

if __name__ == '__main__':
    app.run(debug=True)
