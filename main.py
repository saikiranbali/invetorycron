import psycopg2
from app import app
from flask import flash, request
# from db_config import mysql
from flask import jsonify
# import psycopg2
# with open("C:/Users/Sai kiran/Desktop/abm.json") as jsonFile:
#     data = json.load(jsonFile)

import requests
# from flask import flash, request
# from werkzeug import generate_password_hash, check_password_hash


		
@app.route('/getdata', methods=['GET'])
def add_user():
	try:
		data = requests.get('http://farzibi.farziengineer.co/api/queries/652/results.json?api_key=GfqcjrjeR8K2QuaNkgEfpviNcFrNBXfDpoJsUT2f', 
        headers={'Accept': 'application/json'})
		print("nani")

		# print(f"Response: {r.json()}")
		data = data.json()
		conn1 = psycopg2.connect(
		host="database-crm.cazl4vulkacd.ap-south-1.rds.amazonaws.com",
		database="database_crm",
		user="database_gg_crm",
		password="Crmpostgres123"
		)
		# create a cursor
		cur1 = conn1.cursor()
		cur1.execute("truncate table inventory")
		conn1.commit()



			
		c = (data["query_result"]["data"]["rows"])

		for k in c:
			if k['quantity'] == 0:
				warehouse_name = k['Warehouse']
				varient_id = k['product_variant_id']
				sku = k['sku']
				varient_name = k['name']
				price_amount = k['price_amount']
				cost_price_amount = k['cost_price_amount']
				quantity = k['quantity']
				is_published = k['published_sta']
				print(warehouse_name)
				print(varient_id)
				print(sku)
				print(varient_name)
				print(price_amount)
				print(cost_price_amount)
				print(quantity)
				print(is_published)
				# conn = psycopg2.connect(
				# host="database-crm.cazl4vulkacd.ap-south-1.rds.amazonaws.com",
				# database="database_crm",
				# user="database_gg_crm",
				# password="Crmpostgres123"
				# )
				# # create a cursor
				# cur = conn.cursor()
				# cur.execute("truncate table inventory")

				cur1.execute("INSERT INTO inventory (warehouse_name, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, is_published) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (warehouse_name, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, is_published))
				conn1.commit()
				# cur.execute("select * from product")
				cur1.execute("select * from inventory")
				print(cur1.fetchall())





		# get the data from the dict
		resp = jsonify('Data added successfully!')
		resp.status_code = 200
		return resp

		# _name = _json['name']
		# _email = _json['email']
		# _password = _json['pwd']
		# # validate the received values
		# if _name and _email and _password and request.method == 'POST':
		# 	#do not save password as a plain text
		# 	_hashed_password = generate_password_hash(_password)
		# 	# save edits
		# 	sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
		# 	data = (_name, _email, _hashed_password,)
		# 	conn = mysql.connect()
		# 	cursor = conn.cursor()
		# 	cursor.execute(sql, data)
		# 	conn.commit()
		# 	resp = jsonify('User added successfully!')
		# 	resp.status_code = 200
		# 	return resp
		# else:
		# 	return not_found()
	except Exception as e:
		print(e)
	finally:
		print("done")





		
# @app.route('/users')
# def users():
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		cursor.execute("SELECT * FROM tbl_user")
# 		rows = cursor.fetchall()
# 		resp = jsonify(rows)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
		
# @app.route('/user/<int:id>')
# def user(id):
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
# 		row = cursor.fetchone()
# 		resp = jsonify(row)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
# @app.route('/update', methods=['POST'])
# def update_user():
# 	try:
# 		_json = request.json
# 		_id = _json['id']
# 		_name = _json['name']
# 		_email = _json['email']
# 		_password = _json['pwd']		
# 		# validate the received values
# 		if _name and _email and _password and _id and request.method == 'POST':
# 			#do not save password as a plain text
# 			_hashed_password = generate_password_hash(_password)
# 			# save edits
# 			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
# 			data = (_name, _email, _hashed_password, _id,)
# 			conn = mysql.connect()
# 			cursor = conn.cursor()
# 			cursor.execute(sql, data)
# 			conn.commit()
# 			resp = jsonify('User updated successfully!')
# 			resp.status_code = 200
# 			return resp
# 		else:
# 			return not_found()
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
		
# @app.route('/delete/<int:id>')
# def delete_user(id):
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor()
# 		cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
# 		conn.commit()
# 		resp = jsonify('User deleted successfully!')
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
		
if __name__ == "__main__":
    app.run()
