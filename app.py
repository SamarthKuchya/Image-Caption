from flask import Flask,render_template,request
import Caption_it

# if __name__ == "__main__"
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def marks():
    if request.method=='POST':
        f=request.files['userfile']
        print(f.filename)
        path="./static/{}".format(f.filename)
        f.save(path)
        output=Caption_it.predict_caption(path)
        
        result_dic={
            'image':path,
            'caption':output
        }

    return render_template('index.html',your_caption=result_dic['caption'],user_image=result_dic['image'])

if __name__ == "__main__":
    # app.debug = True
    app.run(debug=True) #debug=true means if we change the file it will directly reflect in the browser
