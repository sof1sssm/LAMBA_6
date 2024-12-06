from flask import Flask, request

app = Flask(__name__)

@app.route('/health')
def health(): 
  return 'OK'
  
@app.route('/process', methods=['GET', 'POST'])
def process():
  return 'OK'
  
if __name__ == '__main__':
  app.run(port=5000, debug=True)
