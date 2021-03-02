from flask import Flask, request
from flask_restful import Api, Resource
import numpy as np

app = Flask(__name__)
api = Api(app)


class LinearSimultan(Resource):
    def get(self):
        request_data = request.get_json()
        A = np.array(request_data['A'])
        B = np.array(request_data['B'])
        X = np.linalg.solve(A, B)
        return {'data': {
            'A': A.tolist(),
            'B': B.tolist(),
            'X': X.tolist()
        }}


api.add_resource(LinearSimultan, "/linear-simultan")

if __name__ == "__main__":
    app.run(debug=True)
