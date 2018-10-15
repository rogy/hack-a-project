from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from models.project import ProjectModel
from models.role import RoleModel


class Project(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pname',
                        type=str,
                        required=True,
                        help="Project name is missing")
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="Project description is missing")

    parser.add_argument('roles',
                        required=True,
                        action='append',
                        help="Project roles is missing")

    @jwt_required()
    def get(self, pname):
        project = ProjectModel.find_by_name(pname)
        if project:
            return project.json(), 200
        return {'message': "Project named '{}' is not found".format(pname)}, 404

    @jwt_required()
    def post(self):
        data = Project.parser.parse_args()
        project = ProjectModel(data['pname'], data['description'], int(current_identity))  # TODO: fix this <class 'werkzeug.local.LocalProxy'> to int problem

        # for rolestr in data['roles']:
        #     rolejson = eval(rolestr)
        #     role = RoleModel(rolejson['title'], rolejson['description'])
        #     try:
        #         role.save_to_db()
        #     except:
        #         return {"message": "An error occured inserting the role"}, 500

        try:
            project.save_to_db()
        except:
            return {"message": "An error occured inserting the project"}, 500
        return project.json(), 201

    @jwt_required()
    def delete(self, pname):
        project = ProjectModel.find_by_name(pname)
        if project:
            project.delete_from_db()
        return {'message': "Project named '{}' is deleted".format(pname)}

    @jwt_required()
    def put(self, pname):
        data = Project.parser.parse_args()
        project = ProjectModel.find_by_name(pname)
        if project:
            project.owner = data['owner']
        else:
            project = ProjectModel(pname, **data)
        project.save_to_db()
        return project.json()


class ProjectList(Resource):
    """docstring for ProjectList"""

    def get(self):
        return {'items': [project.json() for project in ProjectModel.query.all()]}
