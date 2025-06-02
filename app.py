from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    # Extract form data
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('email')
    phone = request.form.get('phone')
    service = request.form.get('service')
    message = request.form.get('message')
    
    # Print form data to console
    print("=== New Contact Form Submission ===")
    print(f"Name: {first_name} {last_name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Service: {service}")
    print(f"Message: {message}")
    print("=" * 40)
    
    # Return simple response
    return "Thanks for your message!"

# Optional: Serve FBX models explicitly (if needed)
@app.route('/static/models/<path:filename>')
def serve_model(filename):
    return send_from_directory('static/models', filename)

# Optional: Serve images if having issues
@app.route('/static/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('static/images', filename)

# Add review submission endpoint
@app.route('/submit-review', methods=['POST'])
def submit_review():
    try:
        data = request.get_json()
        name = data.get('name')
        rating = data.get('rating')
        review = data.get('review')
        
        print(f"New Review - Name: {name}, Rating: {rating}, Review: {review}")
        
        return jsonify({'status': 'success', 'message': 'Review submitted successfully'})
    except Exception as e:
        print(f"Error submitting review: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to submit review'}), 500
    # Extract review data
    name = request.form.get('reviewName')
    email = request.form.get('reviewEmail')
    rating = request.form.get('rating')
    review_text = request.form.get('reviewText')
    
    # Print review data to console
    print("=== New Review Submission ===")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Rating: {rating}/5 stars")
    print(f"Review: {review_text}")
    print("=" * 40)
    
    return "Thank you for your review!"

if __name__ == '__main__':
    app.run(debug=True)
