from flask import *
from werkzeug.utils import secure_filename

from src.dbcnt import *

app=Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')
@app.route('/viewfarmer')
def view_farmer():
    qry="SELECT farmers.*FROM farmers JOIN login ON login.id=farmers.farmerloginid WHERE login.type='pending'"
    res=selectall(qry)
    return render_template('viewfarmer.html',val=res)
@app.route('/approve')
def approve():
    id=request.args.get('id')
    qry="update login set type='farmer'where id=%s"
    value=(str(id))
    iud(qry,value)
    return'''<script>alert("approved as farmer");window.location="/viewfarmer"</script>'''

@app.route('/reject')
def reject():
    id = request.args.get('id')
    qry = "update login set type='reject'where id=%s"
    value = (id)
    iud(qry, value)
    return '''<script>alert("rejected");window.location="/viewfarmer"</script>'''


@app.route('/viewuser')
def viewuser():
    qry = "select*FROM user"
    res = selectall(qry)
    return render_template('viewuser.html', val=res)
@app.route('/deliverydetails')
def viewdeliverydetails():
    qry="SELECT *FROM `bill table`"
    res=selectall(qry)
    return render_template('viewdeliverydetails.html',val=res)
@app.route('/viewmore')
def viewmore():
    id=request.args.get('id')

    qry="SELECT `products`.`productname`,`order`.`quandity`,`user`.`firstname`,`user`.`lastname`FROM `products`JOIN`order`ON`products`.`productid`=`order`.`itemid`JOIN`user`ON`user`.`userloginid`=`order`.`userid`WHERE `order`.`billid`=%s"
    val=(str(id))
    res=selectall2(qry,val)
    return render_template('viewmore.html',val=res)
@app.route('/feedback')
def feedback():
    qry="SELECT `user`.`firstname`,`lastname`,`feedback`.* FROM `feedback` JOIN `user` ON `user`.`userloginid`=`feedback`.`userloginid`"
    res=selectall(qry)
    return render_template('feedback.html',val=res)
@app.route('/farmerreg')
def farmerreg():
    return render_template('farmerreg.html')
@app.route('/addproduct',methods=['post'])
def addproduct():
    type=request.form['Submit']
    print(type)
    if type=="Search":
        info=request.form['select']
        print(info)
        qry="SELECT*FROM`products`WHERE `type`=%s"
        val=info
        res=selectall2(qry,val)
        return render_template('viewproducts.html',val=res,ress=info)
    else:
        return render_template("addproduct.html")

@app.route('/add',methods=['post'])
def add():
        productname = request.form['textfield']
        producttype = request.form['select']
        description = request.form['textarea']
        image = request.files['file']
        fname=secure_filename(image.filename)
        image.save('static/uploads/'+fname)
        wholesaleprice = request.form['textfield2']
        retailprice = request.form['textfield4']
        quantity = request.form['textfield3']
        qry="insert into products values(null,%s,%s,%s,%s,%s,%s,%s)"
        val=(productname,description,fname,wholesaleprice,retailprice,quantity,producttype)
        iud(qry,val)
        return '''<script>alert("added successfully");window.location="/viewproducts"</script>'''

@app.route('/editproducts')
def editproducts():
    id=request.args.get('id')
    qry="SELECT*FROM`products`WHERE`productid`=%s"
    val=(id)
    res=selectone(qry,val)
    return render_template('editproducts.html',val=res)
@app.route('/delete')
def delete():
    id=request.args.get('id')
    qry = "DELETE FROM `products`WHERE`productid`=%s"
    val=(id)
    iud(qry, val)
    return '<script>alert("DELETED SUCCESSFULLY");window.location="/viewproducts"</script>'
