from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.project import ProjectModel


class Project(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('owner',
                        type=str,
                        required=True,
                        help="")

    def get(self, pname):
        project = ProjectModel.find_by_name(pname)
        if project:
            return project.json(), 200
        return {'message': "Project named '{}' is not found".format(pname)}, 404

    def post(self, pname):
        if ProjectModel.find_by_name(pname):
            return {'message': "An project with name '{}' already exists.".format(pname)}, 400
        data = Project.parser.parse_args()
        project = ProjectModel(pname, **data)

        try:
            project.save_to_db()
        except:
            return {"message": "An error occured inserting the project"}, 500
        return project.json(), 201

    def delete(self, pname):
        project = ProjectModel.find_by_name(pname)
        if project:
            project.delete_from_db()

        return {'message': "Project named '{}' is deleted".format(pname)}
