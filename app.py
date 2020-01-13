# DESAFIO SRE - Simples API REST
# Feito em Python, contido em um container Docker
# 2019 - Andrei Oliveira
import datetime
from flask import Flask, render_template, request, redirect, url_for, Response
from flask_restful import Resource, Api, abort
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Request

app = Flask(__name__)

engine = create_engine('sqlite:///requests.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/api', methods = ['GET', 'POST'])
def apiFunction():
   if request.method == 'GET':
      return get_requests()
   elif request.method == 'POST':
      req_data = request.get_json()   
      if not req_data:
           abort(Response('Error: no json sent', 400))
      if 'component' not in req_data:
           abort(Response('Error: component is missing', 400))
      component = req_data['component']
      if 'version' not in req_data:
           abort(Response('Error: version is missing', 400))
      version = req_data['version']
      if 'owner' not in req_data:
           abort(Response('Error: owner is missing', 400))
      owner = req_data['owner']
      if 'status' not in req_data:
           abort(Response('Error: status is missing', 400))
      status = req_data['status']
      return registerRequest(component, version, owner, status)

@app.route('/api/', methods = ['GET', 'PUT', 'DELETE'])
def apiFunctionId(id):
   if request.method == 'GET':
      return get_request(id)

   elif request.method == 'PUT':
      req_data = request.get_json()
      if not req_data:
           abort(Response('Error: no json sent', 400))
      if 'component' not in req_data:
           abort(Response('Error: component is missing', 400))
      component = req_data['component']
      if 'version' not in req_data:
           abort(Response('Error: version is missing', 400))
      version = req_data['version']
      if 'owner' not in req_data:
           abort(Response('Error: owner is missing', 400))
      owner = req_data['owner']
      if 'status' not in req_data:
           abort(Response('Error: status is missing', 400))
      status = req_data['status']
      return updateRequest(id, component, version, owner, status, date)

   elif request.method == 'DELETE':
      return deleteRequest(id)

def get_requests():
   all_requests = session.query(Request).all()
   return jsonify(requests_json= [r.serialize for r in all_requests])

def get_request(request_id):
   requests = session.query(Request).filter_by(id = request_id).one()
   return jsonify(request= requests.serialize)

def registerRequest(component, version, owner, status):
   newRequest = Request(component=component, version=version, owner=owner, status=status)
   session.add(newRequest)
   session.commit()
   return jsonify(Request=newRequest.serialize)

def updateRequest(id, component, version, owner, status, date):
   updatedRequest = session.query(Request).filter_by(id = id).one()
   if not component:
       updatedRequest.component = component
   if not version:
       updatedRequest.version = version
   if not owner:
       updatedRequest.owner = owner
   if not status:
       updatedRequest.status = status
   updatedRequest.date = date
   session.add(updatedRequest)
   session.commit()
   return 'Updated a Request with id %s' % id

def deleteRequest(id):
   requestToDelete = session.query(Request).filter_by(id = id).one()
   session.delete(requestToDelete)
   session.commit()
   return 'Removed Request with id %s' % id

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0')
