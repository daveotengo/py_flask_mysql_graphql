
from schema import schema
from flask_graphql import GraphQLView

app = Flask(__name__)






app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


if __name__=="__main__":
    app.run(debug=True,host='localhost',port=5004)