from flask import Flask, request, jsonify
import text2em
import time
import logging

app= Flask(__name__)

@app.post('/emotion')
def get_emotion():
    logging.info(request.get_json()["text"])
    body = request.get_json()
    result = text2em.get_emotion(body["text"])
    emo = max(result, key=result.get)
    return (emo)

if __name__ == "__main__":
    from waitress import serve
    logging.info('Serving on http://localhost:5000')
    serve(app, host="localhost", port=5000)