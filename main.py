import search_service
import traceback
from quart import request
from flask import Flask, request, jsonify

app = Flask(__name__)

# This key can be anything, though you will likely want a randomly generated sequence.
_SERVICE_AUTH_KEY = "0123456788abcdef"


@app.route("/search/quick")
def get_quicksearch():
    level = "quick"
    search_result = ""
    try:
        query = request.args.get("query")
        print(f"level: {level}, query: {query}")
        search_result = search_service.run_chat(query, level)
    except:
        traceback.print_exc()
    return jsonify(
        {
            "response": search_result,
            "credibility_definitions": {
                "Official Source": "Source is a government agency.",
                "Whitelisted Source": "Source is approved in your curation list.",
                "Third-Party Source": "Source does not appear in your curation list and may have varying levels of reliability.",
                "Blacklisted Source": "Source has been explicitly banned in your curation list.",
            },
        }
    ), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
