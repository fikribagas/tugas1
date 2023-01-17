from flask import Flask, render_template
app = Flask(__name__)
@app.route('/fikri')
def gethobi():
 hobi1= 'Bermain game'
 hobi2= 'bermain bola'
 hobi3= 'memasak'
 return render_template('fikri.html', hobi1 = {{hobi1}} , hobi2 = {{hobi2}} , hobi3 = {{hobi3}})
if __name__ == '__main__':
 app.run(debug=True)