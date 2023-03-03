from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods =["GET"])
def server_status():
    return "Server On"

@app.route("/info", methods =["GET"])
def info_route():
    return "This server was written for BME547"

@app.route("/HDL_analsis", methods = ["POST"])
def HDL_route_handler():
    """
    in_data = {"name": <patient_name>, "HDL_value": <HDL_result>}
    """
    from blood_calculator import HDL_analysis
    in_data = request.get_json()
    diagnosis = HDL_analysis(in_data["HDL_value"])
    return diagnosis


if __name__ == "__main__":
    app.run()


