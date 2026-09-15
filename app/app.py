from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker", "completed": True},
    {"id": 2, "title": "Learn Kubernetes", "completed": False}
]


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if (
	not data
	or "title" not in data
	or not isinstance(data["title"], str)
	or not data["title"].strip()
	):
        return jsonify({"error": "title is required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"].strip(),
        "completed": False
    }

    tasks.append(task)

    return jsonify(task), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
