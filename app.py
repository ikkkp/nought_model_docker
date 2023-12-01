from flask import Flask, request, jsonify

from model.nougat_model_base import nougatProcessor_base

app = Flask(__name__)


@app.route('/Ocean_PDF2Text', methods=['POST'])
def Ocean_PDF2Text():
    # Check if the request is a POST request
    if request.method == 'POST':
        try:
            # Access the JSON data from the request body
            request_data = request.get_json()

            # Check if the required fields are present in the JSON data
            if 'messages' in request_data and 'image_path' in request_data['messages'] and 'output_token' in \
                    request_data['messages']:
                image_path = request_data['messages']['image_path']
                output_token = int(request_data['messages']['output_token'])

                # Now you can use image_path and output_token as needed
                result = nougatProcessor_base(image_path, "facebook/nougat-base", output_token)

                # Return the result as JSON
                return jsonify({"status": "success", "result": result})
            else:
                # Return an error response if the required fields are not present
                return jsonify({"status": "error", "error": "Invalid JSON format"}), 400

        except Exception as e:
            # Handle any exceptions that may occur during processing
            return jsonify({"error": str(e)}), 500
    else:
        # Handle other HTTP methods if necessary
        return 'Method Not Allowed', 405


if __name__ == '__main__':
    app.run(debug=True)
