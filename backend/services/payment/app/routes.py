from flask import jsonify, request
from app import app
from .services import processing_data
from .models import Payment

@app.route('/payment/test', methods = ["GET"])
def test_payment():
     if request.method == "GET":
        return jsonify("success")


@app.route('/payment', methods = ["POST"])
def send_data_to_stripe():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            order = request.get_json()
            print("\nReceived an order in JSON:", order)

            # do the actual work
            # 1. Send order info {cart items}
            result = processing_data(order)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "place_order.py internal error: " + ex_str
            }), 500
        
        except Exception as e:  # Catch potential errors from call_flight_inventory
            return jsonify({"error": "Flight inventory service error"}), 500 


    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400
            
    