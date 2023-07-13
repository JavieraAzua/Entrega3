def total_carrito(request):
	total = 0
	if request.user in request.session:
		try:
			for key, value in request.session['carrito'].items():
				#variable total autoincrementable
				total = total +(int(value['precio']))*(value['cantidad'])
		except	Exception:
				request.session['carrito']={}
				total = 0
	return {'total':int(total)}
