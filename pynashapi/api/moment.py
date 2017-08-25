from datetime import date

from flask import abort, request, jsonify

from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from pynashapi.api import API
from pynashapi.models import Moment
from pynashapi.resources.base_resource import BaseResource
from pynashapi.schemas.moment import MomentSchema


class Moments(BaseResource):
    def get(self):
        moments = Moment.query.order_by(Moment.event_date).all()

        if not moments:
            abort(404)

        return MomentSchema().dump(moments, many=True).data

    def post(self):
        request_json = request.get_json(force=True)
        try:
            validation_errors = MomentSchema().validate(request_json)
            moment_details = request_json['data']['attributes']
            if validation_errors:
                raise ValidationError(validation_errors)

            month, day, year = [
                int(x) for x in moment_details['event_date'].split('-')
            ]
            moment_details['event_date'] = date(
                month=month, day=day, year=year)

            mmt = Moment(**moment_details)
            mmt.add()
            results = MomentSchema().dump(mmt).data
            return results, 201

        except ValidationError as err:
            resp = jsonify(err.messages)
            resp.status_code = 403
            return resp

        except SQLAlchemyError as err:
            resp = jsonify(str(err))
            resp.status_code = 403
            return resp


API.add_resource(Moments, '/moments/')

MOMENTS_HOLDER = None
