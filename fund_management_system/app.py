from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from models import Fund
from database import init_db, add_fund, get_all_funds, get_fund_by_id, update_fund_performance, delete_fund, migrate_data

app = Flask(__name__)
api = Api(app)

# Error messages
ERROR_MESSAGES = {
    400: "Bad Request: The request could not be understood.",
    404: "Not Found: The requested URL was not found on the server.",
    500: "Internal Server Error: The server encountered an internal error.",
}

# Error handling decorators
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": ERROR_MESSAGES[400]}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": ERROR_MESSAGES[404]}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": ERROR_MESSAGES[500]}), 500

# Simple test endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"

class FundList(Resource):
    def get(self):
        funds = get_all_funds()
        return jsonify([fund.to_dict() for fund in funds])

    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        required_fields = ['name', 'manager_name', 'description', 'nav', 'date_of_creation', 'performance']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        new_fund = Fund(None, data['name'], data['manager_name'], data['description'], data['nav'], data['date_of_creation'], data['performance'])
        add_fund(new_fund)
        return jsonify({"message": "Fund added successfully"})

class FundResource(Resource):
    def get(self, fund_id):
        fund = get_fund_by_id(fund_id)
        if fund:
            return jsonify(fund.to_dict())
        return jsonify({"message": "Fund not found"}), 404

    def put(self, fund_id):
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        performance = data.get('performance')
        if performance is None:
            return jsonify({"error": "Missing 'performance' field in request data"}), 400

        update_fund_performance(fund_id, performance)
        return jsonify({"message": "Fund performance updated successfully"})

    def delete(self, fund_id):
        delete_fund(fund_id)
        return jsonify({"message": "Fund deleted successfully"})

api.add_resource(FundList, '/funds')
api.add_resource(FundResource, '/funds/<int:fund_id>')

if __name__ == '__main__':
    init_db()  # Initialize the database
    migrate_data()  # Migrate the data
    app.run(debug=True)