@app.route('/editproducts2',methods=['post'])
def editproducts2():
    try:
        id=request.form['id']
        productname=request.form['textfield']
        producttype = request.form['select']
        description = request.form['textarea']
        image = request.files['file']
        fname = secure_filename(image.filename)
        image.save('static/uploads/' + fname)
        wholesaleprice = request.form['textfield2']
        retailprice = request.form['textfield4']
        quantity = request.form['textfield3']
        qry="UPDATE `products`SET `productname`=%s,`description`=%s,`wholesaleprice`=%s,`retailprice`=%s,`quandity`=%s,`type`=%s , image=%s WHERE `productid`=%s"
        val=(productname,description,wholesaleprice,retailprice,quantity,producttype,fname,id)
        iud(qry,val)
        return '''<script>alert("UPDATED SUCCESSFULLY");window.location="/viewproducts"</script>'''
    except Exception as e:
        id = request.form['id']
        productname = request.form['textfield']
        producttype = request.form['select']
        description = request.form['textarea']
        # image = request.files['file']
        # fname = secure_filename(image.filename)
        # image.save('static/uploads/' + fname)
        wholesaleprice = request.form['textfield2']
        retailprice = request.form['textfield4']
        quantity = request.form['textfield3']
        qry = "UPDATE `products`SET `productname`=%s,`description`=%s,`wholesaleprice`=%s,`retailprice`=%s,`quandity`=%s,`type`=%s WHERE `productid`=%s"
        val = (productname, description, wholesaleprice, retailprice, quantity, producttype, id)
        iud(qry, val)
        return '''<script>alert("UPDATED SUCCESSFULLY");window.location="/viewproducts"</script>'''



@app.route('/viewproducts')
def viewproducts():
    return render_template('viewproducts.html',ress="")
@app.route('/farmershome')
def farmershome():
    return render_template('farmershome.html')


@app.route('/vieworder')
def vieworder():
    qry="SELECT `bill table`.`billid`,`bill table`.`date`,`bill table`.`totalamount`,`user`.`firstname`,`user`.`lastname`FROM`bill table`JOIN `user` ON`user`.`userloginid`=`bill table`.`userloginid`"
    res=selectall(qry)
    return render_template('vieworder.html',val=res)
@app.route('/moredetails',methods=['post','get'])
def moredetails():
    bid=request.args.get('bid')
    qry="SELECT `products`.`productname`,`order`.`quandity`,`order`.`amount`FROM `products`JOIN`order`ON`products`.`productid`=`order`.`orderid`WHERE`order`.`billid`=%s"
    val=bid
    res=selectall2(qry,val)
    return render_template('moredetails.html',val=res)
@app.route('/viewfeedback')
def viewfeedback():
    qry="SELECT `feedback`.`date`,`feedback`.`feedback`,`user`.`firstname`,`user`.`lastname`FROM feedback JOIN `user`ON `user`.`userloginid`=`feedback`.`userloginid`"
    res=selectall(qry)
    return render_template('viewfeedback.html',val=res)
@app.route('/viewdeleverydetails1')
def viewdeleverydetails1():
    id = request.args.get('id')
    qry="SELECT `user`.`firstname`,`user`.`lastname`,`products`.`productname`,`order`.`quandity` FROM `order` JOIN `products` ON `products`.`productid`=`order`.`itemid` JOIN `user` ON `user`.`userloginid`=`order`.`userid` WHERE `order`.`billid`=%s"
    val=(id)
    res=selectall2(qry,val)
    return render_template('viewdeleverydetails1.html',val=res)
@app.route('/logins',methods=['post'])
def logins():
    username=request.form['textfield']
    password=request.form['textfield2']
    print(username,password)
    qry="select *from login where username=%s and password=%s"
    value=(username,password)
    s=selectone(qry,value)
    if s is None:
        return'''<script>alert("user not find");window.location="/"</script>'''
    elif s[3]=="admin":
        return'''<script>alert("logined as admin");window.location="/adminhome"</script>'''
    elif s[3]=="farmer":
        return'''<script>alert("logined as farmer");window.location="/farmershome"</script>'''



app.run(debug=True)
